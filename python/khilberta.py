#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import *

<<<<<<< HEAD
droga = 8
=======
droga = 3
>>>>>>> 2f48727d9e37d574d882da4183a0d79b6b1e2d25

def c(t):
    if t > 0:
        u(t - 1)
        setheading(180)
        forward(droga)
        c(t - 1)
        setheading(270)
        forward(droga)
        c(t - 1)
        setheading(0)
        forward(droga)
        n(t - 1)


def u(t):
    if t > 0:
        c(t - 1)
        setheading(270)
        forward(droga)
        u(t - 1)
        setheading(180)
        forward(droga)
        u(t - 1)
        setheading(90)
        forward(droga)
        d(t - 1)


def d(t):
    if t > 0:
        n(t - 1)
        setheading(0)
        forward(droga)
        d(t - 1)
        setheading(90)
        forward(droga)
        d(t - 1)
        setheading(180)
        forward(droga)
        u(t - 1)


def n(t):
    if t > 0:
        d(t - 1)
        setheading(90)
        forward(droga)
        n(t - 1)
        setheading(0)
        forward(droga)
        n(t - 1)
        setheading(270)
        forward(droga)
        c(t - 1)


def main(args):
    speed(0)  # najszybsze rysowanie
    c(10)
    done()

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
