#!/usr/bin/env python

def r8_factorial ( n ):

#*****************************************************************************80
#
## R8_FACTORIAL returns N factorial.
#
#  Discussion:
#
#    factorial ( N ) = Product ( 1 <= I <= N ) I
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 June 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the argument of the function.
#    0 <= N.
#
#    Output, real VALUE, the factorial of N.
#
  from sys import exit

  if ( n < 0 ):
    print ''
    print 'R8_FACTORIAL - Fatal error!'
    print '  N < 0.'
    exit ( 'R8_FACTORIAL - Fatal error!' )

  value = 1.0

  for i in range ( 2, n + 1 ):
    value = value * i

  return value

def r8_factorial_test ( ):

#*****************************************************************************80
#
## R8_FACTORIAL_TEST tests R8_FACTORIAL.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    27 December 2014
#
#  Author:
#
#    John Burkardt
#
  from r8_factorial_values import r8_factorial_values

  print ''
  print 'R8_FACTORIAL_TEST'
  print '  R8_FACTORIAL evaluates the factorial function.'
  print ''
  print '      N                     Exact',
  print '                  Computed'

  n_data = 0

  while ( True ):

    n_data, n, f1 = r8_factorial_values ( n_data )

    if ( n_data == 0 ):
      break

    f2 = r8_factorial ( n )

    print '  %4d  %24.16g  %24.16g' % ( n, f1, f2 )
#
#  Terminate.
#
  print ''
  print 'R8_FACTORIAL_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  r8_factorial_test ( )
  timestamp ( )
