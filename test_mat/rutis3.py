#! /usr/bin/env python
#
def rutis3 ( ):

#*****************************************************************************80
#
## RUTIS3 returns the RUTIS3 matrix.
#
#  Example:
#
#    4 -5  0  3
#    0  4 -3 -5
#    5 -3  4  0
#    3  0  5  4
#
#  Properties:
#
#    A is not symmetric: A' /= A.
#
#    A is integral, therefore det ( A ) is integral, and 
#    det ( A ) * inverse ( A ) is integral.
#
#    A has distinct eigenvalues.
#
#    A has a pair of complex eigenvalues.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 February 2015
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
    [ 4.0, -5.0,  0.0,  3.0 ], \
    [ 0.0,  4.0, -3.0, -5.0 ], \
    [ 5.0, -3.0,  4.0,  0.0 ], \
    [ 3.0,  0.0,  5.0,  4.0 ] ] )

  return a

def rutis3_condition ( ):

#*****************************************************************************80
#
## RUTIS3_CONDITION returns the L1 condition of the RUTIS3 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real VALUE, the condition.
#
  a_norm = 12.0
  b_norm = 0.5
  value = a_norm * b_norm

  return value

def rutis3_condition_test ( ):

#*****************************************************************************80
#
## RUTIS3_CONDITION_TEST tests RUTIS3_CONDITION.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 February 2015
#
#  Author:
#
#    John Burkardt
#
  from rutis3 import rutis3
  from r8mat_print import r8mat_print

  print ''
  print 'RUTIS3_CONDITION_TEST'
  print '  RUTIS3_CONDITION computes the condition of the RUTIS3 matrix.'
  print ''

  n = 4
  a = rutis3 ( )
  r8mat_print ( n, n, a, '  RUTIS3 matrix:' )

  value = rutis3_condition ( )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'RUTIS3_CONDITION_TEST'
  print '  Normal end of execution.'

  return

def rutis3_determinant ( ):

#*****************************************************************************80
#
## RUTIS3_DETERMINANT returns the determinant of the RUTIS3 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real VALUE, the determinant.
#
  value = 624.0

  return value

def rutis3_determinant_test ( ):

#*****************************************************************************80
#
## RUTIS3_DETERMINANT_TEST tests RUTIS3_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 February 2015
#
#  Author:
#
#    John Burkardt
#
  from rutis3 import rutis3
  from r8mat_print import r8mat_print

  print ''
  print 'RUTIS3_DETERMINANT_TEST'
  print '  RUTIS3_DETERMINANT computes the determinant of the RUTIS3 matrix.'
  print ''

  n = 4
  a = rutis3 ( )
  r8mat_print ( n, n, a, '  RUTIS3 matrix:' )

  value = rutis3_determinant ( )
  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'RUTIS3_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def rutis3_inverse ( ):

#*****************************************************************************80
#
## RUTIS3_INVERSE returns the inverse of the RUTIS3 matrix.
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
    [  103.0,  125.0,   -5.0,  79.0 ], \
    [    5.0,  103.0,  -79.0, 125.0 ], \
    [ -125.0,  -79.0,  103.0,  -5.0 ], \
    [   79.0,    5.0, -125.0, 103.0 ] ] )

  for i in range ( 0, 4 ):
    for j in range ( 0, 4 ):
      a[i,j] = a[i,j] / 624.0

  return a

def rutis3_test ( ):

#*****************************************************************************80
#
## RUTIS3_TEST tests RUTIS3.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 February 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'RUTIS3_TEST'
  print '  RUTIS3 computes the RUTIS3 matrix.'

  n = 4
  a = rutis3 ( )
  r8mat_print ( n, n, a, '  RUTIS3 matrix:' )

  print ''
  print 'RUTIS3_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  rutis3_test ( )
  timestamp ( )
