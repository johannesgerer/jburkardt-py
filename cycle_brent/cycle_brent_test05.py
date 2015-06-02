#/usr/bin/env python

def cycle_brent_test05 ( ) :

#*****************************************************************************80
#
## CYCLE_BRENT_TEST05 tests CYCLE_BRENT for F5.
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
  from f5 import f5
  from cycle_brent import cycle_brent

  print
  print 'CYCLE_BRENT_TEST05'
  print '  Test CYCLE_BRENT for F5().'
  print '  f5(i) = mod ( 16383 * i + 1, 65536 ).'

  x0 = 1
  print
  print '  Starting argument X0 = %d' % ( x0 )

  [ lam, mu ] = cycle_brent ( f5, x0 )

  print
  print '  Reported cycle length is %d' % ( lam )
  print '  Expected value is 8'
  print
  print '  Reported distance to first cycle element is %d' % ( mu )
  print '  Expected value is 0'

  i = 0
  x0 = 1
  print
  print '  %d  %d' % ( i, x0 )
  for i in range ( 1, 11 ):
    x0 = f5 ( x0 )
    print '  %d  %d' % ( i, x0 )

  return

if ( __name__ == '__main__' ) :
  cycle_brent_test05 ( )
