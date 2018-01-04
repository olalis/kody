/*
 * kl2ag2_Lis_petla3.cpp
 */


#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
	int n = 0;
	int m = 0;
    
	cout << "Podaj szerokość: " << endl;
    cin >> n;
	cout << "Podaj wysokość: " << endl;
    cin >> m;
    
    int i = 1;
    
    if ( i > n)
    {
        cout << "Nie istnieje taki prostokąt" << endl;
    }
    if ( i == n)
    {
        while (i != m + 1)
        {
            cout << "*" << endl;
            i += 1;
        }
    }
    else
    {
        while (i != m)
        {
            cout << "*";
            i += 1;
        }
        cout << "*" << endl;
        
        int j = 1;
        while (j != m - 1)
        {
            int k = 1;
            cout << "*";
            while (k != (m - 1))
            {
                cout << "#";
                k += 1;
            }
            cout << "*" << endl;
            j += 1;
        }
        int c = 1;
        while (c != m)
        {
            cout << "*";
            c += 1;
        }
        cout << "*" << endl;
    }
    
        
    
	return 0;
}

