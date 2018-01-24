/*
 * cos.cpp
 */


#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    int n = 0;
    cout << "Podaj liczbę: " << endl;
    cin >> n;
    
    int i = 2;
    
    while (true)
    {
        if (i * i > n)
        {
            cout << "Liczba pierwsza." << endl;
            break;
        }
        
        if (i * i <= n || n % i == 0)
        {
            cout << "Liczba złożona." << endl;
            break;
        }
        
        if (i * i <= n  || n % i != 0)
        {
                i = i + 1;
        }
    }
    
    return 0;
}

