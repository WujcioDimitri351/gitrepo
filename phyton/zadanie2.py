#!/usr/bin/env python
# -*- coding: utf-8 -*-



def main(args):
    n = int(input('Podaj liczbę(liczba musi byc dodatnia):'))
    m = int(input('Podaj drugą liczbę(liczba musi byc większa od poprzedniej):'))
    c = list(range(n, m))
    print(c, m)
        
        
        
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
