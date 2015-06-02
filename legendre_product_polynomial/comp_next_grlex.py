#!/usr/bin/env python

def comp_next_grlex ( kc, xc ):

#*****************************************************************************80
#
## COMP_NEXT_GRLEX returns the next composition in grlex order.
#
#  Discussion:
#
#    Example:
#
#    KC = 3
#
#    #   XC(1) XC(2) XC(3)  Degree
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
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, int KC, the number of parts of the composition.
#    1 <= KC.
#
#    Input/output, int XC[KC], the current composition.
#    Each entry of XC must be nonnegative.
#    On return, XC has been replaced by the next composition in the
#    grlex order.
#
  from sys import exit
#
#  Ensure that 1 <= KC.
#
  if ( kc < 1 ):
    print ''
    print 'COMP_NEXT_GRLEX - Fatal error!'
    print '  KC < 1'
    exit ( 'COMP_NEXT_GRLEX - Fatal error!' );
#
#  Ensure that 0 <= XC(I).
#
  for i in range ( 0, kc ):
    if ( xc[i] < 0 ):
      print ''
      print 'COMP_NEXT_GRLEX - Fatal error!'
      print '  XC[I] < 0'
      exit ( 'COMP_NEXT_GRLEX - Fatal error!' )
#
#  Find I, the index of the rightmost nonzero entry of X.
#
  i = 0
  for j in range ( kc, 0, -1 ):
    if ( 0 < xc[j-1] ):
      i = j
      break
#
#  set T = X(I)
#  set XC(I) to zero,
#  increase XC(I-1) by 1,
#  increment XC(KC) by T-1.
#
  if ( i == 0 ):
    xc[kc-1] = 1
    return xc
  elif ( i == 1 ):
    t = xc[0] + 1
    im1 = kc
  elif ( 1 < i ):
    t = xc[i-1]
    im1 = i - 1

  xc[i-1] = 0
  xc[im1-1] = xc[im1-1] + 1
  xc[kc-1] = xc[kc-1] + t - 1

  return xc

def comp_next_grlex_test ( ):

#*****************************************************************************80
#
## COMP_NEXT_GRLEX_TEST tests COMP_NEXT_GRLEX.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 October 2014
#
#  Author:
#
#    John Burkardt
#
  from i4vec_sum import i4vec_sum
  import numpy as np

  kc = 3

  print ''
  print 'COMP_NEXT_GRLEX_TEST'
  print '  A COMP is a composition of an integer N into K parts.'
  print '  Each part is nonnegative.  The order matters.'
  print '  COMP_NEXT_GRLEX determines the next COMP in'
  print '  graded lexicographic (grlex) order.'
  
  xc = np.zeros ( kc, dtype = np.int32 )

  print ''
  print '  Rank:     NC       COMP'
  print '  ----:     --   ------------'

  for rank in range ( 1, 72 ):
    if ( rank == 1 ):
      for j in range ( 0, kc ):
        xc[j] = 0
    else:
      xc = comp_next_grlex ( kc, xc )

    nc = i4vec_sum ( kc, xc )

    print '   %3d: ' % ( rank ),
    print '    %2d = ' % ( nc ),
    for j in range ( 0, kc - 1 ):
      print '%2d + ' % ( xc[j] ),
    print '%2d' % ( xc[kc-1] )
#
#  When XC(1) == NC, we have completed the compositions associated with
#  a particular integer, and are about to advance to the next integer.
#
    if ( xc[0] == nc ):
      print '  ----:     --   ------------'

  print ''
  print 'COMP_NEXT_GRLEX_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp

  timestamp ( )
  comp_next_grlex_test ( )
  timestamp ( )
