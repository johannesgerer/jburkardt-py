#!/usr/bin/env python

def c8_atan ( c ):

#*****************************************************************************80
#
## C8_ATAN evaluates the inverse tangent of a C8.
#
#  Discussion:
#
#    Here we use the relationship:
#
#      C8_ATAN ( Z ) = ( i / 2 ) * log ( ( 1 - i * z ) / ( 1 + i * z ) )
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
  from c8_log import c8_log

  arg = ( 1.0 - 1j * c ) / ( 1.0 + 1j * c )

  value = 0.5 * 1j * c8_log ( arg )

  return value

def c8_atan_test ( ):

#*****************************************************************************80
#
## C8_ATAN_TEST tests C8_ATAN.
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
  from c8_tan import c8_tan
  from c8_uniform_01 import c8_uniform_01

  print ''
  print 'C8_ATAN_TEST'
  print '  C8_ATAN computes the inverse tangent of a C8.'
  print ''
  print '       C1=C8_UNIFORM_01          C2=C8_ATAN(C1)             C3=C8_TAN(C2)'
  print '     ---------------------     ---------------------     ---------------------'
  print ''

  seed = 123456789

  for i in range ( 0, 10 ):
    c1, seed = c8_uniform_01 ( seed )
    c2 = c8_atan ( c1 )
    c3 = c8_tan ( c2 );
    print '  (%12f,%12f)  (%12f,%12f)  (%12f,%12f)' \
      % ( c1.real, c1.imag, c2.real, c2.imag, c3.real, c3.imag )

  print ''
  print 'C8_ATAN_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  c8_atan_test ( )
  timestamp ( )

