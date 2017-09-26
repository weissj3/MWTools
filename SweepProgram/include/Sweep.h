#ifndef _SWEEP_H_
#define _SWEEP_H_
#include "SweepRunInstance.h"
#include "Scheduler.h"

class sweep
{
private:
    scheduler * Scheduler;

    int wedge;
    area AREA;
    background BG;
    stream * STR;
    int numStreams;

    std::string StarFileName;

    double paramMin1;
    double paramMax1;
    double numSteps1;
    double paramMin2;
    double paramMax2;
    double numSteps2;
    
    double * xparam;
    double * yparam;    
    
    bool initialized; 

    int print_file();
    void init(std::ifstream &infile);

public:
    ~sweep();
    sweep() { initialized = false; }
    sweep(std::string paramFile, std::string starFileName, scheduler * sched, std::string param1, double min1, double max1, double steps1, std::string param2, double min2, double max2, double steps2);
    int run(std::string outputFileName);
    void cleanup();

};

#endif

