#!/usr/bin/env python

def r8_to_i4 ( xmin, xmax, x, ixmin, ixmax ):

#*****************************************************************************80
#
## R8_TO_I4 maps X in [XMIN, XMAX] to integer IX in [IXMIN, IXMAX].
#
#  Discussion:
#
#    IX := IXMIN + ( IXMAX - IXMIN ) * ( X - XMIN ) / ( XMAX - XMIN )
#    IX := min ( IX, max ( IXMIN, IXMAX ) )
#    IX := max ( IX, min ( IXMIN, IXMAX ) )
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
#    Input, real XMIN, XMAX, the range.  XMAX and
#    XMIN must not be equal.  It is not necessary that XMIN be less than XMAX.
#
#    Input, real X, the number to be converted.
#
#    Input, integer IXMIN, IXMAX, the allowed range of the output
#    variable.  IXMAX corresponds to XMAX, and IXMIN to XMIN.
#    It is not necessary that IXMIN be less than IXMAX.
#
#    Output, integer IX, the value in the range [IXMIN,IXMAX] that
#    corresponds to X.
#
  from math import floor
  from sys import exit

  if ( xmax == xmin ):
    print ''
    print 'R8_TO_I4 - Fatal error!'
    print '  XMAX = XMIN, making a zero divisor.'
    print '  XMAX = %g' % ( xmax )
    print '  XMIN = %g' % ( xmin ) 
    exit ( 'R8_TO_I4 - Fatal error!' )

  temp = ( ( xmax - x        ) * ixmin   \
         + (        x - xmin ) * ixmax ) \
         / ( xmax     - xmin )

  if ( 0.0 <= temp ):
    temp = temp + 0.5
  else:
    temp = temp - 0.5

  ix = floor ( temp )

  return ix


def r8_to_i4_test ( ):

#*****************************************************************************80
#
## R8_TO_I4_TEST tests R8_TO_I4.
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
  print ''
  print 'R8_TO_I4_TEST'
  print '  R8_TO_I4 finds an integer IX in [IXMIN,IXMAX]'
  print '  corresponding to X in [XMIN,XMAX].'

  xmin = 2.5
  x = 3.5
  xmax = 5.5

  ixmin = 10
  ixmax = 40

  ix = r8_to_i4 ( xmin, xmax, x, ixmin, ixmax )

  print ''
  print '   XMIN = %12f,  X = %12f,  XMAX = %12f' % (  xmin,  x,  xmax )
  print '  IXMIN = %12d, IX = %12d, IXMAX = %12d' % ( ixmin, ix, ixmax )
#
#  Terminate.
#
  print ''
  print 'R8_TO_I4_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_to_i4_test ( )
  timestamp ( )
