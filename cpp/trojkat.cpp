/*
 * trojkat.cpp
 * program pobiera trzy boki trójkąta
 * sprawdza czy da sie z nich zbudodować trójkąt
 * oblicza obwód i pole (ze wzoru Herona)
 * i drukuje na ekranie odpowiedni komunikat
 */


#include <iostream>
#include <cmath>

using namespace std;

int main(int argc, char **argv)
{
    int a, b, c;
    float obwod = 0;
    float p = 0;
    a = b = c = 0;
    cout << "Podaj trzy boki trójkąta:";
    cin >> a >> b >> c;
    if (a + b > c && a + c > b && c + b > a) 
    {
        cout << "Mozna zbudowac trojkąt!!!" << endl;
        obwod = a + b + c;
        cout << "obwod =" << obwod << endl;
        p = 0.5 * obwod;
        cout << "p =" << p << endl;
        cout << "pole =" << sqrt (p*(p - a)*(p - b)*(p - c)) << endl;
    } else 
    { cout << "Nie można zbudować trójkąta" << endl;
    }
    return 0;
}

