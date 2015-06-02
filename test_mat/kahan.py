#! /usr/bin/env python
#
def kahan ( alpha, m, n ):

#*****************************************************************************80
#
## KAHAN returns the KAHAN matrix.
#
#  Formula:
#
#    if ( I = J )
#      A(I,I) =  sin(ALPHA)^(I)
#    elseif ( I < J )
#      A(I,J) = - sin(ALPHA)^(I) * cos(ALPHA)
#    else
#      A(I,J) = 0
#
#  Example:
#
#    ALPHA = 0.25, N = 4
#
#    S  -C*S    -C*S      -C*S
#    0     S^2  -C*S^2    -C*S^2
#    0     0       S^3    -C*S^3
#    0     0       0         S^4
#
#    where
#
#      S = sin(ALPHA), C=COS(ALPHA)
#
#  Properties:
#
#    A is upper triangular.
#
#    A = B * C, where B is a diagonal matrix and C is unit upper triangular.
#    For instance, for the case M = 3, N = 4:
#
#    A = | S 0    0    |  * | 1 -C -C  -C |
#        | 0 S^2  0    |    | 0  1 -C  -C |
#        | 0 0    S^3  |    | 0  0  1  -C |
#
#    A is generally not symmetric: A' /= A.
#
#    A has some interesting properties regarding estimation of
#    condition and rank.
#
#    det ( A ) = sin(ALPHA)^(N*(N+1)/2).
#
#    LAMBDA(I) = sin ( ALPHA )^I
#
#    A is nonsingular if and only if sin ( ALPHA ) =/= 0.
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Nicholas Higham,
#    A survey of condition number estimation for triangular matrices,
#    SIAM Review,
#    Volume 9, 1987, pages 575-596.
#
#    W Kahan,
#    Numerical Linear Algebra,
#    Canadian Mathematical Bulletin,
#    Volume 9, 1966, pages 757-801.
#
#  Parameters:
#
#    Input, real ALPHA, the scalar that defines A.  A typical
#    value is 1.2.  The "interesting" range of ALPHA is 0 < ALPHA < PI.
#
#    Input, integer M, N, the number of rows and columns of A.
#
#    Output, real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( m, n ) )

  for i in range ( 0, m ):

    si = np.sin ( alpha ) ** ( i + 1 )
    csi = - np.cos ( alpha ) * si

    for j in range ( 0, n ):

      if ( j == i ):
        a[i,j] = si
      elif ( i < j ):
        a[i,j] = csi

  return a

def kahan_determinant ( alpha, n ):

#*****************************************************************************80
#
## KAHAN_DETERMINANT computes the determinant of the KAHAN matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real ALPHA, the parameter.
#
#    Input, integer N, the order of the matrix.
#
#    Output, real VALUE, the determinant.
#
  import numpy as np

  power = ( n * ( n + 1 ) ) // 2
  value = ( np.sin ( alpha ) ) ** power

  return value

def kahan_determinant_test ( ):

#*****************************************************************************80
#
## KAHAN_DETERMINANT_TEST tests KAHAN_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 December 2015
#
#  Author:
#
#    John Burkardt
#
  from kahan import kahan
  from r8_uniform_01 import r8_uniform_01
  from r8mat_print import r8mat_print

  print ''
  print 'KAHAN_DETERMINANT_TEST'
  print '  KAHAN_DETERMINANT computes the KAHAN determinant.'

  seed = 123456789

  m = 5
  n = m
  alpha, seed = r8_uniform_01 ( seed )
  a = kahan ( alpha, m, n )
  r8mat_print ( m, n, a, '  KAHAN matrix:' )

  value = kahan_determinant ( alpha, n )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'KAHAN_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def kahan_inverse ( alpha, n ):

#*****************************************************************************80
#
## KAHAN_INVERSE returns the inverse of the KAHAN matrix.
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
#    Input, real ALPHA, the scalar that defines A.  A typical 
#    value is 1.2.  The "interesting" range of ALPHA is 0 < ALPHA < PI.
#
#    Input, integer N, the order of A.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  ci = np.cos ( alpha );

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( i == j ):
        a[i,j] = 1.0;
      elif ( i == j - 1 ):
        a[i,j] = ci;
      elif ( i < j ):
        a[i,j] = ci * ( 1.0 + ci ) ** ( j - i - 1 )
#
#  Scale the columns.
#
  for j in range ( 0, n):
    si = np.sin ( alpha ) ** ( j + 1 )
    for i in range ( 0, n ):
      a[i,j] = a[i,j] / si

  return a

def kahan_test ( ):

#*****************************************************************************80
#
## KAHAN_TEST tests KAHAN.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 February 2015
#
#  Author:
#
#    John Burkardt
#
  from r8_uniform_01 import r8_uniform_01
  from r8mat_print import r8mat_print

  print ''
  print 'KAHAN_TEST'
  print '  KAHAN computes the KAHAN matrix.'

  seed = 123456789

  m = 5
  n = 5
  alpha, seed = r8_uniform_01 ( seed )
  a = kahan ( alpha, m, n )
  r8mat_print ( m, n, a, '  KAHAN matrix:' )

  print ''
  print 'KAHAN_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  kahan_test ( )
  timestamp ( )
