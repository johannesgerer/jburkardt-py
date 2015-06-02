#!/usr/bin/env python
#
def normal_ms_mean ( mu, sigma ):

#*****************************************************************************80
#
## NORMAL_MS_MEAN returns the mean of the Normal MS distribution.
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
#    Output, real VALUE, the mean of the PDF.
# 
  value = mu

  return value

def normal_ms_mean_test ( ):

#*****************************************************************************80
#
## NORMAL_MS_MEAN_TEST tests NORMAL_MS_MEAN.
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
  import numpy as np
  from normal_ms_sample import normal_ms_sample
  from r8vec_max import r8vec_max
  from r8vec_mean import r8vec_mean
  from r8vec_min import r8vec_min

  print ''
  print 'NORMAL_MS_MEAN_TEST'
  print '  NORMAL_MS_MEAN computes the mean'
  print '  of the Normal MS distribution.'

  mu = 100.0
  sigma = 15.0

  m = normal_ms_mean ( mu, sigma )

  print ''
  print '  PDF parameter MU = %g' % ( mu )
  print '  PDF parameter SIGMA = %g' % ( sigma )
  print '  PDF mean = %g' % ( m )

  nsample = 1000
  seed = 123456789

  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i], seed = normal_ms_sample ( mu, sigma, seed )

  ms = r8vec_mean ( nsample, x )
  xmax = r8vec_max ( nsample, x )
  xmin = r8vec_min ( nsample, x )

  print ''
  print '  Sample size =     %6d' % ( nsample )
  print '  Sample mean =     %14g' % ( ms )
  print '  Sample maximum =  %14g' % ( xmax )
  print '  Sample minimum =  %14g' % ( xmin )

  print ''
  print 'NORMAL_MS_MEAN_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  normal_ms_mean_test ( )
  timestamp ( )

