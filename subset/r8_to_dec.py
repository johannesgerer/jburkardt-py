#! /usr/bin/env python
#
def r8_to_dec ( dval, dec_digit ):

#*****************************************************************************80
#
## R8_TO_DEC converts a real quantity to a decimal representation.
#
#  Discussion:
#
#    Given the real value DVAL, the routine computes integers
#    MANTISSA and EXPONENT so that it is approximately true that:
#
#      DVAL = MANTISSA * 10 ^ EXPONENT
#
#    In particular, only DEC_DIGIT digits of DVAL are used in constructing the
#    representation.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    25 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real DVAL, the value whose decimal representation
#    is desired.
#
#    Input, integer DEC_DIGIT, the number of decimal digits.
#
#    Output, integer MANTISSA, EXPONENT, the approximate decimal 
#    representation of DVAL.
#

#
#  Special cases.
#
  if ( dval == 0.0 ):
    mantissa = 0
    exponent = 0
    return mantissa, exponent
#
#  Factor DVAL = MANTISSA_DOUBLE * 10^EXPONENT
#
  mantissa_double = dval
  exponent = 0
#
#  Now normalize so that 
#  10^(DEC_DIGIT-1) <= ABS(MANTISSA_DOUBLE) < 10^(DEC_DIGIT)
#
  ten1 = 10.0 ** ( dec_digit - 1 )
  ten2 = 10.0 ** dec_digit

  while ( abs ( mantissa_double ) < ten1 ):
    mantissa_double = mantissa_double * 10.0
    exponent = exponent - 1

  while ( ten2 <= abs ( mantissa_double ) ):
    mantissa_double = mantissa_double / 10.0
    exponent = exponent + 1
#
#  MANTISSA is the integer part of MANTISSA_DOUBLE, rounded.
#
  mantissa = int ( mantissa_double )
#
#  Now divide out any factors of ten from MANTISSA.
#
  if ( mantissa != 0 ):
    while ( 10 * ( mantissa // 10 ) == mantissa ):
      mantissa = ( mantissa // 10 )
      exponent = exponent + 1

  return mantissa, exponent

def r8_to_dec_test ( ):

#*****************************************************************************80
#
## R8_TO_DEC tests R8_TO_DEC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 May 2015
#
#  Author:
#
#    John Burkardt
#
  from i4_uniform_ab import i4_uniform_ab
  from r8_uniform_01 import r8_uniform_01

  print ''
  print 'R8_TO_DEC_TEST'
  print '  R8_TO_DEC converts a real number to a decimal;'

  dec_digit = 5

  print ''
  print '  The number of decimal digits is %d' % ( dec_digit )

  seed = 123456789

  print ''
  print '        R   =>     A    * 10^B'
  print ''

  for i in range ( 0, 10 ):

    r, seed = r8_uniform_01 ( seed )
    e, seed = i4_uniform_ab ( 0, +10, seed )

    r = r * 10.0 ** e

    a, b = r8_to_dec ( r, dec_digit )

    print '  %12g  %6d  %6d' % ( r, a, b )
#
#  Terminate.
#
  print ''
  print 'R8_TO_DEC_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_to_dec_test ( )
  timestamp ( )

