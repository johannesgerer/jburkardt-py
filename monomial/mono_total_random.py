#!/usr/bin/env python

def mono_total_random ( m, n, seed ):

#*****************************************************************************80
#
## MONO_TOTAL_RANDOM: random monomial with total degree equal to N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 November 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the spatial dimension.
#
#    Input, integer N, the degree.
#    0 <= N.
#
#    Input, integer SEED, the random number seed.
#
#    Output, integer X[M], the random monomial.
#
#    Output, integer RANK, the rank of the monomial.
#
#    Output, integer SEED, the random number seed.
#
  from i4_uniform_ab import i4_uniform_ab
  from mono_unrank_grlex import mono_unrank_grlex
  from mono_upto_enum import mono_upto_enum

  rank_min = mono_upto_enum ( m, n - 1 ) + 1
  rank_max = mono_upto_enum ( m, n )
  rank, seed = i4_uniform_ab ( rank_min, rank_max, seed )
  x = mono_unrank_grlex ( m, rank )

  return x, rank, seed

def mono_total_random_test ( ):

#*****************************************************************************80
#
## MONO_TOTAL_RANDOM_TEST tests MONO_TOTAL_RANDOM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 November 2014
#
#  Author:
#
#    John Burkardt
#
  m = 3

  print ''
  print 'MONO_TOTAL_RANDOM_TEST'
  print '  MONO_TOTAL_RANDOM selects at random a monomial'
  print '  in M dimensions of total degree N.'

  n = 4

  print ''
  print '  Let M = %d' % ( m )
  print '      N = %d' % ( n )
  print ''

  seed = 123456789
  test_num = 5

  for test in range ( 0, test_num ):
    x, rank, seed = mono_total_random ( m, n, seed )
    print '  %2d    ' % ( rank ),
    for j in range ( 0, m ):
      print '%2d' % ( x[j] ),
    print ''

  print ''
  print 'MONO_TOTAL_RANDOM_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp

  timestamp ( )
  mono_total_random_test ( )
  timestamp ( )
