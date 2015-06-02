#!/usr/bin/env python
#
def normal_ms_variance ( mu, sigma ):

#*****************************************************************************80
#
## NORMAL_MS_VARIANCE returns the variance of the Normal MS distribution.
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
#    Output, real VALUE, the variance of the PDF.
# 
  value = sigma * sigma

  return value

def normal_ms_variance_test ( ):

#*****************************************************************************80
#
## NORMAL_MS_VARIANCE_TEST tests NORMAL_MS_VARIANCE.
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
  from r8vec_variance import r8vec_variance


  print ''
  print 'NORMAL_MS_VARIANCE_TEST'
  print '  NORMAL_MS_VARIANCE computes the variance'
  print '  of the Normal MS distribution.'

  mu = 100.0
  sigma = 15.0

  value = normal_ms_variance ( mu, sigma )

  print ''
  print '  PDF parameter MU = %g' % ( mu )
  print '  PDF parameter SIGMA = %g' % ( sigma )
  print '  PDF variance = %g' % ( value )

  nsample = 1000
  seed = 123456789

  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i], seed = normal_ms_sample ( mu, sigma, seed )

  value = r8vec_variance ( nsample, x )

  print ''
  print '  Sample size =     %6d' % ( nsample )
  print '  Sample variance = %14g' % ( value )

  print ''
  print 'NORMAL_MS_VARIANCE_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  normal_ms_variance_test ( )
  timestamp ( )

