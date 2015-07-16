#ifndef _BASICMWCLASS_H_
#define _BASICMWCLASS_H_
#include "Util.h"

//Used for reading input file
class comma_ctype : public std::ctype<char>
{
private:
    mask comma_table[table_size];

public:
    comma_ctype(size_t refs = 0) : ctype<char>(&comma_table[0], false, refs)
    {
        for(int i = 0; i < 256; i++)
        {
            comma_table[i] = classic_table()[i];
        }
        comma_table[','] = (mask)space;
    }
};


class basicMWClass
{
private: 
    bool initialized; 
    void init(std::ifstream &infile);

protected:
    int wedge;
    area AREA;
    background BG;
    stream * STR;
    int numStreams;
    int print_file();

public:
    ~basicMWClass();
    basicMWClass() { initialized = false; }
    basicMWClass(std::string paramFile);
    basicMWClass(const basicMWClass & BMWC);
    basicMWClass(int w, const area & a, const background & b, const std::vector <stream> & s);
    basicMWClass(int w, const area & a, const background & b, const stream * s, int numstreams);

    double * getParamByName(std::string paramName);
    void cleanup();
};

#endif

