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
#include "Sweep.h"

using namespace std;

void print_file(int wedge, background &BG, vector<stream> &STR, area &AREA)
{
    ofstream output;
    output.open("sweepParams.lua");
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
}

void init(ifstream &infile, int &wedge, background &BG, vector <stream> &STR, area &AREA)
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

double * getParamByName(string paramName, &BG, &STR)
{
    if(paramName == "q")
    {
        return &BG.q;
    }
    else if(paramName == "r0")
    {
        return &BG.r0;
    }
    else if(paramName == "epsilon1")
    {
        return &STR[0].epsilon;
    }
    else if(paramName == "mu1")
    {
        return &STR[0].mu;
    }
    else if(paramName == "r1")
    {
        return &STR[0].r;
    }
    else if(paramName == "theta1")
    {
        return &STR[0].theta;
    }
    else if(paramName == "phi1")
    {
        return &STR[0].phi;
    }
    else if(paramName == "sigma1")
    {
        return &STR[0].sigma;
    }
    else if(paramName == "epsilon2")
    {
        return &STR[1].epsilon;
    }
    else if(paramName == "mu2")
    {
        return &STR[1].mu;
    }
    else if(paramName == "r2")
    {
        return &STR[1].r;
    }
    else if(paramName == "theta2")
    {
        return &STR[1].theta;
    }
    else if(paramName == "phi2")
    {
        return &STR[1].phi;
    }
    else if(paramName == "sigma2")
    {
        return &STR[1].sigma;
    }
    else if(paramName == "epsilon3")
    {
        return &STR[2].epsilon;
    }
    else if(paramName == "mu3")
    {
        return &STR[2].mu;
    }
    else if(paramName == "r3")
    {
        return &STR[2].r;
    }
    else if(paramName == "theta3")
    {
        return &STR[2].theta;
    }
    else if(paramName == "phi3")
    {
        return &STR[2].phi;
    }
    else if(paramName == "sigma3")
    {
        return &STR[2].sigma;
    }
    else
    {
        return NULL;
    }
}


int main (int argc, char* argv[]) 
{
    if(argc < 2)
    {
        cout << "Proper Usage <Input file> <Number of Steps> <Path to Separation>" << endl;
        return -1;
    }
    clock_t timer;
    int numSteps = atoi(argv[2]);
    ifstream infile;
    infile.open(argv[1]);
    ofstream output;
    output.open("list.txt");

    int wedge;
    background BG;
    vector <stream> STR;
    area AREA;
    time_t time1, time2;

    init(infile, wedge, BG, STR, AREA);
    infile.close();
    
    string a = "-a./sweepParams.lua", s = "-s./stars-15-sim-1Jun1.txt";
    
    double result = 0;
    int counter = 0;
    double * xparam = &STR[0].theta;
    double * yparam = &STR[0].phi;
    double paramMin1 = 1.22;
    double paramMax1 = 2.48;
    double numSteps1 = 50;
    double paramMin2 = 2.42;
    double paramMax2 = 3.68;
    double numSteps2 = 50;
    int i = 0;
    time(&time1);
    for(*xparam = paramMin1; *xparam < paramMax1; *xparam += (paramMax1-paramMin1)/numSteps1 )
    {
        for(*yparam = paramMin2; *yparam < paramMax2; *yparam += (paramMax2-paramMin2)/numSteps2)
        {
            print_file(wedge, BG, STR, AREA);
            pid_t id = fork();
            if (id == 0)
            {
                execl((char *)argv[3], "milkyway_separation",  (char *)s.c_str(), (char *)a.c_str(), "-t", "-f", "-i", NULL);
                exit(0);
            }
            else if (id < 0)
            {
                cerr << "Failed to fork" << endl;
                exit(1);
            }
            int childExitStatus;
            waitpid( id, &childExitStatus, 0);
            if( !WIFEXITED(childExitStatus) )
            {
                cerr << "waitpid() exited with an error: Status= " << WEXITSTATUS(childExitStatus) << endl;
                return 0;
            }
            else if( WIFSIGNALED(childExitStatus) )
            {
                cerr << "waitpid() exited due to a signal: " << WTERMSIG(childExitStatus) << endl;
                return 0;
            }

            infile.open("results.txt");
            infile >> result;
            infile.close();
            output << setprecision(6) << *xparam << " " << setprecision(6) << *yparam << " " << setprecision(16) << result <<  endl;
            if(i % (int)(numSteps1 * numSteps2/10) == 0)
            {
                cout << counter << "0%" << endl;
                counter++;
            }
            i++;
        }        
    }
    time(&time2);
    output << "Time to run: " << difftime(time2, time1) << endl;    
    return 0;
}
