#!/usr/bin/env python

def i4_swap ( x, y ) :

#*****************************************************************************80
#
## I4_SWAP swaps two I4's.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer X, Y, two values to interchange.
#
#    Output, integer X, Y, the interchanged values.
#
  return y, x

def i4_swap_test ( ):

#*****************************************************************************80
#
## I4_SWAP_TEST tests I4_SWAP.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 September 2014
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'I4_SWAP_TEST'
  print '  I4_SWAP swaps two I4''s.'

  i = 1
  j = 202

  print ''
  print '  Before swapping: '
  print ''
  print '  I = %d' % ( i )
  print '  J = %d' % ( j )

  i, j = i4_swap ( i, j )

  print ''
  print '  After swapping: '
  print ''
  print '  I = %d' % ( i )
  print '  J = %d' % ( j )
#
#  Terminate.
#
  print ''
  print 'I4_SWAP_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_swap_test ( )
  timestamp ( )
