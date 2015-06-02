#!/usr/bin/env python

def cycle_brent_test02 ( ) :

#*****************************************************************************80
#
## CYCLE_BRENT_TEST02 tests CYCLE_BRENT for F2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 May 2013
#
#  Author:
#
#    John Burkardt
#
  from f2 import f2
  from cycle_brent import cycle_brent

  print
  print 'CYCLE_BRENT_TEST02'
  print '  Test CYCLE_BRENT for F2().'
  print '  f2(i) = mod ( 22 * i + 1, 72 ).'

  x0 = 0
  print
  print '  Starting argument X0 = %d' % ( x0 )

  [ lam, mu ] = cycle_brent ( f2, x0 )

  print
  print '  Reported cycle length is %d' % ( lam )
  print '  Expected value is 9'
  print
  print '  Reported distance to first cycle element is %d' % ( mu )
  print '  Expected value is 3'

  return

if ( __name__ == '__main__' ):
  cycle_brent_test02 ( )
