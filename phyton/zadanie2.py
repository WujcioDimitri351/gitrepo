#!/usr/bin/env python
# -*- coding: utf-8 -*-



def main(args):
    n = int(input('Podaj liczbę(liczba musi byc dodatnia):'))
    m = int(input('Podaj drugą liczbę(liczba musi byc większa od poprzedniej):'))
    if n<0:
        n = 0
    if m<0:
        m = 0
    if n==0 and m==0 :
        print('Nie ma takiej liczby naturalnej')
    elif n == 0 and m > 0:
            for i in range(n ,m + 1):
                print(i, " ", end = "")
    elif n > m:
        print('Źle podałeś liczby')
    else:
        for i in range(n ,m + 1):
            print(i, " ", end = "")
            
        
    
        
        
        
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
