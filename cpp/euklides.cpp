/*
 * potega.cpp
 */


#include <iostream>

using namespace std;

int euklides(int a, int b)
{
    while(a != b)
    {
        if (a > b)
        {
            a = a - b;
        }
        else
        {
            b = b - a;
        }
    }
    return a;
}

int euklides2(int a, int b)
{
    while (a > 0)
    {
        a = a % b;
        b = b - a;
    }
    return b;
}

int main(int argc, char **argv)
{
    int a = 0;
    int b = 0;
    
    cout << "Podaj liczbę: " ;
    cin >> a ; 
    cout << "Podaj liczbę: " ;
    cin >> b ; 
    
    cout << "Wynik: " << euklides(a, b) << endl;
    cout << "Wynik: " << euklides2(a, b) << endl;
    
    return 0;
}


