#!/usr/bin/env python

def mono_next_grlex ( m, x ):

#*****************************************************************************80
#
## MONO_NEXT_GRLEX returns the next monomial in grlex order.
#
#  Discussion:
#
#    Example:
#
#    M = 3
#
#    #  X(1)  X(2)  X(3)  Degree
#      +------------------------
#    1 |  0     0     0        0
#      |
#    2 |  0     0     1        1
#    3 |  0     1     0        1
#    4 |  1     0     0        1
#      |
#    5 |  0     0     2        2
#    6 |  0     1     1        2
#    7 |  0     2     0        2
#    8 |  1     0     1        2
#    9 |  1     1     0        2
#   10 |  2     0     0        2
#      |
#   11 |  0     0     3        3
#   12 |  0     1     2        3
#   13 |  0     2     1        3
#   14 |  0     3     0        3
#   15 |  1     0     2        3
#   16 |  1     1     1        3
#   17 |  1     2     0        3
#   18 |  2     0     1        3
#   19 |  2     1     0        3
#   20 |  3     0     0        3
#
#    Thanks to Stefan Klus for pointing out a discrepancy in a previous
#    version of this code, 05 February 2015.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the spatial dimension.
#
#    Input, integer X[M], the current monomial.
#    The first element is X = [ 0, 0, ..., 0, 0 ].
#
#    Output, integer X[M], the next monomial.
#

#
#  Ensure that 1 <= D.
#
  if ( m < 1 ):
    print ''
    print 'MONO_NEXT_GRLEX - Fatal error!'
    print '  M < 1'
    sys.exit ( 'MONO_NEXT_GRLEX - Fatal error!' )
#
#  Ensure that 0 <= X(I).
#
  for i in range ( 0, m ):
    if ( x[i] < 0 ):
      print ''
      print 'MONO_NEXT_GRLEX - Fatal error!'
      print '  X[I] < 0'
      sys.exit ( 'MONO_NEXT_GRLEX - Fatal error!' )
#
#  Find I, the index of the rightmost nonzero entry of X.
#
  i = 0
  for j in range ( m, 0, -1 ):
    if ( 0 < x[j-1] ):
      i = j
      break
#
#  set T = X(I)
#  set X(I) to zero,
#  increase X(I-1) by 1,
#  increment X(M) by T-1.
#
  if ( i == 0 ):
    x[m-1] = 1
    return x
  elif ( i == 1 ):
    t = x[0] + 1
    im1 = m
  elif ( 1 < i ):
    t = x[i-1]
    im1 = i - 1

  x[i-1] = 0
  x[im1-1] = x[im1-1] + 1
  x[m-1] = x[m-1] + t - 1

  return x

def mono_next_grlex_test ( ):

#*****************************************************************************80
#
## MONO_NEXT_GRLEX_TEST tests MONO_NEXT_GRLEX.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 4

  print ''
  print 'MONO_NEXT_GRLEX_TEST'
  print '  MONO_NEXT_GRLEX computes the next monomial'
  print '  in M variables in grlex order.'
  print ''
  print '  Let M =  %d' % ( m )

  k = 0
  x = np.zeros ( m )

  while ( True ):

    d = sum ( x )
    print '  %2d  %2d  |' % ( k, d ),
    for i in range ( 0, m ):
      print '  %2d' % x[i],
    print ''

    if ( x[0] == 3 ):
      break
    k = k + 1
    x = mono_next_grlex ( m, x )

  print ''
  print 'MONO_NEXT_GRLEX_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp

  timestamp ( )
  mono_next_grlex_test ( )
  timestamp ( )
