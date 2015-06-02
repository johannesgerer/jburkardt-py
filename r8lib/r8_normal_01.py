#!/usr/bin/env python

def r8_normal_01 ( seed ):

#*****************************************************************************80
#
## R8_NORMAL_01 samples the standard normal probability distribution.
#
#  Discussion:
#
#    The standard normal probability distribution function (PDF) has
#    mean 0 and standard deviation 1.
#
#    The Box-Muller method is used.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    25 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real X, a sample of the standard normal PDF.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  from math import cos
  from math import log
  from math import sqrt
  from r8_uniform_01 import r8_uniform_01

  r8_pi = 3.141592653589793

  r1, seed = r8_uniform_01 ( seed )
  r2, seed = r8_uniform_01 ( seed )

  x = sqrt ( - 2.0 * log ( r1 ) ) * cos ( 2.0 * r8_pi * r2 )

  return x, seed

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
#    26 July 2014
#
#  Author:
#
#    John Burkardt
#
  from r8_normal_01 import r8_normal_01

  seed = 123456789
  test_num = 20

  print ''
  print 'R8_NORMAL_01_TEST'
  print '  R8_NORMAL_01 generates normally distributed'
  print '  random values.'
  print '  Using initial random number seed = %d' % ( seed )
  print ''

  for test in range ( 0, test_num ):

    x, seed = r8_normal_01 ( seed )
    print '  %f' % ( x )
#
#  Terminate.
#
  print ''
  print 'R8_NORMAL_01_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_normal_01_test ( )
  timestamp ( )
