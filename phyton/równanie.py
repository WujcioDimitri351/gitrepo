#!/usr/bin/env python
# -*- coding: utf-8 -*-





def main(args):
    a = int(input('Podaj liczbę:'))
    b = int(input('Podaj liczbę:'))
    if a == 0: 
        if  b == 0:
            print('Nieskączenie wiele rozwiązań')
        else:
            print('Równanie sprzeczne')
    else:
        x = -b/a
        print(x)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
