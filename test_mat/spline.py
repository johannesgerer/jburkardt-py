#! /usr/bin/env python
#
def spline ( n, x ):

#*****************************************************************************80
#
## SPLINE returns the SPLINE matrix.
#
#  Discussion:
#
#    This matrix arises during interpolation with cubic splines.
#
#  Formula:
#
#    if ( I = 1 and J = I )
#      A(I,J) = 2 * X(I)
#    elseif ( I = 1 and J = I + 1 )
#      A(I,J) = X(I)
#    elseif ( I = N and J = I )
#      A(I,J) = 2 * X(N-1)
#    elseif ( I = N and J = I - 1 )
#      A(I,J) = X(N-1)
#    elseif ( J = I )
#      A(I,J) = 2 * (X(I-1)+X(I))
#    elseif ( J = I-1 )
#      A(I,J) = X(I-1)
#    elseif ( J = I + 1 )
#      A(I,J) = X(I)
#    else
#      A(I,J) = 0
#
#  Example:
#
#    N = 5
#    X = ( 1, 1, 1, 1 )
#
#    2   1   0   0  0
#    1   4   1   0  0
#    0   1   4   1  0
#    0   0   1   4  1
#    0   0   0   1  2
#
#    N = 5
#    X = ( 1, 2, 3, 4 )
#
#    2   1   0   0  0
#    1   6   2   0  0
#    0   2  10   3  0
#    0   0   3  14  4
#    0   0   0   4  8
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A is tridiagonal.
#
#    Because A is tridiagonal, it has property A (bipartite).
#
#    A is banded, with bandwidth 3.
#
#    If the entries of X are positive, then A is positive definite.
#
#    If the entries of X are all of one sign, then A is diagonally dominant.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of A.
#
#    Input, real X(N-1), values that represent the spacing 
#    between points, and which define the entries of A.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( i == 0 and j == 0 ):
        a[i,j] = 2.0 * x[0]
      elif ( i == 0 and j == i + 1 ):
        a[i,j] = x[0]
      elif ( i == n - 1 and j == i ):
        a[i,j] = 2.0 * x[n-2]
      elif ( i == n and j == i - 1 ):
        a[i,j] = x[n-2]
      elif ( j == i ):
        a[i,j] = 2.0 * ( x[i-1] + x[i] );
      elif ( j == i - 1 ):
        a[i,j] = x[i-1]
      elif ( j == i + 1 ):
        a[i,j] = x[i]

  return a

def spline_determinant ( n, x ):

#*****************************************************************************80
#
## SPLINE_DETERMINANT computes the determinant of the SPLINE matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 February 2015
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
  determ_nm1 = 2.0 * x[n-2]

  if ( n == 1 ):
    value = determ_nm1;
    return value

  determ_nm2 = determ_nm1
  if ( n == 2 ):
    determ_nm1 = 4.0 *            x[n-2]   * x[n-2] - x[n-2] * x[n-2]
  else:
    determ_nm1 = 4.0 * ( x[n-3] + x[n-2] ) * x[n-2] - x[n-2] * x[n-2]

  if ( n == 2 ):
    value = determ_nm1;
    return value

  for i in range ( n - 3, -1, -1 ):

    if ( i == 0 ):
      value = 2.0 *            x[i]   * determ_nm1 - x[i] * x[i] * determ_nm2
    else:
      value = 2.0 * ( x[i-1] + x[i] ) * determ_nm1 - x[i] * x[i] * determ_nm2
 
    determ_nm2 = determ_nm1;
    determ_nm1 = value
 
  return value

def spline_determinant_test ( ):

#*****************************************************************************80
#
## SPLINE_DETERMINANT_TEST tests SPLINE_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 February 2015
#
#  Author:
#
#    John Burkardt
#
  from spline import spline
  from r8vec_uniform_ab import r8vec_uniform_ab
  from r8mat_print import r8mat_print

  print ''
  print 'SPLINE_DETERMINANT_TEST'
  print '  SPLINE_DETERMINANT computes the SPLINE determinant.'

  m = 5
  n = m
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( n - 1, r8_lo, r8_hi, seed )

  a = spline ( n, x )

  r8mat_print ( m, n, a, '  SPLINE matrix:' )

  value = spline_determinant ( n, x )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'SPLINE_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def spline_inverse ( n, x ):

#*****************************************************************************80
#
## SPLINE_INVERSE returns the inverse of the SPLINE matrix.
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
#  Reference:
#
#    CM daFonseca, J Petronilho,
#    Explicit Inverses of Some Tridiagonal Matrices,
#    Linear Algebra and Its Applications,
#    Volume 325, 2001, pages 7-21.
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, real X(N-1), the parameters.
#
#    Output, real A(N,N), the inverse of the matrix.
#
  import numpy as np
  from r8_mop import r8_mop

  d = np.zeros ( n )
  d[n-1] = 2.0 * x[n-2]
  for i in range ( n - 2, 0, -1 ):
    d[i] = 2.0 * ( x[i-1] + x[i] ) - x[i] * x[i] / d[i+1]
  d[0] = 2.0 * x[0] - x[0] * x[0] / d[1]

  e = np.zeros ( n )
  e[0] = 2.0 * x[0]
  for i in range ( 1, n - 1 ):
    e[i] = 2.0 * ( x[i-1] + x[i] ) - x[i-1] * x[i-1] / e[i-1]
  e[n-1] = 2.0 * x[n-2] - x[n-2] * x[n-2] / e[n-2]

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):

    for j in range ( 0, i + 1 ):
      p1 = 1.0
      for k in range ( j, i ):
        p1 = p1 * x[k]
      p2 = 1.0
      for k in range ( i + 1, n ):
        p2 = p2 * d[k]
      p3 = 1.0
      for k in range ( j, n ):
        p3 = p3 * e[k]
      a[i,j] = r8_mop ( i + j ) * p1 * p2 / p3

    for j in range ( i + 1, n ):
      p1 = 1.0
      for k in range ( i, j ):
        p1 = p1 * x[k]
      p2 = 1.0
      for k in range ( j + 1, n ):
        p2 = p2 * d[k]
      p3 = 1.0
      for k in range ( i, n ):
        p3 = p3 * e[k]
      a[i,j] = r8_mop ( i + j ) * p1 * p2 / p3

  return a

def spline_test ( ):

#*****************************************************************************80
#
## SPLINE_TEST tests SPLINE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 February 2015
#
#  Author:
#
#    John Burkardt
#
  from r8vec_uniform_ab import r8vec_uniform_ab
  from r8mat_print import r8mat_print

  print ''
  print 'SPLINE_TEST'
  print '  SPLINE computes the SPLINE matrix.'

  m = 5
  n = m
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( n - 1, r8_lo, r8_hi, seed )

  a = spline ( n, x )
 
  r8mat_print ( m, n, a, '  SPLINE matrix:' )

  print ''
  print 'SPLINE_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  spline_test ( )
  timestamp ( )
