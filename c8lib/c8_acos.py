#!/usr/bin/env python

def c8_acos ( c ):

#*****************************************************************************80
#
## C8_ACOS evaluates the inverse cosine of a C8.
#
#  Discussion:
#
#    A C8 is a complex value.
#
#    Here we use the relationship:
#
#      C8_ACOS ( Z ) = pi/2 - C8_ASIN ( Z ).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 February 2015
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
  from c8_asin import c8_asin

  r8_pi = 3.141592653589793

  value = 0.5 * r8_pi - c8_asin ( c )

  return value

def c8_acos_test ( ):

#*****************************************************************************80
#
## C8_ACOS_TEST tests C8_ACOS.
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
  from c8_cos import c8_cos
  from c8_uniform_01 import c8_uniform_01

  print ''
  print 'C8_ACOS_TEST'
  print '  C8_ACOS computes the inverse cosine of a C8.'
  print ''
  print '       C1=C8_UNIFORM_01          C2=C8_ACOS(C1)             C3=C8_COS(C2)'
  print '     ---------------------     ---------------------     ---------------------'
  print ''

  seed = 123456789

  for i in range ( 0, 10 ):
    c1, seed = c8_uniform_01 ( seed )
    c2 = c8_acos ( c1 )
    c3 = c8_cos ( c2 );
    print '  (%12f,%12f)  (%12f,%12f)  (%12f,%12f)' \
      % ( c1.real, c1.imag, c2.real, c2.imag, c3.real, c3.imag )

  print ''
  print 'C8_ACOS_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  c8_acos_test ( )
  timestamp ( )

