#ifndef _SWEEP_H_
#define _SWEEP_H_
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
    sweep(std::string paramFile, scheduler * sched);
    int run();
    void cleanup();

};

#endif

