#ifndef _RUNSEPARATIONINSTANCE_H_
#define _RUNSEPARATIONINSTANCE_H_

#include "Util.h"
#include "RunInstance.h"

class runSeparationInstance : public runInstance
{
private:
    std::string StarFileName;

    parameters Params;

protected: 
    virtual pid_t run(std::string pathToBin, unsigned int Id, std::string commandLine);

public:
    runSeparationInstance();
    runSeparationInstance(std::string starFileName, int w, background bg, const stream * str, int numStreams, area ar);
    runSeparationInstance(std::string starFileName, parameters params);
    ~runSeparationInstance();

};

#endif

