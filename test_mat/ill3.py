#! /usr/bin/env python
#
def ill3 ( ):

#*****************************************************************************80
#
## ILL3 returns the ILL3 matrix.
#
#  Discussion:
#
#    This is an ill conditioned 3 by 3 matrix.
#
#  Formula:
#
#    -149  -50 -154
#     537  180  546
#     -27   -9  -25
#
#  Properties:
#
#    A is integral, therefore det ( A ) is integral, and 
#    det ( A ) * inverse ( A ) is integral.
#
#    The eigenvalues are ( 1, 2, 3 ).
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
#  Reference:
#
#    Joan Westlake,
#    A Handbook of Numerical Matrix Inversion and Solution of 
#    Linear Equations,
#    John Wiley, 1968,
#    ISBN13: 978-0471936756,
#    LC: QA263.W47.
#
#  Parameters:
#
#    Output, real A(3,3), the matrix.
#
  import numpy as np

  a = np.array ( [ 
   [ -149.0, -50.0, -154.0 ], \
   [  537.0, 180.0,  546.0 ], \
   [  -27.0,  -9.0,  -25.0 ] ] )

  return a

def ill3_condition ( ):

#*****************************************************************************80
#
## ILL3_CONDITION returns the L1 condition of the ILL3 matrix.
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
#    Output, real VALUE, the L1 condition number.
#
  value = 725 * 299

  return value

def ill3_condition_test ( ):

#*****************************************************************************80
#
## ILL3_CONDITION_TEST tests ILL3_CONDITION.
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
  from ill3 import ill3
  from r8mat_print import r8mat_print

  print ''
  print 'ILL3_CONDITION_TEST'
  print '  ILL3_CONDITION computes the condition of the ILL3 matrix.'
  print ''

  m = 3
  n = m
  a = ill3 ( )
  r8mat_print ( m, n, a, '  ILL3 matrix:' )

  value = ill3_condition ( )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'ILL3_CONDITION_TEST'
  print '  Normal end of execution.'

  return

def ill3_determinant ( ):

#*****************************************************************************80
#
## ILL3_DETERMINANT returns the determinant of the ILL3 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real VALUE, the determinant number.
#
  value = 6.0

  return value

def ill3_determinant_test ( ):

#*****************************************************************************80
#
## ILL3_DETERMINANT_TEST tests ILL3_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 January 2015
#
#  Author:
#
#    John Burkardt
#
  from ill3 import ill3
  from r8mat_print import r8mat_print

  print ''
  print 'ILL3_DETERMINANT_TEST'
  print '  ILL3_DETERMINANT computes the determinant of the ILL3 matrix.'
  print ''

  m = 3
  n = m
  a = ill3 ( )
  r8mat_print ( m, n, a, '  ILL3 matrix:' )

  value = ill3_determinant ( )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'ILL3_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def ill3_eigen_right ( ):

#*****************************************************************************80
#
## ILL3_EIGEN_RIGHT returns the right eigenvectors of the ILL3 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Joan Westlake,
#    A Handbook of Numerical Matrix Inversion and Solution of
#    Linear Equations,
#    John Wiley, 1968,
#    ISBN13: 978-0471936756,
#    LC: QA263.W47.
#
#  Parameters:
#
#    Output, real A(3,3), the right eigenvector matrix.
#
  import numpy as np
#
#  Note that the matrix entries are listed by row.
#
  a = np.array ( [ \
  [ -0.139139989879567,   \
    -0.404061017818396,   \
     0.316227766017190 ], \
  [  0.973979929161820,   \
     0.909137290098421,   \
    -0.948683298050396 ], \
  [ -0.178894272703878,   \
     0.101015254452291,   \
    -0.000000000000407 ] ] )

  return a

def ill3_eigenvalues ( ):

#*****************************************************************************80
#
## ILL3_EIGENVALUES returns the eigenvalues of the ILL3 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Joan Westlake,
#    A Handbook of Numerical Matrix Inversion and Solution of
#    Linear Equations,
#    John Wiley, 1968,
#    ISBN13: 978-0471936756,
#    LC: QA263.W47.
#
#  Parameters:
#
#    Output, real LAMBDA(3), the eigenvalues.
#
  import numpy as np

  lam = np.array ( [ 3.0, 2.0, 1.0 ] )

  return lam

def ill3_inverse ( ):

#*****************************************************************************80
#
## ILL3_INVERSE returns the inverse of the ILL3 matrix.
#
#  Formula:
#
#      69     68/3   70
#    -439/2 -433/6 -224
#       9/2    3/2    5
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 March 2015
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
      [   69.0,         68.0 / 3.0,   70.0 ], \
      [ -439.0 / 2.0, -433.0 / 6.0, -224.0 ], \
      [    4.5,          1.5,          5.0 ] ] )

  return a

def ill3_test ( ):

#*****************************************************************************80
#
## ILL3_TEST tests ILL3.
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
  from r8mat_print import r8mat_print

  print ''
  print 'ILL3_TEST'
  print '  ILL3 computes the ILL3 matrix.'

  m = 3
  n = m
  a = ill3 (  )
  r8mat_print ( m, n, a, '  ILL3 matrix:' )

  print ''
  print 'ILL3_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  ill3_test ( )
  timestamp ( )
