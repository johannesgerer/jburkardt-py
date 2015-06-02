#! /usr/bin/env python
#
def bauer ( ):

#*****************************************************************************80
#
## BAUER returns the BAUER matrix.
#
#  Example:
#
#    -74   80  18 -11  -4  -8
#     14  -69  21  28   0   7
#     66  -72  -5   7   1   4
#    -12   66 -30 -23   3  -3
#      3    8  -7  -4   1   0
#      4  -12   4   4   0   1
#
#  Properties:
#
#    The matrix is integral.
#
#    The inverse matrix is integral.
#
#    The matrix is ill-conditioned.
#
#    The determinant is 1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Virginia Klema, Alan Laub,
#    The Singular Value Decomposition: Its Computation and Some Applications,
#    IEEE Transactions on Automatic Control,
#    Volume 25, Number 2, April 1980.
#
#  Parameters:
#
#    Output, real A(6,6), the matrix.
#
  import numpy as np

  a = np.array ( [ \
   [ -74.0,  80.0,  18.0, -11.0,  -4.0,  -8.0 ], \
   [  14.0, -69.0,  21.0,  28.0,   0.0,   7.0 ], \
   [  66.0, -72.0,  -5.0,   7.0,   1.0,   4.0 ], \
   [ -12.0,  66.0, -30.0, -23.0,   3.0,  -3.0 ], \
   [   3.0,   8.0,  -7.0,  -4.0,   1.0,   0.0 ], \
   [   4.0, -12.0,   4.0,   4.0,   0.0,   1.0 ] ] );

  return a

def bauer_condition ( ):

#*****************************************************************************80
#
## BAUER_CONDITION returns the L1 condition of the BAUER matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real VALUE, the condition.
#
  a_norm = 307.0
  b_norm = 27781.0
  value = a_norm * b_norm

  return value

def bauer_determinant ( ):

#*****************************************************************************80
#
## BAUER_DETERMINANT returns the determinant of the BAUER matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real VALUE, the determinant.
#
  value = 1.0

  return value

def bauer_inverse ( ):

#*****************************************************************************80
#
## BAUER_INVERSE returns the inverse of the BAUER matrix.
#
#  Example:
#
#      1       0      -7     -40     131     -84
#      0       1       7      35    -112      70
#     -2       2      29     155    -502     319
#     15     -12    -192   -1034    3354   -2130
#     43     -42    -600   -3211   10406   -6595
#    -56      52     764    4096  -13276    8421
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real A(6,6), the matrix.
#
  import numpy as np

  a = np.array ( [ \
    [   1.0,       0.0,      -7.0,     -40.0,     131.0,     -84.0 ], \
    [   0.0,       1.0,       7.0,      35.0,    -112.0,      70.0 ], \
    [  -2.0,       2.0,      29.0,     155.0,    -502.0,     319.0 ], \
    [  15.0,     -12.0,    -192.0,   -1034.0,    3354.0,   -2130.0 ], \
    [  43.0,     -42.0,    -600.0,   -3211.0,   10406.0,   -6595.0 ], \
    [ -56.0,      52.0,     764.0,    4096.0,  -13276.0,    8421.0 ] ] )

  return a

def bauer_test ( ):

#*****************************************************************************80
#
## BAUER_TEST tests BAUER.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 March 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'BAUER_TEST'
  print '  BAUER computes the BAUER matrix.'

  n = 6
  a = bauer ( )
  r8mat_print ( n, n, a, '  BAUER matrix:' )

  print ''
  print 'BAUER_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  bauer_test ( )
  timestamp ( )
