#!/usr/bin/env python

def rnglib_test01 ( ):

#*****************************************************************************80
#
## RNGLIB_TEST01 calls I4_UNIFORM 10 times, just to show how it is done.
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
  from i4_uniform import i4_uniform
  from initialize import initialize

  print ''
  print 'RNGLIB_TEST01'
  print '  I4_UNIFORM ( ) returns a random positive integer'
  print '  using the current generator.'
#
#  Initialize the package.
#
  print ''
  print '  INITIALIZE initializes the random number generator.'
  print '  It only needs to be called once before using the package.'

  initialize ( )
#
#  Set the current generator index to #1.
#
  g = 1
  cgn_set ( g )
  print ''
  print '  Current generator index = %d' % ( g )
#
#  Now call I4_UNIFORM().
#
  print ''
  print '   I     I4_UNIFORM ( )'
  print ''

  for i in range ( 1, 11 ):
    j = i4_uniform ( )
    print '  %2d  %12d' % ( i, j )

if ( __name__ == '__main__' ):
  rnglib_test01 ( )
