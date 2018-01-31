#!/usr/bin/env python
# -*- coding: utf-8 -*-


def dec2other(liczba10, podstawa):
    """Konwersja liczby dziesiętnej na system o podanej podstawie"""
    liczba = []  # pusta lista do zapamiętywania reszt
    while liczba10 != 0:
        reszta = liczba10 % podstawa
        if reszta > 9:
            reszta = chr(reszta + 55)  # wykorzystanie kodu ASCII
        liczba.append(str(reszta))
        liczba10 = int(liczba10 / podstawa)  # uwaga
    liczba.reverse()  # odwracanie kolejności elementów
    return "".join(liczba)


def zamiana1():
    """Pobieranie danych wejściowych"""
    liczba = int(input("Podaj liczbę: "))
    podstawa = int(input("Podaj podstawę: "))
    while podstawa < 2 or podstawa > 16:
        podstawa = int(input("Podaj podstawę: "))
    print("Wynik konwersji: {}(10) = {}({})".format(
        liczba, dec2other(liczba, podstawa), podstawa))


def other2dec(liczba, podstawa):
    """Zamiana podanej liczby na system dziesietny"""
    #  123(7) = 1 * 7^2 + 2 * 7^1 + 3
    liczba10 = 0
    potega = len(liczba) - 1
    for cyfra in liczba:
        if not cyfra.isdigit():
            liczba10 += (ord(cyfra.upper()) - 55) * (podstawa ** potega)
        else:
            liczba10 += int(cyfra) * (podstawa ** potega)
        potega -= 1


def zamiana2():
    """Pobieranie danych wejściowych"""
    liczba = input("Podaj liczbę: ")
    podstawa = int(input("Podaj podstawę: "))

    while podstawa < 2 or podstawa > 16:
        podstawa = int(input("Podaj podstawę: "))
    print("Wynik konwersji: {}({}}) = {}(10)".format(
        liczba, podstawa, other2dec(liczba, podstawa)))


def main(args):
    print("Zamiana liczby dziesiętnej na liczbę o podanej podstawie "
          "<2;16> lub odwrotnie")
    zamiana1()
    zamiana2()
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
