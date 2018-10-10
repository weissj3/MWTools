#include "RunSeparationInstance.h"
using namespace std;


runSeparationInstance::runSeparationInstance() : runInstance()
{
}

runSeparationInstance::runSeparationInstance(std::string starFileName, int w, background bg, const stream * str, int numStreams, area ar) : runInstance()
{
    StarFileName = starFileName;
    vector <stream> tmpstreams;
    if (str)
    {
        for(int i = 0; i < numStreams; i++)
        {   
            tmpstreams.push_back(str[i]);
        }
    }
    Params = parameters(w, bg, tmpstreams, ar);
}

runSeparationInstance::runSeparationInstance(std::string starFileName, parameters params) : runInstance()
{
    StarFileName = starFileName;
    Params = params;
}

runSeparationInstance::~runSeparationInstance() {}

pid_t runSeparationInstance::run(string pathToBin, unsigned int Id, string commandLine)
{
    string directory = prepRun(pathToBin, Id);

    runPid = fork();
    if (runPid == 0)
    {
        string a = "-a./sweepParams.lua", s = "-s../" + StarFileName;  //Eventually will be part of config file
        if(chdir((char *) directory.c_str()))
        {
            cerr << "Failed to change to directory " << directory << endl;
            exit(-1);
        }
        if(Params.print("sweepParams.lua"))
        {
            cerr << "Failed to print parameter file for sweep" << endl;
            exit(-1);
        }
        execl("./milkyway_separation", "milkyway_separation",  (char *)s.c_str(), (char *)a.c_str(), "-c", "-t", "-f", "-i", (char *) commandLine.c_str(), NULL);
        exit(0);
    }
    else if (runPid < 0)
    {
        cerr << "Failed to fork" << endl;
        runPid = 0;
        return runPid;
    }
    return runPid;

}

