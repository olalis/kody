/*
 * silnia.cpp
 */


#include <iostream>

using namespace std;

int silnia_it(int liczba)
{
    int wynik = 1;
    int i = 1;
    while (i <= liczba)
    {
        wynik = wynik * i;
        i = i + 1;
    }
    return wynik;
}   

int silnia_rek(int liczba)
{
    if (liczba < 2)
    {
        return 1;
    }
    return silnia_rek(liczba - 1) * liczba;
}

int main(int argc, char **argv)
{
    int liczba = 0;
    
    cout << "Podaj liczbę: " ;
    cin >> liczba ; 
    
    cout << "Wynik: " << silnia_it(liczba) << endl;
    cout << "Wynik: " << silnia_rek(liczba) << endl;
    
    return 0;
}

