#!/usr/bin/env python

def c8_to_polar ( c ):

#*****************************************************************************80
#
## C8_TO_POLAR converts a C8 to polar form.
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
#    Input, complex C, the value.
#
#    Output, real R, T, the polar form.
#
  from c8_arg import c8_arg
  from c8_mag import c8_mag

  r = c8_mag ( c )
  t = c8_arg ( c )

  return r, t

def c8_to_polar_test ( ):

#*****************************************************************************80
#
## C8_TO_POLAR_TEST tests C8_TO_POLAR.
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
  from polar_to_c8 import polar_to_c8

  print ''
  print 'C8_TO_POLAR_TEST'
  print '  C8_TO_POLAR computes the polar form of a C8.'
  print ''
  print '       C1=C8_UNIFORM_01       (R2,T2)=C8_TO_POLAR(C1)    C3=POLAR_TO_C8(R2,T2)'
  print '     ---------------------     ---------------------     ---------------------'
  print ''

  seed = 123456789

  for i in range ( 0, 10 ):
    c1, seed = c8_uniform_01 ( seed )
    r2, t2 = c8_to_polar ( c1 )
    c3 = polar_to_c8 ( r2, t2 )
    print '  (%12f,%12f)  (%12f,%12f)  (%12f,%12f)' % ( c1.real, c1.imag, r2, t2, c3.real, c3.imag )

  print ''
  print 'C8_TO_POLAR_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  c8_to_polar_test ( )
  timestamp ( )

