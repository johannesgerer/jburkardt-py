#!/usr/bin/env python

def r8_beta ( x, y ):

#*****************************************************************************80
#
## R8_BETA returns the value of the Beta function.
#
#  Complaint:
#
#    Because of the MISERABLE local installation of Python, the gamma
#    function is currently not accessible...
#
#  Discussion:
#
#    The formula is
#
#      BETA(X,Y) = ( GAMMA(X) * GAMMA(Y) ) / GAMMA(X+Y)
#
#    Both X and Y must be greater than 0.
#
#  Properties:
#
#    BETA(X,Y) = BETA(Y,X).
#    BETA(X,Y) = Integral ( 0 <= T <= 1 ) T^(X-1) (1-T)^(Y-1) dT.
#    BETA(X,Y) = GAMMA(X) * GAMMA(Y) / GAMMA(X+Y)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 January 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, Y, the two parameters that define the Beta function.
#    X and Y must be greater than 0.
#
#    Output, real VALUE, the value of the Beta function.
#
  from r8_gamma import r8_gamma
  from sys import exit

  if ( x <= 0.0 or y <= 0.0 ):
    print ''
    print 'R8_BETA - Fatal error!'
    print '  Both X and Y must be greater than 0.'
    exit ( 'R8_BETA - Fatal error!' )

  value = r8_gamma ( x ) * r8_gamma ( y ) / r8_gamma ( x + y )

  return value

def r8_beta_test ( ):

#*****************************************************************************80
#
## R8_BETA_TEST demonstrates the use of R8_BETA.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 January 2015
#
#  Author:
#
#    John Burkardt
#
  from beta_values import beta_values

  print ''
  print 'R8_BETA_TEST:'
  print '  R8_BETA evaluates the Beta function.'
  print ''
  print '         X         Y                 BETA(X,Y)            R8_BETA(X,Y)'
  print ''

  n_data = 0

  while ( True ):

    n_data, x, y, fx1 = beta_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_beta ( x, y )

    print '  %8.4g  %8.4g  %24.16g  %24.16g' % ( x, y, fx1, fx2 )

  print ''
  print 'R8_BETA_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  r8_beta_test ( )
  timestamp ( )
