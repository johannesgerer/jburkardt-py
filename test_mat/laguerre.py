#! /usr/bin/env python
#
def laguerre ( n ):

#*****************************************************************************80
#
## LAGUERRE returns the LAGUERRE matrix.
#
#  Example:
#
#    N = 8
#
#      1      .     .      .    .    .    .    .
#      1     -1     .      .    .    .    .    .
#      2     -4     1      .    .    .    .    .   /    2
#      6    -18     9     -1    .    .    .    .   /    6
#     24    -96    72    -16    1    .    .    .   /   24
#    120   -600   600   -200   25   -1    .    .   /  120
#    720  -4320  5400  -2400  450  -36    1    .   /  720
#   5040 -35280 52920 -29400 7350 -882   49   -1   / 5040
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is lower triangular.
#
#    The columns of A alternate in sign.
#
#    A(I,1) = 1
#    A(I,I) = (-1)^(I-1) / (I-1)!.
#
#    LAMBDA(I) = (-1)^(I-1) / (I-1)!.
#
#    det ( A ) = product ( 1 <= I <= N ) (-1)^(I-1) / (I-1)!
#
#    The I-th row contains the coefficients of the Laguerre
#    polynomial of degree I-1.
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 October 2007
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz, Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#  Parameters:
#
#    Input, integer N, the order of A.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  a[0,0] = 1.0

  if ( 1 < n ):

    a[1,0] = 1.0
    a[1,1] = -1.0

    if ( 2 < n ):

      for i in range ( 3, n + 1 ):
        for j in range ( 0, n ):
          if ( j == 0 ):
            a[i-1,j] = ( float ( 2 * i - 3 ) * a[i-2,j] \
                      +  float (   - i + 2 ) * a[i-3,j] ) \
                      /  float (     i - 1 )
          else:
            a[i-1,j] = ( float ( 2 * i - 3 ) * a[i-2,j] \
                      -  float (         1 ) * a[i-2,j-1] \
                      +  float (   - i + 2 ) * a[i-3,j] ) \
                      /  float (     i - 1 )

  return a

def laguerre_determinant ( n ):

#*****************************************************************************80
#
## LAGUERRE_DETERMINANT computes the determinant of the LAGUERRE matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Output, real VALUE, the determinant.
#
  from r8_factorial import r8_factorial

  value = 1.0
  p = + 1.0
  for i in range ( 0, n ):
    value = value * p / r8_factorial ( i )
    p = - p

  return value

def laguerre_determinant_test ( ):

#*****************************************************************************80
#
## LAGUERRE_DETERMINANT_TEST tests LAGUERRE_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 February 2015
#
#  Author:
#
#    John Burkardt
#
  from laguerre import laguerre
  from r8mat_print import r8mat_print

  print ''
  print 'LAGUERRE_DETERMINANT_TEST'
  print '  LAGUERRE_DETERMINANT computes the LAGUERRE determinant.'

  m = 5
  n = m
 
  a = laguerre ( n )

  r8mat_print ( m, n, a, '  LAGUERRE matrix:' )

  value = laguerre_determinant ( n )

  print '  Value =  %g' % ( value )

  print ''
  print 'LAGUERRE_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def laguerre_inverse ( n ):

#*****************************************************************************80
#
## LAGUERRE_INVERSE returns the inverse of the LAGUERRE matrix.
#
#  Example:
#
#    N = 9
#
#        1        .       .        .       .        .       .       .     .
#        1       -1       .        .       .        .       .       .     .
#        2       -4       2        .       .        .       .       .     .
#        6      -18      18       -6       .        .       .       .     .
#       24      -96     144      -96      24        .       .       .     .
#      120     -600    1200    -1200     600     -120       .       .     .
#      720    -4320   10800   -14400   10800    -4320     720       .     .
#     5040   -35280  105840  -176400  176400  -105840   35280   -5040     .
#     40320 -322560 1128960 -2257920 2822400 -2257920 1128960 -322560 40320
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is lower triangular.
#
#    The columns of A alternate in sign.
#
#    A(I,1) = (I-1)!
#    A(I,I) = (I-1)! * ( -1 ) ^ (N+1)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 October 2007
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of A.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  a[0,0] = 1.0

  if ( 1 < n ):

    a[1,0] = 1.0
    a[1,1] = -1.0

    if ( 2 < n ):
      
      for i in range ( 2, n ):
        for j in range ( 0, n ):

          if ( j == 0 ):
            a[i,j] = float ( i ) * ( a[i-1,j]              )
          else:
            a[i,j] = float ( i ) * ( a[i-1,j] - a[i-1,j-1] )

  return a

def laguerre_test ( ):

#*****************************************************************************80
#
## LAGUERRE_TEST tests LAGUERRE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 February 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'LAGUERRE_TEST'
  print '  LAGUERRE computes the LAGUERRE matrix.'

  m = 5
  n = m

  a = laguerre ( n )
 
  r8mat_print ( m, n, a, '  LAGUERRE matrix:' )

  print ''
  print 'LAGUERRE_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  laguerre_test ( )
  timestamp ( )
