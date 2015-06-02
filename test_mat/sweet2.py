#! /usr/bin/env python
#
def sweet2 ( ):

#*****************************************************************************80
#
## SWEET2 returns the SWEET2 matrix.
#
#  Example:
#
#     4.0  8.0  1.0  6.0  2.0  3.0
#     6.0  4.0  8.0  1.0  6.0  2.0
#    71/15 6.0  4.0  8.0  1.0  6.0
#     5.0 71/15 6.0  4.0  8.0  1.0
#     3.0  5.0 71/15 6.0  4.0  8.0
#     1.0  3.0  5.0 71/15 6.0  4.0
#
#  Properties:
#
#    A is Toeplitz: constant along diagonals.
#
#    A is generally not symmetric: A' /= A.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Per Hansen, Tony Chan,
#    FORTRAN Subroutines for General Toeplitz Systems,
#    ACM Transactions on Mathematical Software,
#    Volume 18, Number 3, September 1992, pages 256-273.
#
#    Douglas Sweet,
#    The use of pivoting to improve the numerical performance of
#    Toeplitz solvers,
#    In "Advanced Algorithms and Architectures for Signal Processing",
#    Edited by J M Speiser,
#    Proceedings SPIE 696, 1986, pages 8-18.
#
#  Parameters:
#
#    Output, real A(6,6), the matrix.
#
  import numpy as np

  n = 6

  v = np.array ( [ 1.0, 3.0, 5.0, 71.0 / 15.0, 6.0, 4.0, \
    8.0, 1.0, 6.0, 2.0, 3.0 ] )

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      a[i,j] = v[j-i+5];

  return a

def sweet2_condition ( ):

#*****************************************************************************80
#
## SWEET2_CONDITION returns the L1 condition of the SWEET2 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real VALUE, the condition.
#
  a_norm = 30.733333333333334
  b_norm = 1.601605164968818
  value = a_norm * b_norm

  return value

def sweet2_condition_test ( ):

#*****************************************************************************80
#
## SWEET2_CONDITION_TEST tests SWEET2_CONDITION.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 February 2015
#
#  Author:
#
#    John Burkardt
#
  from sweet2 import sweet2
  from r8mat_print import r8mat_print

  print ''
  print 'SWEET2_CONDITION_TEST'
  print '  SWEET2_CONDITION computes the condition of the SWEET2 matrix.'
  print ''

  n = 6
  a = sweet2 ( )
  r8mat_print ( n, n, a, '  SWEET2 matrix:' )

  value = sweet2_condition ( )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'SWEET2_CONDITION_TEST'
  print '  Normal end of execution.'

  return

def sweet2_determinant ( ):

#*****************************************************************************80
#
## SWEET2_DETERMINANT returns the determinant of the SWEET2 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real VALUE, the determinant.
#
  value = 9.562518834567902E+03

  return value

def sweet2_determinant_test ( ):

#*****************************************************************************80
#
## SWEET2_DETERMINANT_TEST tests SWEET2_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 February 2015
#
#  Author:
#
#    John Burkardt
#
  from sweet2 import sweet2
  from r8mat_print import r8mat_print

  print ''
  print 'SWEET2_DETERMINANT_TEST'
  print '  SWEET2_DETERMINANT computes the determinant of the SWEET2 matrix.'
  print ''

  n = 6
  a = sweet2 ( )
  r8mat_print ( n, n, a, '  SWEET2 matrix:' )

  value = sweet2_determinant ( )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'SWEET2_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def sweet2_inverse ( ):

#*****************************************************************************80
#
## SWEET2_INVERSE returns the inverse of the SWEET2 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real A(6,6), the matrix.
#
  import numpy as np

  a = np.array ( [ \
  [ -0.188192659589482,  -0.145188896312202,   0.063613055049687, \
     0.406962974759668,   0.271408731947181,  -0.526238847310597 ], \
  [  0.324411348442568,   0.213721529181228,  -0.131983821377206, \
    -0.344055452089408,  -0.168794206390780,   0.271408731947181 ], \
  [  0.038585525550130,   0.275974273184732,   0.137312031652403, \
    -0.366985595257679,  -0.344055452089408,   0.406962974759669 ], \
  [ -0.105091418281329,  -0.159756451255461,   0.216482246086901, \
     0.137312031652403,  -0.131983821377206,   0.063613055049687 ], \
  [ -0.043938024069266,  -0.157319070822594,  -0.159756451255461, \
     0.275974273184732,   0.213721529181228,  -0.145188896312202 ], \
  [ -0.054227038968746,  -0.043938024069265,  -0.105091418281329, \
     0.038585525550129,   0.324411348442568,  -0.188192659589482 ] ] )

  return a



def sweet2_test ( ):

#*****************************************************************************80
#
## SWEET2_TEST tests SWEET2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 February 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'SWEET2_TEST'
  print '  SWEET2 computes the SWEET2 matrix.'

  n = 6
  a = sweet2 ( )
  r8mat_print ( n, n, a, '  SWEET2 matrix:' )

  print ''
  print 'SWEET2_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  sweet2_test ( )
  timestamp ( )
