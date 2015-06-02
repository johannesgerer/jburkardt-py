#!/usr/bin/env python

def i4_fall ( x, n ):

#*****************************************************************************80
#
## I4_FALL computes the falling factorial function [X]_N.
#
#  Discussion:
#
#    Note that the number of "injections" or 1-to-1 mappings from
#    a set of N elements to a set of M elements is [M]_N.
#
#    The number of permutations of N objects out of M is [M]_N.
#
#    Moreover, the Stirling numbers of the first kind can be used
#    to convert a falling factorial into a polynomial, as follows:
#
#      [X]_N = S^0_N + S^1_N * X + S^2_N * X^2 + ... + S^N_N X^N.
#
#  Formula:
#
#    [X]_N = X * ( X - 1 ) * ( X - 2 ) * ... * ( X - N + 1 ).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    27 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer X, the argument of the falling factorial function.
#
#    Input, integer N, the order of the falling factorial function.
#    If N = 0, FALL = 1, if N = 1, FALL = X.  Note that if N is
#    negative, a "rising" factorial will be computed.
#
#    Output, integer VALUE, the value of the falling factorial function.
#
  value = 1

  arg = x

  if ( 0 < n ):

    for i in range ( 0, n ):
      value = value * arg
      arg = arg - 1.0

  elif ( n < 0 ):

    for i in range ( n, 0 ):
      value = value * arg
      arg = arg + 1

  return value

def i4_fall_test ( ):

#*****************************************************************************80
#
## I4_FALL_TEST tests I4_FALL.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    27 October 2014
#
#  Author:
#
#    John Burkardt
#
  from i4_fall_values import i4_fall_values

  print ''
  print 'I4_FALL_TEST'
  print '  I4_FALL evaluates the falling factorial Fall(I,N).'
  print ''
  print '         M         N      Exact         I4_FALL(M,N)'

  n_data = 0

  while ( True ):

    n_data, m, n, f1 = i4_fall_values ( n_data )

    if ( n_data == 0 ):
      break

    f2 = i4_fall ( m, n )

    print '  %8d  %8d  %12d  %12d' % ( m, n, f1, f2 )      
#
#  Terminate.
#
  print ''
  print 'I4_FALL_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_fall_test ( )
  timestamp ( )
