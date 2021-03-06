#include "Hessian.h"
#include <armadillo>

using namespace std;

hessian::hessian(string paramFile, string starFileName, scheduler * sched, const vector <double> &stepSizes)
{
    if(!sched)
    {
        throw string("Hessians require a scheduler");
    }
    Scheduler = sched;
    StarFileName = starFileName;
//Read in basic parameters from file
    Params = parameters(paramFile);
    StepSizes = stepSizes;
    initialized = true;
}

hessian::~hessian()
{
    cleanup();
}

void hessian::cleanup()
{
    if(initialized)
    {    
        initialized = false;  
    }
}

int hessian::run(std::string outputFileName, bool append)
{
    if(!initialized)
    {
        cerr << "Must initialized before running hessian" << endl;
        return -1;
    }
    //Clean out old file
    ofstream output;
    if(append)
    {
        output.open(outputFileName.c_str(), ios::out|ios::app);
    }
    else
    {
        output.open(outputFileName.c_str());
    }
    //Queue up all of the likelihood calculations for the second derivatives
    for(int i = 0; i < Params.numParams(); i++)
    {
        for(int j = i; j < Params.numParams(); j++)
        {
            parameters tempParams = Params;
            tempParams[i] = tempParams[i] + StepSizes[i];
            if( i!=j ) tempParams[j] = tempParams[j] + StepSizes[j];
            Scheduler->requestRun(new runInstance(StarFileName, tempParams));
            tempParams = Params;
            tempParams[i] = tempParams[i] + StepSizes[i];
            tempParams[j] = tempParams[j] - StepSizes[j];
            Scheduler->requestRun(new runInstance(StarFileName, tempParams));
            tempParams = Params;
            tempParams[i] = tempParams[i] - StepSizes[i];
            tempParams[j] = tempParams[j] + StepSizes[j];
            Scheduler->requestRun(new runInstance(StarFileName, tempParams));
            tempParams = Params;
            tempParams[i] = tempParams[i] - StepSizes[i];
            if (i != j) tempParams[j] = tempParams[j] - StepSizes[j];
            Scheduler->requestRun(new runInstance(StarFileName, tempParams));
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
    //Request Results from all likelihood calculations and finish derivative calculations
    arma::Mat <double> hessian(Params.numParams(), Params.numParams());
    vector<runInstance*> finishedRuns = Scheduler->getFinishedRuns();

    int count = 0;
    for( int i = 0; i < Params.numParams(); i++ )
    {
        for( int j = i; j < Params.numParams(); j++)
        {
            if(!(finishedRuns[count * 4] && finishedRuns[count * 4 + 1] && finishedRuns[count * 4 + 2] && finishedRuns[count * 4 + 3]))
            {
                cerr << "Missing Run Results" << endl;
                Scheduler->cleanup();
                return -1;
            }
            hessian(i, j) = (finishedRuns[count * 4]->getLikelihood() - finishedRuns[count * 4 + 1]->getLikelihood() - finishedRuns[count * 4 + 2]->getLikelihood() + finishedRuns[count * 4 + 3]->getLikelihood()) / (4.0 * StepSizes[i] * StepSizes[j]);
            if (i == j) hessian(i,j) = hessian(i,j) * 4.0;
            hessian(j,i) = hessian(i,j);
            count++;
        }
    }
    arma::Mat <double> varience = hessian.i();

    output << "Hessian:\n"
           << hessian << endl
           << "Varience:\n"
           << varience << endl;

    output << "Errors:";
    for(int i = 0; i < Params.numParams(); i++)
    {
        output << "   " << sqrt(2.0 * abs(varience(i, i)));
    }
    output << endl;

    Scheduler->cleanup();

    return schedulerStatus;

}

 
