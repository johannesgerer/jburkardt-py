#! /usr/bin/env python
#
def conex1 ( alpha ):

#*****************************************************************************80
#
## CONEX1 returns the CONEX1 matrix.
#
#  Discussion:
#
#    The CONEX1 matrix is a counterexample to the LINPACK condition
#    number estimator RCOND available in the LINPACK routine DGECO.
#
#  Formula:
#
#    1  -1 -2*ALPHA   0
#    0   1    ALPHA    -ALPHA
#    0   1  1+ALPHA  -1-ALPHA
#    0   0  0           ALPHA
#
#  Example:
#
#    ALPHA = 100
#
#    1  -1  -200     0
#    0   1   100  -100
#    0   1   101  -101
#    0   0     0   100
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Alan Cline, RK Rew,
#    A set of counterexamples to three condition number estimators,
#    SIAM Journal on Scientific and Statistical Computing,
#    Volume 4, 1983, pages 602-611.
#
#  Parameters:
#
#    Input, real ALPHA, the scalar defining A.  
#    A common value is 100.0.
#
#    Output, real A(4,4), the matrix.
#
  import numpy as np

  a = np.array ( [
    [ 1.0, -1.0, -2.0 * alpha,   0.0         ], \
    [ 0.0,  1.0,        alpha,       - alpha ], \
    [ 0.0,  1.0,  1.0 + alpha, - 1.0 - alpha ], \
    [ 0.0,  0.0,  0.0,                 alpha ] \
  ] )

  return a

def conex1_condition ( alpha ):

#*****************************************************************************80
#
## CONEX1_CONDITION returns the L1 condition of the CONEX1 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real ALPHA, the scalar defining A.  
#    A common value is 100.0.
#
#    Output, real VALUE, the L1 condition.
#
  a_norm = max ( 3.0, 3.0 * abs ( alpha ) + abs ( 1.0 + alpha ) )
  v1 = abs ( 1.0 - alpha ) + abs ( 1.0 + alpha ) + 1.0
  v2 = 2.0 * abs ( alpha ) + 1.0
  v3 = 2.0 + 2.0 / abs ( alpha )
  b_norm = max ( v1, max ( v2, v3 ) )
  value = a_norm * b_norm

  return value

def conex1_condition_test ( ):

#*****************************************************************************80
#
## CONEX1_CONDITION_TEST tests CONEX1_CONDITION.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 February 2015
#
#  Author:
#
#    John Burkardt
#
  from conex1 import conex1
  from r8mat_print import r8mat_print
  from r8_uniform_ab import r8_uniform_ab

  print ''
  print 'CONEX1_CONDITION_TEST'
  print '  CONEX1_CONDITION computes the condition of the CONEX1 matrix.'
  print ''

  m = 4
  n = m

  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )

  a = conex1 ( alpha )
  r8mat_print ( m, n, a, '  CONEX1 matrix:' )

  value = conex1_condition ( alpha )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'CONEX1_CONDITION_TEST'
  print '  Normal end of execution.'

  return

def conex1_determinant ( alpha ):

#*****************************************************************************80
#
## CONEX1_DETERMINANT returns the determinant of the CONEX1 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real ALPHA, the scalar defining A.  
#    A common value is 100.0.
#
#    Output, real DETERM, the determinant.
#
  determ = alpha

  return determ

def conex1_determinant_test ( ):

#*****************************************************************************80
#
## CONEX1_DETERMINANT_TEST tests CONEX1_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 January 2015
#
#  Author:
#
#    John Burkardt
#
  from conex1 import conex1
  from r8mat_print import r8mat_print
  from r8_uniform_ab import r8_uniform_ab

  print ''
  print 'CONEX1_DETERMINANT_TEST'
  print '  CONEX1_DETERMINANT computes the determinant of the CONEX1 matrix.'
  print ''

  m = 4
  n = m

  alpha_lo = 1.0
  alpha_hi = 100.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( alpha_lo, alpha_hi, seed )

  a = conex1 ( alpha )
  r8mat_print ( m, n, a, '  CONEX1 matrix:' )

  value = conex1_determinant ( alpha )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'CONEX1_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def conex1_inverse ( alpha ):

#*****************************************************************************80
#
#% CONEX1_INVERSE returns the inverse of the CONEX1 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real ALPHA, the scalar defining A.  
#    A common value is 100.0.
#
#    Output, real A(4,4), the matrix.
#
  import numpy as np

  a = np.zeros ( ( 4, 4 ) )

  a[0,0] =  1.0
  a[0,1] =  1.0 - alpha
  a[0,2] =        alpha
  a[0,3] =  2.0

  a[1,0] =  0.0
  a[1,1] =  1.0 + alpha
  a[1,2] =      - alpha
  a[1,3] =  0.0

  a[2,0] =  0.0
  a[2,1] = -1.0
  a[2,2] =  1.0
  a[2,3] =  1.0 / alpha

  a[3,0] = 0.0
  a[3,1] = 0.0
  a[3,2] = 0.0
  a[3,3] = 1.0 / alpha

  return a

def conex1_test ( ):

#*****************************************************************************80
#
## CONEX1_TEST tests CONEX1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 January 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print
  from r8_uniform_ab import r8_uniform_ab

  print ''
  print 'CONEX1_TEST'
  print '  CONEX1 computes the CONEX1 matrix.'

  m = 4
  n = m

  alpha_lo = 1.0
  alpha_hi = 100.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( alpha_lo, alpha_hi, seed )

  a = conex1 ( alpha )
  r8mat_print ( m, n, a, '  CONEX1 matrix:' )

  print ''
  print 'CONEX1_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  conex1_test ( )
  timestamp ( )
