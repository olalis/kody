/*
 * car.cpp
 */
#include <iostream>
#include <cstdlib>
#include "car.h"
#include <string>

using namespace std;

Car::Car() {
    marka = model = "";
    rocznik = przebieg = 0;
}

Car::Car(string mr, string ml, int r, int p) {
    if (r < 1900) r = 1901;
    marka = mr;
    model = ml;
    rocznik = r;
    przebieg = p;
}

Car::dodaj(){
    cout << "Dodaj samochód" << endl;
    cout << "Marka: "; cin >> marka;
    cout << "Model: "; cin >> model;
    cout << "Rocznik: "; cin >> rocznik;
    cout << "przebieg: "; cin >> przebieg;
    
}

Car::dane(){
    cout << "\nTwoje Piękne auto: " << endl;
    cout << "Marka: " << marka << endl;
    cout << "Model: " << model << endl;
    cout << "Rocznik: " << rocznik << endl;
    cout << "przebieg: " << przebieg << endl;
    
}
