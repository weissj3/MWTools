#ifndef _HESSIAN_H_
#define _HESSIAN_H_

#include "BasicMWClass"


class hessian : public basicMWClass
{
private:

    matrix Matrix;
    scheduler * Sched;




public:
    hessian();
    hessian(scheduler * sched, std::string paramFile);
    int calculate();
    double derivative(std::string param, double step, 


};

#endif

