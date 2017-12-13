/*
 * fibonacci.cpp
 */


#include <iostream>

using namespace std;

int fib_iter(int n)
{
    if ( n == 0)
        return 0;
    else if ( n == 1)
        return 1;
    int a = 0;
    int b = 1;
    int tmp;
    cout << a << endl;
    for (int i = 1 ; i < n; i++) 
    {   tmp = b;
        b = a + b;
        a = tmp;
        cout << a << " " << b << " " << "Iloraz: " << b / a << endl;
    }
    cout << a << " " << b << " " << "Iloraz: " << b / a << endl;
    return b;
}

int fib_rek(int n)
{
    if (n < 2)
    {
        return 1;
    }
    return fib_rek(n - 2) + fib_rek(n - 1);
}

int main(int argc, char **argv)
{
    int n = 0;
    cout << "Numer wyrazu ciągu: " << endl;
    cin >> n;
    cout << fib_iter(n) << endl; 
    cout << "  " << endl; 
    cout << fib_rek(n) << endl; 
       
    return 0;
}

