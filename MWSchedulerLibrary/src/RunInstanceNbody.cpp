#include "RunInstanceNbody.h"
using namespace std;

runInstanceNbody::runInstanceNbody() : runInstance()
{
}

runInstanceNbody::runInstanceNbody(string histFN, string luaFN, nbodyParameters params) : runInstance()
{
    HistogramFileName = histFN;
    LuaFileName = luaFN;
    Params = params;

}

pid_t runInstanceNbody::run(string pathToBin, unsigned int Id, string commandLine)
{
    string directory = prepRun(pathToBin, Id);
    //Fork to run MW@home to evaluate point
    runPid = fork();
    if (runPid == 0)
    {
        string f = "-f../" + LuaFileName, h = "-h../" + HistogramFileName;  //Eventually will be part of config file
        if(chdir((char *) directory.c_str()))
        {
            cerr << "Failed to change to directory " << directory << endl;
            exit(-1);
        }
        execl("./milkyway", "milkyway", (char *) f.c_str(), (char *) h.c_str(), " -i ",  (char *) to_string(Params[0]).c_str(), (char *) to_string(Params[1]).c_str(), (char *) to_string(Params[2]).c_str(), (char *) to_string(Params[3]).c_str(), (char *) to_string(Params[4]).c_str(), NULL);
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


