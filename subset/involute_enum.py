#! /usr/bin/env python
#
def involute_enum ( n ):

#*****************************************************************************80
#
## INVOLUTE_ENUM enumerates the involutions of N objects.
#
#  Discussion:
#
#    An involution is a permutation consisting only of fixed points and
#    pairwise transpositions.
#
#    An involution is its own inverse permutation.
#
#  Recursion:
#
#    S(0) = 1
#    S(1) = 1
#    S(N) = S(N-1) + (N-1) * S(N-2)
#
#  First values:
#
#     N         S(N)
#     0           1
#     1           1
#     2           2
#     3           4
#     4          10
#     5          26
#     6          76
#     7         232
#     8         764
#     9        2620
#    10        9496
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of objects to be permuted.
#
#    Output, integer S(0:N), the number of involutions of 0, 1, 2, ... N
#    objects.
#
  import numpy as np

  s = np.zeros ( n + 1 )

  s[0] = 1

  if ( n <= 0 ):
    return s

  s[1] = 1

  for i in range ( 2, n + 1 ):
    s[i] = s[i-1] + ( i - 1 ) * s[i-2]

  return s

def involute_enum_test ( ):

#*****************************************************************************80
#
## INVOLUTE_ENUM_TEST tests INVOLUTE_ENUM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    19 December 2014
#
#  Author:
#
#    John Burkardt
#
  n = 10

  print ''
  print 'INVOLUTE_ENUM_TEST'
  print '  INVOLUTE_ENUM counts involutions;'
  print ''
  print '  N    # of involutions'
  print ''

  s = involute_enum ( n )

  for i in range ( 0, n + 1 ):
    print '  %8d  %8d' % ( i, s[i] )
#
#  Terminate.
#
  print ''
  print 'INVOLUTE_ENUM_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  involute_enum_test ( )
  timestamp ( )
