#!/usr/bin/env python
# -*- coding: utf-8 -*-


def DN(start, stop):
    if start % 2 == 0:
        start=start + 1
        for  i in range(start, stop+1, 2):
            print(i)

        

def main(args):
    start = int(input('Podaj początek zakresu:'))
    stop = int(input('Podaj koniec zakresu:'))
    DN(start , stop)

    
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
