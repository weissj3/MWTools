#ifndef _SWEEP_H_
#define _SWEEP_H_
#include "Util.h"

class sweep
{
private:
    int wedge;
    area AREA;
    background BG;
    std::vector<stream> STR;

    double paramMin1;
    double paramMax1;
    double numSteps1;
    double paramMin2;
    double paramMax2;
    double numSteps2;

    bool initialized; 

    int print_file();
    void init(std::ifstream &infile);

public:
    sweep() { initialized = false; }
    sweep(std::string paramFile);
    int run(std::string pathToSep, std::string resultFileName);

};

#endif

