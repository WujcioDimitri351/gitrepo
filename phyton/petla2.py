#!/usr/bin/env python
# -*- coding: utf-8 -*-

def s_l():
    """
    Funkcja pobiera liczby od użytkownika póki suma nie przekroczy 75
    """  
    suma = 0
    i = 0
    while suma < 75:
        A = int(input('Podaj liczbę:'))
        if i == 0 and A > 75:
            print('Nie chcesz za dużo?')
            continue
        suma = suma + A
        i = i + 1
    print(suma)
    
    
def main(args):
    s_l()
    return 0
    
    
    
    

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
