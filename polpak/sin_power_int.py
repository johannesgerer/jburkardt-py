#!/usr/bin/env python
#
def sin_power_int ( a, b, n ):

#*****************************************************************************80
#
## SIN_POWER_INT evaluates the sine power integral.
#
#  Discussion:
#
#    The function is defined by
#
#      SIN_POWER_INT(A,B,N) = Integral ( A <= T <= B ) ( sin ( t ))^n dt
#
#    The algorithm uses the following fact:
#
#      Integral sin^n ( t ) = (1/n) * (
#        sin^(n-1)(t) * cos(t) + ( n-1 ) * Integral sin^(n-2) ( t ) dt )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters
#
#    Input, real A, B, the limits of integration.
#
#    Input, integer N, the power of the sine function.
#
#    Output, real VALUE, the value of the integral.
#
  import numpy as np
  from sys import exit

  if ( n < 0 ):
    print ''
    print 'SIN_POWER_INT - Fatal error!'
    print '  Power N < 0.'
    exit ( 'SIN_POWER_INT - Fatal error!' )

  sa = np.sin ( a );
  sb = np.sin ( b );
  ca = np.cos ( a );
  cb = np.cos ( b );

  if ( ( n % 2 ) == 0 ):
    value = b - a
    mlo = 2
  else:
    value = ca - cb
    mlo = 3

  for m in range ( mlo, n + 1, 2 ):
    value = ( ( m - 1 ) * value \
            + sa ** ( m - 1 ) * ca \
            - sb ** ( m - 1 ) * cb ) / float ( m )

  return value

def sin_power_int_test ( ):

#*****************************************************************************80
#
## SIN_POWER_INT_TEST tests SIN_POWER_INT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 February 2015
#
#  Author:
#
#    John Burkardt
#
  from sin_power_int_values import sin_power_int_values

  print ''
  print 'SIN_POWER_INT_TEST'
  print '  SIN_POWER_INT returns values of'
  print '  the integral of SIN(X)^N from A to B.'
  print ''
  print '      A         B          N      Exact           Computed'
  print ''

  n_data = 0

  while ( True ):

    n_data, a, b, n, fx = sin_power_int_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = sin_power_int ( a, b, n )

    print '  %8f  %8f  %6d  %14e  %14e' % ( a, b, n, fx, fx2 )
 
  print ''
  print 'SIN_POWER_INT_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  sin_power_int_test ( )
  timestamp ( )
