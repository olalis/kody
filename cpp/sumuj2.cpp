/*
 * sumuj.cpp
 * 
 */


#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    int suma = 0; //suma kolejnych cyfr
    int liczba = 0; //liczba wprowadzana
    
    
    for(;;) //petla nieskończona 
    {
        cout << "podaj liczbe:" << endl;
        cin >> liczba;
        //suma = suma + liczba
        suma += liczba;
        if (suma > 100) break;
        
    }
    cout << "suma:" << suma << endl;
    return 0;
}

