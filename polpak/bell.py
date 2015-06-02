#!/usr/bin/env python
#
def bell ( n ):

#*****************************************************************************80
#
## BELL returns the Bell numbers from 0 to N.
#
#  Discussion:
#
#    The Bell number B(N) is the number of restricted growth functions
#    on N.
#
#    Note that the Stirling numbers of the second kind, S^m_n, count the
#    number of partitions of N objects into M classes, and so it is
#    true that
#
#      B(N) = S^1_N + S^2_N + ... + S^N_N.
#
#  Definition:
#
#    The Bell number B(N) is defined as the number of partitions (of
#    any size) of a set of N distinguishable objects.
#
#    A partition of a set is a division of the objects of the set into
#    subsets.
#
#  Examples:
#
#    There are 15 partitions of a set of 4 objects:
#
#      (1234), (123)(4), (124)(3), (12)(34), (12)(3)(4),
#      (134)(2), (13)(24), (13)(2)(4), (14)(23), (1)(234),
#      (1)(23)(4), (14)(2)(3), (1)(24)(3), (1)(2)(34), (1)(2)(3)(4)
#
#    and so B(4) = 15.
#
#  First values:
#
#     N         B(N)
#     0           1
#     1           1
#     2           2
#     3           5
#     4          15
#     5          52
#     6         203
#     7         877
#     8        4140
#     9       21147
#    10      115975
#
#  Recursion:
#
#    B(I) = sum ( 1 <= J <= I ) Binomial ( I-1, J-1 ) * B(I-J)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of Bell numbers desired.
#
#    Output, integer B(1:N+1), the Bell numbers from 0 to N.
#
  import numpy as np
  from i4_choose import i4_choose

  b = np.zeros ( n + 1 )

  b[0] = 1

  for i in range ( 1, n + 1 ):
    b[i] = 0
    for j in range ( 1, i + 1 ):
      b[i] = b[i] + i4_choose ( i - 1, j - 1 ) * b[i-j]

  return b

def bell_test ( ):

#*****************************************************************************80
#
## BELL_TEST tests BELL.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 December 2014
#
#  Author:
#
#    John Burkardt
#
  from bell_values import bell_values

  print ''
  print 'BELL_TEST'
  print '  BELL computes Bell numbers.'
  print ''
  print '   N  exact C(I)  computed C(I)'
  print ''

  n_data = 0

  while ( True ):

    n_data, n, c = bell_values ( n_data )

    if ( n_data == 0 ):
      break

    c2 = bell ( n )

    print '  %2d  %8d  %8d' % ( n, c, c2[n] )
 
  print ''
  print 'BELL_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  bell_test ( )
  timestamp ( )
