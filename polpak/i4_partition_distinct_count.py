#!/usr/bin/env python

def i4_partition_distinct_count ( n ):

#*****************************************************************************80
#
## I4_PARTITION_DISTINCT_COUNT returns any value of Q(N).
#
#  Discussion:
#
#    A partition of an integer N is a representation of the integer
#    as the sum of nonzero positive integers.  The order of the summands
#    does not matter.  The number of partitions of N is symbolized
#    by P(N).  Thus, the number 5 has P(N) = 7, because it has the 
#    following partitions:
#
#    5 = 5
#      = 4 + 1 
#      = 3 + 2 
#      = 3 + 1 + 1 
#      = 2 + 2 + 1 
#      = 2 + 1 + 1 + 1 
#      = 1 + 1 + 1 + 1 + 1
#
#    However, if we require that each member of the partition
#    be distinct, we are computing something symbolized by Q(N).
#    The number 5 has Q(N) = 3, because it has the following partitions 
#    into distinct parts:
#
#    5 = 5
#      = 4 + 1 
#      = 3 + 2 
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#  Parameters:
#
#    Input, integer N, the integer to be partitioned.
#
#    Output, integer VALUE, the number of partitions of the integer
#    into distinct parts.
#
  import numpy as np
  from i4_is_triangular import i4_is_triangular

  c = np.zeros ( n + 1 );

  c[0] = 1

  for i in range ( 1, n + 1 ):

    if ( i4_is_triangular ( i ) ):
      c[i] = 1
    else:
      c[i] = 0

    k = 0
    k_sign = -1

    while ( True ):

      k = k + 1
      k_sign = - k_sign
      k2 = k * ( 3 * k + 1 )

      if ( i < k2 ):
        break

      c[i] = c[i] + k_sign * c[i-k2]

    k = 0
    k_sign = -1

    while ( 1 ):

      k = k + 1
      k_sign = -k_sign
      k2 = k * ( 3 * k - 1 )

      if ( i < k2 ):
        break

      c[i] = c[i] + k_sign * c[i-k2]

  value = c[n]

  return value

def i4_partition_distinct_count_test ( ):

#*****************************************************************************80
#
## I4_PARTITION_DISTINCT_COUNT_TEST tests I4_PARTITION_DISTINCT_COUNT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    14 February 2015
#
#  Author:
#
#    John Burkardt
#
  from partition_distinct_count_values import partition_distinct_count_values

  print ''
  print 'I4_PARTITION_DISTINCT_COUNT_TEST'
  print '  I4_CHOOSE evaluates C(N,K).'
  print '  For the number of partitions of an integer'
  print '  into distinct parts,'
  print '  I4_PARTITION_DISTINCT_COUNT computes any value;'
  print ''
  print '     N       Exact F    Q(N)'
  print ''

  n_data = 0

  while ( True ):

    n_data, n, c = partition_distinct_count_values ( n_data )

    if ( n_data == 0 ):
      break

    c2 = i4_partition_distinct_count ( n )

    print '  %8d  %8d  %8d' % ( n, c, c2 )

  print ''
  print 'I4_PARTITION_DISTINCT_COUNT_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_partition_distinct_count_test ( )
  timestamp ( )
