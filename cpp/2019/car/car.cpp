/*
 * car.cpp
 */
#include <iostream>
#include <cstdlib>
#include "car.h"
#include "osoba.h"

using namespace std;

Car::Car() {
    marka=model="";
    rocznik=przebieg=0;
}

Car::Car(string mr, string ml, int r, int p) {
    if (r <= 1990) r = 1990;
    marka = mr;
    model = ml;
    rocznik = r;
    przebieg = p;
}

void Car::dodaj() {
    cout << "Dodaj samochód:"<< endl;
    cout << "Marka: "; cin>>marka;
    cout << "Model: "; cin>>model;
    cout << "Rocznik: "; cin>>rocznik;
    cout << "Przebieg: "; cin>>przebieg;
}

void Car::dane() {
    cout << "\nTwoje piękne auto:"<< endl;
    cout << "Marka: " << marka << endl;
    cout << "Model: " << model << endl;
    cout << "Rocznik: " << rocznik << endl;
    cout << "Przebieg: " << przebieg << endl;
}

void Car::laduj(int ile) {
    cout << "Ile osób chcesz wziąść: "; cin>>ile;
    for(int i=0; i < ile; i++){
        Osoba osoby[i];
        cout << "Dodaj osobę:"<< endl;
        cout << "Imię: "; cin>> osoby[i].imie;
        cout << "Nazwisko : "; cin>> osoby[i].nazwisko;
        cout << "Wiek: "; cin>> osoby[i].wiek;
        cout << "Płeć: "; cin>> osoby[i].plec;
        
    }
}

void Car::pasazerowie() {
    for(int i=0; i < ile; i++){
        cout << "\nTwoj pasażer" << i+1 <<" :"<< endl;
        cout << "Imię: " << osoby[i].imie << endl;
        cout << "Nazwisko: " << osoby[i].nazwisko<< endl;
        cout << "Wiek: " << osoby[i].wiek << endl;
        cout << "Płeć: " << osoby[i].plec << endl;
    }
}
