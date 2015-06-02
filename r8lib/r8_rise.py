#!/usr/bin/env python

def r8_rise ( x, n ):

#*****************************************************************************80
#
## R8_RISE computes the rising factorial function [X]^N.
#
#  Discussion:
#
#    [X]^N = X * ( X + 1 ) * ( X + 2 ) * ... * ( X + N - 1 ).
#
#    Note that the number of ways of arranging N objects in M ordered
#    boxes is [M]^N.  (Here, the ordering of the objects in each box matters).
#    Thus, 2 objects in 2 boxes have the following 6 possible arrangements:
#
#      -|12, 1|2, 12|-, -|21, 2|1, 21|-.
#
#    Moreover, the number of non-decreasing maps from a set of
#    N to a set of M ordered elements is [M]^N / N!.  Thus the set of
#    nondecreasing maps from (1,2,3) to (a,b,c,d) is the 20 elements:
#
#      aaa, abb, acc, add, aab, abc, acd, aac, abd, aad
#      bbb, bcc, bdd, bbc, bcd, bbd, ccc, cdd, ccd, ddd.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    25 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the argument of the rising factorial function.
#
#    Input, integer N, the order of the rising factorial function.
#    If N = 0, RISE = 1, if N = 1, RISE = X.  Note that if N is
#    negative, a "falling" factorial will be computed.
#
#    Output, real VALUE, the value of the rising factorial function.
#
  value = 1.0

  arg = x

  if ( 0 < n ):

    for i in range ( 0, n ):
      value = value * arg
      arg = arg + 1.0

  elif ( n < 0 ):

    for i in range ( n, 0 ):
      value = value * arg
      arg = arg - 1.0

  return value

def r8_rise_test ( ):

#*****************************************************************************80
#
## R8_RISE_TEST tests R8_RISE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    26 December 2014
#
#  Author:
#
#    John Burkardt
#
  from r8_rise_values import r8_rise_values

  print ''
  print 'R8_RISE_TEST'
  print '  R8_RISE evaluates the rising factorial Rise(X,N).'
  print ''
  print '      X        N                     Exact',
  print '                  Computed'
  print ''

  n_data = 0

  while ( True ):

    n_data, x, n, f1 = r8_rise_values ( n_data )

    if ( n_data == 0 ):
      break

    f2 = r8_rise ( x, n )

    print '  %8.4g  %4d  %24.16g  %24.16g' % ( x, n, f1, f2 )
#
#  Terminate.
#
  print ''
  print 'R8_RISE_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_rise_test ( )
  timestamp ( )
