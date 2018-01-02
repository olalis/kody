/*
 * rekurencja6_kl2ag2_lis.cpp
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

int f4_rek(int tab [], int i)
{
    if (i == 1)
    {
        return tab[0];
    }
    return tab[i - 1];
}


int main(int argc, char **argv)
{
    int rozmiar = 0;
    cout << "Ile liczb podasz?" << endl;
    cin >> rozmiar ;
    
    int liczby [rozmiar];
    
    pobierzDane(liczby, rozmiar);
    
    cout << ": " << f4_rek(liczby, rozmiar) << endl;
    
	return 0;
}

