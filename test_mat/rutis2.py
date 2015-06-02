#! /usr/bin/env python
#
def rutis2 ( ):

#*****************************************************************************80
#
## RUTIS2 returns the RUTIS2 matrix.
#
#  Example:
#
#    5 4 1 1
#    4 5 1 1
#    1 1 4 2
#    1 1 2 4
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#    A is integral, therefore det ( A ) is integral, and 
#    det ( A ) * inverse ( A ) is integral.
#
#    A has distinct eigenvalues.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 January 2015
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
   [  5.0,  4.0,  1.0,  1.0 ], \
   [  4.0,  5.0,  1.0,  1.0 ], \
   [  1.0,  1.0,  4.0,  2.0 ], \
   [  1.0,  1.0,  2.0,  4.0 ] ] );

  return a

def rutis2_condition ( ):

#*****************************************************************************80
#
## RUTIS2_CONDITION returns the L1 condition of the RUTIS2 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real VALUE, the condition.
#
  a_norm = 11.0
  b_norm = 1.04
  value = a_norm * b_norm

  return value

def rutis2_condition_test ( ):

#*****************************************************************************80
#
## RUTIS2_CONDITION_TEST tests RUTIS2_CONDITION.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 January 2015
#
#  Author:
#
#    John Burkardt
#
  from rutis2 import rutis2
  from r8mat_print import r8mat_print

  print ''
  print 'RUTIS2_CONDITION_TEST'
  print '  RUTIS2_CONDITION computes the condition of the RUTIS2 matrix.'
  print ''

  n = 4
  a = rutis2 ( )
  r8mat_print ( n, n, a, '  RUTIS2 matrix:' )

  value = rutis2_condition ( )
  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'RUTIS2_CONDITION_TEST'
  print '  Normal end of execution.'

  return

def rutis2_determinant ( ):

#*****************************************************************************80
#
## RUTIS2_DETERMINANT returns the determinant of the RUTIS2 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real VALUE, the determinant.
#
  value = 100.0

  return value

def rutis2_determinant_test ( ):

#*****************************************************************************80
#
## RUTIS2_DETERMINANT_TEST tests RUTIS2_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 January 2015
#
#  Author:
#
#    John Burkardt
#
  from rutis2 import rutis2
  from r8mat_print import r8mat_print

  print ''
  print 'RUTIS2_DETERMINANT_TEST'
  print '  RUTIS2_DETERMINANT computes the determinant of the RUTIS2 matrix.'
  print ''

  n = 4
  a = rutis2 ( )
  r8mat_print ( n, n, a, '  RUTIS2 matrix:' )

  value = rutis2_determinant ( )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'RUTIS2_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def rutis2_eigen_right ( ):

#*****************************************************************************80
#
## RUTIS2_EIGEN_RIGHT returns the right eigenvectors of the RUTIS2 matrix.
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
#    Output, real A(4,4), the right eigenvector matrix.
#
  import numpy as np

  a = np.array ( [ \
    [  2.0, -1.0,  0.0, -1.0 ], \
    [  2.0, -1.0,  0.0,  1.0 ], \
    [  1.0,  2.0, -1.0,  0.0 ], \
    [  1.0,  2.0,  1.0,  0.0 ] ] )

  return a

def rutis2_eigenvalues ( ):

#*****************************************************************************80
#
## RUTIS2_EIGENVALUES returns the eigenvalues of the RUTIS2 matrix.
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
#    Output, real LAM(4), the eigenvalues.
#
  import numpy as np

  lam = np.array ( [ \
    [ 10.0 ], \
    [  5.0 ], \
    [  2.0 ], \
    [  1.0 ] ] )

  return lam

def rutis2_inverse ( ):

#*****************************************************************************80
#
## RUTIS2_INVERSE returns the inverse of the RUTIS2 matrix.
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
#    Output, real A(4,4), the matrix.
#
  import numpy as np
#
#  Note that the matrix entries are listed by row.
#
  a = np.array ( [ \
    [  28.0,  -22.0, -1.0, -1.0 ], \
    [ -22.0,   28.0, -1.0, -1.0 ], \
    [  -1.0,   -1.0, 17.0, -8.0 ], \
    [  -1.0,   -1.0, -8.0, 17.0 ] ] )

  for j in range ( 0, 4 ):
    for i in range ( 0, 4 ):
      a[i,j] = a[i,j] / 50.0

  return a

def rutis2_test ( ):

#*****************************************************************************80
#
## RUTIS2_TEST tests RUTIS2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 January 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'RUTIS2_TEST'
  print '  RUTIS2 computes the RUTIS2 matrix.'

  n = 4
  a = rutis2 ( )
  r8mat_print ( n, n, a, '  RUTIS2 matrix:' )

  print ''
  print 'RUTIS2_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  rutis2_test ( )
  timestamp ( )
