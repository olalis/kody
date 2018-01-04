/*
 * rekurencja1_kl2ag2_lis.cpp
 */


#include <iostream>

using namespace std;

int fun1_rek(int n)
{
    if (n == 1)
    {
        return 1;
    }
    if (n == 2)
    {
        return 2;
    }
    return (fun1_rek (n - 1)) + (2 * n) + (fun1_rek (n - 2));
}

int main(int argc, char **argv)
{
	int n = 0;
    cout << "Podaj numer wyrazu: " << endl;
    cin >> n;
    
    cout << "Wynik: " << fun1_rek(n) << endl;
    
	return 0;
}

