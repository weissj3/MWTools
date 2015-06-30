#ifndef _SCHEDULER_H_
#define _SCHEDULER_H_

#include "RunInstance.h"

class scheduler
{
private:

    bool GPUfree;
    int CoresFree;
    std::vector <runInstance*> CPUpids;
    pid_t GPUpid;
    std::queue <runInstance*> runQueue;
    std::list <runInstance*> printQueue;



public:
    scheduler();
    scheduler(bool useGPU, int numCores);
    ~scheduler();
    
    int requestRun(int wedge, background BG, const stream * STR, int numStreams, area AREA, double xparam, double yparam);
    int update();
    void cleanup();


};

#endif

