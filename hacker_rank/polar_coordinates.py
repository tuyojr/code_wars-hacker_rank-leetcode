# https://www.hackerrank.com/challenges/polar-coordinates/problem?isFullScreen=true

import cmath
if __name__ == '__main__':
    z = complex(input())
    print(abs(z))
    print(cmath.phase(z))