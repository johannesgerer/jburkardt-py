#!/usr/bin/env python
#
def normal_01_mean ( ):

#*****************************************************************************80
#
## NORMAL_01_MEAN returns the mean of the Normal 01 PDF.
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
#    Output, real VALUE, the mean of the PDF.
# 
  value = 0.0

  return value

def normal_01_mean_test ( ):

#*****************************************************************************80
#
## NORMAL_01_MEAN_TEST tests NORMAL_01_MEAN.
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
  import numpy as np
  from normal_01_sample import normal_01_sample
  from r8vec_max import r8vec_max
  from r8vec_mean import r8vec_mean
  from r8vec_min import r8vec_min

  print ''
  print 'NORMAL_01_MEAN_TEST'
  print '  NORMAL_01_MEAN computes the Normal 01 mean;'

  m = normal_01_mean ( )

  print ''
  print '  PDF mean =      %14g' % ( m )

  nsample = 1000
  seed = 123456789

  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i], seed = normal_01_sample ( seed )

  ms = r8vec_mean ( nsample, x )
  xmax = r8vec_max ( nsample, x )
  xmin = r8vec_min ( nsample, x )

  print ''
  print '  Sample size =     %6d' % ( nsample )
  print '  Sample mean =     %14g' % ( ms )
  print '  Sample maximum =  %14g' % ( xmax )
  print '  Sample minimum =  %14g' % ( xmin )

  print ''
  print 'NORMAL_01_MEAN_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  normal_01_mean_test ( )
  timestamp ( )


