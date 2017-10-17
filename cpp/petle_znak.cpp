/*
 * petle_switch.cpp
 * Program pobiera numer miesiąca i wyświetla jego nazwę
 */


#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    char zn = 't'; // deklaracja
    
     while (zn == 't' || zn == 'T' || zn == 'n' || zn == 'N')
    {
        cout << "Podaj znak:" << endl;
        cin >> zn;
    }
    
    //while (true)
    //{
        //cout << "Podaj znak:" << endl;
        //cin >> zn;
        //if (zn == 't' || zn == 'T' || zn == 'n' || zn == 'N')
            //cout << zn << endl;
        //else
            //break;
    //}
    

    
    return 0;
}

