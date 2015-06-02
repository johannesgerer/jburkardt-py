#!/usr/bin/env python
#
def r8_acosh ( x ):

#*****************************************************************************80
#
## R8_ACOSH evaluates the arc-hyperbolic cosine of an R8 argument.
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
#    Original FORTRAN77 version by Wayne Fullerton.
#    Python version by John Burkardt.
#
#  Reference:
#
#    Wayne Fullerton,
#    Portable Special Function Routines,
#    in Portability of Numerical Software,
#    edited by Wayne Cowell,
#    Lecture Notes in Computer Science, Volume 57,
#    Springer 1977,
#    ISBN: 978-3-540-08446-4,
#    LC: QA297.W65.
#
#  Parameters:
#
#    Input, real X, the argument.
#
#    Output, real VALUE, the arc-hyperbolic cosine of X.
#
  from math import log
  from math import sqrt
  from sys import exit

  if ( x < 1.0 ):
    print ''
    print 'R8_ACOSH - Fatal error!'
    print '  X < 1.0'
    exit ( 'R8_ACOSH - Fatal error!' )

  r8_tiny = 1.0E-30
  xmax = 1.0 / sqrt ( r8_tiny )

  if ( x < xmax ):
    value = log ( x + sqrt ( x * x - 1.0 ) )
  else:
    dln2 = 0.69314718055994530941723212145818
    value = dln2 + log ( x )

  return value

def r8_acosh_test ( ):

#*****************************************************************************80
#
## R8_ACOSH_TEST tests R8_ACOSH.
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
  from math import cosh

  print ''
  print 'R8_ACOSH_TEST'
  print '  R8_ACOSH computes the arc-hyperbolic-cosine of an angle.'
  print ''
  print '       X            A=R8_ACOSH(X)    COSH(A)'
  print ''

  for test in range ( 0, 9 ):

    x = 1.0 + ( test ) / 2.0
    a = r8_acosh ( x )
    x2 = cosh ( a )

    print '  %14.6g  %14.6g  %14.6g' % ( x, a, x2 )
#
#  Terminate.
#
  print ''
  print 'R8_ACOSH_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_acosh_test ( )
  timestamp ( )
