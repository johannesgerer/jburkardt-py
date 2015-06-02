#!/usr/bin/env python

def r8_round2 ( nplace, x ):

#*****************************************************************************80
#
## R8_ROUND2 rounds a number to a specified number of binary digits.
#
#  Discussion:
#
#    Assume that the input quantity X has the form
#
#      X = S * J * 2^L
#
#    where S is plus or minus 1, L is an integer, and J is a binary
#    mantissa which is either exactly zero, or greater than or equal
#    to 0.5 and less than 1.0.
#
#    Then on return, XROUND will satisfy
#
#      XROUND = S * K * 2^L
#
#    where S and L are unchanged, and K is a binary mantissa which
#    agrees with J in the first NPLACE binary digits and is zero
#    thereafter.
#
#    If NPLACE is 0, XROUND will always be zero.
#
#    If NPLACE is 1, the mantissa of XROUND will be 0 or 0.5.
#
#    If NPLACE is 2, the mantissa of XROUND will be 0, 0.25, 0.50,
#    or 0.75.
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
#  Parameters:
#
#    Input, integer NPLACE, the number of binary digits to
#    preserve.  NPLACE should be 0 or positive.
#
#    Input, real X, the number to be decomposed.
#
#    Output, real XROUND, the rounded value of X.
#
  xround = 0.0
#
#  1: Handle the special case of 0.
#
  if ( x == 0.0 ):
    return xround

  if ( nplace <= 0 ):
    return xround
#
#  2: Determine the sign S.
#
  if ( 0.0 < x ):
    s = 1
    xtemp = x
  else:
    s = -1
    xtemp = -x
#
#  3: Force XTEMP to lie between 1 and 2, and compute the
#  logarithm L.
#
  l = 0

  while ( 2.0 <= xtemp ):
    xtemp = xtemp / 2.0
    l = l + 1

  while ( xtemp < 1.0 ):
    xtemp = xtemp * 2.0
    l = l - 1
#
#  4: Strip out the digits of the mantissa as XMANT, and decrease L.
#
  xmant = 0.0
  iplace = 0

  while ( True ):

    xmant = 2.0 * xmant

    if ( 1.0 <= xtemp ):
      xmant = xmant + 1.0
      xtemp = xtemp - 1.0

    iplace = iplace + 1

    if ( xtemp == 0.0 or nplace <= iplace ):
      xround = s * xmant * 2.0 ** l
      break

    l = l - 1
    xtemp = xtemp * 2.0

  return xround

def r8_round2_test ( ):

#*****************************************************************************80
#
## R8_ROUND2_TEST tests R8_ROUND2.
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
  from math import pi
  from r8_round2 import r8_round2

  x = pi

  print ''
  print 'R8_ROUND2_TEST'
  print '  R8_ROUND2 rounds a number to a'
  print '  specified number of base 2 digits.'
  print ''
  print '  Test effect on PI:'
  print '  X = %f' % ( x )
  print ''
  print '  NPLACE  XROUND'
  print ''

  for i in range ( 0, 21 ):
    nplace = i
    xround = r8_round2 ( nplace, x )
    print '  %8d  %f' % ( i, xround )
#
#  Terminate.
#
  print ''
  print 'R8_ROUND2_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_round2_test ( )
  timestamp ( )
