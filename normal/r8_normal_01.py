#!/usr/bin/env python

def r8_normal_01 ( seed ):

#*****************************************************************************80
#
## R8_NORMAL_01 returns a unit pseudonormal R8.
#
#  Discussion:
#
#    The standard normal probability distribution function (PDF) has
#    mean 0 and standard deviation 1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 March 2015
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

  r1, seed = r8_uniform_01 ( seed )
  r2, seed = r8_uniform_01 ( seed )
  value = np.sqrt ( - 2.0 * np.log ( r1 ) ) * np.cos ( 2.0 * np.pi * r2 )

  return value, seed

def r8_normal_01_test ( ):

#*****************************************************************************80
#
## R8_NORMAL_01_TEST tests R8_NORMAL_01.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 March 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'R8_NORMAL_01_TEST'
  print '  R8_NORMAL_01 computes pseudonormal values with'
  print '  mean 0.0 and standard deviation 1.0.'

  seed = 123456789

  print ''
  print '  SEED = %d' % ( seed )
  print ''
  for i in range ( 0, 10 ):
    r, seed = r8_normal_01 ( seed )
    print '  %2d  %14f' % ( i, r )

  print ''
  print 'R8_NORMAL_01_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_normal_01_test ( )
  timestamp ( )
