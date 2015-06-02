#! /usr/bin/env python
#
def fibonacci3 ( n ):

#*****************************************************************************80
#
## FIBONACCI3 returns the FIBONACCI3 matrix.
#
#  Example:
#
#    N = 5
#
#    1 -1  0  0  0
#    1  1 -1  0  0
#    0  1  1 -1  0
#    0  0  1  1 -1
#    0  0  0  1  1
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
#    A is integral: int ( A ) = A.
#
#    The determinant of A is the Fibonacci number F(N+1).
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 January 2015
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

  for i in range ( 1, n ):
    a[i,i-1] = 1.0

  for i in range ( 0, n ):
    a[i,i] = 1.0

  for i in range ( 0, n - 1 ):
    a[i,i+1] = -1.0

  return a

def fibonacci3_determinant ( n ):

#*****************************************************************************80
#
## FIBONACCI3_DETERMINANT returns the determinant of the FIBONACCI3 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 January 2015
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
  f1 = 0
  f2 = 0
  f3 = 1

  for i in range ( 0, n ): 
    f1 = f2
    f2 = f3
    f3 = f1 + f2

  value = f3

  return value

def fibonacci3_determinant_test ( ):

#*****************************************************************************80
#
## FIBONACCI3_DETERMINANT_TEST tests FIBONACCI3_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 January 2015
#
#  Author:
#
#    John Burkardt
#
  from fibonacci3 import fibonacci3
  from r8mat_print import r8mat_print

  print ''
  print 'FIBONACCI3_DETERMINANT_TEST'
  print '  FIBONACCI3_DETERMINANT computes the determinant of the FIBONACCI3 matrix.'
  print ''

  m = 5
  n = m

  a = fibonacci3 ( n )
  r8mat_print ( m, n, a, '  FIBONACCI3 matrix:' )

  value = fibonacci3_determinant ( n )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'FIBONACCI3_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def fibonacci3_inverse ( n ):

#*****************************************************************************80
#
## FIBONACCI3_INVERSE returns the inverse of the FIBONACCI3 matrix.
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
#    CM daFonseca, J Petronilho,
#    Explicit Inverses of Some Tridiagonal Matrices,
#    Linear Algebra and Its Applications,
#    Volume 325, 2001, pages 7-21.
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Output, real A(N,N), the inverse of the matrix.
#
  import numpy as np
  from r8_mop import r8_mop

  a = np.zeros ( ( n, n ) )

  d = np.zeros ( n )

  d[n-1] = 1.0
  for i in range ( n - 2, -1, -1 ):
    d[i] = 1.0 + 1.0 / d[i+1]

  for i in range ( 0, n ):
    for j in range ( 0, i + 1 ):

      p1 = 1.0
      for k in range ( i + 1, n ):
        p1 = p1 * d[k]
      p2 = 1.0
      for k in range ( 0, n - j ):
        p2 = p2 * d[k]
      a[i,j] = r8_mop ( i + j ) * p1 / p2

    for j in range ( i + 1, n ):
      p1 = 1.0
      for k in range ( j + 1, n ):
        p1 = p1 * d[k]
      p2 = 1.0
      for k in range ( 0, n - i ):
        p2 = p2 * d[k]
      a[i,j] = p1 / p2

  return a

def fibonacci3_test ( ):

#*****************************************************************************80
#
## FIBONACCI3_TEST tests FIBONACCI3.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 January 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'FIBONACCI3_TEST'
  print '  FIBONACCI3 computes the FIBONACCI3 matrix.'

  m = 5
  n = m

  a = fibonacci3 ( n )
  r8mat_print ( m, n, a, '  FIBONACCI3 matrix:' )

  print ''
  print 'FIBONACCI3_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  fibonacci3_test ( )
  timestamp ( )
