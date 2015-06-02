#!/usr/bin/env python

def c8_normal_01 ( seed ):

#*****************************************************************************80
#
## C8_NORMAL_01 returns a unit normally distributed complex number.
#
#  Discussion:
#
#    The value has mean 0 and standard deviation 1.
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
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, complex C, a sample of the PDF.
#
#    Output, integer SEED, a seed for the random number generator.
#
  import numpy as np
  from r8_uniform_01 import r8_uniform_01

  v1, seed = r8_uniform_01 ( seed )
  v2, seed = r8_uniform_01 ( seed )

  x = np.sqrt ( - 2.0 * np.log ( v1 ) ) * np.cos ( 2.0 * np.pi * v2 )
  y = np.sqrt ( - 2.0 * np.log ( v1 ) ) * np.sin ( 2.0 * np.pi * v2 )

  c = x + y * 1j

  return c, seed

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
#    13 February 2015
#
#  Author:
#
#    John Burkardt
#
  seed = 123456789

  print ''
  print 'C8_NORMAL_01_TEST'
  print '  C8_NORMAL_01 computes pseudonormal complex values.'

  print '';
  print '  The initial seed is %d' % ( seed )
  print ''

  for i in range ( 1, 11 ):
    [ c, seed ] = c8_normal_01 ( seed )
    print '  %6d  ( %f, %f )' % ( i, c.real, c.imag )

  print ''
  print 'C8_NORMAL_01_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  c8_normal_01_test ( )
  timestamp ( )

