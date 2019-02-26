/*
 * formatowanie.cpp
 */


#include <iostream>
#include <iomanip>
#include <cstdio>
#include <math.h> // stała M_PI

using namespace std;


int main(int argc, char **argv)
{
    int lint = 100;
    float lrze = 12.546;
    
    //~ios_base::fmtflags fx;
    //~fx |= cout.hex;
    //~fx |= cout.showbase;
    
    //~cout.flags(fx);
    cout << hex << showbase;
    cout << lint << endl;
    
    cout << M_PI << endl;
    cout.precision(3);
    cout << M_PI << endl;
    cout.width(20); // minimalne szerokość pola
    cout.fill('-');
    cout << lrze << endl;
    cout << setw(20) << lrze << endl;
    
    printf("%12f\n", 10*M_PI);
    printf("Hex: %#x\nOct: %#o\n", lint, lint);
    
    return 0;
}

