#include "RunInstance.h"

using namespace std;

runInstance::runInstance()
{
    likelihood = 1;
    runId = 0;
    xparam = 0;
    yparam = 0;
}

runInstance::runInstance(background bg, const stream * str, int numStreams, area ar, double x, double y)
{
    likelihood = 1;
    runId = 0;
    BG = bg;

    for(int i = 0; i < numStreams; i++)
    {
        STR.push_back(str[i]);
    }

    AREA = ar;
    xparam = x;
    yparam = y;
}
    
bool runInstance::isRunning()
{
    return runId;
}

bool isFinished()
{
    if(likelihood < 0)
    {
        return true;
    }

    return false;
}

int runInstance::printParams(string filename)
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


int runInstance::printLikelihood(string filename)
{
    



}









    
