#!/usr/bin/env python

def c8_sinh ( c ):

#*****************************************************************************80
#
## C8_SINH evaluates the hyperbolic sine of a C8.
#
#  Discussion:
#
#    Here we use the relationship:
#
#      C8_SINH ( C ) = ( C8_EXP ( C ) - C8_EXP ( - C ) ) / 2
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

  value =  ( c8_exp ( c ) - c8_exp ( - c ) ) / 2.0

  return value

def c8_sinh_test ( ):

#*****************************************************************************80
#
## C8_SINH_TEST tests C8_SINH.
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
  from c8_asinh import c8_asinh
  from c8_uniform_01 import c8_uniform_01

  print ''
  print 'C8_SINH_TEST'
  print '  C8_SINH computes the hyperbolic sine of a C8.'
  print ''
  print '       C1=C8_UNIFORM_01          C2=C8_SINH(C1)             C3=C8_ASINH(C2)'
  print '     ---------------------     ---------------------     ---------------------'
  print ''

  seed = 123456789

  for i in range ( 0, 10 ):
    c1, seed = c8_uniform_01 ( seed )
    c2 = c8_sinh ( c1 )
    c3 = c8_asinh ( c2 );
    print '  (%12f,%12f)  (%12f,%12f)  (%12f,%12f)' \
      % ( c1.real, c1.imag, c2.real, c2.imag, c3.real, c3.imag )

  print ''
  print 'C8_SINH_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  c8_sinh_test ( )
  timestamp ( )

