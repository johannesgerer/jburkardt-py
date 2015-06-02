#!/usr/bin/env python

def i4_choose ( n, k ):

#*****************************************************************************80
#
## I4_CHOOSE computes the binomial coefficient C(N,K) as an I4.
#
#  Discussion:
#
#    The value is calculated in such a way as to avoid overflow and
#    roundoff.  The calculation is done in integer arithmetic.
#
#    The formula used is:
#
#      C(N,K) = N! / ( K! * (N-K)! )
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
#  Reference:
#
#    ML Wolfson, HV Wright,
#    Algorithm 160:
#    Combinatorial of M Things Taken N at a Time,
#    Communications of the ACM,
#    Volume 6, Number 4, April 1963, page 161.
#
#  Parameters:
#
#    Input, integer N, K, are the values of N and K.
#
#    Output, integer VALUE, the number of combinations of N
#    things taken K at a time.
#
  mn = min ( k, n - k );

  if ( mn < 0 ):

    value = 0

  elif ( mn == 0 ):

    value = 1

  else:

    mx = max ( k, n - k )
    value = mx + 1

    for i in range ( 2, mn + 1 ):
      value = ( value * ( mx + i ) ) / i

  return value

def i4_choose_test ( ):

#*****************************************************************************80
#
## I4_CHOOSE_TEST tests I4_CHOOSE.
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
  print ''
  print 'I4_CHOOSE_TEST'
  print '  I4_CHOOSE evaluates C(N,K).'
  print ''
  print '       N       K     CNK'

  for n in range ( 0, 5 ):
    print ''
    for k in range ( 0, n + 1 ):
      cnk = i4_choose ( n, k )

      print '  %6d  %6d  %6d' % ( n, k, cnk )

  print ''
  print 'I4_CHOOSE_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp

  timestamp ( )
  i4_choose_test ( )
  timestamp ( )
