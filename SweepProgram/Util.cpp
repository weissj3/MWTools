#include "Util.h"

double * getParamByName(std::string paramName, background &BG, stream * STR)
{
    if(!STR)
    {
        std::cerr << "Tried to get param without initializing streams" << std::endl;
        return NULL;
    }
    if(paramName == "q")
    {
        return &(BG.q);
    }
    else if(paramName == "r0")
    {
        return &(BG.r0);
    }
    else if(paramName == "epsilon1")
    {
        return &(STR[0].epsilon);
    }
    else if(paramName == "mu1")
    {
        return &(STR[0].mu);
    }
    else if(paramName == "r1")
    {
        return &(STR[0].r);
    }
    else if(paramName == "theta1")
    {
        return &(STR[0].theta);
    }
    else if(paramName == "phi1")
    {
        return &(STR[0].phi);
    }
    else if(paramName == "sigma1")
    {
        return &(STR[0].sigma);
    }
    else if(paramName == "epsilon2")
    {
        return &(STR[1].epsilon);
    }
    else if(paramName == "mu2")
    {
        return &(STR[1].mu);
    }
    else if(paramName == "r2")
    {
        return &(STR[1].r);
    }
    else if(paramName == "theta2")
    {
        return &(STR[1].theta);
    }
    else if(paramName == "phi2")
    {
        return &(STR[1].phi);
    }
    else if(paramName == "sigma2")
    {
        return &(STR[1].sigma);
    }
    else if(paramName == "epsilon3")
    {
        return &(STR[2].epsilon);
    }
    else if(paramName == "mu3")
    {
        return &(STR[2].mu);
    }
    else if(paramName == "r3")
    {
        return &(STR[2].r);
    }
    else if(paramName == "theta3")
    {
        return &(STR[2].theta);
    }
    else if(paramName == "phi3")
    {
        return &(STR[2].phi);
    }
    else if(paramName == "sigma3")
    {
        return &(STR[2].sigma);
    }
    else
    {
        return NULL;
    }
}


