/*************************************************************************************
*                           Generates .lua Parameter Files                            *
*                                                                                     *
*                                                                                     *
*                                                                                     *
*                                                                                     *
*                                                                                     *
*                                                                                     *
*                                                                                     *
*                                                                                     *
*                                                                                     *
**************************************************************************************/
#include "Hessian.h"

using namespace std;


//Definitely Better Ways to do file parsing for this
//Maybe I will come back to this project another day.
int main (int argc, char* argv[]) 
{
    if(argc < 1)
    {
        cout << "Proper Usage < Config File >" << endl;
        return -1;
    }

    ifstream infile;
    infile.open(argv[1]);
    if(!infile.is_open())
    {
        cerr << "Failed to open config file." << endl;
        return -1;
    }
    bool gpu;
    int numCores;
    string temp;
    string sepPath, paramsPath;
    infile >> temp >> sepPath >> temp >> paramsPath;
    infile >> temp >> boolalpha >> gpu >> temp >> numCores;
    clock_t timer;
    scheduler * Scheduler;
    hessian * Hessian;
    Scheduler = new scheduler(gpu, numCores, sepPath);
    try
    {
        Hessian = new hessian(paramsPath, Scheduler, pName1, pName2);
    }
    catch(string error)
    {
        cerr << error << endl;
        return -1;
    } 
    time_t time1, time2;
    time(&time1);
    if(Hessian->run(outputFileName) < 0)
    {
        return -1;
    }
    time(&time2);
    cout << "Time to run: " << difftime(time2, time1) << endl;   
    Sweep->cleanup(); 
    delete Sweep;
    delete Scheduler;

    return 0;
}
