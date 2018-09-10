#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main(args):
    ile = int(input("Ile razy chcesz skorzystac z programu?"))
    i = 0

    while i < ile:
        a = float(input('Podaj masę ciała: '))
        b = float(input('Podaj wzrost: '))

        while b > 3:
            b = b / 10

        c = float(a / (b * b))

        print(c)

        if c < 18.5:
            print ("niedowaga")
        elif c < 25:
            print ("norma")
        elif c < 30:
            print ("nadwaga")
        elif c >= 30:
            print ("otyłość")
        i = i + 1

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
