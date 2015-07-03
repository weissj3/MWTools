#include "Scheduler.h"

using namespace std;

scheduler::scheduler()
{
    useGPU = false;
    CoresFree = 0;
    totalRuns = 0;
    GPUInstance = NULL;
}

scheduler::scheduler(bool GPUapp, int numCores, string separationPath)
{
    useGPU = GPUapp;
    if(useGPU)
    {
        numCores -= 1;
    }
    CoresFree = numCores;

    totalRuns = 0;
    CPUInstances.resize(numCores, NULL);
    GPUInstance = NULL;
    pathToSep = separationPath;
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
        totalRuns++;
        return 0;
    }
    return -1;
}

int scheduler::updateRunning()
{
    //Update all Current Runs
    if(GPUInstance)
    {
        if(GPUInstance->updateStatus() < 0)
        {
            return -1;
        }
    }
    for(int i = 0; i < CPUInstances.size(); i++)
    {
        if(CPUInstances[i])
        {
            if((CPUInstances[i])->updateStatus() < 0)
            {
                return -1;
            }
        }
    }
    return 0;
}

int scheduler::cleanUpFinished()
{
    //Handle runs that finished during update
    if(GPUInstance)
    {
        if(GPUInstance->isFinished())
        {
            GPUInstance = NULL;
        }
    }
    for(int i = 0; i < CPUInstances.size(); i++)
    {
        if(CPUInstances[i])
        {
            if((CPUInstances[i])->isFinished())
            {
                CPUInstances[i] = NULL;
            }
        }
    }
    return 0;
}

int scheduler::startNewRuns()
{
    //Handle runs that finished during update
    if(!GPUInstance and useGPU and !runQueue.empty())
    {
        GPUInstance = runQueue.front();
        if(GPUInstance->runGPU(pathToSep, CPUInstances.size() + 1))
        {
            if((runQueue.size() % totalRuns / 20) == 0)
            {
                outputProgress();
            } 
            printQueue.push(GPUInstance);
            runQueue.pop();
        }
    }
    for(int i = 0; i < CPUInstances.size(); i++)
    {
        if(!CPUInstances[i] and !runQueue.empty())
        {
            CPUInstances[i] = runQueue.front();
            if(CPUInstances[i]->runCPU(pathToSep, i))
            {
                if((runQueue.size() % totalRuns / 20) == 0)
                {
                    outputProgress();
                }

		printQueue.push(CPUInstances[i]);
                runQueue.pop();
            }
        }
    }
    return 0;
}

int scheduler::printFinishedRuns()
{
    //Handle runs that finished during update
    while(!printQueue.empty() and (printQueue.front())->isFinished())
    {
        if(printQueue.front()->printLikelihood("list.txt"))  //Eventually take name from config file.
        {
            return -1;
        }
        delete printQueue.front();
        printQueue.pop();
    }
    return 0;
}

int scheduler::update()
{
    int result = 0;
    result = updateRunning();
    if(result < 0)
    {
        return result;
    }
    result = cleanUpFinished();
    if(result < 0)
    {
        return result;
    }
    result = startNewRuns();
    if(result < 0)
    {
        return result;
    }
    result = printFinishedRuns();
    if(result < 0)
    {
        return result;
    }
    if(printQueue.empty() and runQueue.empty() and !GPUInstance)
    {
        for(int i = 0; i < CPUInstances.size(); i++)
        {
            if(CPUInstances[i])
            {
                return 0;
            }
        }
        //Jobs done return 1;
        return 1;
    }

    return 0;
  
}

void scheduler::cleanup()
{
    //Kill Child Processes
    if(GPUInstance)
    {
        GPUInstance->killRun();
    }
    for(int i = 0; i < CPUInstances.size(); i++)
    {
        if(CPUInstances[i])
        {
            (CPUInstances[i])->killRun();
        }
    }

    //Clean up leftover dynamic memory
    while(!printQueue.empty())
    {
        delete printQueue.front();
        printQueue.pop();
    }
    while(!runQueue.empty())
    {
        delete runQueue.front();
        runQueue.pop();
    }
}

void scheduler::outputProgress()
{
    cout << 100. * ( 1. - (float)runQueue.size()/(float)totalRuns) << endl;
}

