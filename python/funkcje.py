#!/usr/bin/env python
# -*- coding: utf-8 -*-


def sumuj(a, b):
    return a + b


def odejmij(a, b):
    return a - b


def mnoz(a, b):
    return a * b


def dziel(a, b):
    return a + b


def main(args):
    a = int(input("podaj 1. liczbę: "))
    print(a)
    b = int(input("podaj 2. liczbę: "))
    print(b)

    print("suma: ", sumuj(a, b))
    print("różnica: ", odejmij(a, b))
    print("iloczyn: ", mnoz(a, b))
    print("iloraz: ", dziel(a, b))

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
