#!/usr/bin/env python

def c8_div ( c1, c2 ):

#*****************************************************************************80
#
## C8_DIV divides two C8's.
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
#    Input, complex C1, C2, the values.
#
#    Output, complex VALUE, the function value.
#
  from c8_real import c8_real
  from c8_imag import c8_imag

  a = c8_real ( c1 )
  b = c8_imag ( c1 )
  c = c8_real ( c2 )
  d = c8_imag ( c2 )

  e = c * c + d * d

  f = ( a * c + b * d ) / e
  g = ( b * c - a * d ) / e

  value = f + g * 1j

  return value

def c8_div_test ( ):

#*****************************************************************************80
#
## C8_DIV_TEST tests C8_DIV.
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
  from c8_uniform_01 import c8_uniform_01

  print ''
  print 'C8_DIV_TEST'
  print '  C8_DIV divides two C8s.'
  print ''
  print '       C1=C8_UNIFORM_01          C2=C8_UNIFORM_01          C3=C8_DIV(C1,C2)      C4=C1/C2'
  print '     ---------------------     ---------------------     ---------------------     ---------------------'
  print ''

  seed = 123456789

  for i in range ( 0, 10 ):
    c1, seed = c8_uniform_01 ( seed )
    c2, seed = c8_uniform_01 ( seed )
    c3 = c8_div ( c1, c2 )
    c4 = c1 / c2
    print '  (%12f,%12f)  (%12f,%12f)  (%12f,%12f)  (%12f,%12f)' \
      % ( c1.real, c1.imag, c2.real, c2.imag, c3.real, c3.imag, c4.real, c4.imag )

  print ''
  print 'C8_DIV_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  c8_div_test ( )
  timestamp ( )

