#! /usr/bin/env python
#
def cheby_van2 ( n ):

#*****************************************************************************80
#
## CHEBY_VAN2 returns the CHEBY_VAN2 matrix.
#
#  Discussion:
#
#    CHEBY_VAN2 is the Chebyshev Vandermonde-like matrix.
#
#  Discussion:
#
#    The formula for this matrix has been slightly modified, by a scaling
#    factor, in order to make it closer to its inverse.
#
#  Formula:
#
#    A(I,J) = ( 1 / sqrt ( N - 1 ) ) * cos ( (I-1) * (J-1) * PI / (N-1) )
#
#  Example:
#
#    N = 4
#
#                 1      1           1           1
#    1/sqrt(3) *  1  COS(PI/3)   COS(2*PI/3) COS(3*PI/3)
#                 1  COS(2*PI/3) COS(4*PI/3) COS(6*PI/3)
#                 1  COS(3*PI/3) COS(6*PI/3) COS(9*PI/3)
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    The entries of A are based on the extrema of the Chebyshev
#    polynomial T(n-1).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 December 2014
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
  from math import cos
  from math import sqrt
  import numpy as np

  r8_pi = 3.141592653589793

  a = np.zeros ( ( n, n ) )

  if ( n == 1 ):
    a[0,0] = 1.0
    return a

  t = sqrt ( n - 1 )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      angle = ( i * j ) * r8_pi / ( n - 1 )
      a[i,j] = cos ( angle ) / t

  return a

def cheby_van2_determinant ( n ):

#*****************************************************************************80
#
## CHEBY_VAN2_DETERMINANT computes the determinant of the CHEBY_VAN2 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 December 2014
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
  from r8_mop import r8_mop
  from math import floor
  from math import sqrt

  if ( n <= 0 ):
    determ = 0.0
  elif ( n == 1 ):
    determ = 1.0
  else:
    determ = r8_mop ( floor ( n / 2 ) ) * sqrt ( 2.0 ) ** ( 4 - n )

  return determ

def cheby_van2_determinant_test ( ):

#*****************************************************************************80
#
## CHEBY_VAN2_DETERMINANT_TEST tests CHEBY_VAN2_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 December 2014
#
#  Author:
#
#    John Burkardt
#
  from cheby_van2 import cheby_van2
  from r8mat_print import r8mat_print

  print ''
  print 'CHEBY_VAN2_DETERMINANT_TEST'
  print '  CHEBY_VAN2_DETERMINANT computes the CHEBY_VAN2 determinant.'

  m = 5
  n = 5
  a = cheby_van2 ( n )
  r8mat_print ( n, n, a, '  CHEBY_VAN2 matrix:' )

  value = cheby_van2_determinant ( n )
  print '  Value =  %g' % ( value )

  print ''
  print 'CHEBY_VAN2_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def cheby_van2_inverse ( n ):

#*****************************************************************************80
#
#% CHEBY_VAN2_INVERSE inverts the CHEBY_VAN2 matrix.
#
#  Discussion:
#
#    CHEBY_VAN2 is the Chebyshev Vandermonde-like matrix.
#
#  Formula:
#
#    if ( I == 1 or N ) .and. ( J == 1 or N ) then
#      A(I,J) = ( 1 / (2*sqrt(N-1)) ) * cos ( (I-1) * (J-1) * PI / (N-1) )
#    else if ( I == 1 or N ) .or. ( J == 1 or N ) then
#      A(I,J) = ( 1 / (  sqrt(N-1)) ) * cos ( (I-1) * (J-1) * PI / (N-1) )
#    else
#      A(I,J) = ( 2 /    sqrt(N-1)  ) * cos ( (I-1) * (J-1) * PI / (N-1) )
#
#
#  Example:
#
#    N = 4
#
#                1/2    1             1           1/2
#    1/sqrt(3) *  1   2*COS(PI/3)   2*COS(2*PI/3)       COS(3*PI/3)
#                 1   2*COS(2*PI/3) 2*COS(4*PI/3)       COS(6*PI/3)
#                1/2    COS(3*PI/3)   COS(6*PI/3) 1/2 * COS(9*PI/3)
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    The entries of A are based on the extrema of the Chebyshev
#    polynomial T(n-1).
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

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      angle = float ( i * j ) * np.pi / float ( n - 1 )

      a[i,j] = np.cos ( angle )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      a[i,j] = 2.0 * a[i,j] / np.sqrt ( float ( n - 1 ) )

  for j in range ( 0, n ):
    a[0,j]   = 0.5 * a[0,j]
    a[n-1,j] = 0.5 * a[n-1,j]

  for i in range ( 0, n ):
    a[i,0]   = 0.5 * a[i,0]
    a[i,n-1] = 0.5 * a[i,n-1]

  return a

def cheby_van2_test ( ):

#*****************************************************************************80
#
## CHEBY_VAN2_TEST tests CHEBY_VAN2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 December 2014
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'CHEBY_VAN2_TEST'
  print '  CHEBY_VAN2 computes the CHEBY_VAN2 matrix.'

  m = 5
  n = 5
  a = cheby_van2 ( n )
  r8mat_print ( m, n, a, '  CHEBY_VAN2 matrix:' )

  print ''
  print 'CHEBY_VAN2_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  cheby_van2_test ( )
  timestamp ( )
