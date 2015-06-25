#include "Sweep.h"

using namespace std;

sweep::sweep(string paramFile)
{
//Read in basic parameters from file
    ifstream infile;
    infile.open(paramFile.c_str());
    if(!infile.is_open())
    {
        throw string("Failed to open init file");
    }
    init(infile);


//Eventually replace this by reading in from config file
    paramMin1 = 1.22;
    paramMax1 = 2.48;
    numSteps1 = 5.;
    paramMin2 = 2.42;
    paramMax2 = 3.68;
    numSteps2 = 5.;
    initialized = true;
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
    AREA.print(output);     
    output << "\n   }\n}\n";
    output.close();
    return 0;
}

//Designed to read in from lua file without actually using lua (maybe actually integrate lua interpreter later)
void sweep::init(ifstream &infile)
{
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
            >> temp >> temp >> AREA.r_min
            >> temp >> temp >> AREA.r_max
            >> temp >> temp >> AREA.r_steps
            >> temp >> temp >> AREA.mu_min
            >> temp >> temp >> AREA.mu_max
            >> temp >> temp >> AREA.mu_steps
            >> temp >> temp >> AREA.nu_min
            >> temp >> temp >> AREA.nu_max
            >> temp >> temp >> AREA.nu_steps;
}



int sweep::run(string pathToSep, string resultFileName)
{
    if(!initialized)
    {
        cerr << "Must initialized before running sweep" << endl;
        return -1;
    }
    ofstream output;
    output.open("list.txt");
    ifstream infile;

    string a = "-a./sweepParams.lua", s = "-s./stars-15-sim-1Jun1.txt";

    double result = 0;
    int status = 0;
    int i = 0;
    //Step over parameters
    for(STR[0].theta = paramMin1; STR[0].theta < paramMax1; STR[0].theta += (paramMax1-paramMin1)/numSteps1 )
    {
        for(STR[0].phi = paramMin2; STR[0].phi < paramMax2; STR[0].phi += (paramMax2-paramMin2)/numSteps2)
        {
            if(print_file())
            {
                cerr << "Failed to print parameter file for sweep" << endl;
                return -1;
            }
            //Fork to run MW@home to evaluate point
            pid_t id = fork();
            if (id == 0)
            {
                execl((char *)pathToSep.c_str(), "milkyway_separation",  (char *)s.c_str(), (char *)a.c_str(), "-t", "-f", "-i", NULL);
                exit(0);
            }
            else if (id < 0)
            {
                cerr << "Failed to fork" << endl;
                return -1;
            }
            int childExitStatus;
            //BLOCK until done running
            waitpid( id, &childExitStatus, 0);
            if( !WIFEXITED(childExitStatus) )
            {
                cerr << "waitpid() exited with an error: Status= " << WEXITSTATUS(childExitStatus) << endl;
                return -1;
            }
            else if( WIFSIGNALED(childExitStatus) )
            {
                cerr << "waitpid() exited due to a signal: " << WTERMSIG(childExitStatus) << endl;
                return -1;
            }
            //read in result from MW@home
            infile.open("results.txt");
            if(!infile.is_open())
            {
                cerr << "Failed to open results" << endl;
                return -1;
            }
            infile >> result;
            infile.close();
            //Print Likelihood and corresponding params to file
            output << STR[0].theta << " " << STR[0].phi << " " << setprecision(16) << result <<  endl;
            if(i % (int)(numSteps1 * numSteps2/10) == 0)
            {
                cout << status << "0%" << endl;
                status++;
            }
            i++;
        }        
    }


    return 0;

}

 
