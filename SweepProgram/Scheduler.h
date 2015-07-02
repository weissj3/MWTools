#ifndef _SCHEDULER_H_
#define _SCHEDULER_H_

#include "RunInstance.h"

class scheduler
{
private:

    bool useGPU;
    int CoresFree;
    std::vector <runInstance*> CPUInstances;
    runInstance * GPUInstance;
    std::queue <runInstance*> runQueue;
    std::queue <runInstance*> printQueue;
    std::string pathToSep;

    int updateRunning();
    int cleanUpFinished();
    int startNewRuns();
    int printFinishedRuns();

public:
    scheduler();
    scheduler(bool GPUapp, int numCores, std::string separationPath);
    ~scheduler();
    
    int requestRun(int wedge, background BG, const stream * STR, int numStreams, area AREA, double xparam, double yparam);
    int update();
    void cleanup();


};

#endif

