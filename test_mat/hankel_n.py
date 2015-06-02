#! /usr/bin/env python
#
def hankel_n ( n ):

#*****************************************************************************80
#
## HANKEL_N returns the HANKEL_N matrix.
#
#  Formula:
#
#    A(I,J) = I+J-1 for I+J-1 <= N + 1
#           = 0     otherwise 
#
#  Example:
#
#    N = 5
#
#    1  2  3  4  5
#    2  3  4  5  0
#    3  4  5  0  0
#    4  5  0  0  0
#    5  0  0  0  0
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A is a Hankel matrix: constant along anti-diagonals.
#
#    determinant ( A ) = (-1)^(N/2) * N^N
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ n, n ] )

  for j in range ( 0, n ):
    for i in range ( 0, n - j ):
      a[i,j] = i + j + 1
    for i in range ( n - j, n ):
      a[i,j] = 0.0

  return a

def hankel_n_condition ( n ):

#*****************************************************************************80
#
## HANKEL_N_CONDITION returns the L1 condition of the HANKEL_N matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Output, real VALUE, the L1 condition.
#
  import numpy as np

  v = np.zeros ( n )

  v[0] = 1.0 / float ( n )
  for i in range ( 1, n ):
    for j in range ( 0, i ):
      v[i] = v[i] - ( n + j - i ) * v[j]
    v[i] = v[i] / n

  a_norm = float ( n * ( n + 1 ) ) / 2.0
  b_norm = np.sum ( abs ( v ) )
  value = a_norm * b_norm

  return value

def hankel_n_determinant ( n ):

#*****************************************************************************80
#
## HANKEL_N_DETERMINANT computes the determinant of the HANKEL_N matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 January 2015
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
  from math import floor
  from r8_mop import r8_mop

  determ = r8_mop ( floor ( n / 2 ) ) * ( n ** n )

  return determ

def hankel_n_determinant_test ( ):

#*****************************************************************************80
#
## HANKEL_N_DETERMINANT_TEST tests HANKEL_N_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 January 2015
#
#  Author:
#
#    John Burkardt
#
  from hankel_n import hankel_n
  from r8mat_print import r8mat_print

  print ''
  print 'HANKEL_N_DETERMINANT_TEST'
  print '  HANKEL_N_DETERMINANT computes the HANKEL_N determinant.'

  m = 5
  n = m
  a = hankel_n ( n )
  r8mat_print ( m, n, a, '  HANKEL_N matrix:' )

  value = hankel_n_determinant ( n )
  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'HANKEL_N_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def hankel_n_inverse ( n ):

#*****************************************************************************80
#
## HANKEL_N_INVERSE returns the inverse of the HANKEL_N matrix.
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
#    Input, integer N, the order of the matrix.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  v = np.zeros ( n )

  v[0] = 1.0 / float ( n )
  for i in range ( 1, n ):
    for j in range ( 0, i ):
      v[i] = v[i] - float ( n + j - i ) * v[j]
    v[i] = v[i] / float ( n )

  a = np.zeros ( ( n, n ) )

  for j in range ( 0, n ):
    for i in range ( n - 1 - j, n ):
      a[i,j] = v[i+j+1-n]

  return a

def hankel_n_test ( ):

#*****************************************************************************80
#
## HANKEL_N_TEST tests HANKEL_N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 January 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'HANKEL_N_TEST'
  print '  HANKEL_N computes the HANKEL_N matrix.'

  m = 5
  n = m
  a = hankel_n ( n )
  r8mat_print ( m, n, a, '  HANKEL_N matrix:' )

  print ''
  print 'HANKEL_N_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  hankel_n_test ( )
  timestamp ( )
