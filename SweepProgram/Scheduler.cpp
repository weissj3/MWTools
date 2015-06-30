#include "Scheduler.h"

using namespace std;

scheduler::scheduler()
{
    GPUfree = false;
    CoresFree = 0;
}

scheduler::scheduler(bool useGPU, int numCores)
{
    GPUfree = useGPU;
    if(useGPU)
    {
        numCores -= 1;
    }
    CoresFree = numCores;

    CPUpids.resize(numCores, 0);
    GPUpid = 0;
}

scheduler::~scheduler()
{
    cleanup();
}

int scheduler::requestRun(int wedge, background BG, const stream * STR, int numStreams, area AREA, double xparam, double yparam)
{
    runInstance * newRun = new runInstance(wedge, BG, STR, numStreams, AREA, xparam, yparam);
    if(newRun)
    {
        runQueue.push(newRun);
        return 0;
    }
    return -1;
}

int scheduler::update()
{
    
    
    return -1;
    
}

void scheduler::cleanup()
{


}
