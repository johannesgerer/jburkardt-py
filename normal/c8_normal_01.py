#!/usr/bin/env python

def c8_normal_01 ( seed ):

#*****************************************************************************80
#
## C8_NORMAL_01 returns a unit pseudonormal C8.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real VALUE, a normally distributed
#    random value.
#
#    Output, integer SEED, an updated seed for the random
#    number generator.
#
  import numpy as np
  from r8_uniform_01 import r8_uniform_01

  v1, seed = r8_uniform_01 ( seed )
  v2, seed = r8_uniform_01 ( seed )

  x_r = np.sqrt ( - 2.0 * np.log ( v1 ) ) * np.cos ( 2.0 * np.pi * v2 )
  x_c = np.sqrt ( - 2.0 * np.log ( v1 ) ) * np.sin ( 2.0 * np.pi * v2 )

  value = complex ( x_r, x_c )

  return value, seed

def c8_normal_01_test ( ):

#*****************************************************************************80
#
## C8_NORMAL_01_TEST tests C8_NORMAL_01.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 March 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'C8_NORMAL_01_TEST'
  print '  C8_NORMAL_01 computes complex pseudonormal values with'
  print '  mean 0.0 and standard deviation 1.0.'

  seed = 123456789

  print ''
  print '  SEED = %d' % ( seed )
  print ''
  for i in range ( 0, 10 ):
    r, seed = c8_normal_01 ( seed )
    print '  %2d  (%14g, %14g)' % ( i, r.real, r.imag )

  print ''
  print 'C8_NORMAL_01_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  c8_normal_01_test ( )
  timestamp ( )
