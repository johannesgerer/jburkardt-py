#!/usr/bin/env python

def r8_mant ( x ):

#*****************************************************************************80
#
## R8_MANT computes the "mantissa" or "fraction part" of X.
#
#  Formula:
#
#    X = S * R * 2**L
#
#    S is +1 or -1,
#    R is a real value between 1.0 and 2.0,
#    L is an integer.
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
#    Input, real X, the number to be decomposed.
#
#    Output, integer S, the "sign" of the number.
#    S will be -1 if X is less than 0, and +1 if X is greater
#    than or equal to zero.
#
#    Output, real R, the mantissa of X.  R will be greater
#    than or equal to 1, and strictly less than 2.  The one
#    exception occurs if X is zero, in which case R will also
#    be zero.
#
#    Output, integer L, the integer part of the logarithm (base 2) of X.
#

#
#  Determine the sign.
#
  if ( x < 0.0 ):
    s = -1
  else:
    s = 1
#
#  Set R to the absolute value of X, and L to zero.
#  Then force R to lie between 1 and 2.
#
  if ( x < 0.0 ):
    r = -x
  else:
    r = x

  l = 0
#
#  Time to bail out if X is zero.
#
  if ( x == 0.0 ):
    return s, r, l

  while ( 2.0 <= r ):
    r = r / 2.0
    l = l + 1

  while ( r < 1.0 ):
    r = r * 2.0
    l = l - 1

  return s, r, l

def r8_mant_test ( ):

#*****************************************************************************80
#
## R8_MANT_TEST tests R8_MANT.
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
  from r8_mant import r8_mant

  x = -314.159

  print ''
  print 'R8_MANT_TEST'
  print '  R8_MANT decomposes a value.'
  print ''
  print '  Number to be decomposed:'
  print '  %g' % ( x )

  s, r, l = r8_mant ( x )

  print ''
  print '  R8_MANT: X = %d * %f * 2^ %d' % ( s, r, l )
#
#  Terminate.
#
  print ''
  print 'R8_MANT_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_mant_test ( )
  timestamp ( )
