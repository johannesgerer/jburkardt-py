#!/usr/bin/env python

def i4_factorial ( n ) :

#*****************************************************************************80
#
## I4_FACTORIAL computes the factorial function.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the argument.
#
#    Output, integer VALUE, the value of the factorial function.
#
  value = 1
  for i in range ( 1, n + 1 ):
    value = value * i

  return value

def i4_factorial_test ( ):

#*****************************************************************************80
#
## I4_FACTORIAL_TEST tests I4_FACTORIAL.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    18 December 2014
#
#  Author:
#
#    John Burkardt
#
  from i4_factorial_values import i4_factorial_values

  print ''
  print 'I4_FACTORIAL_TEST'
  print '  I4_FACTORIAL evaluates the factorial function.'
  print ''
  print '         N      Exact         I4_FACTORIAL(N)'
  print ''

  n_data = 0

  while ( True ):

    n_data, n, f1 = i4_factorial_values ( n_data )

    if ( n_data == 0 ):
      break

    f2 = i4_factorial ( n )

    print '  %8d  %12d  %12d' % ( n, f1, f2 )      
#
#  Terminate.
#
  print ''
  print 'I4_FACTORIAL_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_factorial_test ( )
  timestamp ( )
