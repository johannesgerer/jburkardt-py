#!/usr/bin/env python

def get_seed ( ):

#*****************************************************************************80
#
## GET_SEED returns a random seed for the random number generator.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    07 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, integer SEED, a random seed value.
#
  import time
  from math import floor
#
#  Get a floating point number, measured in seconds,
#  that represents the elapsed time since the epoch.
#
  seed = time.time ( )
#
#  Reduce the number to an integer.
#
  seed = floor ( seed )
#
#  Use modulo arithmetic to get an integer between 1 and I4_HUGE.
#
  i4_huge = 2147483647
  seed = ( seed % i4_huge ) + 1

  return seed

def get_seed_test ( ):

#*****************************************************************************80
#
## GET_SEED_TEST tests GET_SEED.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    07 April 2013
#
#  Author:
#
#    John Burkardt
#
  from r8_uniform_01 import r8_uniform_01

  print ''
  print 'GET_SEED_TEST'
  print '  GET_SEED picks an initial seed value for R8_UNIFORM_01.'
  print '  The value chosen should vary over time, because'
  print '  the seed is based on reading the clock.'
  print ''
  print '  This is just the "calendar" clock, which does'
  print '  not change very fast, so calling GET_SEED several'
  print '  times in a row may result in the same value.'

  seed = 12345678
  seed_old = seed

  print ''
  print '  Initial seed is %d' % ( seed )
  print ''
  print '  Next 3 values of R8_UNIFORM_01:'
  print ''

  for j in range ( 0, 3 ):
    [ r, seed ] = r8_uniform_01 ( seed )
    print '  %f' % ( r )

  for i in range ( 0, 4 ):

    while ( True ):

      seed = get_seed ( )

      if ( seed != seed_old ):
        seed_old = seed
        break

    print ''
    print '  New seed from GET_SEED is = %d' % ( seed )
    print ''
    print '  Next 3 values of R8_UNIFORM_01:'
    print ''

    for j in range ( 0, 3 ):
      [ r, seed ] = r8_uniform_01 ( seed )
      print '  %f' % ( r )

  print ''
  print 'GET_SEED_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  get_seed_test ( )
  timestamp ( )
