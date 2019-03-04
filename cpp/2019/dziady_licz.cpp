/*
 * pliki.cpp
 */

#include <iostream>
#include <fstream>
#include <cstring>
#include <cstdlib>
#include <iomanip>

using namespace std;

// tekst.txt
// tekst.bak


int liczSam(char plik[]) {
    ifstream wejscie(plik);
    if (!wejscie) { cout << "Błąd otwarcia pliku!"; return 0; }
    char plik2[15];
    strcpy(plik2, plik);
    char *wsk;
    wsk = strstr(plik2, ".txt");
    strncpy(wsk, ".bak", 4);
    ofstream wyjscie(plik2);
    if (!wyjscie) { cout << "Błąd otwarcia pliku!"; return 0; }
    
    char z; // pojedynczy odczytany znak
    int ile, ilea, ileo, ilee, ileu, iley, ilei;
    ile = ilea = ileo = ilee = ileu = iley = ilei = 0;
    
    while(!wejscie.eof()) {
        wejscie.get(z);  // odczytanie pojedynczego znaku
        if (wejscie) {
            if ((int)z == 97 or (int)z == 65 ) ilea++;
            if ((int)z == 79 or (int)z == 111 ) ileo++;
            if ((int)z == 69 or (int)z == 101 ) ilee++;
            if ((int)z == 85 or (int)z == 117 ) ileu++;
            if ((int)z == 89 or (int)z == 121 ) iley++;
            if ((int)z == 73 or (int)z == 105 ) ilei++;
        }
    }
    
    wejscie.close(); wyjscie.close();
    cout << setw(10) << "A:" << ilea << endl;
    cout << setw(10) << "O:" << ileo << endl;
    cout << setw(10) << "E:" << ilee << endl;
    cout << setw(10) << "U:" << ileu << endl;
    cout << setw(10) << "Y:" << iley << endl;
    cout << setw(10) << "I:" << ilei << endl;
    return ile;
}




int main(int argc, char **argv)
{
    char nazwa[15];
    cout << "Podaj nazwę pliku: ";
    cin >> nazwa;
    liczSam(nazwa);
    
    
    return 0;
}

