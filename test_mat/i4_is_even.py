#!/usr/bin/env python

def i4_is_even ( i ):

#*****************************************************************************80
#
## I4_IS_EVEN returns TRUE if I is even.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer I, the integer to be tested.
#
#    Output, boolean VALUE, is TRUE if I is even.
#
  value = ( ( i % 2 ) == 0 )

  return value

def i4_is_even_test ( ) :

#*****************************************************************************80
#
## I4_IS_EVEN_TEST tests I4_IS_EVEN.
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
  print 'I4_IS_EVEN_TEST'
  print '  I4_IS_EVEN reports whether an I4 is even.'
  print ' '
  print '         I  I4_IS_EVEN(I)'
  print ' '

  for i in range ( -2, 26 ):
    j = i4_is_even ( i )
    print '  %8d  %r' % ( i, j )

  print ''
  print 'I4_IS_EVEN_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_is_even_test ( )
  timestamp ( )
