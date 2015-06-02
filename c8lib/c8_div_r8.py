#!/usr/bin/env python

def c8_div_r8 ( c1, r2 ):

#*****************************************************************************80
#
## C8_DIV_R8 divides a C8 by an R8.
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
#    Input, complex C1, real R2, the values.
#
#    Output, complex VALUE, the function value.
#
  from c8_real import c8_real
  from c8_imag import c8_imag

  a = c8_real ( c1 ) / r2
  b = c8_imag ( c1 ) / r2

  value = a + b * 1j

  return value

def c8_div_r8_test ( ):

#*****************************************************************************80
#
## C8_DIV_R8_TEST tests C8_DIV_R8.
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
  from r8_uniform_01 import r8_uniform_01

  print ''
  print 'C8_DIV_R8_TEST'
  print '  C8_DIV_R8 divides a C8 by an R8.'
  print ''
  print '       C1=C8_UNIFORM_01          R2=R8_UNIFORM_01          C3=C8_DIV_R8(C1,RC2)      C4=C1/R2'
  print '     ---------------------     ---------------------     ---------------------     ---------------------'
  print ''

  seed = 123456789

  for i in range ( 0, 10 ):
    c1, seed = c8_uniform_01 ( seed )
    r2, seed = r8_uniform_01 ( seed )
    c3 = c8_div_r8 ( c1, r2 )
    c4 = c1 / r2
    print '  (%12f,%12f)   %12f               (%12f,%12f)  (%12f,%12f)' \
      % ( c1.real, c1.imag, r2, c3.real, c3.imag, c4.real, c4.imag )

  print ''
  print 'C8_DIV_R8_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  c8_div_r8_test ( )
  timestamp ( )

