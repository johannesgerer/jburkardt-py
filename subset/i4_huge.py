#!/usr/bin/env python

def i4_huge ( ):

#*****************************************************************************80
#
## I4_HUGE returns a "huge" I4.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    04 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, integer VALUE, a huge integer.
#
  value = 2147483647

  return value;

def i4_huge_test ( ) :

#*****************************************************************************80
#
## I4_HUGE_TEST tests I4_HUGE.
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
  print ''
  print 'I4_HUGE_TEST'
  print '  I4_HUGE returns a huge integer.'
  print ''
  i = i4_huge ( )
  print '  I4_HUGE() = %d' % ( i )
#
#  Terminate.
#
  print ''
  print 'I4_HUGE_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_huge_test ( )
  timestamp ( )

