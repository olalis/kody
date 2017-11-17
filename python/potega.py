#!/usr/bin/env python
# -*- coding: utf-8 -*-
# a0 = 1
# a1 = a
# an = a * ... * a (n-czynników) dla N+ - {0, 1}


def potega_it(podstawa, wykladnik):
    wynik = 1
    for i in range(wykladnik):
        wynik = wynik * podstawa
    return wynik


def main(args):
    podstawa = int(input('Podaj podstawę: '))
    wykladnik = int(input('Podaj wykładnik: '))

    assert type(podstawa) == int
    assert type(wykladnik) == int

    assert potega_it(100, 0) == 1
    assert potega_it(100, 1) == 100
    assert potega_it(2, 3) == 8

    print('Wynik: ', potega_it(podstawa, wykladnik))
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
