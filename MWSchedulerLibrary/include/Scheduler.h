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
    std::queue <runInstance*> printQueue;
    std::string pathToSep;

    unsigned int totalRuns;

    int updateRunning();
    int cleanUpFinished();
    int startNewRuns();
    int printFinishedRuns();

public:
    scheduler();
    scheduler(int numGPUs, int runsPerGPU, int numCores, std::string separationPath);
    ~scheduler();
   
    void outputProgress(); 
    int requestRun(std::string outFileName, std::string starFileName, int wedge, background BG, const stream * STR, int numStreams, area AREA, double xparam, double yparam);
    int update();
    void cleanup();


};

#endif

