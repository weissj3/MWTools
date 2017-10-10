#include "Sweep.h"

using namespace std;

sweep::sweep(string paramFile, string starFileName, scheduler * sched, string param1, double min1, double max1, double steps1, string param2, double min2, double max2, double steps2)
{
    if(!sched)
    {
        throw string("Sweeps require a scheduler");
    }
    Scheduler = sched;
    StarFileName = starFileName;
//Read in basic parameters from file
    ifstream infile;
    infile.open(paramFile.c_str());
    if(!infile.is_open())
    {
        throw string("Failed to open init file");
    }
    STR = NULL;
    init(infile);

    paramMin1 = min1;
    paramMax1 = max1;
    numSteps1 = steps1;
    paramMin2 = min2;
    paramMax2 = max2;
    numSteps2 = steps2;
    xparam = getParamByName(param1, BG, STR);
    yparam = getParamByName(param2, BG, STR);
    if(!xparam or !yparam)
    {
        throw string("Could not find parameters by name");
    }

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
            >> temp >> temp >> BG.epsilon
            >> temp >> temp >> BG.q
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



int sweep::run(std::string outputFileName)
{
    if(!initialized)
    {
        cerr << "Must initialized before running sweep" << endl;
        return -1;
    }
    //Clean out old file
    ofstream output;
    output.open(outputFileName.c_str());
    output.close();

    //Step over parameters
    if(numSteps1 == 0)
    {
        for(*yparam = paramMin2; *yparam <= paramMax2; *yparam += (paramMax2-paramMin2)/(numSteps2 - 1))
        {
            Scheduler->requestRun(new sweepRunInstance(outputFileName, StarFileName, wedge, BG, STR, numStreams, AREA, *xparam, *yparam));
        }        
    }
    else if(numSteps2 == 0)
    {
        for(*xparam = paramMin1; *xparam <= paramMax1; *xparam += (paramMax1-paramMin1)/(numSteps1 - 1))
        {
            Scheduler->requestRun(new sweepRunInstance(outputFileName, StarFileName, wedge, BG, STR, numStreams, AREA, *xparam, *yparam));
        }     
    }
    else
    {
        for(*xparam = paramMin1; *xparam <= paramMax1; *xparam += (paramMax1-paramMin1)/(numSteps1 - 1) )
        {
            for(*yparam = paramMin2; *yparam < paramMax2; *yparam += (paramMax2-paramMin2)/(numSteps2 - 1))
            {
                Scheduler->requestRun(new sweepRunInstance(outputFileName, StarFileName, wedge, BG, STR, numStreams, AREA, *xparam, *yparam));
            }        
        }
    }

    int schedulerStatus = 0;
    while(!schedulerStatus)
    {
        schedulerStatus = Scheduler->update();
        sleep(2);
    }

    if(schedulerStatus < 0)
    {
        cerr << "Exited with error " << schedulerStatus << endl;
    }
    else
    {
        vector <runInstance*> results = Scheduler->getFinishedRuns();
        for(int i = 0; i < results.size(); i++)
        {
            if(results[i])
            {
                ((sweepRunInstance*) results[i])->printLikelihood();
            }
            else
            {
                cerr << "Missing Sweep Result " << i << endl;
            }
        }
    }

    Scheduler->cleanup();

    return schedulerStatus;

}

 
