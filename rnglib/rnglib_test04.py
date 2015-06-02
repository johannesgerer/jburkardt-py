#!/usr/bin/env python

def rnglib_test04 ( ):

#*****************************************************************************80
#
## RNGLIB_TEST04 demonstrates the use of multiple streams.
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
  print 'RNGLIB_TEST04'
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
  print '  Let us call generators #3, #6 and #9.'
#
#  Use three separate generators, 3, 6 and 9.
#  Force them to start at their initial seeds.
#
  g = [ 3, 6, 9 ]
  print ''
  for j in range ( 0, 3 ):
    print '  Initialize generator %d' % ( g[j] )
    cgn_set ( g[j] )
    init_generator ( 0 )
#
#  Call the generators in the order 3, 6, 9.
#
  print ''
  print '   I    R4_UNIFORM_01 ( 3 )  R4_UNIFORM_01 ( 6 )  R4_UNIFORM_01 ( 9 )'
  print ''
  for i in range ( 1, 11 ):
    print '  %2d' % ( i ),
    for j in range ( 0, 3 ):
      cgn_set ( g[j] )
      u = r4_uniform_01 ( )
      print '  %14.6g' % ( u ),
    print ''
#
#  Restart the generators at their initial seeds.
#
  g = [ 6, 9, 3 ]
  print ''
  for j in range ( 0, 3 ):
    print '  Reinitialize generator %d' % ( g[j] )
    cgn_set ( g[j] )
    init_generator ( 0 )
#
#  Call them in a different order, same result.
#
  print ''
  print '   I    R4_UNIFORM_01 ( 6 )  R4_UNIFORM_01 ( 9 )  R4_UNIFORM_01 ( 3 )'
  print ''
  for i in range ( 1, 11 ):
    print '  %2d' % ( i ),
    for j in range ( 0, 3 ):
      cgn_set ( g[j] )
      u = r4_uniform_01 ( )
      print '  %14.6g' % ( u ),
    print ''

if ( __name__ == '__main__' ):
  rnglib_test04 ( )
