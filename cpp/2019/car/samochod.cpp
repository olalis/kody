/*
 * samochod.cpp
 */
#include <iostream>
#include <cstdlib>
#include "car.h"
#include "osoba.h"

using namespace std;

int main(int argc, char **argv)
{   
	Car s1 = Car();
    s1.dodaj();
    s1.dane();
    s1.laduj(3);
    s1.pasazerowie();

	return 0;
}

