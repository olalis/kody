/*
 * binarnie.cpp
 */


#include <iostream>

using namespace std;

int wyszukaj_liniowo(int l[], int n, int el)
{
    for(int i = 0; i < n; i++)
    {
        if(l[i] == el)
        return i;
    }
    return  -1;
 }

int main(int argc, char **argv)
{
    int lista [] = {4, 3, 7, 0, 2, 3, 1, 9, -4};
    int el = 3;
    int n = 9;
    
    cout << wyszukaj_liniowo(lista, n, el) << endl;
    return 0;
}
