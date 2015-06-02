#! /usr/bin/env python
#
def i4_partition_count ( n ):

#*****************************************************************************80
#
## I4_PARTITION_COUNT computes the number of partitions of an integer.
#
#  Discussion:
#
#    Partition numbers are difficult to compute.  This routine uses
#    Euler's method, which observes that:
#
#      P(0) = 1
#      P(N) =   P(N-1)  + P(N-2)
#             - P(N-5)  - P(N-7)
#             + P(N-12) + P(N-15)
#             - ...
#
#      where the numbers 1, 2, 5, 7, ... to be subtracted from N in the
#      indices are the successive pentagonal numbers, (with both positive 
#      and negative indices) with the summation stopping when a negative 
#      index is reached.
#
#  First values:
#
#    N   P
#
#    0   1
#    1   1
#    2   2
#    3   3
#    4   5
#    5   7
#    6  11
#    7  15
#    8  22
#    9  30
#   10  42
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John Conway and Richard Guy,
#    The Book of Numbers,
#    Springer Verlag, 1996, page 95.
#
#  Parameters:
#
#    Input, integer N, the index of the highest partition number desired.
#
#    Output, integer P[0:N], the partition numbers.
#
  import numpy as np
  from pent_enum import pent_enum

  p = np.zeros ( n + 1 )

  p[0] = 1

  for i in range ( 1, n + 1 ):

    p[i] = 0

    j = 0
    sgn = 1

    while ( True ):

      j = j + 1
      pj = pent_enum ( j )

      if ( i < pj ):
        break

      p[i] = p[i] + sgn * p[i-pj]
      sgn = -sgn

    j = 0
    sgn = 1

    while ( True ):

      j = j - 1
      pj = pent_enum ( j );

      if ( i < pj ):
        break

      p[i] = p[i] + sgn * p[i-pj]
      sgn = -sgn

  return p

def i4_partition_count_test ( ):

#*****************************************************************************80
#
## I4_PARTITION_COUNT_TEST tests I4_PARTITION_COUNT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 May 2015
#
#  Author:
#
#    John Burkardt
#
  from i4_partition_count_values import i4_partition_count_values

  print ''
  print 'I4_PARTITION_COUNT_TEST'
  print '  I4_PARTITION_COUNT counts partitions of an integer.'

  n_data = 0

  print ''
  print '   N     Exact     Count'
  print ''

  while ( True ):

    n_data, n, p = i4_partition_count_values ( n_data )

    if ( n_data == 0 ):
      break

    p2 = i4_partition_count ( n )
 
    print '  %4d  %8d  %8d' % ( n, p, p2[n] )
#
#  Terminate.
#
  print ''
  print 'I4_PARTITION_COUNT_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_partition_count_test ( )
  timestamp ( )
