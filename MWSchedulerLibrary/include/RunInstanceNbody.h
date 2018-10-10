#ifndef _RUNINSTANCENBODY_H_
#define _RUNINSTANCENBODY_H_
#include "RunInstance.h"
#include "NbodyParameters.h"

class runInstanceNbody: public runInstance
{
private:

    std::string HistogramFileName;
    std::string LuaFileName;

    nbodyParameters Params;

    virtual pid_t run(std::string pathToBin, unsigned int Id, std::string commandLine);


public:

    runInstanceNbody();
    runInstanceNbody(std::string histFN, std::string luaFN, nbodyParameters params);
    
};

#endif
