#! /usr/bin/env python
#
def routh ( n, x ):

#*****************************************************************************80
#
## ROUTH returns the ROUTH matrix.
#
#  Formula:
#
#    A is tridiagonal.
#    A(1,1)   =          X(1).
#    A(I-1,I) =   sqrt ( X(I) ), for I = 2 to N.
#    A(I,I-1) = - sqrt ( X(I) ), for I = 2 to N.
#
#  Example:
#
#    N = 5, X = ( 1, 4, 9, 16, 25 )
#
#    1 -2  0  0  0
#    2  0 -3  0  0
#    0  3  0 -4  0
#    0  0  4  0 -5
#    0  0  0  5  0
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is tridiagonal.
#
#    Because A is tridiagonal, it has property A (bipartite).
#
#    A is banded, with bandwidth 3.
#
#    A is integral, therefore det ( A ) is integral, and 
#    det ( A ) * inverse ( A ) is integral.
#
#    det ( A ) = product ( X(N) * X(N-2) * X(N-4) * ... * X(N+1-2*(N/2)) )
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of A.
#
#    Input, real X(N), the data that defines the matrix.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( i == 0 and j == 0 ):
        a[i,j] = abs ( x[0] )
      elif ( i == j + 1 ):
        a[i,j] = np.sqrt ( abs ( x[i] ) );
      elif ( i == j - 1 ):
        a[i,j] = - np.sqrt ( abs ( x[i+1] ) )

  return a

def routh_determinant ( n, x ):

#*****************************************************************************80
#
## ROUTH_DETERMINANT computes the determinant of the ROUTH matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, real X(N-1), the elements.
#
#    Output, real VALUE, the determinant.
#
  value = 1.0
  for i in range ( n - 1, -1, -2 ):
    value = value * x[i]

  return value

def routh_determinant_test ( ):

#*****************************************************************************80
#
## ROUTH_DETERMINANT_TEST tests ROUTH_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 February 2015
#
#  Author:
#
#    John Burkardt
#
  from routh import routh
  from r8vec_uniform_ab import r8vec_uniform_ab
  from r8mat_print import r8mat_print

  print ''
  print 'ROUTH_DETERMINANT_TEST'
  print '  ROUTH_DETERMINANT computes the ROUTH determinant.'

  m = 5
  n = m
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( n, r8_lo, r8_hi, seed )

  a = routh ( n, x )

  r8mat_print ( m, n, a, '  ROUTH matrix:' )

  value = routh_determinant ( n, x )

  print '  Value =  %g' % ( value )

  print ''
  print 'ROUTH_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def routh_test ( ):

#*****************************************************************************80
#
## ROUTH_TEST tests ROUTH.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 February 2015
#
#  Author:
#
#    John Burkardt
#
  from r8vec_uniform_ab import r8vec_uniform_ab
  from r8mat_print import r8mat_print

  print ''
  print 'ROUTH_TEST'
  print '  ROUTH computes the ROUTH matrix.'

  m = 5
  n = m
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( n, r8_lo, r8_hi, seed )

  a = routh ( n, x )
 
  r8mat_print ( m, n, a, '  ROUTH matrix:' )

  print ''
  print 'ROUTH_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  routh_test ( )
  timestamp ( )
