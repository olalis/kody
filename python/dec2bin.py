#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  dec2bin.py
#  


def main(args):
    
    znakA = 'A'
    znakB = 'B'
    l14 = 14
    l15 = 15
    print(znakA, znakB)
    print(l14, l15)
    
    reszty[16]
    liczba = 0
    
    podstawa = 0
        
    print("Podaj liczbę i podstawę: ")
    input ( liczba, podstawa)
    
    i = 0; # indeks tabeli
    
    reszty[i] =  liczba % podstawa
    liczba = liczba / podstawa
    i += 1
    
    while liczba > 0:
        reszty[i] =  liczba % podstawa
        liczba = liczba / podstawa
        i += 1
    
    while i - 1 >= 0:
        i -= 1
        print( reszty[i])
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
