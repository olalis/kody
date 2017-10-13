/*
 * petle_switch.cpp
 * Program pobiera numer miesiąca i wyświetla jego nazwę
 */


#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    int m = 0;
    //while (1)
    //{
        //cout << "Podaj miesiąc:" << endl;
        //cin >> m;
        //if (m < 13 && m > 0)
            //break;
    //}
    
     while (m < 1 || m > 12)// pętla zaporowa
    {
        cout << "Podaj miesiąc (1 - 12):" << endl;
        cin >> m;
    }
    
    //if (m == 1)
        //cout << "Styczeń" << m << endl;
    //else if (m == 2)
        //cout << "Luty" << m << endl;
    //else if (m == 3)
        //cout << "Marzec" << m << endl;
    
    switch(m) 
    {
        case 1:
            cout << "Styczeń";
        break;
        case 2:
            cout << "Luty";
        break;
        case 3:
            cout << "Marzec";
        break;
        case 4:
            cout << "Kwiecień";
        break;
        case 5:
            cout << "Maj";
        break;
    }
    
    return 0;
}

