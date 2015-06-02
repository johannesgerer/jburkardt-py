#!/usr/bin/env python

def r8_modp ( x, y ):

#*****************************************************************************80
#
## R8_MODP returns the nonnegative remainder of real division.
#
#  Discussion:
#
#    If
#      REM = R8_MODP ( X, Y )
#      RMULT = ( X - REM ) / Y
#    then
#      X = Y * RMULT + REM
#    where REM is always nonnegative.
#
#    The MOD function computes a result with the same sign as the
#    quantity being divided.  Thus, suppose you had an angle A,
#    and you wanted to ensure that it was between 0 and 360.
#    Then mod(A,360.0) would do, if A was positive, but if A
#    was negative, your result would be between -360 and 0.
#
#    On the other hand, R8_MODP(A,360.0) is between 0 and 360, always.
#
#  Example:
#
#        I         J     MOD R8_MODP  R8_MODP Factorization
#
#      107        50       7       7    107 =  2 *  50 + 7
#      107       -50       7       7    107 = -2 * -50 + 7
#     -107        50      -7      43   -107 = -3 *  50 + 43
#     -107       -50      -7      43   -107 =  3 * -50 + 43
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    01 June 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the number to be divided.
#
#    Input, real Y, the number that divides X.
#
#    Output, real VALUE, the nonnegative remainder when X is divided by Y.
#
  from sys import exit

  if ( y == 0.0 ):
    print ''
    print 'R8_MODP - Fatal error!'
    print '  R8_MODP ( X, Y ) called with Y = %f' % ( y )
    exit ( 'R8_MODP - Fatal error!' )

  value = ( x % y )

  if ( value < 0.0 ):
    value = value + abs ( y )

  return value

def r8_modp_test ( ):

#*****************************************************************************80
#
## R8_MODP_TEST tests R8_MODP.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 June 2013
#
#  Author:
#
#    John Burkardt
#
  from r8_uniform_ab import r8_uniform_ab

  test_num = 10

  print ''
  print 'R8_MODP_TEST'
  print '  R8_MODP returns the remainder after division.'
  print '  Unlike the MATLAB MOD, R8_MODP ( X, Y ) is positive.'
  print ''
  print '      X       Y      MOD(X,Y)  R8_MODP(X,Y)'
  print ''

  x_lo = -10.0
  x_hi = +10.0

  seed = 123456789

  for test in range ( 0, test_num ):

    [ x, seed ] = r8_uniform_ab ( x_lo, x_hi, seed )
    [ y, seed ] = r8_uniform_ab ( x_lo, x_hi, seed )

    z1 = ( x % y )
    z2 = r8_modp ( x, y )

    print '  %12f  %12f  %12f  %12f' % ( x, y, z1, z2 )
#
#  Terminate.
#
  print ''
  print 'R8_MODP_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_modp_test ( )
  timestamp ( )
