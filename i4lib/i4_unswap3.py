#!/usr/bin/env python

def i4_unswap3 ( i, j, k ) :

#*****************************************************************************80
#
## I4_UNSWAP3 unswaps three integer values.
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
#    Input, integer I, J, K, the values to be unswapped.
#
#    Output, integer I, J, K, the unswapped values.
#
  return k, i, j

def i4_unswap3_test ( ):

#*****************************************************************************80
#
## I4_UNSWAP3_TEST tests I4_UNSWAP3.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 May 2015
#
#  Author:
#
#    John Burkardt
#
  from i4_swap3 import i4_swap3

  print ''
  print 'I4_UNSWAP3_TEST'
  print '  I4_UNSWAP3 swaps three I4''s.'
  print '  It can also reverse the effect of I4_SWAP3.'
  print ''
  print '  Starting with (I,J,K), unswap 3 times.'
  print ''

  i = 1
  j = 202
  k = 3003003

  print '  %8d  %8d  %8d' % ( i, j, k )

  for l in range ( 0, 3 ):
    i, j, k = i4_unswap3 ( i, j, k )
    print '  %8d  %8d  %8d' % ( i, j, k )

  print ''
  print '  Start with (I,J,K), swap, then unswap.'
  print ''

  i = 1
  j = 202
  k = 3003003

  print '  %8d  %8d  %8d' % ( i, j, k )
  i, j, k = i4_swap3 ( i, j, k )
  print '  %8d  %8d  %8d' % ( i, j, k )
  i, j, k = i4_unswap3 ( i, j, k )
  print '  %8d  %8d  %8d' % ( i, j, k )
#
#  Terminate.
#
  print ''
  print 'I4_UNSWAP3_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_unswap3_test ( )
  timestamp ( )
