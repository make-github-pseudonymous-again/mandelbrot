
# max nb of iterations
M = 100
# side resolution
N = 200
# d
D = 2

x1 = -2.25
x2 = 0.75
y1 = -1.5
y2 = 1.5

def div ( z , max_iteration , d ) :

    _z = 0

    for i in range( max_iteration ) :

        _z = _z ** d + z

        if abs( _z ) > 2 : return i

    return max_iteration

real = [ i / N for i in range( int(x1*N) , int(x2*N) ) ]
imag = [ i / N for i in range( int(y1*N) , int(y2*N) ) ]

image = [ [ div( complex( r , i ) , M , D ) for r in real ] for i in imag ]

import matplotlib.pyplot as plt

plt.imshow( image )
plt.show( )
