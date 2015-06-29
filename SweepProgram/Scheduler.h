#ifndef _SCHEDULER_H_
#define _SCHEDULER_H_

#include "RunInstance.h"

class scheduler
{
private:

    bool GPUfree;
    int CoresFree;
    std::vector <pid_t> CPUpids;
    pid_t GPUpid;
    std::queue <runInstance> runQueue;
    std::list <runInstance> printQueue;



public:
    scheduler();
    scheduler(bool useGPU, int numCores);
    
    int requestRun(runInstance params);
    int update();
    void cleanup();


};

#endif

