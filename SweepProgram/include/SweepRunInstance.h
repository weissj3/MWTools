#include "RunInstance.h"

class sweepRunInstance : public runInstance
{
private:

    std::string outputFileName;

    double xparam;
    double yparam;


public:

    sweepRunInstance();

    sweepRunInstance(std::string outFile, std::string starFileName, int w, background bg, const stream * str, int numStreams, area ar, double x, double y);

    ~sweepRunInstance();

    int printLikelihood();

};

