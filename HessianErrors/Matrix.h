#ifndef _MATRIX_H_
#define _MATRIX_H_

class matrix
{
private:
    doube ** values;
    unsigned int m, n;
    bool initialized;

public:
    matrix();
    matrix(const matrix & mat);
    ~matrix();
    matrix(unsigned int sizem, unsigned int sizen);

    void setM(unsigned int y, unsigned int x, double value);
    double getM(unsigned int y, unsigned int x);
    void scale(double s);

};

#endif

