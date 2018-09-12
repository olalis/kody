/*
 * funkcje.cpp
 * 
 */


#include <iostream>

using namespace std;

float dodaj(float a, float b)
{
    return a+b;
}

float odejmij (float c, float d)
{
    return c - d;
}

float mnoz(float e, float f)
{
    return e * f;
}

float dziel (float g, float h)
{
    if (h == 0)
    {
        cout << "Nie dzieli sie przez 0!" << endl;
        return 0;
    }
    return g/h;
}     

int main(int argc, char **argv)
{
    float a, b;
    a = b = 0;
    char znak; 
    int czy = 1;
    
    while (czy != 0)
    {
        cout << "Podaj znak:" << endl;
        cin >> znak;
        cout << "Podaj dwie liczby:" << endl;
        cin >> a >> b ;
        if (znak == '+')
        {
            cout << dodaj(a, b)<< endl;
        }
        else if (znak == '-')
        { 
            cout << odejmij(a, b) << endl;
        }
        else if (znak == '*')
        { 
            cout << mnoz(a, b) << endl;
        }
        else if (znak == '/')
        { 
            cout << dziel(a, b) << endl;
        }
        
        cout << "Czy chcesz wykonać jakieś działanie ponownie? (wpisz 1 jeśli tak lub 0 jeśli nie) "<<endl;
        cin >> czy;
    }
    
    
    return 0;
}

