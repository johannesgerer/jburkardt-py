#!/usr/bin/env python

def c8_tan ( c ):

#*****************************************************************************80
#
## C8_TAN evaluates the tangent of a C8.
#
#  Discussion:
#
#    We use the relationship:
#
#      C8_TAN ( C ) = - i * ( C8_EXP ( i * C ) - C8_EXP ( - i * C ) ) 
#                         / ( C8_EXP ( I * C ) + C8_EXP ( - i * C ) )
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

  value =  - 1j * ( c8_exp ( 1j * c ) - c8_exp ( - 1j * c ) ) \
     /            ( c8_exp ( 1j * c ) + c8_exp ( - 1j * c ) )

  return value

def c8_tan_test ( ):

#*****************************************************************************80
#
## C8_TAN_TEST tests C8_TAN.
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
  from c8_atan import c8_atan
  from c8_uniform_01 import c8_uniform_01

  print ''
  print 'C8_TAN_TEST'
  print '  C8_TAN computes the tangent of a C8.'
  print ''
  print '       C1=C8_UNIFORM_01          C2=C8_TAN(C1)             C3=C8_ATAN(C2)'
  print '     ---------------------     ---------------------     ---------------------'
  print ''

  seed = 123456789

  for i in range ( 0, 10 ):
    c1, seed = c8_uniform_01 ( seed )
    c2 = c8_tan ( c1 )
    c3 = c8_atan ( c2 );
    print '  (%12f,%12f)  (%12f,%12f)  (%12f,%12f)' \
      % ( c1.real, c1.imag, c2.real, c2.imag, c3.real, c3.imag )

  print ''
  print 'C8_TAN_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  c8_tan_test ( )
  timestamp ( )

