#!/usr/bin/env python

def r8_wrap ( r, rlo, rhi ):

#*****************************************************************************80
#
## R8_WRAP forces an R8 to lie between given limits by wrapping.
#
#  Discussion:
#
#    An R8 is a real value.
#
#  Example:
#
#    RLO = 4.0, RHI = 8.0
#
#     R  Value
#
#    -2     8
#    -1     4
#     0     5
#     1     6
#     2     7
#     3     8
#     4     4
#     5     5
#     6     6
#     7     7
#     8     8
#     9     4
#    10     5
#    11     6
#    12     7
#    13     8
#    14     4
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
#    Input, real R, a value.
#
#    Input, real RLO, RHI, the desired bounds.
#
#    Output, real R, a "wrapped" version of the value.
#
  from math import floor
#
#  Guarantee RLO2 < RHI2.
#
  rlo2 = min ( rlo, rhi )
  rhi2 = max ( rlo, rhi )
#
#  Find the width.
#
  rwide = rhi2 - rlo2
#
#  Add enough copies of (RHI2-RLO2) to R so that the
#  result ends up in the interval RLO2 - RHI2.
#
  if ( rwide == 0.0 ):
    value = rlo
  elif ( r < rlo2 ):
    n = floor ( ( rlo2 - r ) / rwide ) + 1
    value = r + n * rwide
    if ( value == rhi ):
      value = rlo
  else:
    n = floor ( ( r - rlo2 ) / rwide )
    value = r - n * rwide
    if ( value == rlo ):
      value = rhi

  return value

def r8_wrap_test ( ):

#*****************************************************************************80
#
## R8_WRAP_TEST tests R8_WRAP
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 July 2014
#
#  Author:
#
#    John Burkardt
#
  from r8_uniform_ab import r8_uniform_ab

  a = - 2.0
  b = 12.0
  rhi = 6.5
  rlo = 3.0
  seed = 123456789
  test_num = 20

  print ''
  print 'R8_WRAP_TEST'
  print '  R8_WRAP "wraps" an R8 to lie within an interval:'
  print ''
  print '  Wrapping interval is %f, %f' % ( rlo, rhi )
  print ''
  print '      R      R8_WRAP ( R )'
  print ''

  for test in range ( 0, test_num ):

    r, seed = r8_uniform_ab ( a, b, seed )
    r2 = r8_wrap ( r, rlo, rhi )
    print '  %14g  %14g' % ( r, r2 )
#
#  Terminate.
#
  print ''
  print 'R8_WRAP_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_wrap_test ( )
  timestamp ( )
