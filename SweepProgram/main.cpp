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
#include "Sweep.h"

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
    cout << "Using: " << sepPath << ", " << paramsPath << ", " << gpu << ", " << numCores << endl;
    clock_t timer;
    scheduler * Scheduler;
    sweep * Sweep;
    while(!infile.eof())
    {
        string pName1, pName2, outputFileName;
        double min1, max1, step1, min2, max2, step2;
        infile >> pName1 >> temp >> min1 >> temp >> max1 >> temp >> step1 >> pName2 >> temp >> min2 >> temp >> max2 >> temp >> step2 >> temp >> outputFileName;
        cout << "Running Sweep with Params:" << endl;
        cout << pName1 << endl << "Min: " << min1 << endl << "Max: " << max1 << endl << "Steps: " << step1 << endl;
        cout << pName2 << endl << "Min: " << min2 << endl << "Max: " << max2 << endl << "Steps: " << step2 << endl;
        Scheduler = new scheduler(gpu, numCores, sepPath);
        try
        {
            Sweep = new sweep(paramsPath, Scheduler, pName1, min1, max1, step1, pName2, min2, max2, step2);
        }
        catch(string error)
        {
            cerr << error << endl;
            return -1;
        } 
        time_t time1, time2;
        time(&time1);
        if(Sweep->run(outputFileName) < 0)
        {
            return -1;
        }
        time(&time2);
        cout << "Time to run: " << difftime(time2, time1) << endl;   
        Sweep->cleanup(); 
        delete Sweep;
        delete Scheduler;
    }
    return 0;
}
