/*************************************************************************************
*                           Generates .lua Parameter Files                            *
*                                                                                     *
*                           Changeable Variables:                                     *
*                           lines: 47, 48 (interval info)                             *
*                           lines: 50-69 (Initial Parameters)                         *
*                           lines: 72, 108 (Changing Parameter)                       *
*                                                                                     *
*                                                                                     *
*                                                                                     *
*                                                                                     *
**************************************************************************************/
#include "Sweep.h"

using namespace std;



int main (int argc, char* argv[]) 
{
    if(argc < 2)
    {
        cout << "Proper Usage <Input file> <Path to Separation>" << endl;
        return -1;
    }
    clock_t timer;
    sweep Sweep1;
    try
    {
        Sweep1 = sweep(argv[1]);
    }
    catch(string error)
    {
        cerr << error << endl;
        return -1;
    }    
    
    time_t time1, time2;
    time(&time1);

    if(Sweep1.run(argv[2], "list.txt"))
    {
        return -1;
    }

    time(&time2);
    cout << "Time to run: " << difftime(time2, time1) << endl;    
    return 0;
}
