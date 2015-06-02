#!/usr/bin/env python

def cycle_brent_test01 ( ):

#*****************************************************************************80
#
## CYCLE_BRENT_TEST01 tests CYCLE_BRENT for a tiny example.
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
  from cycle_brent import cycle_brent
  from f1 import f1

  print
  print 'CYCLE_BRENT_TEST01'
  print '  Test CYCLE_BRENT on F1().'
  print '  f1(0) = 6.'
  print '  f1(1) = 6.'
  print '  f1(2) = 0.'
  print '  f1(3) = 1.'
  print '  f1(4) = 4.'
  print '  f1(5) = 3.'
  print '  f1(6) = 3.'
  print '  f1(7) = 4.'
  print '  f1(8) = 0.'

  x0 = 2;
  print
  print '  Starting argument X0 = %d' % ( x0 )

  [ lam, mu ] = cycle_brent ( f1, x0 )

  print
  print '  Reported cycle length is %d' % ( lam )
  print '  Expected value is 3'
  print
  print '  Reported distance to first cycle element is %d' % ( mu )
  print '  Expected value is 2'

  return

if ( __name__ == '__main__' ):
  cycle_brent_test01 ( )
