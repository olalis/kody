#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  
import sqlite3

def kwerenda1(cur):
    
    cur.execute("""
    SELECT klasa, przedmiot, AVG(ocena) AS srednia FROM oceny 
    INNER JOIN uczniowie ON uczniowie.id = oceny.id_uczen 
    INNER JOIN klasy ON uczniowie.id_klasa = klasy.id 
    INNER JOIN przedmioty ON oceny.id_przedmiot = przedmioty.id
    WHERE przedmiot = "matematyka"
    GROUP BY klasy.id 
    ORDER BY srednia DESC
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
    #SELECT nazwisko, egz_mat, egz_hum FROM uczniowie
        #WHERE egz_mat > 40 and(or) egz_hum > 40 #wybiera uczniów z najlepszymi wynikami lub/i
    #SELECT nazwisko, egz_mat, egz_hum FROM uczniowie
        #WHERE egz_hum > 40
        #ORDER BY egz_mat DESC  #Sortowanie rosnące (ASC) lub malejące (DESC)
        #LIMIT 5 #ilość najlepszych wyników
    #SELECT AVG(egz_mat) FROM uczniowie #liczy średnią
    #SELECT plec, AVG(egz_mat), AVG(egz_hum), AVG(egz_jez) FROM uczniowie GROUP BY plec #Grupowanie wegług czegoś
    #SELECT plec, COUNT(id) FROM uczniowie WHERE egz_mat > (SELECT AVG(egz_mat) FROM uczniowie) GROUP BY plec
    #SELECT COUNT nazwisko, imie, klasa FROM uczniowie INNER JOIN klasy ON uczniowie.id_klasa = klasy.id
    #SELECT klasa, COUNT(uczniowie.id) AS ilosc FROM uczniowie #alias
        #INNER JOIN klasy ON uczniowie.id_klasa = klasy.id
        #GROUP BY klasa
        #ORDER BY ilosc desc
    # SELECT nazwisko, imie, ocena FROM uczniowie INNER JOIN oceny ON uczniowie.id = oceny.id_uczen
    #WITH srednie AS(
        #SELECT nazwisko, imie, AVG(ocena) AS srednia FROM uczniowie 
        #INNER JOIN oceny ON uczniowie.id = oceny.id_uczen
        #GROUP BY uczniowie.id
        #) 
        #SELECT nazwisko, imie, srednia FROM srednie
        #WHERE srednia > 3.8
    #SELECT klasa, AVG(ocena) AS srednia FROM oceny INNER JOIN uczniowie ON uczniowie.id = oceny.id_uczen INNER JOIN klasy ON uczniowie.id_klasa = klasy.id GROUP BY klasy.id ORDER BY srednia DESC
    #SELECT przedmiot, AVG(ocena) AS srednia FROM oceny INNER JOIN przedmioty ON oceny.id_przedmiot = przedmioty.id
        #GROUP BY id_przedmiot
        #ORDER BY srednia desc
    SELECT klasa, przedmiot, AVG(ocena) AS srednia FROM oceny 
    INNER JOIN uczniowie ON uczniowie.id = oceny.id_uczen 
    INNER JOIN klasy ON uczniowie.id_klasa = klasy.id 
    INNER JOIN przedmioty ON oceny.id_przedmiot = przedmioty.id
    WHERE przedmiot = "matematyka"
    GROUP BY klasy.id 
    ORDER BY srednia DESC
    
    for row in cur.fetchall():
        print(tuple(row))

def main(args):
    #KONFIGURACJA###############
    baza = 'uczniowie'
    tabele = ['uczniowie', 'klasy', 'przedmioty', 'oceny']
    roz = '.csv'
    naglowki = False #czy pliki żrodłowe zawierają naglowki?
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
