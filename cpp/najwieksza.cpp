/*
 * hello.cpp
 * pobierz dwie liczby wyjściowe od użytkownika i wydrukuj wiekszą
 */


#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    int a, b;
    a = b = 0;
    cout << "Podaj dwie liczby:";
    cin >> a >> b;
    if (a > b) 
    {
        cout << "Większe a=";
        cout << a;
    } else if (b > a) 
    {
        cout << "Większe b=";
        cout << b;
    }else //if (a == b) 
    {
        cout << "równe, a=" << a << ", b=" << b;
    }
    return 0;
}

