#!/usr/bin/env python

def mono_unrank_grlex ( m, rank ):

#*****************************************************************************80
#
## MONO_UNRANK_GRLEX computes the monomial of given grlex rank.
#
#  Licensing:
#
#   This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the spatial dimension.
#    1 <= M.
#
#    Input, integer RANK, the rank of the monomial.
#
#    Output, integer X[M], the monomial.
#
  from i4_choose import i4_choose
  import numpy as np
#
#  Ensure that 1 <= M.
#
  if ( m < 1 ):
    print ''
    print 'MONO_UNRANK_GRLEX - Fatal error!'
    print '  M < 1'
    sys.exit ( 'MONO_UNRANK_GRLEX - Fatal error!' )
#
#  Ensure that 1 <= RANK.
#
  if ( rank < 1 ):
    print ''
    print 'MONO_UNRANK_GRLEX - Fatal error!'
    print '  RANK < 1'
    sys.exit ( 'MONO_UNRANK_GRLEX - Fatal error!' )

  x = np.zeros ( m, dtype = np.int32 )
#
#  Special case M = 1.
#
  if ( m == 1 ):
    x[0] = rank - 1
    return x
#
#  Determine the appropriate value of NM.
#  Do this by adding up the number of compositions of sum 0, 1, 2, 
#  ..., without exceeding RANK.  Moreover, RANK - this sum essentially
#  gives you the rank of the composition within the set of compositions
#  of sum NM.  And that's the number you need in order to do the
#  unranking.
#
  rank1 = 1
  nm = -1
  while ( True ):
    nm = nm + 1
    r = i4_choose ( nm + m - 1, nm )
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
  ks = m - 1
  ns = nm + m - 1
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
  x[0] = xs[0] - 1
  for i in range ( 2, m ):
    x[i-1] = xs[i-1] - xs[i-2] - 1
  x[m-1] = ns - xs[ks-1]

  return x

def mono_unrank_grlex_test ( ):

#******************************************************************************/
#
## MONO_UNRANK_GRLEX_TEST tests MONO_UNRANK_GRLEX.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 October 2014
#
#  Author:
#
#    John Burkardt
#
  from i4_uniform_ab import i4_uniform_ab
  from mono_upto_enum import mono_upto_enum
  from mono_upto_next_grlex import mono_upto_next_grlex
  import numpy as np

  m = 3
  print ''
  print 'MONO_UNRANK_GRLEX'
  print '  MONO_UNRANK_GRLEX is given a rank, and returns the corresponding'
  print '  monomial in the sequence of all monomials in M dimensions'
  print '  in grlex order.'

  print ''
  print '  For reference, print a monomial sequence with ranks.'

  n = 4
  rank_max = mono_upto_enum ( m, n )

  print ''
  print '  Let M = %d' % ( m )
  print '      N = %d' % ( n )
  print ''

  x = np.zeros ( m, dtype = np.int32 )

  i = 1

  while ( True ):
    print '  %2d    ' % ( i ),
    for j in range ( 0, m ):
      print '%2d' % ( x[j] ),
    print ''

    if ( x[0] == n ):
      break

    mono_upto_next_grlex ( m, n, x )
    i = i + 1

  print ''
  print '  Now choose random ranks between 1 and %d' % ( rank_max )
  print ''

  seed = 123456789
  test_num = 5

  for test in range ( 0, test_num ):
    rank, seed = i4_uniform_ab ( 1, rank_max, seed )
    x = mono_unrank_grlex ( m, rank )
    print '  %2d    ' % ( rank ),
    for j in range ( 0, m ):
      print '%2d' % ( x[j] ),
    print ''

  print ''
  print 'MONO_UNRANK_GRLEX_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp

  timestamp ( )
  mono_unrank_grlex_test ( )
  timestamp ( )
