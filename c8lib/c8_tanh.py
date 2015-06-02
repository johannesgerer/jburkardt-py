#!/usr/bin/env python

def c8_tanh ( c ):

#*****************************************************************************80
#
## C8_TANH evaluates the hyperbolic tangent of a C8.
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

  value = ( c8_exp ( c ) - c8_exp ( - c ) ) / ( c8_exp ( c ) + c8_exp ( - c ) )

  return value

def c8_tanh_test ( ):

#*****************************************************************************80
#
## C8_TANH_TEST tests C8_TANH.
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
  from c8_atanh import c8_atanh
  from c8_uniform_01 import c8_uniform_01

  print ''
  print 'C8_TANH_TEST'
  print '  C8_TANH computes the tangent of a C8.'
  print ''
  print '       C1=C8_UNIFORM_01          C2=C8_TANH(C1)             C3=C8_ATANH(C2)'
  print '     ---------------------     ---------------------     ---------------------'
  print ''

  seed = 123456789

  for i in range ( 0, 10 ):
    c1, seed = c8_uniform_01 ( seed )
    c2 = c8_tanh ( c1 )
    c3 = c8_atanh ( c2 );
    print '  (%12f,%12f)  (%12f,%12f)  (%12f,%12f)' \
      % ( c1.real, c1.imag, c2.real, c2.imag, c3.real, c3.imag )

  print ''
  print 'C8_TANH_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  c8_tanh_test ( )
  timestamp ( )

