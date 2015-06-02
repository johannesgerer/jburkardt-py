#!/usr/bin/env python

def r8_factorial2 ( n ):

#*****************************************************************************80
#
## R8_FACTORIAL2 computes the double factorial function.
#
#  Formula:
#
#    FACTORIAL2( N ) = Product ( N * (N-2) * (N-4) * ... * 2 )  (N even)
#                    = Product ( N * (N-2) * (N-4) * ... * 1 )  (N odd)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 June 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the argument of the double factorial function.
#    If N is less than 1, VALUE is returned as 1.
#
#    Output, real VALUE, the value of N!!.
#
  value = 1;

  if ( n < 1 ):
    return value

  while ( 1 < n ):
    value = value * n
    n = n - 2

  return value

def r8_factorial2_test ( ):

#*****************************************************************************80
#
## R8_FACTORIAL2_TEST tests R8_FACTORIAL2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    08 February 2015
#
#  Author:
#
#    John Burkardt
#
  from r8_factorial2_values import r8_factorial2_values

  print ''
  print 'R8_FACTORIAL2_TEST'
  print '  R8_FACTORIAL2 evaluates the double factorial function.'
  print ''
  print '      N                     Exact',
  print '                  Computed'

  n_data = 0

  while ( True ):

    n_data, n, f1 = r8_factorial2_values ( n_data )

    if ( n_data == 0 ):
      break

    f2 = r8_factorial2 ( n )

    print '  %4d  %24.16g  %24.16g' % ( n, f1, f2 )
 
  print ''
  print 'R8_FACTORIAL2_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  r8_factorial2_test ( )
  timestamp ( )
