/*
 * bmi.cpp
 */


#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    float a = 0;
    float b = 0;
    float c = 0;
    int ile = 0;
    int i = 0;
    
    cout << "Ile razy chcesz skorzystac z programu?" << endl;
    cin >> ile;
    
    while (i < ile)
    {
        cout << "Podaj masę ciała:" << endl;
        cin >> a;
        cout << "Podaj wzrost:" << endl;
        cin >> b;
        
        while (b > 4)
        {
            b = b/10;
        }
        
        c=a/(b*b);
        cout << c << endl;
        
        if (c < 18.5)
        {
            cout << "niedowaga" << endl;
        }
        else if (c < 25 )
        { 
            cout << "norma" << endl;
        }
        else if (c < 30)
        { 
            cout << "nadwaga" << endl;
        }
        else if (c >= 30)
        { 
            cout << "otyłość" << endl;
        }
        i = i + 1;
    }
    return 0;
}

