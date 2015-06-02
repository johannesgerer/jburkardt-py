#!/usr/bin/env python

def normal_ms_sample ( mu, sigma, seed ):

#*****************************************************************************80
#
## NORMAL_MS_SAMPLE samples the Normal MS distribution.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real MU, SIGMA, the parameters of the PDF.
#    0.0 < SIGMA.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real VALUE, a sample of the standard normal PDF.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  import numpy as np

  from normal_01_sample import normal_01_sample

  y, seed = normal_01_sample ( seed )
 
  value = mu + sigma * y

  return value, seed

def normal_ms_sample_test ( ):

#*****************************************************************************80
#
## NORMAL_MS_SAMPLE_TEST tests NORMAL_MS_SAMPLE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 March 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'NORMAL_MS_SAMPLE_TEST'
  print '  NORMAL_MS_SAMPLE samples'
  print '  the Normal MS distribution.'

  mu = 100.0
  sigma = 15.0
  seed = 123456789

  print ''
  print '  PDF parameter MU = %g\n' % ( mu )
  print '  PDF parameter SIGMA = %g' % ( sigma )

  print ''
  for i in range ( 0, 10 ):
    x, seed = normal_ms_sample ( mu, sigma, seed )
    print '  %4d  %14.6g' % ( i, x )

  print ''
  print 'NORMAL_MS_SAMPLE_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  normal_ms_sample_test ( )
  timestamp ( )
