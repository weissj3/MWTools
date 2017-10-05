#ifndef _Hessian_H_
#define _Hessian_H_
#include "Scheduler.h"
#include <vector>
#include <armadillo>


class hessian
{
private:
    scheduler * Scheduler;

    parameters Params;
    
    std::string StarFileName;

    std::vector <double> StepSizes;

    bool initialized; 

public:
    ~hessian();
    hessian() { initialized = false; }
    hessian(std::string paramFile, std::string starFileName, scheduler * sched, const std::vector <double> &stepSizes);
    int run(std::string outputFileName);
    void cleanup();

};

#endif

