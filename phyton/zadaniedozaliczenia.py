#!/usr/bin/env python
# -*- coding: utf-8 -*-



def sl():
    b = 0
    c = 0
    a = 1
    while a > 0 or a < 0 :
        if a % 5 == 0:
            c = c + 1
        if a % 7 == 0:
            b = b + 1
        a = int(input('Podaj liczbę:'))
            
    print(c)
    print(b)
    
    
def main(args):
    sl()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
