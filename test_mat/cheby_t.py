#! /usr/bin/env python
#
def cheby_t ( n ):

#*****************************************************************************80
#
## CHEBY_T returns the CHEBY_T matrix.
#
#  Example:
#
#    N = 11
#
#    1  .   .    .    .    .    .    .     .   .   .
#    .  1   .    .    .    .    .    .     .   .   .
#   -1  .   2    .    .    .    .    .     .   .   .
#    . -3   .    4    .    .    .    .     .   .   .
#    1  .  -8    .    8    .    .    .     .   .   .
#    .  5   .  -20    .   16    .    .     .   .   .
#   -1  .  18    .  -48    .   32    .     .   .   .
#    . -7   .   56    . -112    .   64     .   .   .
#    1  . -32    .  160    . -256    .   128   .   .
#    .  9   . -120    .  432    . -576     . 256   .
#   -1  .  50    . -400    . 1120    . -1280   . 512
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is integral: int ( A ) = A.
#
#    A is reducible.
#
#    A is lower triangular.
#
#    Each row of A sums to 1.
#
#    det ( A ) = 2^( (N-1) * (N-2) / 2 )
#
#    A is not normal: A' * A /= A * A'.
#
#    For I = 1:
#      LAMBDA(1) = 1
#    For 1 < I
#      LAMBDA(I) = 2^(I-2)
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 January 2015
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

  a[1,1] = 1.0

  if ( n == 2 ):
    return

  for i in range ( 2, n ):
    for j in range ( 0, n ):
      if ( j == 0 ):
        a[i,j] = - a[i-2,j]
      else:
        a[i,j] = 2.0 * a[i-1,j-1] - a[i-2,j]

  return a

def cheby_t_determinant ( n ):

#*****************************************************************************80
#
## CHEBY_T_DETERMINANT computes the determinant of the CHEBY_T matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 January 2015
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
  power = ( ( n - 1 ) * ( n - 2 ) ) // 2
  determ = 2 ** power

  return determ

def cheby_t_determinant_test ( ):

#*****************************************************************************80
#
## CHEBY_T_DETERMINANT_TEST tests CHEBY_T_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 January 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'CHEBY_T_DETERMINANT_TEST'
  print '  CHEBY_T_DETERMINANT computes the CHEBY_T determinant.'

  m = 5
  n = m
  a = cheby_t ( n )
  r8mat_print ( m, n, a, '  CHEBY_T matrix:' )

  value = cheby_t_determinant ( n )
  print '  Value =  %g' % ( value )

  print ''
  print 'CHEBY_T_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def cheby_t_inverse ( n ):

#*****************************************************************************80
#
## CHEBY_T_INVERSE returns the inverse of the CHEBY_T matrix.
#
#  Example:
#
#    N = 11
#
#      1   .   .  .   .  .  .  .  .  .  .
#      .   1   .  .   .  .  .  .  .  .  .
#      1   .   1  .   .  .  .  .  .  .  .  /   2
#      .   3   .  1   .  .  .  .  .  .  .  /   4
#      3   .   4  .   1  .  .  .  .  .  .  /   8
#      .  10   .  5   .  1  .  .  .  .  .  /  16
#     10   .  15  .   6  .  1  .  .  .  .  /  32
#      .  35   . 21   .  7  .  1  .  .  .  /  64
#     35   .  56  .  28  .  8  .  1  .  .  / 128
#      . 126   . 84   . 36  .  9  .  1  .  / 256
#    126   . 210  . 120  . 45  . 10  .  1  / 512
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

    a[1,1] = 1.0

    if ( 2 < n ):

      for i in range ( 2, n ):
        for j in range ( 0, n ):
          if ( j == 0 ):
            a[i,j] =                      a[i-1,j+1]   / 2.0
          elif ( j == 1 ):
            a[i,j] = ( 2.0 * a[i-1,j-1] + a[i-1,j+1] ) / 2.0
          elif ( j < n - 1 ):
            a[i,j] = (       a[i-1,j-1] + a[i-1,j+1] ) / 2.0
          else:
            a[i,j] =         a[i-1,j-1]                / 2.0

  return a

def cheby_t_test ( ):

#*****************************************************************************80
#
## CHEBY_T_TEST tests CHEBY_T.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 January 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'CHEBY_T_TEST'
  print '  CHEBY_T computes the CHEBY_T matrix.'

  m = 5
  n = m
  a = cheby_t ( n )
  r8mat_print ( m, n, a, '  CHEBY_T matrix:' )

  print ''
  print 'CHEBY_T_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  cheby_t_test ( )
  timestamp ( )
