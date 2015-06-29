#ifndef _RUNINSTANCE_H_
#define _RUNINSTANCE_H_

#include "Util.h"

class runInstance
{
private:
    
    background BG;
    std::vector <stream> STR;
    area AREA;

    double xparam;
    double yparam;

    unsigned int runId;
    double likelihood;

    int printParams(string filename);
    
public:
    runInstance();
    runInstance(background bg, const stream * str, area ar, double x, double y);
    
    bool isRunning();
    bool isFinished();
    pid_t runCPU(unsigned int Id);
    pid_t runGPU(unsigned int Id);
    
    printLikelihood(string filename);
    


};

#endif

