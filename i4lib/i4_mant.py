#!/usr/bin/env python

def i4_mant ( x ) :

#*****************************************************************************80
#
## I4_MANT computes the "mantissa" of an R8.
#
#  Discussion:
#
#    This routine computes the "mantissa" or "fraction part" of a real
#    number X, which it stores as a pair of integers, (J/K).
#
#    It also computes the sign, and the integer part of the logarithm
#    (base 2) of X.
#
#    On return:
#
#      X = S * (J/K) * 2^L
#
#    where
#
#      S is +1 or -1,
#      K is a power of 2,
#      1 <= (J/K) < 2,
#      L is an integer.
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
#  Parameters:
#
#    Input, real X, the number to be decomposed.
#
#    Output, integer S, the "sign" of the number.
#    S will be -1 if X is less than 0, and +1 if X is greater
#    than or equal to zero.
#
#    Output, integer J, the top part of the mantissa fraction.
#
#    Output, integer K, the bottom part of the mantissa
#    fraction.  K is a power of 2.
#
#    Output, integer L, the integer part of the logarithm (base 2) of X.
#

#
#  1: Handle the special case of 0.
#
  if ( x == 0.0 ):
    s = 1
    j = 0
    k = 1
    l = 0
    return s, j, k, l
#
#  2: Determine the sign S.
#
  if ( 0.0 < x ):
    s = 1
  else:
    s = -1
    x = -x
#
#  3: Force X to lie between 1 and 2, and compute the logarithm L.
#
  l = 0

  while ( 2.0 <= x ):
    x = x / 2.0
    l = l + 1

  while ( x < 1.0 ):
    x = x * 2.0
    l = l - 1
#
#  4: Now strip out the mantissa as J/K.
#
  j = 0
  k = 1

  while ( True ):

    j = 2 * j

    if ( 1.0 <= x ):
      j = j + 1
      x = x - 1.0

    if ( x == 0.0 ):
      break

    k = 2 * k
    x = x * 2.0

  return s, j, k, l

def i4_mant_test ( ) :

#*****************************************************************************80
#
## I4_MANT_TEST tests I4_MANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 May 2013
#
#  Author:
#
#    John Burkardt
#
  x = -314.159;

  print ''
  print 'I4_MANT_TEST'
  print '  I4_MANT decomposes an integer.'
  print ''
  print '  Number to be decomposed is X = %f' % ( x )

  [ s, j, k, l ] = i4_mant ( x )

  print ''
  print '  X = %d * ( %d / %d ) * 2 ^ (%d)' % ( s, j, k, l )
#
#  Terminate.
#
  print ''
  print 'I4_MANT_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_mant_test ( )
  timestamp ( )
