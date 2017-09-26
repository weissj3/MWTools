#ifndef _SCHEDULER_H_
#define _SCHEDULER_H_

#include "RunInstance.h"

class scheduler
{
private:

    int GPUsFree;
    int CoresFree;
    int RunsPerGPU;
    std::vector <runInstance*> CPUInstances;
    std::vector <runInstance*> GPUInstances;
    std::queue <runInstance*> runQueue;
    std::vector <runInstance*> finishedRuns;
    std::string pathToSep;

    unsigned int totalRuns;

    int updateRunning();
    int cleanUpFinished();
    int startNewRuns();

public:
    scheduler();
    scheduler(int numGPUs, int runsPerGPU, int numCores, std::string separationPath);
    ~scheduler();
   
    void outputProgress(); 
    int requestRun(runInstance* newRun);
    
    int update();
    void cleanup();
    std::vector <runInstance*> getFinishedRuns() { return finishedRuns; }
    void clearFinishedRuns();

};

#endif

