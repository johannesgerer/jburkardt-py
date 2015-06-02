#! /usr/bin/env python
#
def moler2 ( ):

#*****************************************************************************80
#
## MOLER2 returns the MOLER2 matrix.
#
#  Discussion:
#
#    This is a 5 by 5 matrix for which the challenge is to find the EXACT
#    eigenvalues and eigenvectors.
#
#  Formula:
#
#       -9     11    -21     63    -252
#       70    -69    141   -421    1684
#     -575    575  -1149   3451  -13801
#     3891  -3891   7782 -23345   93365
#     1024  -1024   2048  -6144   24572
#
#  Properties:
#
#    A is defective.
#
#    The Jordan normal form of A has just one block, with eigenvalue
#    zero, because A^k is nonzero for K = 0, 1, 2, 3, 4, but A^5=0.
#
#    det ( A ) = 0.
#
#    TRACE(A) = 0.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real A(5,5), the matrix.
#
  import numpy as np

  a = np.array ( [ \
      [     -9.0,     11.0,    -21.0,     63.0,   -252.0 ], \
      [     70.0,    -69.0,    141.0,   -421.0,   1684.0 ], \
      [   -575.0,    575.0,  -1149.0,   3451.0, -13801.0 ], \
      [   3891.0,  -3891.0,   7782.0, -23345.0,  93365.0 ], \
      [   1024.0,  -1024.0,   2048.0,  -6144.0,  24572.0 ] ] )

  return a

def moler2_determinant ( ):

#*****************************************************************************80
#
## MOLER2_DETERMINANT returns the determinant of the MOLER2 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real VALUE, the determinant.
#
  value = 0.0

  return value

def moler2_determinant_test ( ):

#*****************************************************************************80
#
## MOLER2_DETERMINANT_TEST tests MOLER2_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 March 2015
#
#  Author:
#
#    John Burkardt
#
  from moler2 import moler2
  from r8mat_print import r8mat_print

  print ''
  print 'MOLER2_DETERMINANT_TEST'
  print '  MOLER2_DETERMINANT computes the determinant of the MOLER2 matrix.'
  print ''

  m = 5
  n = m

  a = moler2 ( )
  r8mat_print ( m, n, a, '  MOLER2 matrix:' )

  value = moler2_determinant ( )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'MOLER2_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def moler2_null_left ( ):

#*****************************************************************************80
#
## MOLER2_NULL_LEFT returns a left null vector of the MOLER2 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the order of the matrix.
#
#    Output, real X(M), the left null vector.
#
  import numpy as np

  x = np.array ( [ [ 4.0 ], [ -8.0 ], [ 20.0 ], [ -64.0 ], [ 255.0 ] ] )

  return x

def moler2_null_left_test ( ):

#*****************************************************************************80
#
## MOLER2_NULL_LEFT_TEST tests MOLER2_NULL_LEFT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 March 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_is_null_left import r8mat_is_null_left
  from r8mat_print import r8mat_print
  from r8vec_print import r8vec_print

  print ''
  print 'MOLER2_NULL_LEFT_TEST'
  print '  MOLER2_NULL_LEFT returns a left null vector of the MOLER2 matrix.'
  print ''

  m = 5
  n = 5

  a = moler2 ( )
  r8mat_print ( m, n, a, '  MOLER2 matrix A:' )

  x = moler2_null_left ( )
  r8vec_print ( m, x, '  Left null vector X:' )

  value = r8mat_is_null_left ( m, n, a, x )

  print ''
  print '  ||x\'*A||/||x|| =  %g' % ( value )

  print ''
  print 'MOLER2_NULL_LEFT_TEST'
  print '  Normal end of execution.'

  return

def moler2_null_right ( ):

#*****************************************************************************80
#
## MOLER2_NULL_RIGHT returns a right null vector for the MOLER2 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real X(5), the null vector.
#
  import numpy as np

  x = np.array ( [ [ 0.0 ], [ -21.0 ], [ 142.0 ], [ -973.0 ], [ -256.0 ] ] )

  return x

def moler2_test ( ):

#*****************************************************************************80
#
## MOLER2_TEST tests MOLER2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 February 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'MOLER2_TEST'
  print '  MOLER2 computes the MOLER2 matrix.'

  m = 5
  n = m

  a = moler2 ( )
  r8mat_print ( m, n, a, '  MOLER2 matrix:' )

  print ''
  print 'MOLER2_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  moler2_test ( )
  moler2_determinant_test ( )
  moler2_null_left_test ( )
  timestamp ( )
