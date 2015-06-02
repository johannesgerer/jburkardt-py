#!/usr/bin/env python

def rnglib_test02 ( ):

#*****************************************************************************80
#
## RNGLIB_TEST02 calls R4_UNIFORM_01 10 times, just to show how it is done.
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
  from initialize import initialize
  from r4_uniform_01 import r4_uniform_01

  print ''
  print 'RNGLIB_TEST02'
  print '  R4_UNIFORM_01 ( ) returns a random real number'
  print '  in [0,1] using the current generator.'
#
#  Initialize the package.
#
  print ''
  print '  INITIALIZE initializes the random number generator.'
  print '  It only needs to be called once before using the package.'

  initialize ( )
#
#  Set the current generator index to #2.
#
  g = 2
  cgn_set ( g )
  print ''
  print '  Current generator index = %d' % ( g )
#
#  Repeatedly call R4_UNIFORM_01().
#
  print ''
  print '   I     R4_UNIFORM_01 ( )'
  print ''

  for i in range ( 1, 11 ):
    u = r4_uniform_01 ( )
    print '  %2d  %14.6g' % ( i, u )

if ( __name__ == '__main__' ):
  rnglib_test02 ( )
