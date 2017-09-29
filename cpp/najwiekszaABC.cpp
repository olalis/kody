/*
 * hello.cpp
 * pobierz trzy liczby wyjściowe od użytkownika i wydrukuj wiekszą
 */


#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    int a, b, c;
    a = b = c =0;
    cout << "Podaj trzy liczby:";
    cin >> a >> b >> c;
    if (a > b && a > c) 
    {
            cout << "Największe a=" << a;
    } 
    if (b > a && b > c) 
    {
            cout << "Największe b=" << b;
    }
    if (c > a && c > b) 
    {
            cout << "Największe c=" << c;
    }
    if (c == a && c > b) 
    {
            cout << "a równe c" << "  a="<< a << "  c=" << c;
    }
    if (c == b && c > a)
            cout << "b równe c" << "  b="<< b << "  c=" << c;
    
    if (a == b && a > c)
        cout << "a równe b" << "  a="<< a << "  b=" << b;
    
    if (c == b && c == a)
            cout << "a = b = c" << "  a=" << a << "  b="<< b << "  c=" << c;
    

    return 0;
}

