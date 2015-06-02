#! /usr/bin/env python
#
def cheby_u ( n ):

#*****************************************************************************80
#
## CHEBY_U returns the CHEBY_U matrix.
#
#  Example:
#
#    N = 11
#
#    1  .   .    .    .    .    .     .     .   .    .
#    .  2   .    .    .    .    .     .     .   .    .
#   -1  .   4    .    .    .    .     .     .   .    .
#    . -4   .    8    .    .    .     .     .   .    .
#    1  . -12    .   16    .    .     .     .   .    .
#    .  6   .  -32    .   32    .     .     .   .    .
#   -1  .  24    .  -80    .   64     .     .   .    .
#    . -8   .   80    . -192    .   128     .   .    .
#    1  . -40    .  240    . -448     .   256   .    .
#    . 10   . -160    .  672    . -1024     . 512    .
#   -1  .  60    . -560    . 1792     . -2304   . 1024
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is integral: int ( A ) = A.
#
#    A is generally not normal: A' * A /= A * A'.
#
#    A is lower triangular.
#
#    A is reducible.
#
#    The entries of row N sum to N.
#
#    det ( A ) = 2^((N*(N-1))/2).
#
#    LAMBDA(I) = 2^(I-1)
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 January 2015
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

  a = np.zeros ( [ n, n ] )

  a[0,0] = 1.0

  if ( n == 1 ):
    return a

  a[1,1] = 2.0

  if ( n == 2 ):
    return a

  for i in range ( 2, n ):
    for j in range ( 0, n ):
      if ( j == 0 ):
        a[i,j] = - a[i-2,j]
      else:
        a[i,j] = 2.0 * a[i-1,j-1] - a[i-2,j]

  return a

def cheby_u_determinant ( n ):

#*****************************************************************************80
#
## CHEBY_U_DETERMINANT computes the determinant of the CHEBY_U matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Output, real DETERM, the determinant.
#
  power = ( n * ( n - 1 ) ) // 2
  determ = 2 ** power

  return determ

def cheby_u_determinant_test ( ):

#*****************************************************************************80
#
## CHEBY_U_DETERMINANT_TEST tests CHEBY_U_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 January 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'CHEBY_U_DETERMINANT_TEST'
  print '  CHEBY_U_DETERMINANT computes the CHEBY_U determinant.'

  m = 5
  n = m
  a = cheby_u ( n )
  r8mat_print ( m, n, a, '  CHEBY_U matrix:' )

  value = cheby_u_determinant ( n )
  print '  Value =  %g' % ( value )

  print ''
  print 'CHEBY_U_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def cheby_u_inverse ( n ):

#*****************************************************************************80
#
## CHEBY_U_INVERSE returns the inverse of the CHEBY_U matrix.
#
#  Example:
#
#    N = 11
#
#      1   .   .  .   .  .  .  .  .  .  .
#      .   1   .  .   .  .  .  .  .  .  .  /    2
#      1   .   1  .   .  .  .  .  .  .  .  /    4
#      .   2   .  1   .  .  .  .  .  .  .  /    8
#      2   .   3  .   1  .  .  .  .  .  .  /   16
#      .   5   .  4   .  1  .  .  .  .  .  /   32
#      5   .   9  .   5  .  1  .  .  .  .  /   64
#      .  14   . 14   .  6  .  1  .  .  .  /  128
#     14   .  28  .  20  .  7  .  1  .  .  /  256
#      .  42   . 48   . 27  .  8  .  1  .  /  512
#     42   .  90  .  75  . 35  .  9  .  1  / 1024
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 March 2015
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

    a[1,1] = 0.5

    if ( 2 < n ):

      for i in range ( 2, n ):
        for j in range ( 0, n ):
          if ( j == 0 ):
            a[i,j] =                      a[i-1,j+1]   / 2.0
          elif ( j < n - 1 ):
            a[i,j] = (       a[i-1,j-1] + a[i-1,j+1] ) / 2.0
          else:
            a[i,j] =         a[i-1,j-1]                / 2.0

  return a

def cheby_u_test ( ):

#*****************************************************************************80
#
## CHEBY_U_TEST tests CHEBY_U.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 January 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'CHEBY_U_TEST'
  print '  CHEBY_U computes the CHEBY_U matrix.'

  m = 5
  n = m
  a = cheby_u ( n )
  r8mat_print ( m, n, a, '  CHEBY_U matrix:' )

  print ''
  print 'CHEBY_U_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  cheby_u_test ( )
  timestamp ( )
