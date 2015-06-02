#! /usr/bin/env python
#
def rutis1 ( ):

#*****************************************************************************80
#
## RUTIS1 returns the RUTIS1 matrix.
#
#  Example:
#
#    6 4 4 1
#    4 6 1 4
#    4 1 6 4
#    1 4 4 6
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#    A is integral, therefore det ( A ) is integral, and 
#    det ( A ) * inverse ( A ) is integral.
#
#    A has constant row sums.
#
#    Because it has a constant row sum of 15,
#    A has an eigenvalue of 15, and
#    a (right) eigenvector of ( 1, 1, 1, 1 ).
#
#    A has constant column sums.
#
#    Because it has a constant column sum of 15,
#    A has an eigenvalue of 15, and
#    a (left) eigenvector of ( 1, 1, 1, ..., 1 ).
#
#    A has a repeated eigenvalue.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 January 2015
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
#    Output, real A(4,4), the matrix.
#
  import numpy as np

  a = np.array ( [ \
   [  6.0,  4.0,  4.0,  1.0 ], \
   [  4.0,  6.0,  1.0,  4.0 ], \
   [  4.0,  1.0,  6.0,  4.0 ], \
   [  1.0,  4.0,  4.0,  6.0 ] ] );

  return a

def rutis1_condition ( ):

#*****************************************************************************80
#
## RUTIS1_CONDITION returns the L1 condition of the RUTIS1 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real VALUE, the condition.
#
  a_norm = 15.0
  b_norm = 1.0
  value = a_norm * b_norm

  return value

def rutis1_condition_test ( ):

#*****************************************************************************80
#
## RUTIS1_CONDITION_TEST tests RUTIS1_CONDITION.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 January 2015
#
#  Author:
#
#    John Burkardt
#
  from rutis1 import rutis1
  from r8mat_print import r8mat_print

  print ''
  print 'RUTIS1_CONDITION_TEST'
  print '  RUTIS1_CONDITION computes the condition of the RUTIS1 matrix.'
  print ''

  n = 4
  a = rutis1 ( )
  r8mat_print ( n, n, a, '  RUTIS1 matrix:' )

  value = rutis1_condition ( )
  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'RUTIS1_CONDITION_TEST'
  print '  Normal end of execution.'

  return

def rutis1_determinant ( ):

#*****************************************************************************80
#
## RUTIS1_DETERMINANT returns the determinant of the RUTIS1 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real VALUE, the determinant.
#
  value = - 375.0

  return value

def rutis1_determinant_test ( ):

#*****************************************************************************80
#
## RUTIS1_DETERMINANT_TEST tests RUTIS1_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 January 2015
#
#  Author:
#
#    John Burkardt
#
  from rutis1 import rutis1
  from r8mat_print import r8mat_print

  print ''
  print 'RUTIS1_DETERMINANT_TEST'
  print '  RUTIS1_DETERMINANT computes the determinant of the RUTIS1 matrix.'
  print ''

  n = 4
  a = rutis1 ( )
  r8mat_print ( n, n, a, '  RUTIS1 matrix:' )

  value = rutis1_determinant ( )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'RUTIS1_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def rutis1_eigen_right ( ):

#*****************************************************************************80
#
## RUTIS1_EIGEN_RIGHT returns the right eigenvectors of the RUTIS1 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real A(4,4), the right eigenvector matrix.
#
  import numpy as np

  a = np.array ( [ \
    [ 1.0,  1.0,  0.0,  1.0 ], \
    [ 1.0,  0.0,  1.0, -1.0 ], \
    [ 1.0,  0.0, -1.0, -1.0 ], \
    [ 1.0, -1.0,  0.0,  1.0 ] ] )

  return a

def rutis1_eigenvalues ( ):

#*****************************************************************************80
#
## RUTIS1_EIGENVALUES returns the eigenvalues of the RUTIS1 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real LAM(4), the eigenvalues.
#
  import numpy as np

  lam = np.array ( [ \
    [ 15.0 ], \
    [  5.0 ], \
    [  5.0 ], \
    [ -1.0 ] ] )

  return lam

def rutis1_inverse ( ):

#*****************************************************************************80
#
## RUTIS1_INVERSE returns the inverse of the RUTIS1 matrix.
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
#    Output, real A(4,4), the matrix.
#
  import numpy as np
#
#  Note that the matrix entries are listed by row.
#
  a = np.array ( [ \
    [ -2.0,  4.0,  4.0, -5.0 ], \
    [  4.0, -2.0, -5.0,  4.0 ], \
    [  4.0, -5.0, -2.0,  4.0 ], \
    [ -5.0,  4.0,  4.0, -2.0 ] ] )

  for i in range ( 0, 4 ):
    for j in range ( 0, 4 ):
      a[i,j] = a[i,j] / 15.0

  return a

def rutis1_test ( ):

#*****************************************************************************80
#
## RUTIS1_TEST tests RUTIS1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 January 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'RUTIS1_TEST'
  print '  RUTIS1 computes the RUTIS1 matrix.'

  n = 4
  a = rutis1 ( )
  r8mat_print ( n, n, a, '  RUTIS1 matrix:' )

  print ''
  print 'RUTIS1_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  rutis1_test ( )
  timestamp ( )
