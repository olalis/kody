#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  trojkat.py

from math import sqrt


def main(args):
    a, b, c = eval(input('Podaj trzy boki trójkąta oddzielone przecinkami :' ))
    print ("Podano boki: {}, {}, {}" .format(a, b, c))
    trojkat = False
    if a + b > c:
        if a + c > b:
            if b + c > a:
                trojkat = True
    if trojkat:
        print("Da się zbudować trójkąt")
        if a**2+ b**2 == c**2:
            print("Trójkąt jest Prostokątny")
        elif c**2+ b**2 == a**2:
            print("Trójkąt jest Prostokątny")
        elif c**2+ a**2 == b**2:
            print("Trójkąt jest Prostokątny")
        else:
            print("trójkąt nie jest prostokątny")
        p = 0.5*(a + b + c)
        pole = sqrt(p*(p - a)*(p - b)*(p - c))
        print('Pole: {:.4f} ' .format(pole))
        
    else:
        print("nie da się zbudować trójkąta")
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
