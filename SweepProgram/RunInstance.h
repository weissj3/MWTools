#ifndef _RUNINSTANCE_H_
#define _RUNINSTANCE_H_

#include "Util.h"

class runInstance
{
private:
    int wedge;
    background BG;
    std::vector <stream> STR;
    area AREA;

    double xparam;
    double yparam;

    unsigned int runId;
    double likelihood;
    pid_t runPid;


    int printParams();
    pid_t run(std::string pathToSep, unsigned int Id, std::string commandLine);
    
public:
    runInstance();
    runInstance(background bg, const stream * str, int numStreams, area ar, double x, double y);
    
    pid_t getRunPid() { return runPid; }
    unsigned int getId() { return runId; }
    bool isRunning();
    bool isFinished();
    pid_t runCPU(std::string pathToSep, unsigned int Id);
    pid_t runGPU(std::string pathToSep, unsigned int Id);
    
    int printLikelihood(std::string filename);
    


};

#endif

