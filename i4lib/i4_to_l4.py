#!/usr/bin/env python

def i4_to_l4 ( i4 ):

#*****************************************************************************80
#
## I4_TO_L4 converts an I4 to an L4.
#
#  Discussion:
#
#    An I4 is an integer value.
#    An L4 is a boolean value.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer I4, an integer.
#
#    Output, boolean I4_TO_L4, the logical value of I4.
#
  value = ( i4 != 0 )

  return value

def i4_to_l4_test ( ):

#*****************************************************************************80
#
## I4_TO_L4_TEST tests I4_TO_L4. 
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
  print 'I4_TO_L4_TEST'
  print '  I4_TO_L4 converts an I4 to an L4.'
  print ''
  print '  I4   L4'
  print ''

  for i4 in range ( -5, +6 ):

    l4 = i4_to_l4 ( i4 )
    print '  %2d  %s' % ( i4, l4 )
#
#  Terminate.
#
  print ''
  print 'I4_TO_L4_TEST'
  print '  Normal end of execution.'

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_to_l4_test ( )
  timestamp ( )
