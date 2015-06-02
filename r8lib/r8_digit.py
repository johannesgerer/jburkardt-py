#!/usr/bin/env python

def r8_digit ( x, idigit ):

#*****************************************************************************80
#
## R8_DIGIT returns a particular decimal digit of an R8.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    03 June 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the number whose NDIG-th decimal digit
#    is desired.  If X is zero, all digits will be returned as 0.
#
#    Input, integer IDIGIT, the position of the desired decimal digit.
#    A value of 1 means the leading digit, a value of 2 the second digit
#    and so on.
#
#    Output, integer DIGIT, the value of the IDIGIT-th decimal digit of X.
#
  from math import floor

  if ( x == 0.0 ):
    digit = 0
    return digit

  if ( idigit <= 0 ):
    digit = 0
    return digit
#
#  Force X to lie between 1 and 10.
#
  x = abs ( x )

  while ( x < 1.0 ):
    x = x * 10.0

  while ( 10.0 <= x ):
    x = x / 10.0

  for i in range ( 0, idigit ):
    ival = floor ( x )
    x = ( x - ival ) * 10.0

  digit = ival

  return digit

def r8_digit_test ( ):

#*****************************************************************************80
#
## R8_DIGIT_TEST tests R8_DIGIT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 April 2009
#
#  Author:
#
#    John Burkardt
#
  maxdig = 20

  r8_pi = 3.141592653589793
  x = r8_pi

  print ''
  print 'R8_DIGIT_TEST'
  print '  R8_DIGIT extracts decimal digits.'
  print ''
  print '  Here, we get digits of %g' % ( x )
  print ''

  print ''
  
  for idigit in range ( -1, maxdig + 1 ):
    print '%3d' % ( idigit ),
  print ''

  print ''

  for idigit in range ( -2, maxdig + 1 ):
    digit = r8_digit ( x, idigit )
    print '%3d' % ( idigit ),
  print ''
#
#  Terminate.
#
  print ''
  print 'R8_DIGIT_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  r8_digit_test ( )
  timestamp ( )

