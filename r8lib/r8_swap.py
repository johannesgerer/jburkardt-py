#!/usr/bin/env python

def r8_swap ( x, y ):

#*****************************************************************************80
#
## R8_SWAP swaps two R8's.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    04 June 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, Y, two values to interchange.
#
#    Output, real X, Y, the interchanged values.
#
  z = y
  y = x
  x = z

  return x, y

def r8_swap_test ( ):

#*****************************************************************************80
#
## R8_SWAP_TEST tests R8_SWAP.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 July 2014
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'R8_SWAP_TEST'
  print '  R8_SWAP swaps two reals.'

  x = 1.0
  y = 3.14159

  print ''
  print '  Before swapping:'
  print ''
  print '    X = %f' % ( x )
  print '    Y = %f' % ( y )

  x, y = r8_swap ( x, y )

  print ''
  print '  After swapping:'
  print ''
  print '    X = %f' % ( x )
  print '    Y = %f' % ( y )
#
#  Terminate.
#
  print ''
  print 'R8_SWAP_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  r8_swap_test ( )
  timestamp ( )
