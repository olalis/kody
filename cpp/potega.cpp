/*
 * potega.cpp
 */


#include <iostream>

using namespace std;

int potega_it(int podstawa, int wykladnik)
{
    int wynik = 1;
    int i = 1;
    while (i <= wykladnik)
    {
        wynik = wynik * podstawa;
        i = i + 1;
    }
    return wynik;
}   

int potega_rek(int podstawa, int wykladnik)
{
    if (wykladnik == 0)
    {
        return 1;
    }
    return potega_rek(podstawa, wykladnik - 1) * podstawa;
}

int main(int argc, char **argv)
{
    int podstawa = 0;
    int wykladnik = 0;
    
    cout << "Podaj podstawę: " ;
    cin >> podstawa ; 
    cout << "Podaj wykładnik: " ;
    cin >> wykladnik ; 
    
    cout << "Wynik: " << potega_it(podstawa, wykladnik) << endl;
    cout << "Wynik: " << potega_rek(podstawa, wykladnik) << endl;
    
    return 0;
}


