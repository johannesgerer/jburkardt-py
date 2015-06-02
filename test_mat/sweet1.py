#! /usr/bin/env python
#
def sweet1 ( ):

#*****************************************************************************80
#
## SWEET1 returns the SWEET1 matrix.
#
#  Example:
#
#    20.0  15.0   2.5   6.0   1.0  -2.0
#    15.0  20.0  15.0   2.5   6.0   1.0
#     2.5  15.0  20.0  15.0   2.5   6.0
#     6.0   2.5  15.0  20.0  15.0   2.5
#     1.0   6.0   2.5  15.0  20.0  15.0
#    -2.0   1.0   6.0   2.5  15.0  20.0
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A is Toeplitz: constant along diagonals.
#
#    A is persymmetric: A(I,J) = A(N+1-J,N+1-I).
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

  value = np.array ( [ 20.0, 15.0, 2.5, 6.0, 1.0, -2.0 ] )

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      a[i,j] = value[abs(j-i)];

  return a

def sweet1_condition ( ):

#*****************************************************************************80
#
## SWEET1_CONDITION returns the L1 condition of the SWEET1 matrix.
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
#    Output, real VALUE, the condition.
#
  a_norm = 61.0
  b_norm = 0.278145899201815
  value = a_norm * b_norm

  return value

def sweet1_condition_test ( ):

#*****************************************************************************80
#
## SWEET1_CONDITION_TEST tests SWEET1_CONDITION.
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
  from sweet1 import sweet1
  from r8mat_print import r8mat_print

  print ''
  print 'SWEET1_CONDITION_TEST'
  print '  SWEET1_CONDITION computes the condition of the SWEET1 matrix.'
  print ''

  n = 6
  a = sweet1 ( )
  r8mat_print ( n, n, a, '  SWEET1 matrix:' )

  value = sweet1_condition ( )
  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'SWEET1_CONDITION_TEST'
  print '  Normal end of execution.'

  return

def sweet1_determinant ( ):

#*****************************************************************************80
#
## SWEET1_DETERMINANT returns the determinant of the SWEET1 matrix.
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
#    Output, real VALUE, the determinant.
#
  value = - 2.0468186E+07

  return value

def sweet1_determinant_test ( ):

#*****************************************************************************80
#
## SWEET1_DETERMINANT_TEST tests SWEET1_DETERMINANT.
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
  from sweet1 import sweet1
  from r8mat_print import r8mat_print

  print ''
  print 'SWEET1_DETERMINANT_TEST'
  print '  SWEET1_DETERMINANT computes the determinant of the SWEET1 matrix.'
  print ''

  n = 6
  a = sweet1 ( )
  r8mat_print ( n, n, a, '  SWEET1 matrix:' )

  value = sweet1_determinant ( )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'SWEET1_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def sweet1_inverse ( ):

#*****************************************************************************80
#
## SWEET1_INVERSE returns the inverse of the SWEET1 matrix.
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
  [  0.073125159943338,  -0.029629732454063,  -0.020045010339460, \
     0.032364910109767,  -0.056244145182187,   0.052945000841794 ], \
  [ -0.029629732454063,   0.046796984109877,   0.019214941666057, \
    -0.056592264698005,   0.069667831091627,  -0.056244145182187 ], \
  [ -0.020045010339460,   0.019214941666057,   0.009031577102143, \
     0.035236537326757,  -0.056592264698005,   0.032364910109767 ], \
  [  0.032364910109767,  -0.056592264698005,   0.035236537326757, \
     0.009031577102143,   0.019214941666057,  -0.020045010339460 ], \
  [ -0.056244145182187,   0.069667831091627,  -0.056592264698005, \
     0.019214941666057,   0.046796984109877,  -0.029629732454063 ], \
  [  0.052945000841794,  -0.056244145182187,   0.032364910109767, \
    -0.020045010339460,  -0.029629732454063,   0.073125159943338 ] ] )

  return a

def sweet1_test ( ):

#*****************************************************************************80
#
## SWEET1_TEST tests SWEET1.
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
  from r8mat_print import r8mat_print

  print ''
  print 'SWEET1_TEST'
  print '  SWEET1 computes the SWEET1 matrix.'

  n = 6
  a = sweet1 ( )
  r8mat_print ( n, n, a, '  SWEET1 matrix:' )

  print ''
  print 'SWEET1_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  sweet1_test ( )
  timestamp ( )
