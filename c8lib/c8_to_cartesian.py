#!/usr/bin/env python

def c8_to_cartesian ( c ):

#*****************************************************************************80
#
## C8_TO_CARTESIAN converts a C8 to cartesian form.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, complex C, the value.
#
#    Output, real X, Y, the cartesian form.
#
  from c8_imag import c8_imag
  from c8_real import c8_real

  x = c8_real ( c )
  y = c8_imag ( c )

  return x, y

def c8_to_cartesian_test ( ):

#*****************************************************************************80
#
## C8_TO_CARTESIAN_TEST tests C8_TO_CARTESIAN.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    13 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from c8_uniform_01 import c8_uniform_01
  from cartesian_to_c8 import cartesian_to_c8

  print ''
  print 'C8_TO_CARTESIAN_TEST'
  print '  C8_TO_CARTESIAN computes the cartesian form of a C8.'
  print ''
  print '       C1=C8_UNIFORM_01       (X2,Y2)=C8_TO_CARTESIAN(C1)    C3=CARTESIAN_TO_C8(X2,Y2)'
  print '     ---------------------     ---------------------     ---------------------'
  print ''

  seed = 123456789

  for i in range ( 0, 10 ):
    c1, seed = c8_uniform_01 ( seed )
    x2, y2 = c8_to_cartesian ( c1 )
    c3 = cartesian_to_c8 ( x2, y2 )
    print '  (%12f,%12f)  (%12f,%12f)  (%12f,%12f)' % ( c1.real, c1.imag, x2, y2, c3.real, c3.imag )

  print ''
  print 'C8_TO_CARTESIAN_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  c8_to_cartesian_test ( )
  timestamp ( )

