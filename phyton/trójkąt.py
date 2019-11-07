#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main(args):
    a = int(input('Podaj bok pierwszy:'))
    b = int(input('Podaj bok drugi:'))
    c = int(input('Podaj bok trzeci:'))
    # ~if a + b > c:
        # ~if a + c > b:
            # ~if b + c > a:
                # ~print('Da się zbudować!')
                # ~return 0
    if a + b > c and b + c > a and a + c > b:
        print('Da się budować!')
    else:
        print('Nie da sie zbudować')
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
