/*
 * wieksza.cpp
 */


#include <iostream>
using namespace std;

int main(int argc, char **argv)
{
    int a, b;
    cout << "Podaj podaj liczbę 1 :";
    cin >> a;
    cout << "Podaj podaj liczbę 2 :";
    cin >> b;
    
    if (a > b){
        cout << "liczba 1 > liczba 2";
        cout << a;
    }
    if ( b>a ){
        cout << "liczba 2 > liczba 1";
        cout << b;
    }
    if ( a == b){
        cout << "liczba 1 = liczba 2";
    }
    

    
    
    
	return 0;
}

