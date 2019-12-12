#!/usr/bin/env python
# -*- coding: utf-8 -*-



def main(args):
    a = 10 
    while a < 100 and a % 3 == 0:
        print(a)
        a = a + 1
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
