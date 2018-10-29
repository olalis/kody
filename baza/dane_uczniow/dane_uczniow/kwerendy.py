#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  
import sqlite3

def kwerenda1(cur):
    
    cur.execute("""
        SELECT * FROM oceny INNER JOIN nazwiska ON nazwiska.nr_ucznia = oceny.nr_ucznia 
    """)
    
    #SELECT * FROM nazwiska WHERE nazwisko LIKE 'G%' #rekordy zaczynające się na daną literę
    #SELECT * FROM nazwiska WHERE imie1 LIKE 'A__a'  #rekord czreroliterowy zaczynający i kończący sie na daną literę
    #SELECT COUNT(*) FROM nazwiska WHERE imie1 LIKE 'A__a' #zliczanie rekordów
    #SELECT * FROM nazwiska INNER JOIN dane_osobowe ON nazwiska.nr_ucznia = dane_osobowe.nr_ucznia # wybierz rekordy z dwóch
    #SELECT COUNT(*) FROM nazwiska INNER JOIN dane_osobowe ON nazwiska.nr_ucznia = dane_osobowe.nr_ucznia 
        #WHERE miejsce_urodz ="Gdańsku" #dokładne dopasowanie pola tekstowego
        #WHERE miejsce_urodz <> "Gdańsku" #dopasowanie odwrotnedo danego pola tekstowego
        #WHERE miesiac = 10 or miesiac = 3 #wybiera konkretne liczby
        #WHERE miesiac >6 and miesiac < 9
     
    for row in cur.fetchall():
        print(tuple(row))

def main(args):
    #KONFIGURACJA###############
    baza = 'uczniowie'
    tabele = ['nazwiska', 'dane_osobowe', 'oceny']
    roz = '.txt'
    naglowki = True #czy pliki żrodłowe zawierają naglowki?
    ############################
    con = sqlite3.connect(baza + '.db') #połączenie
    cur = con.cursor() #obiekt kursor
    
    kwerenda1(cur)
    
    con.commit()
    con.close()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
