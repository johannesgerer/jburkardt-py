#!/usr/bin/env python

def phi ( n ):

#*****************************************************************************80
#
## PHI computes the number of relatively prime predecessors of an integer.
#
#  Definition:
#
#    PHI(N) is the number of integers between 1 and N which are
#    relatively prime to N.  I and J are relatively prime if they
#    have no common factors.  The function PHI(N) is known as
#    "Euler's totient function".
#
#    By convention, 1 and N are relatively prime.
#
#  First values:
#
#     N  PHI(N)
#
#     1    1
#     2    1
#     3    2
#     4    2
#     5    4
#     6    2
#     7    6
#     8    4
#     9    6
#    10    4
#    11   10
#    12    4
#    13   12
#    14    6
#    15    8
#    16    8
#    17   16
#    18    6
#    19   18
#    20    8
#
#  Formula:
#
#    PHI(U*V) = PHI(U) * PHI(V) if U and V are relatively prime.
#
#    PHI(P^K) = P^(K-1) * ( P - 1 ) if P is prime.
#
#    PHI(N) = N * Product ( P divides N ) ( 1 - 1 / P )
#
#    N = Sum ( D divides N ) PHI(D).
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
#    Input, integer N, the value to be analyzed.
#
#    Output, integer VALUE, the value of PHI(N).  If N is less than
#    or equal to 0, PHI will be returned as 0.  If there is not enough
#    room for full factoring of N, PHI will be returned as -1.
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
    print 'PHI - Fatal error!'
    print '  Not enough factorization space.'
 
  value = 1
  for i in range ( 0, nfactor ):
    value = value * factor[i] ** ( power[i] - 1 ) * ( factor[i] - 1 )

  return value

def phi_test ( ):

#*****************************************************************************80
#
## PHI_TEST tests PHI.
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
  from phi_values import phi_values

  print ''
  print 'PHI_TEST'
  print '  PHI computes the PHI function.'
  print ''
  print '         N      Exact         PHI(N)'

  n_data = 0

  while ( True ):

    n_data, n, c1 = phi_values ( n_data )

    if ( n_data == 0 ):
      break

    c2 = phi ( n )

    print '  %8d  %12d  %12d' % ( n, c1, c2 )      
 
  print ''
  print 'PHI_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  phi_test ( )
  timestamp ( )
