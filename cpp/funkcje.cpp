/*
 * funkcje.cpp
 * 
 */


#include <iostream>

using namespace std;

void dodaj(int a, int b) // dleklaracja funkcji
{
    cout << "Suma: " << a+b << endl;
}

int odejmij (int l1, int l2)
{
    return l1-l2;
}

void mnoz(int c, int d)
{
    cout << "Iloczyn: " << c*d << endl;
}

int dziel (int e, int f)
{
    if (f == 0)
    {
        cout << "Nie dzieli sie przez 0!" << endl;
        return 0;
    }
        return e/f;
    
}

int main(int argc, char **argv)
{
    int a, b;
    a = b = 0;
    
    cout << "Podaj dwie liczby:" << endl;
    cin >> a >> b;
    
    dodaj(a, b); // wywołanie funkcji 
    cout << "Różnica: " << odejmij (a, b) << endl;
    mnoz (a, b);
    cout << "Iloraz: " << dziel (a, b) << endl;
    
    return 0;
}

