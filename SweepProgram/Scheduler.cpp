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

int scheduler::requestRun(runInstance params)
{





}

int scheduler::update()
{
    
    
    
    
}

void scheduler::cleanup()
{





}
