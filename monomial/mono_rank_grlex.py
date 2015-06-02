#!/usr/bin/env python

def mono_rank_grlex ( m, x ):

#*****************************************************************************80
#
## MONO_RANK_GRLEX computes the graded lexicographic rank of a monomial.
#
#  Discussion:
#
#    The graded lexicographic ordering is used, over all monomials in 
#    M dimensions, for total degree = 0, 1, 2, ...
#
#    For example, if M = 3, the ranking begins:
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
#   This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 October 2015
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
#    Input, integer X[M], the composition.
#    For each 1 <= I <= M, we have 0 <= X(I).
#
#    Output, integer RANK, the rank.
#
  from i4_choose import i4_choose
  from i4vec_sum import i4vec_sum
  import numpy as np
#
#  Ensure that 1 <= M.
#
  if ( m < 1 ):
    print ''
    print 'MONO_RANK_GRLEX - Fatal error!'
    print '  M < 1'
    sys.exit ( 'MONO_RANK_GRLEX - Fatal error!' )
#
#  Ensure that 0 <= X(I).
#
  for i in range ( 0, m ):
    if ( x[i] < 0 ):
      print ''
      print 'MONO_RANK_GRLEX - Fatal error!'
      print '  X[I] < 0'
      sys.exit ( 'MONO_RANK_GRLEX - Fatal error!' )
#
#  NM = sum ( X )
#
  nm = i4vec_sum ( m, x )
#
#  Convert to KSUBSET format.
#
  ns = nm + m - 1
  ks = m - 1
  if ( 0 < ks ):
    xs = np.zeros ( ks, dtype = np.int32 )
    xs[0] = x[0] + 1
    for i in range ( 2, m ):
      xs[i-1] = xs[i-2] + x[i-1] + 1
#
#  Compute the rank.
#
  rank = 1

  for i in range ( 1, ks + 1 ):
    if ( i == 1 ):
      tim1 = 0
    else:
      tim1 = xs[i-2]

    if ( tim1 + 1 <= xs[i-1] - 1 ):
      for j in range ( tim1 + 1, xs[i-1] ):
        rank = rank + i4_choose ( ns - j, ks - i )

  for n in range ( 0, nm ):
    rank = rank + i4_choose ( n + m - 1, n )

  return rank

def mono_rank_grlex_test ( ):

#******************************************************************************/
#
## MONO_RANK_GRLEX_TEST tests MONO_RANK_GRLEX.
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
  from mono_upto_next_grlex import mono_upto_next_grlex
  import numpy as np

  m = 3
  test_num = 8
  x_test = np.array (  [ \
    0, 0, 0, \
    1, 0, 0, \
    0, 0, 1, \
    0, 2, 0, \
    1, 0, 2, \
    0, 3, 1, \
    3, 2, 1, \
    5, 2, 1 ], dtype = np.int32 )

  print ''
  print 'MONO_RANK_GRLEX_TEST'
  print '  MONO_RANK_GRLEX returns the rank of a monomial in the sequence'
  print '  of all monomials in M dimensions, in grlex order.'

  print ''
  print '  Print a monomial sequence with ranks assigned.'

  n = 4

  print ''
  print '  Let M = %d' % ( m )
  print '      N = %d' % ( n )
  print ''

  x = np.zeros ( m, dtype = np.int32 )

  x[0] = 0
  x[1] = 0
  x[2] = 0

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
  print '  Now, given a monomial, retrieve its rank in the sequence:'
  print ''

  for test in range ( 0, test_num ):
    for j in range ( 0, m ):
      x[j] = x_test[j+test*m]
    rank = mono_rank_grlex ( m, x )

    print '  %3d    ' % ( rank ),
    for j in range ( 0, m ):
      print '%2d' % ( x[j] ),
    print ''

  print ''
  print 'MONO_RANK_GRLEX_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp

  timestamp ( )
  mono_rank_grlex_test ( )
  timestamp ( )
