#! /usr/bin/env python
#
def ijfact2 ( n ):

#*****************************************************************************80
#
## IJFACT2 returns the IJFACT2 matrix.
#
#  Formula:
#
#    A(I,J) = 1 / ( (I+J)! )
#
#  Example:
#
#    N = 4
#
#   1/2   1/6   1/24   1/120
#   1/6   1/24  1/120  1/720
#   1/24  1/120 1/720  1/5040
#   1/120 1/720 1/5040 1/40320
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
#    A is integral: int ( A ) = A.
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    MJC Gover,
#    The explicit inverse of factorial Hankel matrices,
#    Department of Mathematics, University of Bradford, 1993.
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np
  from r8_factorial import r8_factorial

  a = np.zeros ( [ n, n ] )
  for i in range ( 0, n ):
    for j in range ( 0, n ):
      a[i,j] = 1.0 / r8_factorial ( i + j + 2 )

  return a

def ijfact2_determinant ( n ):

#*****************************************************************************80
#
## IJFACT2_DETERMINANT computes the determinant of the IJFACT2 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Output, real VALUE, the determinant.
#
  from r8_factorial import r8_factorial

  value = 1.0

  for i in range ( 0, n ):
    value = value * r8_factorial ( i ) / r8_factorial ( n + 1 + i )

  test = ( n * ( n - 1 ) ) // 2

  if ( test % 2 != 0 ):
    value = - value

  return value

def ijfact2_determinant_test ( ):

#*****************************************************************************80
#
## IJFACT2_DETERMINANT_TEST tests IJFACT2_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 February 2015
#
#  Author:
#
#    John Burkardt
#
  from ijfact2 import ijfact2
  from r8mat_print import r8mat_print

  print ''
  print 'IJFACT2_DETERMINANT_TEST'
  print '  IJFACT2_DETERMINANT computes the IJFACT2 determinant.'

  m = 5
  n = m
 
  a = ijfact2 ( n )

  r8mat_print ( m, n, a, '  IJFACT2 matrix:' )

  value = ijfact2_determinant ( n )

  print '  Value =  %g' % ( value )

  print ''
  print 'IJFACT2_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def ijfact2_test ( ):

#*****************************************************************************80
#
## IJFACT2_TEST tests IJFACT2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 February 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'IJFACT2_TEST'
  print '  IJFACT2 computes the IJFACT2 matrix.'

  m = 5
  n = m

  a = ijfact2 ( n )
 
  r8mat_print ( m, n, a, '  IJFACT2 matrix:' )

  print ''
  print 'IJFACT2_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  ijfact2_test ( )
  timestamp ( )
