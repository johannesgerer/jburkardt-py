#! /usr/bin/env python
#
def fiedler ( m, n, x ):

#*****************************************************************************80
#
## FIEDLER returns the FIEDLER matrix.
#
#  Formula:
#
#    A(I,J) = abs ( X(I) - X(J) )
#
#  Example:
#
#    M = 5, N = 5, X = ( 1, 2, 3, 5, 9 )
#
#    0  1  2  4  8
#    1  0  1  3  7
#    2  1  0  2  6
#    4  3  2  0  4
#    8  7  6  4  0
#
#  Rectangular Properties:
#
#    A has a zero diagonal.
#
#  Square Properties:
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    det ( A ) = (-1)^N * 2^(N-2)
#      * ( X(1) - X(N) ) * product ( 2 <= I <= N ) ( X(I) - X(I-1) ).
#
#    A is nonsingular if the X(I) are distinct.
#
#    The inverse is cyclic tridiagonal; that is, it is tridiagonal, except
#    for nonzero (1,N) and (N,1) entries.
#
#    A has a dominant positive eigenvalue, and all others are negative.
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 October 2007
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Gabor Szego,
#    Solution to problem 3705,
#    American Mathematical Monthly,
#    Volume 43, Number 4, 1936, pages 246-259.
#
#    John Todd,
#    Example A14,
#    Basic Numerical Mathematics,
#    Volume 2: Numerical Algebra,
#    Academic Press, 1977, page 159.
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns of A.
#
#    Input, real X( max (M,N) ), the values that define A.
#
#    Output, real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ m, n ] )

  for j in range ( 0, n ):
    for i in range ( 0, m ):
        a[i,j] = np.abs ( x[i] - x[j] )

  return a

def fiedler_determinant ( n, x ):

#*****************************************************************************80
#
## FIEDLER_DETERMINANT computes the determinant of the FIEDLER matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, real X(N), the fiedler elements.
#
#    Output, real DETERM, the determinant.
#
  determ = 2.0 ** ( n - 2 )

  if ( ( n % 2 ) == 1 ):
    determ = - determ

  for i in range ( 0, n - 1 ):
    for j in range ( i + 1, n ):
      if ( x[j] < x[i] ):
        t    = x[j]
        x[j] = x[i]
        x[i] = t
        determ = - determ

  determ = determ * ( x[n-1] - x[0] )

  for i in range ( 1, n ):
    determ = determ * ( x[i] - x[i-1] )

  return determ

def fiedler_determinant_test ( ):

#*****************************************************************************80
#
## FIEDLER_DETERMINANT_TEST tests FIEDLER_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 January 2015
#
#  Author:
#
#    John Burkardt
#
  from fiedler import fiedler
  from r8vec_uniform_ab import r8vec_uniform_ab
  from r8mat_print import r8mat_print

  print ''
  print 'FIEDLER_DETERMINANT_TEST'
  print '  FIEDLER_DETERMINANT computes the FIEDLER determinant.'

  m = 5
  n = m
  x_lo = -5.0
  x_hi = +5.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( n, x_lo, x_hi, seed )

  a = fiedler ( m, n, x )

  r8mat_print ( m, n, a, '  FIEDLER matrix:' )

  value = fiedler_determinant ( n, x )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'FIEDLER_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def fiedler_inverse ( n, x ):

#*****************************************************************************80
#
## FIEDLER_INVERSE returns the inverse of the FIEDLER matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of A.
#
#    Input, real X(N), the values that define A.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  d1 = 0.5 / ( x[n-1] - x[0] )
  d2 = 0.5 / ( x[0] - x[1] )

  a[0,n-1] = + d1
  a[0,0] = + d1 + d2
  a[0,1] =      - d2

  for i in range ( 1, n - 1 ):
    d1 = 0.5 / ( x[i-1] - x[i] )
    d2 = 0.5 / ( x[i] - x[i+1] )
    a[i,i-1] = - d1
    a[i,i]   = + d1 + d2
    a[i,i+1] =      - d2

  d1 = 0.5 / ( x[n-2] - x[n-1] )
  d2 = 0.5 / ( x[n-1] - x[0] )

  a[n-1,n-2] = - d1
  a[n-1,n-1] =   d1 + d2
  a[n-1,0]   =      + d2

  return a

def fiedler_test ( ):

#*****************************************************************************80
#
## FIEDLER_TEST tests FIEDLER.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 January 2015
#
#  Author:
#
#    John Burkardt
#
  from r8vec_uniform_ab import r8vec_uniform_ab
  from r8mat_print import r8mat_print

  print ''
  print 'FIEDLER_TEST'
  print '  FIEDLER computes the FIEDLER matrix.'

  m = 5
  n = m
  x_lo = -5.0
  x_hi = +5.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( n, x_lo, x_hi, seed )

  a = fiedler ( m, n, x )
 
  r8mat_print ( m, n, a, '  FIEDLER matrix:' )

  print ''
  print 'FIEDLER_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  fiedler_test ( )
  timestamp ( )
