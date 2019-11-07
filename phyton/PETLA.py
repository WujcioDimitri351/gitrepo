#!/usr/bin/env python
# -*- coding: utf-8 -*-



def main(args):
    suma = 0
    for i in range(3):
        L = int(input('Podaj liczbę:'))
        suma = suma + L
    print(suma)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
