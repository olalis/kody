#!/usr/bin/env python
# -*- coding: utf-8 -*-


def sort_wstaw_ros(lista):
    """wersja liniowa"""
    for i in range(1, len(lista)):
        # for (int i = 0; i < n; i++) wersja c++
        el = lista[i]
        k = i - 1
        while k >= 0 and lista[k] > el:  # wyszukiwanie pozycji dla elementu
            lista[k + 1] = lista[k]  # przesuwanie elewntów w góre tabeli
            k -= 1
        lista[k + 1] = el  # wstawianie elementu
    return lista


def sort_wstaw_mal(lista):
    """wersja liniowa"""
    for i in range(1, len(lista)):
        # for (int i = 0; i < n; i++) wersja c++
        el = lista[i]
        k = i - 1
        while k >= 0 and lista[k] < el:  # wyszukiwanie pozycji dla elementu
            lista[k + 1] = lista[k]  # przesuwanie elewntów w góre tabeli
            k -= 1
        lista[k + 1] = el  # wstawianie elementu
    return lista


def main(args):
    lista = [4, 3, 7, 0, 2, 3, 1, 9, -4]
    lista1 = [4, 3, 7, 0, 2, 3, 1, 9, -4]
    lista2 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    print (lista)
    # 1 [3, 4, 7, 0, 2, 3, 1, 9]
    # 2 [3, 4, 7, 0, 2, 3, 1, 9]
    # 3 [0, 3, 4, 7, 2, 3, 1, 9]
    # 4 [0, 2, 3, 4, 7, 3, 1, 9]
    print (sort_wstaw_ros(lista))
    print (sort_wstaw_mal(lista1))
    print (sort_wstaw_ros(lista2))
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
