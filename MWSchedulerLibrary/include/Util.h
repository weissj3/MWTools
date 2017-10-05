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
    comma_ctype(size_t refs = 0) : std::ctype<char>(&comma_table[0], false, refs)
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
    double epsilon;
    double q;
    background() {}
    background(double E, double Q) : epsilon(E), q(Q) {}
    
    void print(std::ofstream & ostr)
    {
        ostr << "epsilon  = " << std::setprecision(16) << epsilon
        << ", \n   q = " << std::setprecision(16) << q;
    }
    double& operator[](unsigned int num)
    {
         switch(num)
         {
             case 0:
                  return epsilon;
             case 1:
                  return q;
             default:
                  throw std::string("Unable to find corresponding parameter.");
                  break;
         }
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
    double& operator[](unsigned int num)
    {
         switch(num)
         {
             case 0:
                  return epsilon;
             case 1:
                  return mu;
             case 2:
                  return r;
             case 3:
                  return theta;
             case 4:
                  return phi;
             case 5:
                  return sigma;
             default:
                  throw std::string("Unable to find corresponding parameter.");
                  break;
         }
    }
};

class parameters
{
public:
    int wedge;
    background BG;
    std::vector <stream> STR;
    area AR;
    
    parameters() {}
    parameters(int w, const std::vector <double> &values, area ar)
    {
        wedge = w;
        if( values.size() >= 2 )
        {
            BG = background(values[0], values[1]);
        }
        int i = 2;
        while( i < values.size() )
        {
            if( values.size() >= i + 6 )
            {
                STR.push_back(stream(values[i], values[i+1], values[i+2], values[i+3], values[i+4], values[i+5]));
            }
            i += 6;
        }
        AR = ar;
    }
    parameters(int w, background bg, const std::vector <stream> &str, area ar)
    {
        wedge = w;
        BG = bg;
        STR = str;
        AR = ar;
    }
    parameters(std::string inFileName);

    int print(std::string fileName);
    void print(std::ofstream & ostr);

    int numParams() { return 2 + 6 * STR.size(); }
    double& operator[](unsigned int num)
    {
        if(num <2)
        {
            return BG[num];
        }
        else
        {
            num -= 2;
            unsigned int strNum = 0;
            while( num > 5 && strNum < STR.size())
            {
                num -= 6;
                strNum += 1;
            }
            return STR[strNum][num];
        }
    }



};

double * getParamByName(std::string paramName, background &BG, stream * STR);

#endif
