#ifndef _NBODYPARAMETERS_H_
#define _NBODYPARAMETERS_H_

#include <vector>
#include "Util.h"

class nbodyParameters: public basicParams
{
public:
    std::vector <double> parameters;

    virtual double& operator[](unsigned int num)
    {
        return parameters[num];
    }
    virtual unsigned int numParams() { return parameters.size(); }

};

#endif
