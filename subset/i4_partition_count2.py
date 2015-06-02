#! /usr/bin/env python
#
def i4_partition_count2 ( n ):

#*****************************************************************************80
#
## I4_PARTITION_COUNT2 computes the number of partitions of an integer.
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
#    29 May 2015
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Albert Nijenhuis, Herbert Wilf,
#    Combinatorial Algorithms,
#    Academic Press, 1978, second edition,
#    ISBN 0-12-519260-6.
#
#  Parameters:
#
#    Input, integer N, the largest integer to be considered.
#
#    Output, integer P[0:N], the partition numbers.
#
  import numpy as np
  
  p = np.zeros ( n + 1 )

  p[0] = 1

  if ( 0 < n ):

    p[1] = 1

    for i in range ( 2, n + 1 ):

      total = 0

      for t in range ( 1, i + 1 ):

        s = 0
        j = i

        while ( True ):

          j = j - t

          if ( 0 < j ):
            s = s + p[j]
          else:
            if ( j == 0 ):
              s = s + 1
            break

        total = total + s * t;

      p[i] = ( total // i )

  return p

def i4_partition_count2_test ( ):

#*****************************************************************************80
#
## I4_PARTITION_COUNT2_TEST tests I4_PARTITION_COUNT2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 May 2015
#
#  Author:
#
#    John Burkardt
#
  from i4_partition_count_values import i4_partition_count_values

  print ''
  print 'I4_PARTITION_COUNT2_TEST'
  print '  I4_PARTITION_COUNT2 counts partitions of an integer.'

  n_data = 0

  print ''
  print '   N     Exact     Count'
  print ''

  while ( True ):

    n_data, n, p = i4_partition_count_values ( n_data )

    if ( n_data == 0 ):
      break

    p2 = i4_partition_count2 ( n )
 
    print '  %4d  %8d  %8d' % ( n, p, p2[n] )
#
#  Terminate.
#
  print ''
  print 'I4_PARTITION_COUNT2_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_partition_count2_test ( )
  timestamp ( )

