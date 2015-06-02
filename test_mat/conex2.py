#! /usr/bin/env python
#
def conex2 ( alpha ):

#*****************************************************************************80
#
## CONEX2 returns the CONEX2 matrix.
#
#  Discussion:
#
#    CONEX2 is a 3 by 3 LINPACK condition number counterexample.
#
#  Formula:
#
#    1   1-1/ALPHA^2 -2
#    0   1/ALPHA     -1/ALPHA
#    0   0            1
#
#  Example:
#
#    ALPHA = 100
#
#    1  0.9999  -2
#    0  0.01    -0.01
#    0  0        1
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is upper triangular.
#
#    det ( A ) = 1 / ALPHA.
#
#    LAMBDA = ( 1, 1/ALPHA, 1 )
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
#    A common value is 100.0.  ALPHA must not be zero.
#
#    Output, real A(3,3), the atrix.
#
  import numpy as np
  from sys import exit

  if ( alpha == 0.0 ):
    print ''
    print 'CONEX2 - Fatal error!'
    print '  The input value of ALPHA was zero.'
    exit ( 'CONEX2 - Fatal error!' )

  a = np.array ( [ \
    [ 1.0, ( alpha * alpha - 1.0 ) / ( alpha * alpha ), -2.0         ], \
    [ 0.0,                     1.0 / alpha,             -1.0 / alpha ], \
    [ 0.0,                     0.0,                      1.0         ] \
  ] )

  return a

def conex2_condition ( alpha ):

#*****************************************************************************80
#
## CONEX2_CONDITION returns the L1 condition of the CONEX2 matrix.
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
#
#    Output, real VALUE, the L1 condition.
#
  c1 = 1.0
  c2 = abs ( 1.0 - 1.0 / alpha ** 2 ) + 1.0 / abs ( alpha )
  c3 = 3.0 + 1.0 / abs ( alpha )
  a_norm = max ( c1, max ( c2, c3 ) )
  c1 = 1.0
  c2 = abs ( ( 1.0 - alpha * alpha ) / alpha ) + abs ( alpha )
  c3 = abs ( ( 1.0 + alpha * alpha ) / alpha ** 2 ) + 2.0
  b_norm = max ( c1, max ( c2, c3 ) )
  value = a_norm * b_norm

  return value

def conex2_condition_test ( ):

#*****************************************************************************80
#
## CONEX2_CONDITION_TEST tests CONEX2_CONDITION.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print
  from r8_uniform_ab import r8_uniform_ab

  print ''
  print 'CONEX2_CONDITION_TEST'
  print '  CONEX2_CONDITION computes the condition of the CONEX2 matrix.'
  print ''

  m = 3
  n = m

  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )

  a = conex2 ( alpha )
  r8mat_print ( m, n, a, '  CONEX2 matrix:' )

  value = conex2_condition ( alpha )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'CONEX2_CONDITION_TEST'
  print '  Normal end of execution.'

  return

def conex2_determinant ( alpha ):

#*****************************************************************************80
#
## CONEX2_DETERMINANT returns the determinant of the CONEX2 matrix.
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
  determ = 1.0 / alpha

  return determ

def conex2_determinant_test ( ):

#*****************************************************************************80
#
## CONEX2_DETERMINANT_TEST tests CONEX2_DETERMINANT.
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
  print 'CONEX2_DETERMINANT_TEST'
  print '  CONEX2_DETERMINANT computes the determinant of the CONEX2 matrix.'
  print ''

  m = 3
  n = m

  alpha_lo = 1.0
  alpha_hi = 100.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( alpha_lo, alpha_hi, seed )

  a = conex2 ( alpha )
  r8mat_print ( m, n, a, '  CONEX2 matrix:' )

  value = conex2_determinant ( alpha )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'CONEX2_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def conex2_inverse ( alpha ):

#*****************************************************************************80
#
## CONEX2_INVERSE returns the inverse of the CONEX2 matrix.
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
#    A common value is 100.0.  ALPHA must not be zero.
#
#    Output, real A(3,3), the matrix.
#
  import numpy as np
  from sys import exit

  a = np.zeros ( ( 3, 3 ) )

  if ( alpha == 0.0 ):
    print ''
    print 'CONEX2_INVERSE - Fatal error!'
    print '  The input value of ALPHA was zero.'
    exit ( 'CONEX2_INVERSE - Fatal error!' )
 
  a[0,0] = 1.0
  a[0,1] = ( 1.0 - alpha * alpha ) / alpha
  a[0,2] = ( 1.0 + alpha * alpha ) / alpha ** 2

  a[1,0] = 0.0
  a[1,1] = alpha
  a[1,2] = 1.0

  a[2,0] = 0.0
  a[2,1] = 0.0
  a[2,2] = 1.0

  return a

def conex2_test ( ):

#*****************************************************************************80
#
## CONEX2_TEST tests CONEX2.
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
  print 'CONEX2_TEST'
  print '  CONEX2 computes the CONEX2 matrix.'

  m = 3
  n = m

  alpha_lo = 1.0
  alpha_hi = 100.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( alpha_lo, alpha_hi, seed )

  a = conex2 ( alpha )
  r8mat_print ( m, n, a, '  CONEX2 matrix:' )

  print ''
  print 'CONEX2_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  conex2_test ( )
  timestamp ( )
