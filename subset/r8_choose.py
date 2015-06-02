#!/usr/bin/env python
#
def r8_choose ( n, k ):

#*****************************************************************************80
#
## R8_CHOOSE computes the binomial coefficient C(N,K) as an R8.
#
#  Discussion:
#
#    The value is calculated in such a way as to avoid overflow and
#    roundoff.  The calculation is done in R8 arithmetic.
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
#    24 March 2015
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
#    Output, real VALUE, the number of combinations of N
#    things taken K at a time.
#
  mn = min ( k, n - k )

  if ( mn < 0 ):

    value = 0.0

  elif ( mn == 0 ):

    value = 1.0

  else:

    mx = max ( k, n - k )
    value = float ( mx + 1 )

    for i in range ( 2, mn + 1 ):
      value = ( value * float ( mx + i ) ) / float ( i )

  return value

def r8_choose_test ( ):

#*****************************************************************************80
#
## R8_CHOOSE_TEST tests R8_CHOOSE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    26 July 2014
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'R8_CHOOSE_TEST'
  print '  R8_CHOOSE evaluates C(N,K).'
  print ''
  print '         N         K       CNK'
 
  for n in range ( 0, 6 ):
    print ''
    for k in range ( 0, n + 1 ):
      cnk = r8_choose ( n, k )
      print '  %8d  %8d  %14.6g' % ( n, k, cnk )
#
#  Terminate.
#
  print ''
  print 'R8_CHOOSE_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_choose_test ( )
  timestamp ( )
