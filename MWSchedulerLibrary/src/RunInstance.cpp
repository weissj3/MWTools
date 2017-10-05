#include "RunInstance.h"
#include <string>

using namespace std;

runInstance::runInstance()
{
    likelihood = 1;
    runId = 0;
}

runInstance::runInstance(string starFileName, int w, background bg, const stream * str, int numStreams, area ar)
{
    StarFileName = starFileName;
    likelihood = 1;
    runId = 0;
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
    
runInstance::runInstance(string starFileName, parameters params)
{
    StarFileName = starFileName;
    Params = params;
}

runInstance::~runInstance()
{
    killRun();
}

void runInstance::killRun()
{
    if(isRunning())
    {
        cout << "Killing Process " << runPid << " with run id " << runId << endl;
        kill(runPid, SIGKILL);
    }
}

bool runInstance::isRunning()
{
    return runPid;
}

bool runInstance::isFinished()
{
    if(likelihood < 0)
    {
        return true;
    }

    return false;
}

pid_t runInstance::runCPU(string pathToSep, unsigned int Id)
{
    string command = "--force-no-opencl";
    return run(pathToSep, Id, command);
}

pid_t runInstance::runGPU(string pathToSep, unsigned int Id, unsigned int gpuNum)
{
    string command = "--device=" + std::to_string(gpuNum);
    return run(pathToSep, Id, command);
}

//To Do:  Test if commandLine will still work with multiple options set.
pid_t runInstance::run(string pathToSep, unsigned int Id, std::string commandLine)
{
    runId = Id;

    stringstream tempstringstream;
    tempstringstream << Id;
    string directory = tempstringstream.str();
    //Lots of system call so lots of error checking
    if(mkdir((char *) directory.c_str(), S_IRWXU | S_IRWXG | S_IROTH | S_IXOTH) and errno != EEXIST)
    {
        cerr << "Failed to create directory " << directory << endl;
        exit(-1);
    }
    
    //Copy MW@home Executable to Fix Lock_file issues  ADD Error checking to make sure is_open and chmod work
    ifstream source(pathToSep.c_str(), ios::binary);
    ofstream dest((directory + "/milkyway_separation").c_str(), ios::binary);

    dest << source.rdbuf();

    source.close();
    dest.close();

    chmod((directory + "/milkyway_separation").c_str(), S_IRUSR | S_IWUSR | S_IXUSR | S_IXGRP | S_IWGRP | S_IRGRP | S_IROTH );
    //Fork to run MW@home to evaluate point
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

int runInstance::updateStatus()
{
    if(!isRunning())
    {
        return 0;
    }
    int childExitStatus;
    if(waitpid( runPid, &childExitStatus, WNOHANG))
    {
        if( !WIFEXITED(childExitStatus) )
        {
            cerr << "waitpid() exited with an error: Status= " << WEXITSTATUS(childExitStatus) << endl;
            return -1;
        }
        else if( WIFSIGNALED(childExitStatus) )
        {
            cerr << "waitpid() exited due to a signal: " << WTERMSIG(childExitStatus) << endl;
            return -1;
        }
        else
        {
            //Get Likelihood
            stringstream tempstringstream;
            tempstringstream << runId;
            string resultFilePath = tempstringstream.str() + "/results.txt";
            ifstream infile;
            infile.open(resultFilePath.c_str());
            if(!infile.is_open())
            {
                cerr << "Failed to open results: " << resultFilePath << endl;
                return -1;
            }
            infile >> likelihood;
            infile.close();
            runPid = 0;
            runId = 0;
            return 0;
        }

    }
    return 0;
}


























    
