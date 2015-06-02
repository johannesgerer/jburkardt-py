#!/usr/bin/env python
#
def r8_abs ( x ):

#*****************************************************************************80
#
## R8_ABS returns the absolute value of an R8.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the number whose absolute value is desired.
#
#    Output, real VALUE, the absolute value of X.
#
  if ( 0.0 <= x ):
    value = + x
  else:
    value = - x

  return value

def r8_abs_test ( ):

#*****************************************************************************80
#
## R8_ABS_TEST tests R8_ABS.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 May 2013
#
#  Author:
#
#    John Burkardt
#
  from r8_uniform_ab import r8_uniform_ab

  r8_lo = -5.0
  r8_hi = +5.0
  test_num = 10
  seed = 123456789

  print ''
  print 'R8_ABS_TEST'
  print '  R8_ABS returns the absolute value of an R8.'
  print ' '
  print '      X         R8_ABS(X)'
  print ' '

  for test in range ( 0, test_num ):
    [ r8, seed ] = r8_uniform_ab ( r8_lo, r8_hi, seed )
    r8_absolute = r8_abs ( r8 )
    print "  %10.6f  %10.6f" % ( r8, r8_absolute )
#
#  Terminate.
#
  print ''
  print 'R8_ABS_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_abs_test ( )
  timestamp ( )
