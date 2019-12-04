/*
 * petlafor.cpp
 */


#include <iostream>
using namespace std;

int main(int argc, char **argv)
{
    int start, stop, suma;
    cout << "Podaj początek przediału :";
    cin >> start;
    cout << "Podaj koniec przedziału :";
    cin >> stop;
    while (stop <= start) {
        cout << "Podaj koniec przedziału :";
        cin >> stop;
    }
    if (start % 2 == 1)
    start++;
    suma = 0;
    for(int i = start; i < stop + 1; i = i + 2) {
        cout << i << endl;
        suma = suma + i;
    }
    
    cout << suma;
	return 0;
}

