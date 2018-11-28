#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  funkcje_skladnia2.py


def mnoz(a, b):
    print (a * b)


def mnoz2(*args):  # zmniena lista argumnetów
    wynik = 1
    for liczba in args:
        wynik *= liczba
    print(wynik)


def wylicz(imie1="adam", imie2="ewa", **kwargs):  # Słownik zmiennej długości
    print(imie1)
    print(imie2)
    for k, v in kwargs.items():
        print('{} {}'.format(k, v))


def main(agrs):
    # mnoz(4, 6)
    # mnoz2(4, 6, 8, 9, 3)
    wylicz(imie1="adam", imie2="ewa", imie3="ola")
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
