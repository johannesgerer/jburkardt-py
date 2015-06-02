#!/usr/bin/env python
#
def motzkin ( n ):

#*****************************************************************************80
#
## MOTZKIN returns the Motzkin numbers up to order N.
#
#  Discussion:
#
#    The Motzkin number A(N) counts the number of distinct paths
#    from (0,0) to (0,N) in which the only steps used are
#    (1,1), (1,-1) and (1,0), and the path is never allowed to
#    go below the X axis.
#
#  First values:
#
#     N  A(N)
#
#     0    1
#     1    1
#     2    2
#     3    4
#     4    9
#     5   21
#     6   51
#     7  127
#     8  323
#     9  835
#    10 2188
#
#  Recursion:
#
#    A(N) = A(N-1) + sum ( 0 <= K <= N-2 ) A(K) * A(N-2-K)
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
#  Reference:
#
#    Eric Weisstein
#    CRC Concise Encyclopedia of Mathematics,
#    CRC Press, 1998
#
#  Parameters:
#
#    Input, integer N, the highest order Motzkin number to compute.
#
#    Output, integer A(1:N+1), the Motzkin numbers.
#
  import numpy as np

  a = np.zeros ( n + 1 )

  a[0] = 1

  for i in range ( 1, n + 1 ):
    a[i] = a[i-1]
    for j in range ( 0, i - 1 ):
      a[i] = a[i] + a[j] * a[i-j-2]

  return a

def motzkin_test ( ):

#*****************************************************************************80
#
## MOTZKIN_TEST tests MOTZKIN.
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
  n = 10

  print ''
  print 'MOTZKIN_TEST'
  print '  MOTZKIN computes the Motzkin numbers A(0:N).'
  print '  A(N) counts the paths from (0,0) to (N,0).'
  print ''
  print '     I  A(I)'
  print ''

  a = motzkin ( n )

  for i in range ( 0, n + 1 ):
    print '  %4d  %10d' % ( i, a[i] )
 
  print ''
  print 'MOTZKIN_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  motzkin_test ( )
  timestamp ( )
