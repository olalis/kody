#!/usr/bin/env python
# -*- coding: utf-8 -*- 
#  


def main(args):
    n = int (input ('Podaj liczbę: '))
    i = 2
    
    while True:
        if i * i > n:
            print ("Liczba pierwsza.")
            break
            
        elif i * i <= n and n % i == 0:
            print ("Liczba złożona.")
            break
            
        elif i * i <= n and n % i != 0:
            i = i + 1
            
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
