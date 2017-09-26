#include "SweepRunInstance.h"

using namespace std;

sweepRunInstance::sweepRunInstance()
{
    xparam = 0;
    yparam = 0;

}

sweepRunInstance::sweepRunInstance(string outFile, string starFileName, int w, background bg, const stream * str, int numStreams, area ar, double x, double y) : runInstance(starFileName, w, bg, str, numStreams, ar)
{
    outputFileName = outFile;
    
    xparam = x;
    yparam = y;
}

sweepRunInstance::~sweepRunInstance()
{
}

int sweepRunInstance::printLikelihood()
{
    ofstream output; 
    output.open(outputFileName.c_str(), fstream::app);
    if(!output.is_open())
    {
        cerr << "Failed to open output file " << outputFileName << endl;
        return -1;
    }
    output << xparam << " " << yparam << " " << setprecision(16) << likelihood <<  endl;
    output.close();
    return 0;
}

