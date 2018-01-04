/*
 * kl2ag2_Lis_dzielniki.cpp
 
 */


#include <iostream>


using namespace std;

int main(int argc, char **argv)
{
    int a = 0;
    
    cout << "Podaj liczbe: ";
    cin >> a;
    
    int i = 1;
    int suma = 0;
    
    while (i != (a + 1))
    {
        if (a % i == 0)
        {
            suma += 1;
            i += 1;
        }
    }
	cout << "Ilość dzielników: " << suma << endl; 
    
	return 0;
}

