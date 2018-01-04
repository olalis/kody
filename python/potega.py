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

# a0 = 1 - warunek brzegowy
# an = a(n- 1) * a dla n > 0


def potega_rek(podstawa, wykladnik):
    if wykladnik == 0:
        return 1
    return potega_rek(podstawa, wykladnik - 1) * podstawa


def main(args):
    podstawa = int(input('Podaj podstawę: '))
    wykladnik = int(input('Podaj wykładnik: '))

    assert type(podstawa) == int
    assert type(wykladnik) == int

    assert potega_it(100, 0) == 1
    assert potega_it(100, 1) == 100
    assert potega_it(2, 3) == 8
    assert potega_rek(100, 0) == 1
    assert potega_rek(100, 1) == 100
    assert potega_rek(2, 3) == 8

    print('Wynik: ', potega_it(podstawa, wykladnik))
    print('Wynik: ', potega_rek(podstawa, wykladnik))
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
