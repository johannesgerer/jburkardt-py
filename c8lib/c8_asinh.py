#!/usr/bin/env python

def c8_asinh ( c ):

#*****************************************************************************80
#
## C8_ASINH evaluates the inverse hyperbolic sine of a C8.
#
#  Discussion:
#
#    Here we use the relationship:
#
#      C8_ASINH ( Z ) = - i * C8_ASIN ( i * Z ).
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

  value = - 1j * c8_asin ( 1j * c )

  return value

def c8_asinh_test ( ):

#*****************************************************************************80
#
## C8_ASINH_TEST tests C8_ASINH.
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
  import numpy as np
  from c8_uniform_01 import c8_uniform_01

  print ''
  print 'C8_ASINH_TEST'
  print '  C8_ASINH computes the inverse sine of a C8.'
  print ''
  print '       C1=C8_UNIFORM_01          C2=C8_ASINH(C1)            C3=SINH(C2)'
  print '     ---------------------     ---------------------     ---------------------'
  print ''

  seed = 123456789

  for i in range ( 0, 10 ):
    c1, seed = c8_uniform_01 ( seed )
    c2 = c8_asinh ( c1 )
    c3 = np.sinh ( c2 );
    print '  (%12f,%12f)  (%12f,%12f)  (%12f,%12f)' \
      % ( c1.real, c1.imag, c2.real, c2.imag, c3.real, c3.imag )

  print ''
  print 'C8_ASINH_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  c8_asinh_test ( )
  timestamp ( )

