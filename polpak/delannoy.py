#!/usr/bin/env python
#
def delannoy ( m, n ):

#*****************************************************************************80
#
## DELANNOY returns the Delannoy numbers up to orders (M,N).
#
#  Discussion:
#
#    The Delannoy number A(M,N) counts the number of distinct paths
#    from (0,0) to (M,N) in which the only steps used are
#    (1,1), (1,0) and (0,1).
#
#  First values:
#
#      \N 0  1   2   3    4     5     6      7      8
#     M-+--------------------------------------------
#     0 : 1  1   1   1    1     1     1      1      1
#     1 : 1  3   5   7    9    11    13     15     17
#     2 : 1  5  13  25   41    61    85    113    145
#     3 : 1  7  25  63  129   231   377    575    833
#     4 : 1  9  41 129  321   681  1289   2241   3649
#     5 : 1 11  61 231  681  1683  3653   7183  13073
#     6 : 1 13  85 377 1289  3653  8989  19825  40081
#     7 : 1 15 113 575 2241  7183 19825  48639 108545
#     8 : 1 17 145 833 3649 13073 40081 108545 265729
#
#  Recursion:
#
#    A(0,0) = 1
#    A(M,0) = 1
#    A(0,N) = 1
#    A(M,N) = A(M-1,N) + A(M,N-1) + A(M-1,N-1)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 January 2015
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
#    Input, integer M, N, define the highest order number to compute.
#
#    Output, integer A(1:M+1,1:N+1), the Delannoy numbers.
#
  import numpy as np

  a = np.zeros ( [ m + 1, n + 1 ] )

  a[0,0] = 1

  for i in range ( 1, m + 1 ):
    a[i,0] = 1

  for j in range ( 1, n + 1 ):
    a[0,j] = 1

  for i in range ( 1, m + 1 ):
    for j in range ( 1, n + 1 ):
      a[i,j] = a[i-1,j] + a[i,j-1] + a[i-1,j-1]

  return a

def delannoy_test ( ):

#*****************************************************************************80
#
## DELANNOY_TEST tests DELANNOY.
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
  m = 8
  n = 8

  print ''
  print 'DELANNOY_TEST'
  print '  DELANNOY computes the Delannoy numbers A(0:M,0:N).'
  print '  A(M,N) counts the paths from (0,0) to (M,N).'
  print ''

  a = delannoy ( m, n )

  for i in range ( 0, m + 1 ):
    print '  %2d  ' % ( i ),
    for j in range ( 0, n + 1 ):
      print '  %6d' % ( a[i,j] ),
    print ''
 
  print ''
  print 'DELANNOY_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  delannoy_test ( )
  timestamp ( )
