#!/usr/bin/env python

def c8_sin ( c ):

#*****************************************************************************80
#
## C8_SIN evaluates the sine of a C8.
#
#  Discussion:
#
#    Here we use the relationship:
#
#      C8_SIN ( C ) = -i ( C8_EXP ( i * C ) - C8_EXP ( - i * C ) ) / 2
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, complex C, the argument.
#
#    Output, complex VALUE, the function value.
#
  from c8_exp import c8_exp

  value = - 1j * ( c8_exp ( 1j * c ) - c8_exp ( - 1j * c ) ) / 2.0

  return value

def c8_sin_test ( ):

#*****************************************************************************80
#
## C8_SIN_TEST tests C8_SIN.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    12 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from c8_asin import c8_asin
  from c8_uniform_01 import c8_uniform_01

  print ''
  print 'C8_SIN_TEST'
  print '  C8_SIN computes the sine of a C8.'
  print ''
  print '       C1=C8_UNIFORM_01          C2=C8_SIN(C1)             C3=C8_ASIN(C2)'
  print '     ---------------------     ---------------------     ---------------------'
  print ''

  seed = 123456789

  for i in range ( 0, 10 ):
    c1, seed = c8_uniform_01 ( seed )
    c2 = c8_sin ( c1 )
    c3 = c8_asin ( c2 );
    print '  (%12f,%12f)  (%12f,%12f)  (%12f,%12f)' \
      % ( c1.real, c1.imag, c2.real, c2.imag, c3.real, c3.imag )

  print ''
  print 'C8_SIN_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  c8_sin_test ( )
  timestamp ( )

