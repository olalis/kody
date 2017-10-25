/*
 * tabele2.cpp
 */


#include <iostream>

using namespace std;

void pobierzDane (int tab [], int ile)
{
    int i;
    cout << "Podaj " << ile << " liczb:" << endl;
    for (i = 0; i < ile; i++)
    {
        cin >> tab [i];
    }
}

int sumuj (int tab [], int ile)
{
    int i = 0;
    int suma = 0;
    cout << "Podane liczby: " << endl;
    for (i = 0; i < ile; i++)
    {
        cout << tab [i] << " " << endl;
        suma += tab[i];
    }
    return suma;
}

int liczsrednia (int tab [], int ile)
{
    return sumuj(tab, ile)/(ile);
    
}


int main(int argc, char **argv)
{
    // const int ROZMIAR = 5;
    int rozmiar = 0;
    cout << "Ile ocen podasz?" << endl;
    cin >> rozmiar ;
    
    int liczby [rozmiar];
    //int suma = 0;
    
    pobierzDane(liczby, rozmiar);
    
    cout << "Suma liczb: " << sumuj(liczby, rozmiar) << endl;
    
    cout << "średnia artmetyczna: " << liczsrednia(liczba, rozmiar) << endl;
    
    
    
    
    return 0;
}

