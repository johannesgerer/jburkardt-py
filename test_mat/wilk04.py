#! /usr/bin/env python
#
def wilk04 ( ):

#*****************************************************************************80
#
## WILK04 returns the WILK04 matrix.
#
#  Formula:
#
#    0.9143D-04  0.0         0.0         0.0
#    0.8762      0.7156D-04  0.0         0.0
#    0.7943      0.8143      0.9504D-04  0.0
#    0.8017      0.6123      0.7165      0.7123D-04
#
#  Properties:
#
#    A is lower triangular.
#
#    LAMBDA = ( 0.9143D-04, 0.7156D-04, 0.9504D-04, 0.7123D-04 ).
#
#  Discussion:
#
#    Since the matrix is already in lower triangular form, errors can
#    occur only in the backsubstitution.  However, even a double
#    precision calculation will show a significant degradation in the
#    solution.  It is also instructive to compare the actual error in
#    the solution to the residual error, A*x-b.
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
#    Rounding Errors in Algebraic Processes,
#    Prentice Hall, 1963, page 105.
#
#  Parameters:
#
#    Output, real A(4,4), the matrix.
#
  import numpy as np

  a = np.array ( [ \
    [ 0.9143E-04, 0.8762,     0.7943,     0.8017 ], \
    [ 0.0000,     0.7156E-04, 0.8143,     0.6123 ], \
    [ 0.0000,     0.0000,     0.9504E-04, 0.7165 ], \
    [ 0.0000,     0.0000,     0.0000,     0.7123E-04 ] ] )

  return a

def wilk04_condition ( ):

#*****************************************************************************80
#
## WILK04_CONDITION returns the L1 condition of the WILK04 matrix.
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
  a_norm = 2.1306;
  b_norm = 1.154098458240528E+16;
  value = a_norm * b_norm;

  return value

def wilk04_condition_test ( ):

#*****************************************************************************80
#
## WILK04_CONDITION_TEST tests WILK04_CONDITION.
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
  from wilk04 import wilk04
  from r8mat_print import r8mat_print

  print ''
  print 'WILK04_CONDITION_TEST'
  print '  WILK04_CONDITION computes the condition of the WILK04 matrix.'
  print ''

  n = 4
  a = wilk04 ( )
  r8mat_print ( n, n, a, '  WILK04 matrix:' )

  value = wilk04_condition ( )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'WILK04_CONDITION_TEST'
  print '  Normal end of execution.'

  return

def wilk04_determinant ( ):

#*****************************************************************************80
#
## WILK04_DETERMINANT returns the determinant of the WILK04 matrix.
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
  value = 0.9143E-04 * 0.7156E-04 * 0.9504E-04 * 0.7123E-04

  return value

def wilk04_determinant_test ( ):

#*****************************************************************************80
#
## WILK04_DETERMINANT_TEST tests WILK04_DETERMINANT.
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
  from wilk04 import wilk04
  from r8mat_print import r8mat_print

  print ''
  print 'WILK04_DETERMINANT_TEST'
  print '  WILK04_DETERMINANT computes the determinant of the WILK04 matrix.'
  print ''

  n = 4
  a = wilk04 ( )
  r8mat_print ( n, n, a, '  WILK04 matrix:' )

  value = wilk04_determinant ( )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'WILK04_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def wilk04_inverse ( ):

#*****************************************************************************80
#
## WILK04_INVERSE returns the inverse of the WILK04 matrix.
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
#    Output, real A(4,4), the matrix.
#
  import numpy as np
#
#  Note that the matrix entries are listed by row.
#
  a = np.array ( [ \
  [  0.000000000001094E+16, \
    -0.000000013391962E+16, \
     0.000114732803288E+16, \
    -1.153978022391245E+16 ], \
  [  0.000000000000000, \
     0.000000000001397E+16, \
    -0.000000011973129E+16, \
     0.000120425263952E+16 ], \
  [  0.000000000000000, \
     0.000000000000000, \
     0.000000000001052E+16, \
    -0.000000010583927E+16 ], \
  [  0.000000000000000, \
     0.000000000000000, \
     0.000000000000000, \
     0.000000000001404E+16 ] ] )

  return a

def wilk04_rhs ( ):

#*****************************************************************************80
#
## WILK04_RHS returns the right hand side of the WILK04 linear system.
#
#  Formula:
#
#    0.6524
#    0.3127
#    0.4186
#    0.7853
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
#    Output, real B(4,1), the right hand side of the system.
#
  import numpy as np

  b = np.array ( [ [ 0.6524 ], [ 0.3127 ], [ 0.4186 ], [ 0.7853 ] ] )

  return b

def wilk04_solution ( ):

#*****************************************************************************80
#
## WILK04_SOLUTION returns the solution of the WILK04 linear system.
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
#    Output, real X(4,1), the solution of the system.
#
  import numpy as np

  x = np.array ( [ \
   [ -9.061709180193406e+15 ], \
   [  9.456494826647572e+11 ], \
   [ -8.311117178175363e+07 ], \
   [  1.102484908044364e+04 ] ] )

  return x

def wilk04_test ( ):

#*****************************************************************************80
#
## WILK04_TEST tests WILK04.
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
  print 'WILK04_TEST'
  print '  WILK04 computes the WILK04 matrix.'

  n = 4
  a = wilk04 ( )
  r8mat_print ( n, n, a, '  WILK04 matrix:' )

  print ''
  print 'WILK04_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  wilk04_test ( )
  timestamp ( )
