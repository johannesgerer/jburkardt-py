#!/usr/bin/env python

def normal_01_sample ( seed ):

#*****************************************************************************80
#
## NORMAL_01_SAMPLE samples the standard normal probability distribution.
#
#  Discussion:
#
#    The standard normal probability distribution function (PDF) has
#    mean 0 and standard deviation 1.
#
#  Method:
#
#    The Box-Muller method is used, which is efficient, but
#    generates two values at a time.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real VALUE, a sample of the standard normal PDF.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  import numpy as np

  from r8_uniform_01 import r8_uniform_01

  r1, seed = r8_uniform_01 ( seed )
  r2, seed = r8_uniform_01 ( seed )

  value = np.sqrt ( - 2.0 * np.log ( r1 ) ) * np.cos ( 2.0 * np.pi * r2 )

  return value, seed

def normal_01_sample_test ( ):

#*****************************************************************************80
#
## NORMAL_01_SAMPLE_TEST tests NORMAL_01_SAMPLE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'NORMAL_01_SAMPLE_TEST'
  print '  NORMAL_01_SAMPLE returns samples from the normal'
  print '  distribution with mean 0 and standard deviation 1.'
  print ''

  seed = 123456789

  for i in range ( 0, 10 ):
    x, seed = normal_01_sample ( seed )
    print '  %4d  %14.6g' % ( i, x )

  print ''
  print 'NORMAL_01_SAMPLE_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  normal_01_sample_test ( )
  timestamp ( )
