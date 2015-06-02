#!/usr/bin/env python
#
def r8_big ( ):

#*****************************************************************************80
#
## R8_BIG returns a "big" real number.
#
#  Discussion:
#
#    The value returned by this function is NOT required to be the
#    maximum representable R8.
#    We simply want a "very large" but non-infinite number.
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
  value = 1.0E+30

  return value

def r8_big_test ( ):

#*****************************************************************************80
#
## R8_BIG_TEST tests R8_BIG.
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
  print 'R8_BIG_TEST'
  print '  R8_BIG returns a "big" R8;'
  print ''
  print '    R8_BIG =  %g' % ( r8_big ( ) )
#
#  Terminate.
#
  print ''
  print 'R8_BIG_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_big_test ( )
  timestamp ( )

