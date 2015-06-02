#!/usr/bin/env python

def plane_partition_num ( n ):

#*****************************************************************************80
#
## PLANE_PARTITION_NUM returns the number of plane partitions of the integer N.
#
#  Discussion:
#
#    A plane partition of a positive integer N is a partition of N in which
#    the parts have been arranged in a 2D array that is nonincreasing across
#    rows and columns.  There are six plane partitions of 3:
#
#      3   2 1   2   1 1 1   1 1   1
#                1           1     1
#                                  1
#
#  First Values:
#
#     N PP(N)
#     0    1
#     1    1
#     2    3
#     3    6
#     4   13
#     5   24
#     6   48
#     7   86
#     8  160
#     9  282
#    10  500
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 April 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Frank Olver, Daniel Lozier, Ronald Boisvert, Charles Clark,
#    NIST Handbook of Mathematical Functions,
#    Cambridge University Press, 2010,
#    ISBN: 978-0521140638,
#    LC: QA331.N57.
#    
#  Parameters:
#
#    Input, integer N, the number, which must be at least 0.
#
#    Output, integer VALUE, the number of plane partitions of N.
#
  import numpy as np

  if ( n < 0 ):
    print ''
    print 'PLANE_PARTITION_NUM - Fatal error!'
    print '  0 <= N is required.'

  pp = np.zeros ( n + 1 )

  nn = 0
  pp[nn] = 1

  nn = 1
  if ( nn <= n ):
    pp[nn] = 1

  for nn in range ( 2, n + 1 ):
    for j in range ( 1, nn + 1 ):
      s2 = 0
      for k in range ( 1, j + 1 ):
        if ( ( j % k ) == 0 ):
          s2 = s2 + k * k
      pp[nn] = pp[nn] + pp[nn-j] * s2
    pp[nn] = pp[nn] / nn

  value = pp[n]

  return value

def plane_partition_num_test ( ):

#*****************************************************************************80
#
## PLANE_PARTITION_NUM_TEST tests PLANE_PARTITION_NUM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 December 2014
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'PLANE_PARTITION_NUM_TEST'
  print '  PLANE_PARTITION_NUM computes the number of plane'
  print '  partitions of an integer.'
  print ''
 
  for n in range ( 1, 11 ):
    p = plane_partition_num ( n )
    print '  %2d  %6d' % ( n, p )

  print ''
  print 'PLANE_PARTITION_NUM_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  plane_partition_num_test ( )
  timestamp ( )
