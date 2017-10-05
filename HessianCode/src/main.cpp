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
    int NumGPUs;
    int RunsPerGPU;
    int numCores;
    string temp;
    string sepPath, paramsPath, starFileName, outputFileName;
    infile >> temp >> sepPath >> temp >> paramsPath >> temp >> starFileName;
    infile >> temp >> outputFileName;
    infile >> temp >> NumGPUs >> temp >> RunsPerGPU >> temp >> numCores;
    cout << "Using: " << sepPath << ", " << paramsPath << "," << starFileName << ", " << NumGPUs << ", " << numCores << endl;
    clock_t timer;
    scheduler * Scheduler;
    hessian * Hessian;
    while(!infile.eof())
    {
        infile >> temp;
        if(temp == "<Steps>")
        {
            vector <double> stepSizes;
            while(1)
            {
                infile >> temp;
                if(temp == "</Steps>")
                {
                    break;
                }
                stepSizes.push_back(stod(temp));
            }
            cout << "Using Step Sizes:";
            for( int i = 0; i < stepSizes.size(); i++ )
            {
                cout << " " << stepSizes[i];
            }
            cout << endl;
            Scheduler = new scheduler(NumGPUs, RunsPerGPU, numCores, sepPath);
            try
            {
                Hessian = new hessian(paramsPath, starFileName, Scheduler, stepSizes);
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
            Hessian->cleanup(); 
            delete Hessian;
            delete Scheduler;
        }
    }
    return 0;
}
