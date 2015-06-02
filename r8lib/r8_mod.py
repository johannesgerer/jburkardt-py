#!/usr/bin/env python

def r8_mod ( x, y ):

#*****************************************************************************80
#
## R8_MOD returns the remainder of R8 division.
#
#  Formula:
#
#    If
#      REM = R8_MOD ( X, Y )
#      RMULT = ( X - REM ) / Y
#    then
#      X = Y * RMULT + REM
#    where REM has the same sign as X, and abs ( REM ) < Y.
#
#  Example:
#
#        X         Y     R8_MOD  R8_MOD Factorization
#
#      107        50       7      107 =  2 *  50 + 7
#      107       -50       7      107 = -2 * -50 + 7
#     -107        50      -7     -107 = -2 *  50 - 7
#     -107       -50      -7     -107 =  2 * -50 - 7
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    25 July 2014
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
#    Output, real VALUE, the remainder when X is divided by Y.
#
  from math import floor
  from sys import exit

  if ( y == 0.0 ):
    print ''
    print 'R8_MOD - Fatal error!'
    print '  R8_MOD ( X, Y ) called with Y = 0.'
    exit ( 'R8_MOD - Fatal error!' )

  value = x - floor ( x / y ) * y

  if ( x < 0.0 and 0.0 < value ):
    value = value - abs ( y )
  elif ( 0.0 < x and value < 0.0 ):
    value = value + abs ( y )

  return value

def r8_mod_test ( ):

#*****************************************************************************80
#
## R8_MOD_TEST tests R8_MOD.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 July 2014
#
#  Author:
#
#    John Burkardt
#
  from r8_uniform_ab import r8_uniform_ab

  test_num = 10

  print ''
  print 'R8_MOD_TEST'
  print '  R8_MOD returns the remainder after division.'
  print ''
  print '        X             Y             (X%Y)    R8_MOD(X,Y)'
  print ''

  x_lo = -10.0
  x_hi = +10.0

  seed = 123456789

  for test in range ( 0, test_num ):

    x, seed = r8_uniform_ab ( x_lo, x_hi, seed )
    y, seed = r8_uniform_ab ( x_lo, x_hi, seed )

    z1 = x % y
    z2 = r8_mod ( x, y )

    print '  %12f  %12f  %12f  %12f' % ( x, y, z1, z2 )
#
#  Terminate.
#
  print ''
  print 'R8_MOD_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_mod_test ( )
  timestamp ( )
