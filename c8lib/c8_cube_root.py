#!/usr/bin/env python

def c8_cube_root ( c ):

#*****************************************************************************80
#
## C8_CUBE_ROOT returns the principal square root of a C8.
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
#    Input, complex C, the number whose square root is desired.
#
#    Output, complex VALUE, the square root of X.
#
  import numpy as np
  from c8_arg import c8_arg
  from c8_mag import c8_mag

  arg = c8_arg ( c )
  mag = c8_mag ( c );

  mag = mag ** ( 1.0 / 3.0 )
  arg = arg / 3.0
  value = mag * complex ( np.cos ( arg ), np.sin ( arg ) )

  return value

def c8_cube_root_test ( ):

#*****************************************************************************80
#
## C8_CUBE_ROOT_TEST tests C8_CUBE_ROOT.
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
  from c8_uniform_01 import c8_uniform_01

  print ''
  print 'C8_CUBE_ROOT_TEST'
  print '  C8_CUBE_ROOT computes the cube root of a C8.'
  print ''
  print '       C1=C8_UNIFORM_01          C2=C8_CUBE_ROOT(C1)             C3=C2*C2*C2'
  print '     ---------------------     ---------------------     ---------------------'
  print ''

  seed = 123456789

  for i in range ( 0, 10 ):
    c1, seed = c8_uniform_01 ( seed )
    c2 = c8_cube_root ( c1 )
    c3 = c2 * c2 * c2;
    print '  (%12f,%12f)  (%12f,%12f)  (%12f,%12f)' \
      % ( c1.real, c1.imag, c2.real, c2.imag, c3.real, c3.imag )

  print ''
  print 'C8_CUBE_ROOT_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  c8_cube_root_test ( )
  timestamp ( )

