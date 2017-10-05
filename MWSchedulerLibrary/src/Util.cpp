#include "Util.h"
using namespace std;


//Designed to read in from lua file without actually using lua (maybe actually integrate lua interpreter later)
parameters::parameters(string inFileName)
{
    ifstream infile;
    infile.open(inFileName.c_str());
    if(!infile.is_open())
    {   
        throw string("Failed to open init file");
    }
    string temp;
    locale x(locale::classic(), new comma_ctype);
    infile.imbue(x);

    infile >> temp >> temp >> wedge
           >> temp >> temp >> temp
           >> temp >> temp >> BG.epsilon
           >> temp >> temp >> BG.q
           >> temp 
           >> temp >> temp >> temp;
    while(1)
    {
        infile >> temp;
        if(temp  == "{")
        {   
            STR.push_back(stream());
        }
        else
        {   
            break;
        }
        infile >> temp >> temp >> STR[STR.size()-1].epsilon
               >> temp >> temp >> STR[STR.size()-1].mu
               >> temp >> temp >> STR[STR.size()-1].r
               >> temp >> temp >> STR[STR.size()-1].theta
               >> temp >> temp >> STR[STR.size()-1].phi
               >> temp >> temp >> STR[STR.size()-1].sigma
               >> temp;
    }
    infile >> temp >> temp >> temp
           >> temp 
           >> temp >> temp >> AR.r_min
           >> temp >> temp >> AR.r_max
           >> temp >> temp >> AR.r_steps
           >> temp >> temp >> AR.mu_min
           >> temp >> temp >> AR.mu_max
           >> temp >> temp >> AR.mu_steps
           >> temp >> temp >> AR.nu_min
           >> temp >> temp >> AR.nu_max
           >> temp >> temp >> AR.nu_steps;
}


int parameters::print(std::string fileName)
{
    ofstream output;
    output.open(fileName.c_str());
    if(!output.is_open())
    {
        cerr << "Unable to open file to print" << endl;
        return -1;
    }
    
    print(output);
    output.close();
    return 0;
}

void parameters::print(std::ofstream & output)
{
    output << "\n wedge = " << wedge
           << " \n \n background = { \n   ";
    BG.print(output);
    output << "\n } \n \n streams = { \n";
    for(int i = 0; i < STR.size(); i++)
    {
        STR[i].print(output);
        if(i != STR.size()-1)
        {
            output << ",\n\n";
        }
        else
        {
            output << "\n";
        }
    }
    output << "}\n\narea = {\n   ";
    AR.print(output);
    output << "\n   }\n}\n";
}
        
double * getParamByName(string paramName, background &BG, stream * STR)
{
    if(!STR)
    {
        cerr << "Tried to get param without initializing streams" << endl;
        return NULL;
    }
    if(paramName == "epsilonBG")
    {
        return &(BG.epsilon);
    }
    else if(paramName == "q")
    {
        return &(BG.q);
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


