#include "BasicMWClass.h"

using namespace std;

basicMWClass::basicMWClass(string paramFile)
{
//Read in basic parameters from file
    ifstream infile;
    infile.open(paramFile.c_str());
    if(!infile.is_open())
    {
        throw string("Failed to open init file");
    }
    STR = NULL;
    init(infile);

    initialized = true; 
}

basicMWClass::~basicMWClass()
{
   cleanup();
}

void basicMWClass::cleanup()
{
    if(initialized)
    {    
        initialized = false;  
        if(STR)
        {   
            delete[] STR;
        }
    }
}

basicMWClass::basicMWClass(int w, const area & a, const background & b, const vector <stream> & s)
{
    wedge = w;
    AREA = a;
    BG = b;
    STR = new stream[s.size()];
    for(int i = 0; i < s.size(); i++)
    {
        STR[i] = s[i];
    }
    numStreams = s.size();
    initialized = true;
}

basicMWClass::basicMWClass(int w, const area & a, const background & b, const stream * s, int ns)
{
    if(!s)
    {
        throw string("Tried to initialize basicMWClass with empty stream");
    }
    wedge = w;
    AREA = a;
    BG = b;
    STR = new stream[ns];
    for(int i = 0; i < ns; i++)
    {
        STR[i] = s[i];
    }
    numStreams = ns;
    initialized = true;
}

basicMWClass::basicMWClass(const basicMWClass & BMWC)
{
    if(BMWC.initialized)
    {
        wedge = BMWC.wedge;
        AREA = BMWC.AREA;
        BG = BMWC.BG;
        if(BMWC.STR)
        {
            STR = new stream[BMWC.numStreams];
            for(int i = 0; i < BMWC.numStreams; i++)
            {
                STR[i] = BMWC.STR[i];
            }
        }
        numStreams = BMWC.numStreams;
        initialized = true;
    }
    initialized = false;
}

//Print parameter file for current step.
int basicMWClass::print_file()
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

//Designed to read in from lua file without actually using lua (maybe actually integrate lua interpreter later)
void basicMWClass::init(ifstream &infile)
{
    vector<stream> STRTMP;
    string temp;
    locale x(locale::classic(), new comma_ctype);
    infile.imbue(x);

    infile >> temp >> temp >> wedge
            >> temp >> temp >> temp
            >> temp >> temp >> BG.q
            >> temp >> temp >> BG.r0
            >> temp
            >> temp >> temp >> temp;
    while(1)
    {
            infile >> temp;
            if(temp  == "{")
            {
                STRTMP.push_back(stream());
            }
            else
            {
                break;
            }
            infile >> temp >> temp >> STRTMP[STRTMP.size()-1].epsilon 
                    >> temp >> temp >> STRTMP[STRTMP.size()-1].mu 
                    >> temp >> temp >> STRTMP[STRTMP.size()-1].r
                    >> temp >> temp >> STRTMP[STRTMP.size()-1].theta
                    >> temp >> temp >> STRTMP[STRTMP.size()-1].phi
                    >> temp >> temp >> STRTMP[STRTMP.size()-1].sigma
                    >> temp;
    }
    infile >> temp >> temp >> temp
            >> temp 
            >> temp >> temp >> AREA.r_min
            >> temp >> temp >> AREA.r_max
            >> temp >> temp >> AREA.r_steps
            >> temp >> temp >> AREA.mu_min
            >> temp >> temp >> AREA.mu_max
            >> temp >> temp >> AREA.mu_steps
            >> temp >> temp >> AREA.nu_min
            >> temp >> temp >> AREA.nu_max
            >> temp >> temp >> AREA.nu_steps;

    STR = new stream[STRTMP.size()];
    if(!STR)
    {
        cerr << "New failed" << endl;
    }
    numStreams = STRTMP.size();
    for(int i = 0; i < STRTMP.size(); i++)
    {
        STR[i] = STRTMP[i];
    }
}
