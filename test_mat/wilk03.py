#! /usr/bin/env python
#
def wilk03 ( ):

#*****************************************************************************80
#
## WILK03 returns the WILK03 matrix.
#
#  Formula:
#
#    1.0E-10  0.9  -0.4
#    0        0.9  -0.4
#    0        0     1.0E-10
#
#  Discussion:
#
#    The linear equation under study is
#      A * X = B,
#    where A is the 3 by 3 Wilkinson matrix, and
#      B = ( 0, 0, 1 )'
#    and the correct solution is
#      X = ( 0, 4.0E+10 / 9.0, 1.0E+10 )
#
#    Since the matrix is already in upper triangular form, errors can
#    occur only in the backsubstitution.
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is upper triangular.
#
#    det ( A ) = 0.9E-20
#
#    LAMBDA = ( 1.0E-10, 0.9, 1.0E-10 )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    James Wilkinson,
#    Error Analysis of Direct Methods of Matrix Inversion,
#    Journal of the Association for Computing Machinery,
#    Volume 8, 1961, pages 281-330.
#
#  Parameters:
#
#    Output, real A(3,3), the matrix.
#
  import numpy as np

  a = np.array ( [ \
   [ 1.0E-10,  0.9, -0.4 ], \
   [ 0.0,      0.9, -0.4 ], \
   [ 0.0,      0.0,  1.0E-10 ] ] )

  return a

def wilk03_condition ( ):

#*****************************************************************************80
#
## WILK03_CONDITION returns the L1 condition of the WILK03 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Output, real COND, the L1 condition number.
#
  cond = 1.8 * ( 13.0 * 1.0E+10 / 9.0 )

  return cond

def wilk03_condition_test ( ):

#*****************************************************************************80
#
## WILK03_CONDITION_TEST tests WILK03_CONDITION.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 December 2014
#
#  Author:
#
#    John Burkardt
#
  from wilk03 import wilk03
  from r8mat_print import r8mat_print

  print ''
  print 'WILK03_CONDITION_TEST'
  print '  WILK03_CONDITION computes the condition of the WILK03 matrix.'
  print ''

  n = 3
  a = wilk03 ( )
  r8mat_print ( n, n, a, '  WILK03 matrix:' )

  value = wilk03_condition ( )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'WILK03_CONDITION_TEST'
  print '  Normal end of execution.'

  return

def wilk03_determinant ( ):

#*****************************************************************************80
#
## WILK03_DETERMINANT returns the determinant of the WILK03 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 February 2015
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
  value = 0.9E-20

  return value

def wilk03_determinant_test ( ):

#*****************************************************************************80
#
## WILK03_DETERMINANT_TEST tests WILK03_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 February 2015
#
#  Author:
#
#    John Burkardt
#
  from wilk03 import wilk03
  from r8mat_print import r8mat_print

  print ''
  print 'WILK03_DETERMINANT_TEST'
  print '  WILK03_DETERMINANT computes the determinant of the WILK03 matrix.'
  print ''

  n = 3
  a = wilk03 ( )
  r8mat_print ( n, n, a, '  WILK03 matrix:' )

  value = wilk03_determinant ( )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'WILK03_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def wilk03_inverse ( ):

#*****************************************************************************80
#
## WILK03_INVERSE returns the inverse of the WILK03 matrix.
#
#  Formula:
#
#    1.0D+10  -1.0D+10  0
#    0         10/9     4/9 * 1.0D+10
#    0         0        1.0D+10
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
#    Output, real A(3,3), the matrix.
#
  import numpy as np
#
#  Note that the matrix entries are listed by row.
#
  a = np.array ( [ \
    [ 1.0E+10, - 1.0E+10,      0.0 ], \
    [ 0.0,       10.0 / 9.0,   4.0E+10 / 9.0 ], \
    [ 0.0,       0.0,          1.0E+10 ] ] )

  return a

def wilk03_rhs ( ):

#*****************************************************************************80
#
## WILK03_RHS returns the right hand side of the WILK03 linear system.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real B(3,1), the right hand side of the system.
#
  import numpy as np

  b = np.array ( [ [ 0.0 ], [ 0.0 ], [ 1.0 ] ] )

  return b

def wilk03_solution ( ):

#*****************************************************************************80
#
## WILK03_SOLUTION returns the solution of the WILK03 linear system.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real X(3,1), the solution of the linear system.
#
  import numpy as np

  x = np.array ( [ [ 0.0 ], [ 4.0E+10 / 9.0 ], [ 1.0E+10 ] ] )

  return x

def wilk03_test ( ):

#*****************************************************************************80
#
## WILK03_TEST tests WILK03.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 December 2014
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'WILK03_TEST'
  print '  WILK03 computes the WILK03 matrix.'

  n = 3
  a = wilk03 ( )
  r8mat_print ( n, n, a, '  WILK03 matrix:' )

  print ''
  print 'WILK03_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  wilk03_test ( )
  timestamp ( )
