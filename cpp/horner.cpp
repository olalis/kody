/*
 * horner.cpp
 */


#include <iostream>

using namespace std;

// w(x) =  2x^3 + 3x^2 + 5x + 4 (8)
// w(x) = x (2x^2 + 3x = 5) + 4
// w(x) = x ( x (2x + 3) + 5) + 4 (3)

float horner_it(int k, float tab[], float x){
    float wynik = tab[0];
    for (int i = 1; i < (k + 1); i++){
        wynik = wynik * x + tab[i];
    }
    return wynik;
}

int main(int argc, char **argv)
{
    float x = 0;
    float tab[4];
    int stopien = 3;
	
    cout << "Podaj argument: " << endl;
        cin >> x;
        
    for (int i = 0; i < 4; i++) {
        cout << "Podaj argument: " << endl;
        cin >> tab[i];
    }
	
    cout << "Warkość wielomianu: " << horner_it(stopien, tab, x) << endl; 
	return 0;
}

