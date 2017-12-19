/*
 * rekurencja6_kl2ag2_lis.cpp
 */


#include <iostream>

using namespace std;

int euklides_rek(int a, int b)
{
    if (b == 0)
    {
        return a;
    }
    return euklides_rek(b, a % b);
}
int main(int argc, char **argv)
{
	int a = 0;
    int b = 0;
    cout << "Podaj liczbę: " << endl;
    cin >> a;
    cout << "Podaj liczbę: " << endl;
    cin >> b;
    
    cout << "Wynik: " << euklides_rek(a, b) << endl;
    
	return 0;
}

