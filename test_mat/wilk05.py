#! /usr/bin/env python
#
def wilk05 ( ):

#*****************************************************************************80
#
## WILK05 returns the WILK05 matrix.
#
#  Formula:
#
#    A(I,J) = 1.8144 / ( I + J + 1 )
#
#  Example:
#
#    0.604800  0.453600  0.362880  0.302400  0.259200
#    0.453600  0.362880  0.302400  0.259200  0.226800
#    0.362880  0.302400  0.259200  0.226800  0.201600
#    0.302400  0.259200  0.226800  0.201600  0.181440
#    0.259200  0.226800  0.201600  0.181440  0.164945
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A is essentially a scaled portion of the Hilbert matrix.
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
#  Reference:
#
#    James Wilkinson,
#    The Algebraic Eigenvalue Problem,
#    Oxford University Press, 1965,
#    page 234.
#
#  Parameters:
#
#    Output, real A(5,5), the matrix.
#
  import numpy as np

  n = 5

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      a[i,j] = 1.8144 / float ( i + j + 3 )

  return a

def wilk05_condition ( ):

#*****************************************************************************80
#
## WILK05_CONDITION returns the L1 condition of the WILK05 matrix.
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
#    Output, real VALUE, the L1 condition.
#
  a_norm = 1.98288
  b_norm = 4.002777777857721E+06
  value = a_norm * b_norm

  return value

def wilk05_condition_test ( ):

#*****************************************************************************80
#
## WILK05_CONDITION_TEST tests WILK05_CONDITION.
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
  from wilk05 import wilk05
  from r8mat_print import r8mat_print

  print ''
  print 'WILK05_CONDITION_TEST'
  print '  WILK05_CONDITION computes the condition of the WILK05 matrix.'
  print ''

  n = 5
  a = wilk05 ( )
  r8mat_print ( n, n, a, '  WILK05 matrix:' )

  value = wilk05_condition ( )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'WILK05_CONDITION_TEST'
  print '  Normal end of execution.'

  return

def wilk05_determinant ( ):

#*****************************************************************************80
#
## WILK05_DETERMINANT returns the determinant of the WILK05 matrix.
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
  value = 3.7995E-15

  return value

def wilk05_determinant_test ( ):

#*****************************************************************************80
#
## WILK05_DETERMINANT_TEST tests WILK05_DETERMINANT.
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
  from wilk05 import wilk05
  from r8mat_print import r8mat_print

  print ''
  print 'WILK05_DETERMINANT_TEST'
  print '  WILK05_DETERMINANT computes the determinant of the WILK05 matrix.'
  print ''

  n = 5
  a = wilk05 ( )
  r8mat_print ( n, n, a, '  WILK05 matrix:' )

  value = wilk05_determinant ( )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'WILK05_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def wilk05_inverse ( ):

#*****************************************************************************80
#
## WILK05_INVERSE returns the inverse of the WILK05 matrix.
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
#    Output, real A(5,5), the matrix.
#
  import numpy as np

  a = np.array ( [ \
  [  0.002025462963002E+06, \
    -0.016203703704040E+06, \
     0.043750000000952E+06, \
    -0.048611111112203E+06, \
     0.019097222222661E+06 ], \
  [ -0.016203703704042E+06, \
     0.138271604941179E+06, \
    -0.388888888897095E+06, \
     0.444444444453843E+06, \
    -0.178240740744515E+06 ], \
  [  0.043750000000962E+06, \
    -0.388888888897136E+06, \
     1.125000000023251E+06, \
    -1.312500000026604E+06, \
     0.534722222232897E+06 ], \
  [ -0.048611111112219E+06, \
     0.444444444453930E+06, \
    -1.312500000026719E+06, \
     1.555555555586107E+06, \
    -0.641666666678918E+06 ], \
  [  0.019097222222669E+06, \
    -0.178240740744564E+06, \
     0.534722222232983E+06, \
    -0.641666666678964E+06, \
     0.267361111116040E+06 ] ] )

  return a

def wilk05_test ( ):

#*****************************************************************************80
#
## WILK05_TEST tests WILK05.
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
  from r8mat_print import r8mat_print

  print ''
  print 'WILK05_TEST'
  print '  WILK05 computes the WILK05 matrix.'

  n = 5
  a = wilk05 ( )
  r8mat_print ( n, n, a, '  WILK05 matrix:' )

  print ''
  print 'WILK05_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  wilk05_test ( )
  timestamp ( )
