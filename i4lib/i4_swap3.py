#!/usr/bin/env python

def i4_swap3 ( i, j, k ) :

#*****************************************************************************80
#
## I4_SWAP3 swaps three I4's.
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
#    Input, integer I, J, K, the values to swap.
#
#    Output, integer I, J, K, the swapped values.
#
  return j, k, i

def i4_swap3_test ( ):

#*****************************************************************************80
#
## I4_SWAP3_TEST tests I4_SWAP3.
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
  print ''
  print 'I4_SWAP3_TEST'
  print '  I4_SWAP3 swaps three I4s.'
  print ''
  print '  Starting with (I,J,K), swap 3 times.'
  print ''

  i = 1
  j = 202
  k = 3003003

  print '  %8d  %8d  %8d' % ( i, j, k )

  for l in range ( 0, 3 ):
    i, j, k = i4_swap3 ( i, j, k )
    print '  %8d  %8d  %8d' % ( i, j, k )
#
#  Terminate.
#
  print ''
  print 'I4_SWAP3_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_swap3_test ( )
  timestamp ( )
