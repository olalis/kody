#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main(args):
    a = b = 0
    int czy = 1

    while (czy != 0)
    {
        cout << "Podaj znak:" << endl;
        cin >> znak;
        cout << "Podaj dwie liczby:" << endl;
        cin >> a >> b ;
        if (znak == '+')
        {
            cout << dodaj(a, b)<< endl;
        }
        if (znak == '-')
        {
            cout << odejmij(a, b) << endl;
        }
        if (znak == '*')
        {
            cout << mnoz(a, b) << endl;
        }
        if (znak == '/')
        {
            cout << dziel(a, b) << endl;
        }

        cout << "Czy chcesz wykonać jakieś działanie ponownie? (wpisz 1 jeśli tak lub 0 jeśli nie "<<endl;
        cin >> czy;
    }

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
