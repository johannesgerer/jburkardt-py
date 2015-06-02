#!/usr/bin/env python
#
def normal_01_variance ( ):

#*****************************************************************************80
#
## NORMAL_01_VARIANCE returns the variance of the Normal 01 PDF.
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
#    Output, real VALUE, the variance of the PDF.
# 
  value = 1.0

  return value

def normal_01_variance_test ( ):

#*****************************************************************************80
#
## NORMAL_01_VARIANCE_TEST tests NORMAL_01_VARIANCE.
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
  from r8vec_variance import r8vec_variance

  print ''
  print 'NORMAL_01_VARIANCE_TEST'
  print '  NORMAL_01_VARIANCE computes the Normal 01 variance;'

  value = normal_01_variance ( )

  print ''
  print '  PDF variance =      %14g' % ( value )

  nsample = 1000
  seed = 123456789

  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i], seed = normal_01_sample ( seed )

  value = r8vec_variance ( nsample, x )

  print ''
  print '  Sample size =     %6d' % ( nsample )
  print '  Sample variance = %14g' % ( value )

  print ''
  print 'NORMAL_01_VARIANCE_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  normal_01_variance_test ( )
  timestamp ( )


