#!/usr/bin/env python
# -*- coding: utf-8 -*-


def szyfruj(tekst, klucz):
    reszta = len(tekst) % klucz
    if reszta:
        tekst += (klucz - reszta) * "."
    j = 1

    for i in range(klucz):
        print(i)
        i = i + klucz
        if i > len(klucz):
            j += 1
            i = j
    for i in range(klucz):
        for j in range(int(len(tekst) / klucz)):
            print (i + j * klucz, tekst[i + j * klucz])
    return szyfrogram


def main(args):
    tekst = input("Podaj tekst: ")
    klucz = int(input("Podaj klucz: "))
    while(2 * klucz > len(tekst)):
        klucz = int(input("Podaj klucz: "))
    szyfrogram = szyfruj(tekst, klucz)
    print(szyfrogram)
    # print(deszyfruj(szyfrogram, klucz))
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
