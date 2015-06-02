#!/usr/bin/env python

def c8_acosh ( c ):

#*****************************************************************************80
#
## C8_ACOSH evaluates the inverse hyperbolic cosine of a C8.
#
#  Discussion:
#
#    A C8 is a complex value.
#
#    Here we use the relationship:
#
#      C8_ACOSH ( Z ) = i * C8_ACOS ( Z ).
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
  from c8_acos import c8_acos

  value = 1j * c8_acos ( c )

  return value

def c8_acosh_test ( ):

#*****************************************************************************80
#
## C8_ACOSH_TEST tests C8_ACOSH.
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
  from c8_cosh import c8_cosh
  from c8_uniform_01 import c8_uniform_01

  print ''
  print 'C8_ACOSH_TEST'
  print '  C8_ACOSH computes the inverse hyperbolic cosine of a C8.'
  print ''
  print '       C1=C8_UNIFORM_01          C2=C8_ACOSH(C1)             C3=C8_COSH(C2)'
  print '     ---------------------     ---------------------     ---------------------'
  print ''

  seed = 123456789

  for i in range ( 0, 10 ):
    c1, seed = c8_uniform_01 ( seed )
    c2 = c8_acosh ( c1 )
    c3 = c8_cosh ( c2 );
    print '  (%12f,%12f)  (%12f,%12f)  (%12f,%12f)' \
      % ( c1.real, c1.imag, c2.real, c2.imag, c3.real, c3.imag )

  print ''
  print 'C8_ACOSH_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  c8_acosh_test ( )
  timestamp ( )

