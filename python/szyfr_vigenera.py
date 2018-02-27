#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  szyfr_vigenera.py
#  


def main(args):
    tekst = input("Podaj tekst: ")
    klucz = input("Podaj klucz: ")
    szyfr = " "
    kod  = " "
    if len(tekst) % len(klucz) == 0:
        for i in range(int(len(tekst) / len(klucz))):
            szyfr += klucz
    else:
        for i in range(int(len(tekst) / len(klucz))):
            szyfr += klucz
        x = szyfr
        for i in range ((len(tekst) - len(x)) + 1):
            szyfr += klucz[i]
    for j in range(len(tekst)):
        if ord(tekst[j]) > 64 and ord(tekst[j]) < 91:
            ascii = ord(tekst[j]) + (ord(szyfr[j]) - 63)
            if ascii > 90:
                ascii -= 26
        elif ord(tekst[j]) > 96 and ord(tekst[j]) < 123:
            ascii = ord(tekst[j]) + (ord(szyfr[j]) - 95)
            if ascii > 122:
                ascii -= 26
        kod += chr(ascii)
    print(kod)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

