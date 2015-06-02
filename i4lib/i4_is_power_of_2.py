#!/usr/bin/env python

def i4_is_power_of_2 ( n ):

#*****************************************************************************80
#
## I4_IS_POWER_OF_2 reports whether an integer is a power of 2.
#
#  Discussion:
#
#    The powers of 2 are 1, 2, 4, 8, 16, and so on.
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
#    Input, integer N, the integer to be tested.
#
#    Output, boolean VALUE, is TRUE if N is a power of 2.
#
  from numpy import floor

  value = False

  if ( n <= 0 ):
    return value

  while ( n != 1 ):

    if ( ( n % 2 ) == 1 ):
      return value

    n = floor ( n / 2 )

  value = True

  return value

def i4_is_power_of_2_test ( ) :

#*****************************************************************************80
#
## I4_IS_POWER_OF_2_TEST tests I4_IS_POWER_OF_2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 May 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'I4_IS_POWER_OF_2_TEST'
  print '  I4_IS_POWER_OF_2 reports whether an I4 is a power of 2.'
  print ' '
  print '         I  I4_IS_POWER_OF_2(I)'
  print ' '

  for i in range ( -4, 26 ):
    j = i4_is_power_of_2 ( i )
    print '  %8d  %r' % ( i, j )
#
#  Terminate.
#
  print ''
  print 'I4_IS_POWER_OF_2_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_is_power_of_2_test ( )
  timestamp ( )
