#!/usr/bin/env python

def sigma ( n ):

#*****************************************************************************80
#
## SIGMA returns the value of SIGMA(N), the divisor sum.
#
#  Definition:
#
#    SIGMA(N) is the sum of the distinct divisors of N, including 1 and N.
#
#  First values:
#
#     N  SIGMA(N)
#
#     1    1
#     2    3
#     3    4
#     4    7
#     5    6
#     6   12
#     7    8
#     8   15
#     9   13
#    10   18
#    11   12
#    12   28
#    13   14
#    14   24
#    15   24
#    16   31
#    17   18
#    18   39
#    19   20
#    20   42
#
#  Formula:
#
#    SIGMA(U*V) = SIGMA(U) * SIGMA(V) if U and V are relatively prime.
#
#    SIGMA(P^K) = ( P^(K+1) - 1 ) / ( P - 1 ) if P is prime.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the value to be analyzed.
#
#    Output, integer VALUE, the value of SIGMA(N).  If N is less than
#    or equal to 0, VALUE will be returned as 0.  If there is not
#    enough room for factoring N, VALUE is returned as -1.
#
  from i4_factor import i4_factor

  maxfactor = 20

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
    print 'SIGMA - Fatal error!'
    print '  Not enough factorization space.'

  value = 1
  for i in range ( 0, nfactor ):
    value = ( value * ( factor[i] ** ( power[i] + 1 ) - 1 ) ) \
      / ( factor[i] - 1 )

  return value

def sigma_test ( ):

#*****************************************************************************80
#
## SIGMA_TEST tests SIGMA.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    26 February 2015
#
#  Author:
#
#    John Burkardt
#
  from sigma_values import sigma_values

  print ''
  print 'SIGMA_TEST'
  print '  SIGMA computes the SIGMA function.'
  print ''
  print '         N      Exact         SIGMA(N)'

  n_data = 0

  while ( True ):

    n_data, n, c1 = sigma_values ( n_data )

    if ( n_data == 0 ):
      break

    c2 = sigma ( n )

    print '  %8d  %12d  %12d' % ( n, c1, c2 )      
 
  print ''
  print 'SIGMA_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  sigma_test ( )
  timestamp ( )
