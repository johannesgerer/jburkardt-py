#!/usr/bin/env python

def r8_swap3 ( x, y, z ):

#*****************************************************************************80
#
## R8_SWAP3 swaps three R8's.
#
#  Example:
#
#    Input:
#
#      X = 1, Y = 2, Z = 3
#
#    Output:
#
#      X = 2, Y = 3, Z = 1
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    07 June 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, Y, Z, three values to be swapped.
#
#    Output, real X, Y, Z, three values to be swapped.
#
  w = x
  x = y
  y = z
  z = w

  return x, y, z

def r8_swap3_test ( ):

#*****************************************************************************80
#
## R8_SWAP3_TEST tests R8_SWAP3.
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
  print 'R8_SWAP3_TEST'
  print '  R8_SWAP3 swaps three reals.'

  x = 1.0
  y = 3.14159
  z = 1952.0

  print ''
  print '  Before  %g  %g  %g' % ( x, y, z )
  print ''

  for i in range ( 0, 3 ):
    x, y, z = r8_swap3 ( x, y, z )
    print '  Swap %d:  %g  %g  %g' % ( i, x, y, z )
#
#  Terminate.
#
  print ''
  print 'R8_SWAP3_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_swap3_test ( )
  timestamp ( )

