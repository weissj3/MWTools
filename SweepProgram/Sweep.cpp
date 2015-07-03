#include "Sweep.h"

using namespace std;

sweep::sweep(string paramFile, scheduler * sched)
{
    if(!sched)
    {
        throw string("Sweeps require a scheduler");
    }
    Scheduler = sched;
//Read in basic parameters from file
    ifstream infile;
    infile.open(paramFile.c_str());
    if(!infile.is_open())
    {
        throw string("Failed to open init file");
    }
    STR = NULL;
    init(infile);


//Eventually replace this by reading in from config file
    paramMin1 = 1.22;
    paramMax1 = 2.48;
    numSteps1 = 50.;
    paramMin2 = 2.42;
    paramMax2 = 3.68;
    numSteps2 = 50.;
    xparam = &(STR[0].theta);
    yparam = &(STR[0].phi);
    initialized = true;
}

sweep::~sweep()
{
   cleanup();
}

void sweep::cleanup()
{
    if(initialized)
    {    
        initialized = false;  
        if(STR)
        {   
            delete[] STR;
        }
    }
}

//Print parameter file for current step.
int sweep::print_file()
{
    ofstream output;
    output.open("sweepParams.lua");
    if(!output.is_open())
    {
        cerr << "Unable to open file to print" << endl;
        return -1;
    }
    output << "\n wedge = " << wedge 
            << " \n \n background = { \n   ";
    BG.print(output);            
    output << "\n } \n \n streams = { \n";
    for(int i = 0; i < numStreams; i++)
    {
        STR[i].print(output);
        if(i != numStreams-1)
        {
            output << ",\n\n";
        }
        else
        {
            output << "\n";
        }
    }
    output << "}\n\narea = {\n   ";
    AREA.print(output);     
    output << "\n   }\n}\n";
    output.close();
    return 0;
}

//Designed to read in from lua file without actually using lua (maybe actually integrate lua interpreter later)
void sweep::init(ifstream &infile)
{
    vector<stream> STRTMP;
    string temp;
    locale x(locale::classic(), new comma_ctype);
    infile.imbue(x);

    infile >> temp >> temp >> wedge
            >> temp >> temp >> temp
            >> temp >> temp >> BG.q
            >> temp >> temp >> BG.r0
            >> temp
            >> temp >> temp >> temp;
    while(1)
    {
            infile >> temp;
            if(temp  == "{")
            {
                STRTMP.push_back(stream());
            }
            else
            {
                break;
            }
            infile >> temp >> temp >> STRTMP[STRTMP.size()-1].epsilon 
                    >> temp >> temp >> STRTMP[STRTMP.size()-1].mu 
                    >> temp >> temp >> STRTMP[STRTMP.size()-1].r
                    >> temp >> temp >> STRTMP[STRTMP.size()-1].theta
                    >> temp >> temp >> STRTMP[STRTMP.size()-1].phi
                    >> temp >> temp >> STRTMP[STRTMP.size()-1].sigma
                    >> temp;
    }
    infile >> temp >> temp >> temp
            >> temp 
            >> temp >> temp >> AREA.r_min
            >> temp >> temp >> AREA.r_max
            >> temp >> temp >> AREA.r_steps
            >> temp >> temp >> AREA.mu_min
            >> temp >> temp >> AREA.mu_max
            >> temp >> temp >> AREA.mu_steps
            >> temp >> temp >> AREA.nu_min
            >> temp >> temp >> AREA.nu_max
            >> temp >> temp >> AREA.nu_steps;

    STR = new stream[STRTMP.size()];
    if(!STR)
    {
        cerr << "New failed" << endl;
    }
    numStreams = STRTMP.size();
    for(int i = 0; i < STRTMP.size(); i++)
    {
        STR[i] = STRTMP[i];
    }
}



int sweep::run()
{
    if(!initialized)
    {
        cerr << "Must initialized before running sweep" << endl;
        return -1;
    }
    ofstream output;
    output.open("list.txt");
    output.close();
    ifstream infile;

    string a = "-a./sweepParams.lua", s = "-s../stars-15-sim-1Jun1.txt";

    double result = 0;
    int status = 0;
    int i = 0;
    //Step over parameters
    for(*xparam = paramMin1; *xparam < paramMax1; *xparam += (paramMax1-paramMin1)/(numSteps1 - 1) )
    {
        for(*yparam = paramMin2; *yparam < paramMax2; *yparam += (paramMax2-paramMin2)/(numSteps2 - 1))
        {
            Scheduler->requestRun(wedge, BG, STR, numStreams, AREA, *xparam, *yparam);
        }        
    }

    int schedulerStatus = 0;
    while(!schedulerStatus)
    {
        schedulerStatus = Scheduler->update();
    }

    if(schedulerStatus < 0)
    {
        cerr << "Exited with error " << schedulerStatus << endl;
    }

    Scheduler->cleanup();

    return schedulerStatus;

}

 
