#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main(args):
    I = input('Podaj imię:')
    print('Witaj',I)
    A = int(input('Podaj liczbę dwu-cyfrową:'))
    if 100 > A > 9:
        print(A)
        AB = int(input('Teraz podaj liczbę jedności tej liczby(np. jak było 15 to napisz 5):'))
        AC = int(input('Teraz podaj liczbę dziesiątek tej liczby(np. jak było 15 to napisz 1):'))
        print('Teraz od pierwszej liczby odejmiemy sumę liczby dziesiatek i jedności(np. 15-1(+5)):')
        ABC = A - (AB+AC)
        print('Wynik:',ABC, 'Wynik na 100% jest podzielny przez 9')
    else:
        print('Miała być dwu-cyfrowa!!!')
    print('Przejdźmy do czegoś innego')
    WA = int(input('Jeśli miałeś/aś urodziny w tym roku to wpisz 1 a jeśli nie to wpisz 2:'))
    AR = 2019
    RU = int(input('Wpisz rok urodzenia:'))
    if WA == 1:
        RUW = AR - RU
        print('Masz',AR - RU,'lat!')
        print('Teraz chcę wiedzieć czy masz rodzeństwo')
        B = int(input('Jeśli masz rodzeństwo wpisz 1, a jeśli nie wpisz 2:'))
        if B == 1:
            BA = int(input('Teraz wpisz 1 jak masz brata lub 2 jak nie:'))
            if BA == 1:
                BC = int(input('Więc masz brata ale czy drugiego brata? 1=Tak 2=Nie:'))
                if BC == 1:
                    BD = int(input('Teraz czy masz siostrę? 1=Tak 2=Nie:'))
                    if BD == 1:
                        BE  = int(input('Nasptępnie czy masz drugą siostrę? 1=Tak 2=Nie:'))
                        if BE == 1:
                            print('Więc jesteś', I,'który ma',RUW,'lat. Posiadasz 2 siostry i 2 braci!')
                        elif BE == 2:
                            print('Więc masz dwóch braci i jedną siostrę')
                    elif BD == 2:
                        print('Więc jesteś', I,'który ma',RUW,'lat. Posiadasz dwóch braci!')
                elif BC == 2:
                    BD = int(input('Następnie czy masz siostrę? 1=Tak 2=Nie:'))
                    if BD == 1:
                        BE  = int(input('Teraz czy masz drugą siostrę? 1=Tak 2=Nie:'))
                        if BE == 1:
                            print('Więc jesteś', I,'który ma',RUW,'lat. Posiadasz jednego brata i dwie siostry!')
                        elif BE == 2:
                            print('Więc jesteś', I,'który ma',RUW,'lat. Masz jednego brata i jedną siostrę!')
                    elif BD == 2:
                        print('Więc jesteś', I,'który ma',RUW,'lat. Posiadasz jednego brata!')
            elif BA == 2:
                BD = int(input('Następnie czy masz siostrę? 1=Tak 2=Nie:'))
                if BD == 1:
                    BE  = int(input('Teraz czy masz drugą siostrę? 1=Tak 2=Nie:'))
                    if BE == 1:
                        print('Więc jesteś', I,'który ma',RUW,'lat. Posiadasz 2 siostry!')
                    elif BE == 2:
                        print('Więc jesteś', I,'który ma',RUW,'lat. Masz jedną siostrę!')
        elif B == 2:  
            print('Więc jesteś', I,'który ma',RUW,'lat i nie masz rodzeństwa!')
    else:
        ARU = AR - RU - 1
        print('Masz',ARU,'lat!')
        print('Teraz chcę wiedzieć czy masz rodzeństwo')
        B = int(input('Jeśli masz rodzeństwo wpisz 1, a jeśli nie wpisz 2:'))
        if B == 1:
            BA = int(input('Teraz wpisz 1 jak masz brata lub 2 jak nie:'))
            if BA == 1:
                BC = int(input('Więc masz brata ale czy drugiego brata? 1=Tak 2=Nie:'))
                if BC == 1:
                    BD = int(input('Teraz czy masz siostrę? 1=Tak 2=Nie:'))
                    if BD == 1:
                        BE  = int(input('Nasptępnie czy masz drugą siostrę? 1=Tak 2=Nie:'))
                        if BE == 1:
                            print('Więc jesteś', I,'który ma',RUW,'lat. Posiadasz 2 siostry i 2 braci!')
                        elif BE == 2:
                            print('Więc masz dwóch braci i jedną siostrę')
                    elif BD == 2:
                        print('Więc jesteś', I,'który ma',RUW,'lat. Posiadasz dwóch braci!')
                elif BC == 2:
                    BD = int(input('Następnie czy masz siostrę? 1=Tak 2=Nie:'))
                    if BD == 1:
                        BE  = int(input('Teraz czy masz drugą siostrę? 1=Tak 2=Nie:'))
                        if BE == 1:
                            print('Więc jesteś', I,'który ma',RUW,'lat. Posiadasz jednego brata i dwie siostry!')
                        elif BE == 2:
                            print('Więc jesteś', I,'który ma',RUW,'lat. Masz jednego brata i jedną siostrę!')
                    elif BD == 2:
                        print('Więc jesteś', I,'który ma',RUW,'lat. Posiadasz jednego brata!')
            elif BA == 2:
                BD = int(input('Następnie czy masz siostrę? 1=Tak 2=Nie:'))
                if BD == 1:
                    BE  = int(input('Teraz czy masz drugą siostrę? 1=Tak 2=Nie:'))
                    if BE == 1:
                        print('Więc jesteś', I,'który ma',RUW,'lat. Posiadasz 2 siostry!')
                    elif BE == 2:
                        print('Więc jesteś', I,'który ma',RUW,'lat. Masz jedną siostrę!')
        elif B == 2:  
            print('Więc jesteś', I,'który ma',RUW,'lat i nie masz rodzeństwa!')
    
                        
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
