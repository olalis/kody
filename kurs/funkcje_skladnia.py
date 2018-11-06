#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  funkcje_skladnia.py

# zmienna globalna, zasięg globalny, przestrzeń nazw (namespace) modułu
a, b = 5, 10
print (a + b)


def sumuj1():  # nowa przestrzeń nazw, przestrzeń funkcji
    print(a + b)


def main(args):
    global a, b
    a, b = 2, 3  # zmienne lokalne, zasięg lokalny, przestrzeń funkcji
    print (a + b)
    sumuj1()
    return 0


def odejmij2(lista):
    lista.appent(lista[0] - lista[1])


def odejmij(a, b):
    print(a - b)
    a, b = 4, 3


def main2(args):
    #    a, b = 2, 3
    #    print (a - b)
    #    odejmij(a, b)
    #    print(a - b)
    l = [3, 4]
    odejmij2(l)
    print(l)
    return 0


if __name__ == '__main__':
    # skrypt został uruchominy a nie zaimportowany
    import sys
    sys.exit(main(sys.argv))
