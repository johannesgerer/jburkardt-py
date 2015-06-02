#! /usr/bin/env python
#
def triv ( n, x, y, z ):

#*****************************************************************************80
#
## TRIV returns the TRIV matrix.
#
#  Discussion:
#
#    The three vectors define the subdiagonal, main diagonal, and
#    superdiagonal.
#
#  Formula:
#
#    if ( J = I - 1 )
#      A(I,J) = X(J)
#    elseif ( J = I )
#      A(I,J) = Y(I)
#    elseif ( J = I + 1 )
#      A(I,J) = Z(I)
#    else
#      A(I,J) = 0
#
#  Example:
#
#    N = 5, X = ( 1, 2, 3, 4 ), Y = ( 5, 6, 7, 8, 9 ), Z = ( 10, 11, 12, 13 )
#
#     5 10  0  0  0
#     1  6 11  0  0
#     0  2  7 12  0
#     0  0  3  8 13
#     0  0  0  4  9
#
#  Properties:
#
#    A is tridiagonal.
#
#    A is banded, with bandwidth 3.
#
#    A is generally not symmetric: A' /= A.
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of A.
#
#    Input, real X(N-1), Y(N), Z(N-1), the vectors that define
#    the subdiagonal, diagonal, and superdiagonal of A.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( j == i - 1 ):
        a[i,j] = x[j]
      elif ( j == i ):
        a[i,j] = y[i]
      elif ( j == i + 1 ):
        a[i,j] = z[i]

  return a

def triv_determinant ( n, x, y, z ):

#*****************************************************************************80
#
## TRIV_DETERMINANT computes the determinant of the TRIV matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, real X(N-1), Y(N), Z(N-1), the vectors that define
#    the subdiagonal, diagonal, and superdiagonal of A.
#
#    Output, real VALUE, the determinant.
#
  determ_nm1 = y[n-1]

  if ( n == 1 ):
    value = determ_nm1
    return value

  determ_nm2 = determ_nm1
  determ_nm1 = y[n-2] * y[n-1] - z[n-2] * x[n-2];

  if ( n == 2 ):
    value = determ_nm1
    return value

  for i in range ( n - 3, -1, -1 ):

    value = y[i] * determ_nm1 - z[i] * x[i] * determ_nm2

    determ_nm2 = determ_nm1
    determ_nm1 = value

  return value

def triv_determinant_test ( ):

#*****************************************************************************80
#
## TRIV_DETERMINANT_TEST tests TRIV_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 February 2015
#
#  Author:
#
#    John Burkardt
#
  from triv import triv
  from r8vec_uniform_ab import r8vec_uniform_ab
  from r8mat_print import r8mat_print

  print ''
  print 'TRIV_DETERMINANT_TEST'
  print '  TRIV_DETERMINANT computes the TRIV determinant.'

  m = 5
  n = m
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( n - 1, r8_lo, r8_hi, seed )
  y, seed = r8vec_uniform_ab ( n, r8_lo, r8_hi, seed )
  z, seed = r8vec_uniform_ab ( n - 1, r8_lo, r8_hi, seed )
  a = triv ( n, x, y, z )

  r8mat_print ( m, n, a, '  TRIV matrix:' )

  value = triv_determinant ( n, x, y, z )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'TRIV_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def triv_inverse ( n, x, y, z ):

#*****************************************************************************80
#
## TRIV_INVERSE returns the inverse of the TRIV matrix.
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
#    Input, real X(N-1), Y(N), Z(N-1), the vectors that define
#    the subdiagonal, diagonal, and superdiagonal of A.
#    No entry of Y can be zero.
#
#    Output, real A(N,N), the inverse of the matrix.
#
  import numpy as np
  from r8_mop import r8_mop
  from sys import exit

  for i in range ( 0, n ):
    if ( y[i] == 0 ):
      print ''
      print 'TRIV_INVERSE - Fatal error!'
      print '  No entry of Y can be zero!'
      exit ( 'TRIV_INVERSE - Fatal error!' )

  d = np.zeros ( n )
  d[n-1] = y[n-1]
  for i in range ( n - 2, -1, -1 ):
    d[i] = y[i] - x[i] * z[i] / d[i+1]

  e = np.zeros ( n )
  e[0] = y[0]
  for i in range ( 1, n ):
    e[i] = y[i] - x[i-1] * z[i-1] / e[i-1]

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
      a[i,j] = r8_mop ( i + j ) * p1 * p2 / p3;

    for j in range ( i + 1, n ):
      p1 = 1.0
      for k in range ( i, j ):
        p1 = p1 * z[k]
      p2 = 1.0
      for k in range ( j + 1, n ):
        p2 = p2 * d[k]
      p3 = 1.0
      for k in range ( i, n ):
        p3 = p3 * e[k]
      a[i,j] = r8_mop ( i + j ) * p1 * p2 / p3

  return a

def triv_test ( ):

#*****************************************************************************80
#
## TRIV_TEST tests TRIV.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 February 2015
#
#  Author:
#
#    John Burkardt
#
  from r8vec_uniform_ab import r8vec_uniform_ab
  from r8mat_print import r8mat_print

  print ''
  print 'TRIV_TEST'
  print '  TRIV computes the TRIV matrix.'

  m = 5
  n = m
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( n - 1, r8_lo, r8_hi, seed )
  y, seed = r8vec_uniform_ab ( n, r8_lo, r8_hi, seed )
  z, seed = r8vec_uniform_ab ( n - 1, r8_lo, r8_hi, seed )
  a = triv ( n, x, y, z )
 
  r8mat_print ( m, n, a, '  TRIV matrix:' )

  print ''
  print 'TRIV_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  triv_test ( )
  timestamp ( )
