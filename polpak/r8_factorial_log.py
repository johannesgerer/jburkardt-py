#!/usr/bin/env python

def r8_factorial_log ( n ):

#*****************************************************************************80
#
## R8_FACTORIAL_LOG computes the natural logarithm of the factorial N!
#
#  Discussion:
#
#    LOG ( FACTORIAL ( N ) )
#      = LOG ( product ( 1 <= I <= N ) I )
#      = sum ( ( 1 <= I <= N ) LOG ( I ) )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    13 February 2010
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the argument of the factorial function.
#    If N is less than 1, VALUE is returned as 0.
#
#    Output, real VALUE, the logarithm of the factorial of N.
#
  from r8_gamma_log import r8_gamma_log

  value = r8_gamma_log ( float ( n + 1 ) )

  return value

def r8_factorial_log_test ( ):

#*****************************************************************************80
#
## R8_FACTORIAL_LOG_TEST tests R8_FACTORIAL_LOG.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    14 February 2015
#
#  Author:
#
#    John Burkardt
#
  from r8_factorial_log_values import r8_factorial_log_values

  print ''
  print 'R8_FACTORIAL_LOG_TEST'
  print '  R8_FACTORIAL_LOG evaluates the factorial log function.'
  print ''
  print '      N                     Exact',
  print '                  Computed'

  n_data = 0

  while ( True ):

    n_data, n, f1 = r8_factorial_log_values ( n_data )

    if ( n_data == 0 ):
      break

    f2 = r8_factorial_log ( n )

    print '  %4d  %24.16g  %24.16g' % ( n, f1, f2 )
 
  print ''
  print 'R8_FACTORIAL_LOG_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  r8_factorial_log_test ( )
  timestamp ( )
