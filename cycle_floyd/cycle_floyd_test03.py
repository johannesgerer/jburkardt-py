#!/usr/bin/env python

def cycle_floyd_test03 ( ) :

#*****************************************************************************80
#
## CYCLE_FLOYD_TEST03 tests CYCLE_FLOYD for F3.
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
  from cycle_floyd import cycle_floyd
  from f3 import f3

  print
  print 'CYCLE_FLOYD_TEST03'
  print '  Test CYCLE_FLOYD for F3().'
  print '  f3(i) = mod ( 123 * i + 456, 100000 ).'

  x0 = 789
  print
  print '  Starting argument X0 = %d' % ( x0 )

  [ lam, mu ] = cycle_floyd ( f3, x0 )

  print
  print '  Reported cycle length is %d' % ( lam )
  print '  Expected value is 50000'
  print
  print '  Reported distance to first cycle element is %d' % ( mu )
  print '  Expected value is 0'

  return

if ( __name__ == '__main__' ) :
  cycle_floyd_test03 ( )
