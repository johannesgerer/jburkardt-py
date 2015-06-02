#!/usr/bin/env python

def rnglib_test03 ( ):

#*****************************************************************************80
#
## RNGLIB_TEST03 demonstrates how the seed can be reset to its initial or last value.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    27 May 2013
#
#  Author:
#
#    John Burkardt
#
  from cgn_set import cgn_set
  from init_generator import init_generator
  from initialize import initialize
  from r4_uniform_01 import r4_uniform_01

  print ''
  print 'RNGLIB_TEST03'
  print '  R4_UNIFORM_01 ( ) returns a random real number'
  print '  in [0,1] using the current generator.'
#
#  Initialize the package.
#
  print ''
  print '  INITIALIZE initializes the random number generator.'
  print '  It only needs to be called once before using the package.'

  initialize ( )

  print ''
  print '  INIT_GENERATOR can reset the seed to the initial value,'
  print '  the last (previous) value, or a new seed.'
#
#  Set the current generator index to 17.
#
  g = 17
  cgn_set ( g )
  print ''
  print '  Current generator index = %d' % ( g )
#
#  Force the current generator to begin at its initial seed.
#
  print ''
  print '  INIT_GENERATOR ( 0 ) starts at the initial seed.'

  init_generator ( 0 )

  print ''
  print '   I    R4_UNIFORM_01 ( )'
  print ''
  for i in range ( 1, 10 ):
    u = r4_uniform_01 ( )
    print '  %2d  %14.6g' % ( i, u )

  print ''
  print '  Calling INIT_GENERATOR ( 0 ) again restarts'
  print '  at the initial seed.'

  init_generator ( 0 )

  print ''
  print '   I    R4_UNIFORM_01 ( )'
  print ''
  for i in range ( 1, 10 ):
    u = r4_uniform_01 ( )
    print '  %2d  %14.6g' % ( i, u )

  print ''
  print '  Calling INIT_GENERATOR ( 2 ) restarts'
  print '  at a new "far ahead" seed.'

  init_generator ( 2 )

  print ''
  print '   I    R4_UNIFORM_01 ( )'
  print ''
  for i in range ( 1, 10 ):
    u = r4_uniform_01 ( )
    print '  %2d  %14.6g' % ( i, u )

  print ''
  print '  Calling INIT_GENERATOR ( 1 ) restarts'
  print '  at the last seed (in this case, the "far ahead"'
  print '  seed specified on the previous call.)'

  print ''
  print '   I    R4_UNIFORM_01 ( )'
  print ''
  for i in range ( 1, 11 ):
    u = r4_uniform_01 ( )
    print '  %2d  %14.6g' % ( i, u )
    if ( ( i % 3 ) == 0 ):
      init_generator ( 1 )
      print '  (Reset to last seed)'

if ( __name__ == '__main__' ):
  rnglib_test03 ( )
