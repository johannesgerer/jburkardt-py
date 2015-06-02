#!/usr/bin/env python

def ch_uniform_ab ( a, b, seed ):

#*****************************************************************************80
#
## CH_UNIFORM_AB returns a scaled pseudorandom CH.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    05 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, character A, B, the minimum and maximum acceptable characters.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, character CH, the randomly chosen character.
#
#    Output, integer SEED, a seed for the random number generator.
#
  import i4_uniform_ab

  i1 = ord ( a )
  i2 = ord ( b )
  [ i3, seed ] = i4_uniform_ab.i4_uniform_ab ( i1, i2, seed )
  ch = chr ( i3 )

  return ch, seed

def ch_uniform_ab_test ( ):

#*****************************************************************************80
#
## CH_UNIFORM_AB_TEST tests CH_UNIFORM_AB.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    05 April 2013
#
#  Author:
#
#    John Burkardt
#
  seed = 123456789

  print ''
  print 'CH_UNIFORM_AB_TEST'
  print '  CH_UNIFORM_AB computes pseudorandom character values'
  print '  in the interval [CLO,CHI].'

  clo = 'A'
  chi = 'J'

  print ''
  print '  The lower endpoint CLO = %c' % ( clo )
  print '  The upper endpoint CHI = %c' % ( chi )
  print '  The initial seed is %d' % ( seed )
  print ''

  for i in range ( 1, 11 ):
    [ ch, seed ] = ch_uniform_ab ( clo, chi, seed )
    print '  %6d  %c' % ( i, ch )

  print ''
  print 'CH_UNIFORM_AB_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  ch_uniform_ab_test ( )
  timestamp ( )
