#!/usr/bin/env python

def r8_huge ( ):

#*****************************************************************************80
#
## R8_HUGE returns a "huge" real number.
#
#  Discussion:
#
#    The value returned by this function is intended to be the largest
#    representable real value.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 September 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real VALUE, a huge number.
#
  value = 1.79769313486231571E+308

  return value

def r8_huge_test ( ):

#*****************************************************************************80
#
## R8_HUGE_TEST tests R8_HUGE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 September 2014
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'R8_HUGE_TEST'
  print '  R8_HUGE returns a "huge" R8;'
  print ''
  print '    R8_HUGE = %g' % ( r8_huge ( ) )

  return

  print ''
  print 'R8_HUGE_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  r8_huge_test ( )
  timestamp ( )
