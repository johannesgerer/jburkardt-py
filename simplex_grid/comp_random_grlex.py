#!/usr/bin/env python

def comp_random_grlex ( kc, rank1, rank2, seed ):

#*****************************************************************************80
#
## COMP_RANDOM_GRLEX: random composition with degree less than or equal to NC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 September 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, int KC, the number of parts in the composition.
#
#    Input, int RANK1, RANK2, the minimum and maximum ranks.
#    1 <= RANK1 <= RANK2.
#
#    Input, int SEED, the random number seed.
#
#    Output, int X[KC], the random composition.
#
#    Output, int RANK, the rank of the composition.
#
#    Output, int SEED, the random number seed.
#
  from comp_unrank_grlex import comp_unrank_grlex
  from i4_uniform_ab import i4_uniform_ab
  from sys import exit
#
#  Ensure that 1 <= KC.
#
  if ( kc < 1 ):
    print ''
    print 'COMP_RANDOM_GRLEX - Fatal error!'
    print '  KC < 1'
    exit ( 'COMP_RANDOM_GRLEX - Fatal error!' );
#
#  Ensure that 1 <= RANK1.
#
  if ( rank1 < 1 ):
    print ''
    print 'COMP_RANDOM_GRLEX - Fatal error!'
    print '  RANK1 < 1'
    exit ( 'COMP_RANDOM_GRLEX - Fatal error!' );
#
#  Ensure that RANK1 <= RANK2.
#
  if ( rank2 < rank1 ):
    print ''
    print 'COMP_RANDOM_GRLEX - Fatal error!'
    print '  RANK2 < RANK1'
    exit ( 'COMP_RANDOM_GRLEX - Fatal error!' )
#
#  Choose RANK between RANK1 and RANK2.
#
  rank, seed = i4_uniform_ab ( rank1, rank2, seed )
#
#  Recover the composition of given RANK.
#
  xc = comp_unrank_grlex ( kc, rank )

  return xc, rank, seed

def comp_random_grlex_test ( ):

#*****************************************************************************80
#
## COMP_RANDOM_GRLEX_TEST tests COMP_RANDOM_GRLEX.
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

  print ''
  print 'COMP_RANDOM_GRLEX_TEST'
  print '  A COMP is a composition of an integer N into K parts.'
  print '  Each part is nonnegative.  The order matters.'
  print '  COMP_RANDOM_GRLEX selects a random COMP in'
  print '  graded lexicographic (grlex) order between indices RANK1 and RANK2.'
  print ''

  kc = 3
  rank1 = 20
  rank2 = 60
  seed = 123456789

  for test in range ( 0, 5 ):
    xc, rank, seed = comp_random_grlex ( kc, rank1, rank2, seed )
    nc = i4vec_sum ( kc, xc )
    print '   %3d: ' % ( rank ),
    print '    %2d = ' % ( nc ),
    for j in range ( 0, kc - 1 ):
      print '%2d + ' % ( xc[j] ),
    print '%2d' % ( xc[kc-1] )

  print ''
  print 'COMP_RANDOM_GRLEX_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp

  timestamp ( )
  comp_random_grlex_test ( )
  timestamp ( )
