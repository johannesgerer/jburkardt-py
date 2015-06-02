#!/usr/bin/env python

def mono_between_random ( m, n1, n2, seed ):

#*****************************************************************************80
#
## MONO_BETWEEN_RANDOM: random monomial with total degree between N1 and N2.
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
#  Parameters:
#
#    Input, integer M, the spatial dimension.
#
#    Input, integer N1, N2, the minimum and maximum degrees.
#    0 <= N1 <= N2.
#
#    Input, integer SEED, the random number seed.
#
#    Output integer X[M], the random monomial.
#
#    Output integer RANK, the rank of the monomial.
#
#    Output, integer SEED, the updated random number seed.
#
  from i4_uniform_ab import i4_uniform_ab
  from mono_unrank_grlex import mono_unrank_grlex
  from mono_upto_enum import mono_upto_enum

  n1_copy = max ( n1, 0 )
  rank_min = mono_upto_enum ( m, n1_copy - 1 ) + 1
  rank_max = mono_upto_enum ( m, n2 )
  rank, seed = i4_uniform_ab ( rank_min, rank_max, seed )
  x = mono_unrank_grlex ( m, rank )

  return x, rank, seed;

def mono_between_random_test ( ):

#*****************************************************************************80
#
## MONO_BETWEEN_RANDOM_TEST tests MONO_BETWEEN_RANDOM.
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
  m = 3

  print ''
  print 'MONO_BETWEEN_RANDOM_TEST09'
  print '  MONO_BETWEEN_RANDOM selects at random a monomial'
  print '  in M dimensions of total degree between N1 and N2.'

  n1 = 2
  n2 = 3

  print ''
  print '  Let M =  %d' % ( m )
  print '      N1 = %d' % ( n1 )
  print '      N2 = %d' % ( n2 )
  print ''

  seed = 123456789
  test_num = 5

  for test in range ( 0, test_num ):
    x, rank, seed = mono_between_random ( m, n1, n2, seed )
    print '  %2d    ' % ( rank ),
    for j in range ( 0, m ):
      print '%2d' % ( x[j] ),
    print ''

  print ''
  print 'MONO_BETWEEN_RANDOM_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp

  timestamp ( )
  mono_between_random_test ( )
  timestamp ( )
