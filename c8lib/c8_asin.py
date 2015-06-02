#!/usr/bin/env python

def c8_asin ( c ):

#*****************************************************************************80
#
## C8_ASIN evaluates the inverse sine of a C8.
#
#  Discussion:
#
#    A C8 is a complex value.
#
#    Here we use the relationship:
#
#      C8_ASIN ( Z ) = - i * log ( i * z + sqrt ( 1 - z * z ) )
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
  import numpy as np

  value = - 1j * np.log ( 1j * c + np.sqrt ( 1.0 - c * c ) )

  return value

def c8_asin_test ( ):

#*****************************************************************************80
#
## C8_ASIN_TEST tests C8_ASIN.
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
  from c8_sin import c8_sin
  from c8_uniform_01 import c8_uniform_01

  print ''
  print 'C8_ASIN_TEST'
  print '  C8_ASIN computes the inverse sine of a C8.'
  print ''
  print '       C1=C8_UNIFORM_01          C2=C8_ASIN(C1)             C3=C8_SIN(C2)'
  print '     ---------------------     ---------------------     ---------------------'
  print ''

  seed = 123456789

  for i in range ( 0, 10 ):
    c1, seed = c8_uniform_01 ( seed )
    c2 = c8_asin ( c1 )
    c3 = c8_sin ( c2 );
    print '  (%12f,%12f)  (%12f,%12f)  (%12f,%12f)' \
      % ( c1.real, c1.imag, c2.real, c2.imag, c3.real, c3.imag )

  print ''
  print 'C8_ASIN_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  c8_asin_test ( )
  timestamp ( )

