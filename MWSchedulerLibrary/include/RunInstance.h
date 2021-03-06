#ifndef _RUNINSTANCE_H_
#define _RUNINSTANCE_H_

#include "Util.h"

class runInstance
{
private:
    std::string StarFileName;
    
    pid_t runPid;
   
    parameters Params;

    pid_t run(std::string pathToSep, unsigned int Id, std::string commandLine);
    unsigned int coreId;

protected:
    unsigned int runId;
    double likelihood;
    
public:
    runInstance();
    runInstance(std::string starFileName, int w, background bg, const stream * str, int numStreams, area ar);
    runInstance(std::string starFileName, parameters params);
    ~runInstance();    

    pid_t getRunPid() { return runPid; }
    unsigned int getId() { return runId; }
    double getLikelihood() { return likelihood; } 
    bool isRunning();
    bool isFinished();
    void setRunId(unsigned int id) { runId = id; }
    
    int updateStatus();

    pid_t runCPU(std::string pathToSep, unsigned int Id);
    pid_t runGPU(std::string pathToSep, unsigned int Id, unsigned int gpuNum);
    
    void killRun();
    



};

#endif

