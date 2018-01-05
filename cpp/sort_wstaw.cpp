/*
 * sort_wstaw.cpp
 */


#include <iostream>

using namespace std;

void sort_wstaw_mal(int lista[], int n)
{
    for(int i = 0; i < n; i++)
    {
        int el = lista[i];
        int k = i - 1;
        while (k >= 0 and lista[k] < el)
        {
            lista[k + 1] = lista[k];
            k -= 1;
        }
        lista[k + 1] = el;
    }
 }
 
 void sort_wstaw_ros(int lista[], int n)
{
    for(int i = 0; i < n; i++)
    {
        int el = lista[i];
        int k = i - 1;
        while (k >= 0 and lista[k] > el)
        {
            lista[k + 1] = lista[k];
            k -= 1;
        }
        lista[k + 1] = el;
    }
 }

int main(int argc, char **argv)
{
    int lista [] = {4, 3, 7, 0, 2, 3, 1, 9, -4};
    int lista2 [] = {4, 3, 7, 0, 2, 3, 1, 9, -4};
    int n = 9;
    
    for(int i = 0; i < n; i++)
    {
        cout << lista[i] << " ";
    }
    cout << " " << endl;
    sort_wstaw_mal(lista, n);
    for(int i = 0; i < n; i++)
    {
        cout << lista[i] << " ";
    }cout << " " << endl;
    sort_wstaw_ros(lista2, n);
    for(int i = 0; i < n; i++)
    {
        cout << lista2[i] << " ";
    }
    return 0;
}
