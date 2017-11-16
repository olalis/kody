#!/usr/bin/env python
# -*- coding: utf-8 -*-
# a0 = 1
# a1 = a
# an = a * ... * a (n-czynników) dla N+ - {0, 1}

    
def potega_it(podstawa, wykladnik):
    
    i = 1
    wynik = 1
    while i <= wykladnik:
        wynik = wynik * podstawa
        i = i + 1
        
    return wynik
        


def main(args):
    podstawa = int (input ('Podaj podstawę: '))
    wykładnik = int (input ('Podaj wykładnik: '))
    
    print('Wynik: ', potega_it(podstawa, wykładnik))
    
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
