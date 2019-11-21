#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main(args):
    A = 0
    while A < 1: 
        A = int(input('Podaj liczbę:'))
    for i in range(0,A+1):
        print(i*i)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
