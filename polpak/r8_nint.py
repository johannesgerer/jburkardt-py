#!/usr/bin/env python

def r8_nint ( x ):

#*****************************************************************************80
#
## R8_NINT returns the nearest integer to an R8.
#
#  Example:
#
#        X        R8_NINT
#
#      1.3         1
#      1.4         1
#      1.5         1 or 2
#      1.6         2
#      0.0         0
#     -0.7        -1
#     -1.1        -1
#     -1.6        -2
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
#    Input, real X, the value.
#
#    Output, integer VALUE, the nearest integer to X.
#
  if ( x < 0.0 ):
    s = -1
  else:
    s = 1

  value = s * round ( abs ( x ) + 0.5 )

  return value

def r8_nint_test ( ):

#*****************************************************************************80
#
## R8_NINT_TEST tests R8_NINT
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

  seed = 123456789
  test_num = 10

  print ''
  print 'R8_NINT_TEST'
  print '  R8_NINT produces the nearest integer.'
  print ''
  print '      X      R8_NINT(X)'
  print ''

  b = -10.0
  c = +10.0

  for test  in range ( 0, test_num ):
    x, seed = r8_uniform_ab ( b, c, seed )
    print '  %10f  %6d' % ( x, r8_nint ( x ) )

  print ''
  print 'R8_NINT_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_nint_test ( )
  timestamp ( )
