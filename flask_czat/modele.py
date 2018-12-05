#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  models.py

from peewee import *

baza = SQliteDatabase('quiz.db')

class BasaModel(Model):
     class Meta:
        database = baza

class Pytanie(BaseModel):
    pytanie = CharField()
    odpok = CharField()


class Odpowiedz(BaseModel):
    pnr = ForeignKeyField(Pytanie, related_name='odpowiedzi')
    odpowiedz = CharField()

def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
