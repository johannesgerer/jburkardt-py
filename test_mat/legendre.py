#! /usr/bin/env python
#
def legendre ( n ):

#*****************************************************************************80
#
## LEGENDRE returns the LEGENDRE matrix.
#
#  Example:
#
#    N = 11
#
#     1    .     .     .      .     .      .      .       .     .     . / 1
#     .    1     .     .      .     .      .      .       .     .     . / 1
#    -1    .     3     .      .     .      .      .       .     .     . / 2
#     .   -3     .     5      .     .      .      .       .     .     . / 2
#     3    .   -30     .     35     .      .      .       .     .     . / 8
#     .   15     .   -70      .    63      .      .       .     .     . / 8
#    -5    .   105     .   -315     .    231      .       .     .     . / 16
#     .  -35     .   315      .  -693      .    429       .     .     . / 16
#    35    . -1260     .   6930     . -12012      .    6435     .     . / 128
#     .  315     . -4620      . 18018      . -25740       . 12155     . / 128
#   -63    .  3465     . -30030     .  90090      . -109395     . 46189 / 256
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is lower triangular.
#
#    The elements of each row sum to 1.
#
#    Because it has a constant row sum of 1,
#    A has an eigenvalue of 1, and
#    a (right) eigenvector of ( 1, 1, 1, ..., 1 ).
#
#    A is reducible.
#
#    The diagonals form a pattern of zero, positive, zero, negative.
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 February 2015
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

    a[1,1] = 1.0

    if ( 2 < n ):

      for i in range ( 2, n ):
        for j in range ( 0, n ):
          if ( j == 0 ):
            a[i,j] = - ( i - 1 ) * a[i-2,j] \
                     / ( i );
          else:
            a[i,j] = ( ( 2 * i - 1 ) * a[i-1,j-1] \
                     + (   - i + 1 ) * a[i-2,j] ) \
                     / (     i     );

  return a

def legendre_determinant ( n ):

#*****************************************************************************80
#
## LEGENDRE_DETERMINANT computes the determinant of the LEGENDRE matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 February 2015
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
  value = 1.0
  t = 1.0

  for i in range ( 3, n + 1 ):
    t = t * float ( 2 * i - 3 ) / float (  i - 1 )
    value = value * t

  return value

def legendre_determinant_test ( ):

#*****************************************************************************80
#
## LEGENDRE_DETERMINANT_TEST tests LEGENDRE_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 February 2015
#
#  Author:
#
#    John Burkardt
#
  from legendre import legendre
  from r8mat_print import r8mat_print

  print ''
  print 'LEGENDRE_DETERMINANT_TEST'
  print '  LEGENDRE_DETERMINANT computes the LEGENDRE determinant.'

  m = 5
  n = m
 
  a = legendre ( n )

  r8mat_print ( m, n, a, '  LEGENDRE matrix:' )

  value = legendre_determinant ( n )

  print '  Value =  %g' % ( value )

  print ''
  print 'LEGENDRE_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def legendre_inverse ( n ):

#*****************************************************************************80
#
## LEGENDRE_INVERSE returns the inverse of the LEGENDRE matrix.
#
#  Example:
#
#    N = 11
#
#       1    .     .    .     .    .    .   .    .   .   .
#       .    1     .    .     .    .    .   .    .   .   .
#       1    .     2    .     .    .    .   .    .   .   . /     3
#       .    3     .    2     .    .    .   .    .   .   . /     5
#       7    .    20    .     8    .    .   .    .   .   . /    35
#       .   27     .   28     .    8    .   .    .   .   . /    63
#      33    .   110    .    72    .   16   .    .   .   . /   231
#       .  143     .  182     .   88    .  16    .   .   . /   429
#     715    .  2600    .  2160    .  832   .  128   .   . /  6435
#       . 3315     . 4760     . 2992    . 960    . 128   . / 12155
#    4199    . 16150    . 15504    . 7904   . 2176   . 256 / 46189
#
#  Properties:
#
#    A is nonnegative.
#
#    The elements of each row sum to 1.
#
#    Because it has a constant row sum of 1,
#    A has an eigenvalue of 1, and
#    a (right) eigenvector of ( 1, 1, 1, ..., 1 ).
#
#    A is lower triangular.
#
#    A is reducible.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 March 2015
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

    a[1,1] = 1.0

    if ( 2 < n ):

      for i in range ( 2, n ):
        for j in range ( 0, n ):

          if ( j == 0 ):

            a[i,j] = (     j + 1 ) * a[i-1,j+1] / ( 2 * j + 3 )

          elif ( j < n - 1 ):

            a[i,j] = (     j     ) * a[i-1,j-1] / ( 2 * j - 1 ) \
                   + (     j + 1 ) * a[i-1,j+1] / ( 2 * j + 3 )

          else:

            a[i,j] = (     j     ) * a[i-1,j-1] / ( 2 * j - 1 );

  return a

def legendre_test ( ):

#*****************************************************************************80
#
## LEGENDRE_TEST tests LEGENDRE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 February 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'LEGENDRE_TEST'
  print '  LEGENDRE computes the LEGENDRE matrix.'

  m = 5
  n = m

  a = legendre ( n )
 
  r8mat_print ( m, n, a, '  LEGENDRE matrix:' )

  print ''
  print 'LEGENDRE_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  legendre_test ( )
  timestamp ( )
