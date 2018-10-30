#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  bmi.py



def main(args):
    m = float(input("Podaj masę: "))
    w = int(input("Podaj wzrost: "))
    
    while w > 3:
            w = w / 100
            
    b =float(m / (w**2))
    
    if b < 18.5:
        print ("BMI:", b, "niedowaga")
    elif b < 25:
        print ("BMI:", b, "norma")
    elif b < 30:
        print ("BMI:", b, "nadwaga")
    else:
        print ("BMI:", b,"otyłość")
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
