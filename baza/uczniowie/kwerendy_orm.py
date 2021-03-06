#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kwerendy_orm.py
import os
from uczniowie_model import *

def kw08():
    """Lista nazwisk uczniów i nazw klas"""
    query = (Uczen
        .select(Uczen.nazwisko, Uczen.klasa.klasa)
        .join(Klasa) #Połączenie tabel
    )
    
    for obj in query:
        print(obj.nazwisko, obj.klasa.klasa)
        
def kw09():
    """Lista klas i ilość uczniów"""
    query = (Uczen
        .select(fn.Count(Uczen.id).alias('ilu'), Uczen.klasa.klasa)
        .join(Klasa) #Połączenie tabel
        .group_by(Klasa)
        .order_by(SQL('ilu').asc())
    )
    
    for obj in query:
        print(obj.klasa.klasa, obj.ilu)
        
def kw10():
    """Lista przedmiotów i ilość ocen"""
    query = (Przedmiot
        .select(fn.Count(Ocena.uczen).alias('ile'), Przedmiot.przedmiot)
        .join(Ocena) #Połączenie tabel
        .group_by(Przedmiot)
        .order_by(SQL('ile').asc())
    )
    
    for obj in query:
        print(obj.przedmiot, obj.ile)

def kw11():
    """Po ile ocen mają wszyscy uczniowie"""
    query = (Ocena
        .select(Ocena.uczen.nazwisko, fn.COUNT(Ocena.id).alias('ile'))
        .join(Uczen)
        .group_by(Ocena.uczen.nazwisko)
        .order_by(SQL('ile').asc())
    )
    for obj in query:
        print(obj.uczen.nazwisko, obj.ile)

def kw12():
    """Średnie ocen poszczególnych uczniów"""
    query = (Ocena
        .select(Ocena.uczen.nazwisko, fn.AVG(Ocena.ocena).alias('srednia'))
        .join(Uczen)
        .group_by(Ocena.uczen.nazwisko)
        .order_by(SQL('srednia').asc())
    )
    for obj in query:
        print(obj.uczen.nazwisko, round(obj.srednia, 2))

def kw13():
    """Średnie ocen ucznia Szymczak z poszczególnych przedmiotów"""
    query = (Ocena
        .select(Ocena.uczen.nazwisko, Ocena.przedmiot.przedmiot, fn.AVG(Ocena.ocena).alias('srednia'))
        .join(Uczen)
        .join_from(Ocena, Przedmiot)
        .where(Ocena.uczen.nazwisko == 'Szymczak')
        .group_by(Ocena.przedmiot.przedmiot)
        .order_by(SQL('srednia').asc())
    )
    for obj in query:
        print(obj.uczen.nazwisko, obj.przedmiot.przedmiot, round(obj.srednia, 2))

def kw14():
    """ilu uczniów ma średnią powyżej 3.5 z wf"""
    query = (Ocena
        .select(Ocena.uczen.nazwisko, fn.AVG(Ocena.ocena).alias('srednia'))
        .join(Uczen)
        .join_from(Ocena, Przedmiot)
        .where(Ocena.przedmiot.przedmiot == 'WF')
        .group_by(Ocena.uczen.nazwisko)
        .order_by(SQL('srednia').asc())
    )
    query = [obj for obj in query if obj.srednia > 3.5]
    for obj in query:
        # if (obj.srednia > 3.5):
        print(obj.uczen.nazwisko, round(obj.srednia, 2))
    print('Liczba uczniów:', len(query))


def main(args):
    baza.connect()  # połączenie z bazą

    kwerendy = [
        "Uczen.select()",
        "Uczen.select().where(Uczen.imie=='Rafał')",
        "Uczen.select().where(Uczen.imie.startswith('G'))",
        "Uczen.select().where(Uczen.egz_mat.between(20, 40))",
        "Uczen.select().where((Uczen.nazwisko=='Piasecki') & (Uczen.imie=='Rafał'))",
        "Uczen.select().order_by(Uczen.egz_mat.asc())",
        "Uczen.select().where(Uczen.plec==1).order_by(Uczen.egz_mat.asc())",
        
    ]
    
    #for obj in eval(kwerendy[6]):
    #    print(obj.nazwisko, obj.imie, obj.egz_mat)
    kw14()
    
    baza.commit()
    baza.close()
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
