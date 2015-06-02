#! /usr/bin/env python
#
def conference ( n ):

#*****************************************************************************80
#
## CONFERENCE returns the CONFERENCE matrix.
#
#  Discussion:
#
#    A conference matrix is a square matrix A of order N, with a zero
#    diagonal, and only 1's and -1's on the offdiagonal, with the property
#    that:
#
#      A * A' = (N-1) * I.
#
#    The algorithm employed here is only valid when N - 1
#    is an odd prime, or a power of an odd prime.
#
#    Conference matrices have a relationship with Hadamard matrices:
#
#      If mod ( P, 4 ) == 3, A is antisymmetric, and
#        I + A is hadamard;
#      Else A is symmetric, and
#        (   I + A, - I + A )
#        ( - I + A, - I - A) is Hadamard.
#
#  Example:
#
#    N = 8
#
#     0  1  1  1  1  1  1  1
#    -1  0 -1 -1  1 -1  1  1
#    -1  1  0 -1 -1  1 -1  1
#    -1  1  1  0 -1 -1  1 -1
#    -1 -1  1  1  0 -1 -1  1
#    -1  1 -1  1  1  0 -1 -1
#    -1 -1  1 -1  1  1  0 -1
#    -1 -1 -1  1 -1  1  1  0
#
#  Properties:
#
#    If N-1 is prime, then A[2:N,2:N] is a circulant matrix.
#
#    If N-1 = 1 mod 4, then A is symmetric.
#
#    If N-1 = 3 mod 4, then A is antisymmetric.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.  N-1 must be an
#    odd prime, or a power of an odd prime.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np
  from legendre_symbol import legendre_symbol

  a = np.zeros ( ( n, n ) )

  for j in range ( 0, n ):
    for i in range ( 0, n ):
      if ( i == 0 and j == 0 ):
        a[i,j] = 0.0
      elif ( i == 0 ):
        a[i,j] = 1.0
      elif ( j == 0 ):
        if ( ( ( n - 1 ) % 4 ) == 1 ):
          a[i,j] = 1.0
        else:
          a[i,j] = -1.0
      else:
        l = legendre_symbol ( i - j, n - 1 )
        a[i,j] = float ( l )

  return a

def conference_determinant ( n ):

#*****************************************************************************80
#
## CONFERENCE_DETERMINANT returns the determinant of the CONFERENCE matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.  N-1 must be an 
#    odd prime, or a power of an odd prime.
#
#    Output, real VALUE, the determinant.
#
  import numpy as np

  if ( ( ( n - 1 ) % 4 ) == 1 ):
    value = - np.sqrt ( float ( n - 1 ) ** n )
  else:
    value = + np.sqrt ( float ( n - 1 ) ** n )

  return value

def conference_inverse ( n ):

#*****************************************************************************80
#
## CONFERENCE_INVERSE returns the inverse of the CONFERENCE matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Output, real CONFERENCE_INVERSE[N,N], the matrix.
#
  import numpy as np
  from legendre_symbol import legendre_symbol

  a = np.zeros ( ( n, n ) )

  for j in range ( 0, n ):
    for i in range ( 0, n ):
      if ( i == 0 and j == 0 ):
        a[i,j] = 0.0
      elif ( i == 0 ):
        a[i,j] = 1.0
      elif ( j == 0 ):
        if ( ( ( n - 1 ) % 4 ) == 1 ):
          a[i,j] = 1.0
        else:
          a[i,j] = - 1.0
      else:
        l = legendre_symbol ( i - j, n - 1 )
        a[i,j] = float ( l )

  if ( ( ( n - 1 ) % 4 ) == 3 ):
    for i in range ( 0, n ):
      for j in range ( 0, n ):
        a[i,j] = - a[i,j]

  if ( 1 < n ):
    for i in range ( 0, n ):
      for j in range ( 0, n ):
        a[i,j] = a[i,j] / float ( n - 1 )

  return a

def conference_test ( ):

#*****************************************************************************80
#
## CONFERENCE_TEST tests CONFERENCE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 April 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'CONFERENCE_TEST'
  print '  CONFERENCE computes the CONFERENCE matrix.'
#
#  Note that N-1 must be an odd prime or a power of an odd prime.
#
  n = 6
  a = conference ( n )
  r8mat_print ( n, n, a, '  CONFERENCE matrix:' )

  print ''
  print 'CONFERENCE_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  conference_test ( )
  timestamp ( )
