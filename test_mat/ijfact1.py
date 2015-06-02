#! /usr/bin/env python
#
def ijfact1 ( n ):

#*****************************************************************************80
#
## IJFACT1 returns the IJFACT1 matrix.
#
#  Formula:
#
#    A(I,J) = (I+J)!
#
#  Example:
#
#    N = 4
#
#     2   6   24   120
#     6  24  120   720
#    24 120  720  5040
#   120 720 5040 40320
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
      a[i,j] = r8_factorial ( i + j + 2 )

  return a

def ijfact1_determinant ( n ):

#*****************************************************************************80
#
## IJFACT1_DETERMINANT computes the determinant of the IJFACT1 matrix.
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

  for i in range ( 1, n ):
    value = value * r8_factorial ( i + 1 ) * r8_factorial ( n - i )

  value = value * r8_factorial ( n + 1 )

  return value

def ijfact1_determinant_test ( ):

#*****************************************************************************80
#
## IJFACT1_DETERMINANT_TEST tests IJFACT1_DETERMINANT.
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
  from ijfact1 import ijfact1
  from r8mat_print import r8mat_print

  print ''
  print 'IJFACT1_DETERMINANT_TEST'
  print '  IJFACT1_DETERMINANT computes the IJFACT1 determinant.'

  m = 5
  n = m
 
  a = ijfact1 ( n )

  r8mat_print ( m, n, a, '  IJFACT1 matrix:' )

  value = ijfact1_determinant ( n )

  print '  Value =  %g' % ( value )

  print ''
  print 'IJFACT1_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def ijfact1_test ( ):

#*****************************************************************************80
#
## IJFACT1_TEST tests IJFACT1.
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
  print 'IJFACT1_TEST'
  print '  IJFACT1 computes the IJFACT1 matrix.'

  m = 5
  n = m

  a = ijfact1 ( n )
 
  r8mat_print ( m, n, a, '  IJFACT1 matrix:' )

  print ''
  print 'IJFACT1_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  ijfact1_test ( )
  timestamp ( )
