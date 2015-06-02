#!/usr/bin/env python
#
def r8_roundb ( ibase, nplace, x ):

#*****************************************************************************80
#
## R8_ROUNDB rounds a number to a given number of digits in a given base.
#
#  Discussion:
#
#    The code does not seem to do a good job of rounding when
#    the base is negative!
#
#    Assume that the input quantity X has the form
#
#      X = S * J * IBASE^L
#
#    where S is plus or minus 1, L is an integer, and J is a
#    mantissa base IBASE which is either exactly zero, or greater
#    than or equal to (1/IBASE) and less than 1.0.
#
#    Then on return, XROUND will satisfy
#
#      XROUND = S * K * IBASE^L
#
#    where S and L are unchanged, and K is a mantissa base IBASE
#    which agrees with J in the first NPLACE digits and is zero
#    thereafter.
#
#    Note that because of rounding, for most bases, most numbers
#    with a fractional quantities cannot be stored exactly in the
#    computer, and hence will have trailing "bogus" digits.
#
#    If NPLACE is 0, XROUND will always be zero.
#
#    If NPLACE is 1, the mantissa of XROUND will be 0,
#    1/IBASE, 2/IBASE, ..., (IBASE-1)/IBASE.
#
#    If NPLACE is 2, the mantissa of XROUND will be 0,
#    IBASE/IBASE^2, (IBASE+1)/IBASE^2, ...,
#    IBASE^2-2/IBASE^2, IBASE^2-1/IBASE^2.
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
#    Input, integer IBASE, the base of the arithmetic.
#    IBASE must not be zero.  Theoretically, IBASE may be negative.
#
#    Input, integer NPLACE, the number of digits base IBASE to
#    preserve.  NPLACE should be 0 or positive.
#
#    Input, real X, the number to be decomposed.
#
#    Output, real XROUND, the rounded value of X.
#
  from math import floor
  from sys import exit

  xround = 0.0
#
#  0: Error checks.
#
  if ( ibase == 0 ):
    print ''
    print 'R8_ROUNDB - Fatal error!'
    print '  The base IBASE cannot be zero.'
    exit ( 'R8_ROUNDB - Fatal error!' )
#
#  1: Handle the special case of 0.
#
  if ( x == 0.0 ):
    return xround

  if ( nplace <= 0 ):
    return xround
#
#  2: Determine the sign IS.
#
  if ( 0.0 < x ):
    s = 1
    xtemp = x
  else:
    s = -1
    xtemp = -x
#
#  3: Force XTEMP to lie between 1 and ABS(IBASE), and compute the
#  logarithm L.
#
  l = 0

  while ( abs ( ibase ) <= abs ( xtemp ) ):

    xtemp = xtemp / ibase

    if ( xtemp < 0.0 ):
      s = - s
      xtemp = -xtemp

    l = l + 1

  while ( abs ( xtemp ) < 1.0 ):

    xtemp = xtemp * ibase

    if ( xtemp < 0.0 ):
      s = - s
      xtemp = -xtemp

    l = l - 1
#
#  4: Now strip out the digits of the mantissa as XMANT, and
#  decrease L.
#
  xmant = 0.0
  iplace = 0
  js = s

  while ( True ):

    xmant = ibase * xmant

    if ( xmant < 0.0 ):
      js = - js
      xmant = -xmant

    if ( 1.0 <= xtemp ):
      xmant = xmant + floor ( xtemp )
      xtemp = xtemp - floor ( xtemp )

    iplace = iplace + 1

    if ( xtemp == 0.0 or nplace <= iplace ):
      xround = js * xmant * ibase ** l
      break

    l = l - 1
    xtemp = xtemp * ibase

    if ( xtemp < 0.0 ):
      s = -s
      xtemp = -xtemp

  return xround

def r8_roundb_test ( ):

#*****************************************************************************80
#
## R8_ROUNDB_TEST tests R8_ROUNDB.
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

  base = 3
  x = pi

  print ''
  print 'R8_ROUNDB_TEST'
  print '  R8_ROUNDB rounds a number to a'
  print '  specified number of base BASE digits.'
  print ''
  print '  Here, we will use BASE = %d' % ( base )
  print ''
  print '  Test effect on PI:'
  print '  X = %f' % ( x )
  print ''
  print '  NPLACE  XROUND'
  print ''

  for i in range ( 0, 21 ):
    nplace = i
    xround = r8_roundb ( base, nplace, x )
    print '  %8d  %f' % ( i, xround )

  print ''
  print '  Try with a negative base:'
  x = 121.0
  base = -3
  nplace = 3
  print ''
  print '  Input quantity is X = %f' % ( x )
  print '  to be rounded in base %d' % ( base )

  for nplace in range ( 1, 6 ):

    xround = r8_roundb ( base, nplace, x )

    print ''
    print '  Output value to %d places is %f' % ( nplace, xround )
#
#  Terminate.
#
  print ''
  print 'R8_ROUNDB_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_roundb_test ( )
  timestamp ( ) 
