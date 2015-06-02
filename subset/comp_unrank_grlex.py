#!/usr/bin/env python

def comp_unrank_grlex ( kc, rank ):

#*****************************************************************************80
#
## COMP_UNRANK_GRLEX computes the composition of given grlex rank.
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
#    Input, int RANK, the rank of the composition.
#    1 <= RANK.
#
#    Output, int XC[KC], the composition XC of the given rank.
#    For each I, 0 <= XC[I] <= NC, and 
#    sum ( 1 <= I <= KC ) XC[I] = NC.
#
  from i4_choose import i4_choose
  from sys import exit
  import numpy as np
#
#  Ensure that 1 <= KC.
#
  if ( kc < 1 ):
    print ''
    print 'COMP_UNRANK_GRLEX - Fatal error!'
    print '  KC < 1'
    exit ( 'COMP_UNRANK_GRLEX - Fatal error!' )
#
#  Ensure that 1 <= RANK.
#
  if ( rank < 1 ):
    print ''
    print 'COMP_UNRANK_GRLEX - Fatal error!'
    print '  RANK < 1'
    exit ( 'COMP_UNRANK_GRLEX - Fatal error!' )
#
#  Determine the appropriate value of NC.
#  Do this by adding up the number of compositions of sum 0, 1, 2, 
#  ..., without exceeding RANK.  Moreover, RANK - this sum essentially
#  gives you the rank of the composition within the set of compositions
#  of sum NC.  And that's the number you need in order to do the
#  unranking.
#
  rank1 = 1
  nc = -1

  while ( True ):
    nc = nc + 1
    r = i4_choose ( nc + kc - 1, nc )
    if ( rank < rank1 + r ):
      break
    rank1 = rank1 + r

  rank2 = rank - rank1
#
#  Convert to KSUBSET format.
#  Apology: an unranking algorithm was available for KSUBSETS,
#  but not immediately for compositions.  One day we will come back
#  and simplify all this.
#
  ks = kc - 1
  ns = nc + kc - 1
  xs = np.zeros ( ks, dtype = np.int32 )
  nksub = i4_choose ( ns, ks )

  j = 1

  for i in range ( 1, ks + 1 ):
    r = i4_choose ( ns - j, ks - i )
    while ( r <= rank2 and 0 < r ):
      rank2 = rank2 - r
      j = j + 1
      r = i4_choose ( ns - j, ks - i )
    xs[i-1] = j
    j = j + 1
#
#  Convert from KSUBSET format to COMP format.
#
  xc = np.zeros ( kc, dtype = np.int32 )
  xc[0] = xs[0] - 1
  for i in range ( 2, kc ):
    xc[i-1] = xs[i-1] - xs[i-2] - 1
  xc[kc-1] = ns - xs[ks-1]

  return xc

def comp_unrank_grlex_test ( ):

#*****************************************************************************80
#
## COMP_UNRANK_GRLEX_TEST tests COMP_UNRANK_GRLEX.
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

  kc = 3

  print ''
  print 'COMP_UNRANK_GRLEX_TEST'
  print '  A COMP is a composition of an integer N into K parts.'
  print '  Each part is nonnegative.  The order matters.'
  print '  COMP_UNRANK_GRLEX determines the parts'
  print '  of a COMP from its rank.'
 
  print ''
  print '  Rank: ->  NC       COMP    '
  print '  ----:     --   ------------ '

  for rank in range ( 1, 72 ):
    xc = comp_unrank_grlex ( kc, rank )
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
#
#  Terminate.
#
  print ''
  print 'COMP_UNRANK_GRLEX_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  comp_unrank_grlex_test ( )
  timestamp ( )
