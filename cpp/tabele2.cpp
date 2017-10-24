/*
 * tabele2.cpp
 */


#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    // const int ROZMIAR = 5;
    int rozmiar = 0;
    cout << "Ile ocen podasz?" << endl;
    cin >> rozmiar ;
    
    int liczby [rozmiar];
    int i;
    int suma = 0;
    
    cout << "Podaj 5 ocen (0-6): " << endl;
    
    for (i = 0; i < rozmiar; i++)
    {
        cin >> liczby [i];
    }
    
    cout << "Podane liczby: " << endl;
    
    for (i = 0; i < rozmiar; i++)
    {
        cout << liczby [i] << " " << endl;
        suma += liczby[i];
    }
    
    cout << "Suma liczb: " << suma << endl;
    
    cout << "średnia artmetyczna: " << float(suma)/float(rozmiar) << endl;
    
    
    
    
    return 0;
}

