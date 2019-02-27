/*
 * wskazniki.cpp
 */


#include <iostream>
using namespace std;

int main(int argc, char **argv)
{
    int i = 13;
    float j = 12.2345;
    int *wsk1; // deklaracja wzskażnika do liczby całkowitej
    float *wsk2; // deklaracja wzskażnika do liczby zmiennoprzecinkowej
    wsk1 = &i;
    wsk2 = &j;
    cout << i << endl;
    cout << wsk1 << endl;
    cout << j << endl;    
    cout << wsk2 << endl;
    cout << *wsk1<< endl;
    *wsk1 = (int)*wsk2;
    cout << *wsk1<< endl;
    
    return 0;
}

