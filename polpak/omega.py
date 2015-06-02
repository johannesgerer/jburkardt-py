#!/usr/bin/env python

def omega ( n ) :

#*****************************************************************************80
#
## OMEGA returns OMEGA(N), the number of distinct prime divisors of N.
#
#  First values:
#
#     N   OMEGA(N)
#
#     1    1
#     2    1
#     3    1
#     4    1
#     5    1
#     6    2
#     7    1
#     8    1
#     9    1
#    10    2
#    11    1
#    12    2
#    13    1
#    14    2
#    15    2
#    16    1
#    17    1
#    18    2
#    19    1
#    20    2
#
#  Formula:
#
#    If N = 1, then
#
#      OMEGA(N) = 1
#
#    else if the prime factorization of N is
#
#      N = P1^E1 * P2^E2 * ... * PM^EM,
#
#    then
#
#      OMEGA(N) = M
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 February 2015
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
#    Output, integer VALUE, the value of OMEGA(N).  But if N is 0 or
#    less, NDIV is returned as 0, a nonsense value.  If there is
#    not enough room for factoring, NDIV is returned as -1.
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
    print 'OMEGA - Fatal error!'
    print '  Not enough factorization space.'

  value = nfactor

  return value

def omega_test ( ):

#*****************************************************************************80
#
## OMEGA_TEST tests OMEGA.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    24 February 2015
#
#  Author:
#
#    John Burkardt
#
  from omega_values import omega_values

  print ''
  print 'OMEGA_TEST'
  print '  OMEGA counts the distinct prime divisors of an integer N.'
  print ''
  print '         N      Exact         OMEGA(N)'

  n_data = 0

  while ( True ):

    n_data, n, c1 = omega_values ( n_data )

    if ( n_data == 0 ):
      break

    c2 = omega ( n )

    print '  %8d  %12d  %12d' % ( n, c1, c2 )      
 
  print ''
  print 'OMEGA_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  omega_test ( )
  timestamp ( )
