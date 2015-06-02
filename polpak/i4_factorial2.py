#!/usr/bin/env python

def i4_factorial2 ( n ) :

#*****************************************************************************80
#
## I4_FACTORIAL2 computes the double factorial N!!
#
#  Discussion:
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
#    08 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the argument of the double factorial function.
#    If N is less than 1, the value is returned as 1.
#
#    Output, integer VALUE, the value of N!!.
#
  if ( n < 1 ):
    value = 1
    return value

  value = 1

  for i in range ( n, 1, -2 ):
    value = value * i

  return value

def i4_factorial2_test ( ):

#*****************************************************************************80
#
## I4_FACTORIAL2_TEST tests I4_FACTORIAL2.
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
  from i4_factorial2_values import i4_factorial2_values

  print ''
  print 'I4_FACTORIAL2_TEST'
  print '  I4_FACTORIAL2 evaluates the double factorial function.'
  print ''
  print '         N      Exact         I4_FACTORIAL2(N)'
  print ''

  n_data = 0

  while ( True ):

    n_data, n, f1 = i4_factorial2_values ( n_data )

    if ( n_data == 0 ):
      break

    f2 = i4_factorial2 ( n )

    print '  %8d  %12d  %12d' % ( n, f1, f2 )      
 
  print ''
  print 'I4_FACTORIAL2_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_factorial2_test ( )
  timestamp ( )
