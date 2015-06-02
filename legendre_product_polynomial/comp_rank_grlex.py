#!/usr/bin/env python

def comp_rank_grlex ( kc, xc ):

#*****************************************************************************80
#
## COMP_RANK_GRLEX computes the graded lexicographic rank of a composition.
#
#  Discussion:
#
#    The graded lexicographic ordering is used, over all KC-compositions
#    for NC = 0, 1, 2, ...
#
#    For example, if KC = 3, the ranking begins:
#
#    Rank  Sum    1  2  3
#    ----  ---   -- -- --
#       1    0    0  0  0
#
#       2    1    0  0  1
#       3    1    0  1  0
#       4    1    1  0  1
#
#       5    2    0  0  2
#       6    2    0  1  1
#       7    2    0  2  0
#       8    2    1  0  1
#       9    2    1  1  0
#      10    2    2  0  0
#
#      11    3    0  0  3
#      12    3    0  1  2
#      13    3    0  2  1
#      14    3    0  3  0
#      15    3    1  0  2
#      16    3    1  1  1
#      17    3    1  2  0
#      18    3    2  0  1
#      19    3    2  1  0
#      20    3    3  0  0
#
#      21    4    0  0  4
#      ..   ..   .. .. ..
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
#    Input, int KC, the number of parts in the composition.
#    1 <= KC.
#
#    Input, int XC[KC], the composition.
#    For each 1 <= I <= KC, we have 0 <= XC(I).
#
#    Output, int RANK, the rank of the composition.
#
  from i4_choose import i4_choose
  from i4vec_sum import i4vec_sum
  from sys import exit
  import numpy as np
#
#  Ensure that 1 <= KC.
#
  if ( kc < 1 ):
    print '';
    print 'COMP_RANK_GRLEX - Fatal error!'
    print '  KC < 1'
    exit ( 'COMP_RANK_GRLEX - Fatal error!' );
#
#  Ensure that 0 <= XC(I).
#
  for i in range ( 0, kc ):
    if ( xc[i] < 0 ):
      print ''
      print 'COMP_RANK_GRLEX - Fatal error!'
      print '  XC[I] < 0'
      exit ( 'COMP_RANK_GRLEX - Fatal error!' );
#
#  NC = sum ( XC )
#
  nc = i4vec_sum ( kc, xc )
#
#  Convert to KSUBSET format.
#
  ns = nc + kc - 1
  ks = kc - 1
  xs = np.zeros ( ks, dtype = np.int32 )

  xs[0] = xc[0] + 1
  for i in range ( 2, kc ):
    xs[i-1] = xs[i-2] + xc[i-1] + 1
#
#  Compute the rank.
#
  rank = 1;

  for i in range ( 1, ks + 1 ):
    if ( i == 1 ):
      tim1 = 0
    else:
      tim1 = xs[i-2];

    if ( tim1 + 1 <= xs[i-1] - 1 ):
      for j in range ( tim1 + 1, xs[i-1] ):
        rank = rank + i4_choose ( ns - j, ks - i )

  for n in range ( 0, nc ):
    rank = rank + i4_choose ( n + kc - 1, n )

  return rank

def comp_rank_grlex_test ( ):

#*****************************************************************************80
#
## COMP_RANK_GRLEX_TEST tests COMP_RANK_GRLEX.
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
  from comp_random_grlex import comp_random_grlex

  print ''
  print 'COMP_RANK_GRLEX_TEST'
  print '  A COMP is a composition of an integer N into K parts.'
  print '  Each part is nonnegative.  The order matters.'
  print '  COMP_RANK_GRLEX determines the rank of a COMP'
  print '  from its parts.'
  print ''
  print '        Actual  Inferred'
  print '  Test    Rank      Rank'
  print ''

  kc = 3
  rank1 = 20
  rank2 = 60
  seed = 123456789

  for test in range ( 0, 5 ):
    xc, rank3, seed = comp_random_grlex ( kc, rank1, rank2, seed )
    rank4 = comp_rank_grlex ( kc, xc )
    print '  %4d  %6d  %8d' % ( test, rank3, rank4 )

  print ''
  print 'COMP_RANK_GRLEX_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp

  timestamp ( )
  comp_rank_grlex_test ( )
  timestamp ( )
