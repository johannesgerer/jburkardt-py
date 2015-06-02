#!/usr/bin/env python

def r8_walsh_1d ( x, digit ):

#*****************************************************************************80
#
## R8_WALSH_1D evaluates the Walsh function.
#
#  Discussion:
#
#    Consider the binary representation of X, and number the digits
#    in descending order, from leading to lowest, with the units digit
#    being numbered 0.
#
#    The Walsh function W(J)(X) is equal to the J-th binary digit of X.
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
#    Input, real X, the argument of the Walsh function.
#
#    Input, integer DIGIT, the index of the Walsh function.
#
#    Output, real VALUE, the value of the Walsh function.
#
  from math import floor
#
#  Hide the effect of the sign of X.
#
  x = abs ( x )
#
#  If DIGIT is positive, divide by 2 DIGIT times.
#  If DIGIT is negative, multiply by 2 (-DIGIT) times.
#
  x = x / 2.0 ** digit
#
#  Make it an integer.
#  Because it's positive, and we're using INT, we don't change the
#  units digit.
#
  n = floor ( x )
#
#  Is the units digit odd or even?
#
  if ( ( n % 2 ) == 0 ):
    value = 0.0
  else:
    value = 1.0

  return value

def r8_walsh_1d_test ( ):

#*****************************************************************************80
#
## R8_WALSH_1D_TEST tests R8_WALSH_1D
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
  from r8_walsh_1d import r8_walsh_1d

  print ''
  print 'R8_WALSH_1D_TEST'
  print '  R8_WALSH_1D evaluates 1D Walsh functions:'
  print ''
  print '  X  W(+2) W(+1) W(0) W(-1) W(-2) W(-3)'
  print ''

  for i in range ( 0, 33 ):

    x = i / 4.0

    wp2 = r8_walsh_1d ( x,  2 )
    wp1 = r8_walsh_1d ( x,  1 )
    w0  = r8_walsh_1d ( x,  0 )
    wm1 = r8_walsh_1d ( x, -1 )
    wm2 = r8_walsh_1d ( x, -2 )
    wm3 = r8_walsh_1d ( x, -3 )

    print '  %10f  %4f  %4f  %4f  %4f  %4f  %4f' \
      % ( x, wp2, wp1, w0, wm1, wm2, wm3 )
#
#  Terminate.
#
  print ''
  print 'R8_WALSH_1D_TEST'
  print '  Normal end of execution'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_walsh_1d_test ( )
  timestamp ( )
