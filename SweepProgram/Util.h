/*************************************************************************************
*                           Generates .lua Parameter Files                            *
*                                                                                     *
*                           Changeable Variables:                                     *
*                           lines: 47, 48 (interval info)                             *
*                           lines: 50-69 (Initial Parameters)                         *
*                           lines: 72, 108 (Changing Parameter)                       *
*                                                                                     *
*                                                                                     *
*                                                                                     *
*                                                                                     *
**************************************************************************************/
#ifndef _UTIL_H_
#define _UTIL_H_

#include <algorithm>
#include <fstream>
#include <iostream>
#include <cstdlib>
#include <vector>
#include <string>
#include <ctime>
#include <iomanip>
#include <unistd.h>
#include <locale>
#include <cstring>
#include <sys/wait.h>
#include <sys/stat.h>
#include <errno.h>
#include <list>
#include <queue>
#include <sstream>


class comma_ctype : public std::ctype<char>
{
private:
    mask comma_table[table_size];

public:
    comma_ctype(size_t refs = 0) : ctype<char>(&comma_table[0], false, refs)
    {
        for(int i = 0; i < 256; i++)
        {
            comma_table[i] = classic_table()[i];
        }
        comma_table[','] = (mask)space;
    }
};

class area
{
public:
    double r_min;
    double r_max;
    double r_steps;

    double mu_min;
    double mu_max;
    double mu_steps;
    
    double nu_min;
    double nu_max;
    double nu_steps;
    
    area() {}
    area(double R_MIN, double R_MAX, double R_STEPS, double MU_MIN, double MU_MAX, double MU_STEPS, double NU_MIN, double NU_MAX, double NU_STEPS) : r_min(R_MIN), r_max(R_MAX), r_steps(R_STEPS), mu_min(MU_MIN), mu_max(MU_MAX), mu_steps(MU_STEPS), nu_min(NU_MIN), nu_max(NU_MAX), nu_steps(NU_STEPS) {}

    void print (std::ofstream & ostr)
    {
        ostr << "{\n      r_min = " << std::setprecision(3) << r_min
            << ",\n      r_max = " << std::setprecision(3) << r_max 
            << ",\n      r_steps = " << (int) r_steps 
            << ",\n\n      mu_min = " << std::setprecision(3) << mu_min 
            << ",\n      mu_max = " << std::setprecision(3) << mu_max 
            << ",\n      mu_steps = " << (int) mu_steps
            << ",\n\n      nu_min = " << std::setprecision(3) << nu_min 
            << ",\n      nu_max = " << std::setprecision(3) << nu_max
            << ",\n      nu_steps = " << (int) nu_steps;
    }
};

class background
{
public:
    double q;
    double r0;
    background() {}
    background(double Q, double R0) : q(Q), r0(R0) {}
    
    void print(std::ofstream & ostr)
    {
        ostr << "q  = " << std::setprecision(16) << q 
        << ", \n   r0 = " << std::setprecision(16) << r0;
    }
};

class stream
{
public:
    double epsilon;
    double mu;
    double r;
    double theta;
    double phi;
    double sigma;
    stream() {}
    stream(double E, double M, double R, double T, double P, double S) : epsilon(E), mu(M), r(R), theta(T), phi(P), sigma(S) {}
    void print(std::ofstream & ostr)
    {
        ostr << "   { \n      epsilon = " << std::setprecision(16) << epsilon 
            << ",\n      mu      = " << std::setprecision(15) << mu 
            << ",\n      r       = " << std::setprecision(17) << r 
            << ",\n      theta   = " << std::setprecision(15) << theta 
            << ",\n      phi     = " << std::setprecision(17) << phi 
            << ",\n      sigma   = " << std::setprecision(17) << sigma 
            << "\n   }";
    }

};

double * getParamByName(std::string paramName, background &BG, std::vector <stream> &STR);

#endif
