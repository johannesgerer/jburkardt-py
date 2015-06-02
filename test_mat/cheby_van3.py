#! /usr/bin/env python
#
def cheby_van3 ( n ):

#*****************************************************************************80
#
## CHEBY_VAN3 returns the CHEBY_VAN3 matrix.
#
#  Discussion:
#
#    CHEBY_VAN3 is the Chebyshev Vandermonde-like matrix.
#
#  Formula:
#
#    A(I,J) = cos ( (I-1) * (J-1/2) * PI / N )
#
#  Example:
#
#    N = 4
#
#        1            1           1            1
#    COS(  PI/8)  COS(3*PI/8) COS( 5*PI/8) COS( 7*PI/8)
#    COS(2*PI/8)  COS(6*PI/8) COS(10*PI/8) COS(14*PI/8)
#    COS(3*PI/8)  COS(9*PI/8) COS(15*PI/8) COS(21*PI/8)
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is "almost" orthogonal.  A * A' = a diagonal matrix.
#
#    The entries of A are based on the zeros of the Chebyshev polynomial T(n).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 January 2015
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
  import numpy as np

  r8_pi = 3.141592653589793

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      angle = i * ( 2 * j + 1 ) * r8_pi / ( 2 * n )

      a[i,j] = cos ( angle )

  return a

def cheby_van3_determinant ( n ):

#*****************************************************************************80
#
## CHEBY_VAN3_DETERMINANT computes the determinant of the CHEBY_VAN3 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 January 2015
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
  from math import sqrt

  determ = r8_mop ( n + 1 ) * sqrt ( float ( n ) ** n ) / sqrt ( 2.0 ** ( n - 1 ) )
 
  return determ

def cheby_van3_determinant_test ( ):

#*****************************************************************************80
#
## CHEBY_VAN3_DETERMINANT_TEST tests CHEBY_VAN3_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 January 2015
#
#  Author:
#
#    John Burkardt
#
  from cheby_van3 import cheby_van3
  from r8mat_print import r8mat_print

  print ''
  print 'CHEBY_VAN3_DETERMINANT_TEST'
  print '  CHEBY_VAN3_DETERMINANT computes the CHEBY_VAN3 determinant.'

  m = 5
  n = m
  a = cheby_van3 ( n )
  r8mat_print ( n, n, a, '  CHEBY_VAN3 matrix:' )

  value = cheby_van3_determinant ( n )
  print '  Value =  %g' % ( value )

  print ''
  print 'CHEBY_VAN3_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def cheby_van3_inverse ( n ):

#*****************************************************************************80
#
## CHEBY_VAN3_INVERSE inverts the CHEBY_VAN3 matrix.
#
#  Discussion:
#
#    CHEBY_VAN3 is the Chebyshev Vandermonde-like matrix.
#
#  Formula:
#
#    if J == 1 then
#      A(I,J) = (1/N) * cos ( (I-1/2) * (J-1) * PI / N )
#    else if 1 < J then
#      A(I,J) = (2/N) * cos ( (I-1/2) * (J-1) * PI / N )
#
#  Example:
#
#    N = 4
#
#    1/4  1/2 cos(  PI/8)  1/2 cos( 2*PI/8)  1/2 cos( 3*PI/8)
#    1/4  1/2 cos(3*PI/8)  1/2 cos( 6*PI/8)  1/2 cos( 9*PI/8)
#    1/4  1/2 cos(5*PI/8)  1/2 cos(10*PI/8)  1/2 cos(15*PI/8)
#    1/4  1/2 cos(7*PI/8)  1/2 cos(14*PI/8)  1/2 cos(21*PI/8)
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

      angle = float ( ( 2 * i + 1 ) * j ) * np.pi / float ( 2 * n )

      a[i,j] = np.cos ( angle ) / float ( n )

  for i in range ( 0, n ):
    for j in range ( 1, n ):
      a[i,j] = 2.0 * a[i,j]

  return a

def cheby_van3_test ( ):

#*****************************************************************************80
#
## CHEBY_VAN3_TEST tests CHEBY_VAN3.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 January 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'CHEBY_VAN3_TEST'
  print '  CHEBY_VAN3 computes the CHEBY_VAN3 matrix.'

  m = 5
  n = m
  a = cheby_van3 ( n )
  r8mat_print ( m, n, a, '  CHEBY_VAN3 matrix:' )

  print ''
  print 'CHEBY_VAN3_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  cheby_van3_test ( )
  timestamp ( )
