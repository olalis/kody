/*
 * kl2ag2_Lis_ulamek.cpp
 */


#include <iostream>

using namespace std;

int zliczaj (int n)
{
    int i = 0;
    int w = 100;
    
    while (i != n)
    {
        w += 10;
        i += 1;
    }
    return w;
}


int main(int argc, char **argv)
{
    int n = 0;
    cout << "Podaj liczbe miesięcy: " << endl;
    cin >> n;
    
	cout << "Stan konta po " << n << "miesiącach:" << zliczaj (n) << endl;
    
	return 0;
}

