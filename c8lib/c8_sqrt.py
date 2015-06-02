#!/usr/bin/env python

def c8_sqrt ( c ):

#*****************************************************************************80
#
## C8_SQRT returns the principal square root of a C8.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, complex C, the number whose square root is desired.
#
#    Output, complex VALUE, the square root of X.
#
  from c8_arg import c8_arg
  from c8_mag import c8_mag
  from math import cos
  from math import sin
  from math import sqrt

  argument = c8_arg ( c )
  magnitude = c8_mag ( c );

  value = sqrt ( magnitude ) \
    * complex ( cos ( argument / 2.0 ), sin ( argument / 2.0 ) )

  return value

def c8_sqrt_test ( ):

#*****************************************************************************80
#
## C8_SQRT_TEST tests C8_SQRT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    10 February 2015
#
#  Author:
#
#    John Burkardt
#
  from c8_uniform_01 import c8_uniform_01

  print ''
  print 'C8_SQRT_TEST'
  print '  C8_SQRT computes the square root of a C8.'
  print ''
  print '       C1=C8_UNIFORM_01          C2=C8_SQRT(C1)             C3=C2*C2'
  print '     ---------------------     ---------------------     ---------------------'
  print ''

  seed = 123456789

  for i in range ( 0, 10 ):
    c1, seed = c8_uniform_01 ( seed )
    c2 = c8_sqrt ( c1 )
    c3 = c2 * c2;
    print '  (%12f,%12f)  (%12f,%12f)  (%12f,%12f)' \
      % ( c1.real, c1.imag, c2.real, c2.imag, c3.real, c3.imag )

  print ''
  print 'C8_SQRT_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  c8_sqrt_test ( )
  timestamp ( )

