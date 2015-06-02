#!/usr/bin/env python

def i4_is_odd ( i ):

#*****************************************************************************80
#
## I4_IS_ODD returns TRUE if I is odd.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer I, the integer to be tested.
#
#    Output, logical VALUE, is TRUE if I is odd.
#
  value = ( ( i % 2 ) == 1 )

  return value

def i4_is_odd_test ( ) :

#*****************************************************************************80
#
## I4_IS_ODD_TEST tests I4_IS_ODD.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 December 2014
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'I4_IS_ODD_TEST'
  print '  I4_IS_ODD reports whether an I4 is odd.'
  print ' '
  print '         I  I4_IS_ODD(I)'
  print ' '

  for i in range ( -2, 26 ):
    j = i4_is_odd ( i )
    print '  %8d  %r' % ( i, j )

  print ''
  print 'I4_IS_ODD_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_is_odd_test ( )
  timestamp ( )
