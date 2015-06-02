#!/usr/bin/env python

def tau ( n ):

#*****************************************************************************80
#
## TAU returns the value of TAU(N), the number of distinct divisors of N.
#
#  Discussion:
#
#    TAU(N) is the number of divisors of N, including 1 and N.
#
#  First values:
#
#     N   TAU(N)
#
#     1    1
#     2    2
#     3    2
#     4    3
#     5    2
#     6    4
#     7    2
#     8    4
#     9    3
#    10    4
#    11    2
#    12    6
#    13    2
#    14    4
#    15    4
#    16    5
#    17    2
#    18    6
#    19    2
#    20    6
#
#  Formula:
#
#    If the prime factorization of N is
#
#      N = P1^E1 * P2^E2 * ... * PM^EM,
#
#    then
#
#      TAU(N) = ( E1 + 1 ) * ( E2 + 1 ) * ... * ( EM + 1 ).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the value to be analyzed.  N must be 1 or
#    greater.
#
#    Output, integer TAUN, the value of TAU(N).  But if N is 0 or
#    less, TAUN is returned as 0, a nonsense value.  If there is
#    not enough room for factoring, TAUN is returned as -1.
#
  from i4_factor import i4_factor

  if ( n <= 0 ):
    value = 0
    return value

  if ( n == 1 ):
    value = 1
    return value
#
#  Factor N.
#
  nfactor, factor, power, nleft = i4_factor ( n )

  if ( nleft != 1 ):
    print ''
    print 'TAU - Fatal error!'
    print '  Not enough factorization space.'

  value = 1
  for i in range ( 0, nfactor ):
    value = value * ( power[i] + 1 )

  return value

def tau_test ( ):

#*****************************************************************************80
#
## TAU_TEST tests TAU.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    25 February 2015
#
#  Author:
#
#    John Burkardt
#
  from tau_values import tau_values

  print ''
  print 'TAU_TEST'
  print '  TAU computes the TAU function.'
  print ''
  print '         N      Exact         TAU(N)'

  n_data = 0

  while ( True ):

    n_data, n, c1 = tau_values ( n_data )

    if ( n_data == 0 ):
      break

    c2 = tau ( n )

    print '  %8d  %12d  %12d' % ( n, c1, c2 )      
 
  print ''
  print 'TAU_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  tau_test ( )
  timestamp ( )
