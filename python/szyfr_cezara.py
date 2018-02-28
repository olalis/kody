#!/usr/bin/env python
# -*- coding: utf-8 -*-


def szyfruj(tekst, klucz):
    """Szyfrowanie tekstu za pomocą szyfru Cezara"""
    szyfrogram = ""
    klucz = klucz % 26
    for znak in tekst:
        if ord(znak) > 64 and ord(znak) < 91:
            ascii = ord(znak) + klucz
            if ascii > 90:
                ascii -= 26
        elif ord(znak) > 96 and ord(znak) < 123:
            ascii = ord(znak) + klucz
            if ascii > 122:
                ascii -= 26
        elif ord(znak) == 32:
            ascii = 32
        szyfrogram += chr(ascii)
    return szyfrogram


def deszyfruj(szyfrogram, klucz):
    tekst = ""
    klucz = klucz % 26
    for znak in szyfrogram:
        if ord(znak) > 64 and ord(znak) < 91:
            ascii = ord(znak) - klucz
            if ascii < 65:
                ascii += 26
        elif ord(znak) > 96 and ord(znak) < 123:
            ascii = ord(znak) - klucz
            if ascii < 97:
                ascii += 26
        elif ord(znak) == 32:
            ascii = 32
        tekst += chr(ascii)
    return tekst


# obsłużyć małe i duże litery
# obsłużyć spacje


def main(args):
    # tekst = input("Podaj tekst: ")
    # klucz = int(input("Podaj klucz: "))
    # szyfrogram = szyfruj(tekst, klucz)
    # print(szyfrogram)
    # print(deszyfruj(szyfrogram, klucz))

    tekst1 = input("Podaj tekst: ")
    klucz1 = int(input("Podaj klucz: "))
    print(deszyfruj(tekst1, klucz1))

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
