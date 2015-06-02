#!/usr/bin/env python
#
def normal_ms_cdf ( x, mu, sigma ):

#*****************************************************************************80
#
## NORMAL_MS_CDF evaluates the CDF of the Normal MS distribution.
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
#    Input, real X, the argument of the CDF.
#
#    Input, real MU, SIGMA, the parameters of the PDF.
#    0.0 < SIGMA.
#
#    Output, real VALUE, the value of the CDF.
#
  from normal_01_cdf import normal_01_cdf

  y = ( x - mu ) / sigma

  value = normal_01_cdf ( y )

  return value

def normal_ms_cdf_test ( ):

#*****************************************************************************80
#
## NORMAL_MS_CDF_TEST tests NORMAL_MS_CDF.
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
  print 'NORMAL_MS_CDF_TEST'
  print '  NORMAL_MS_CDF evaluates the CDF;'

  mu = 100.0
  sigma = 15.0

  print ''
  print '  PDF parameter MU = %g' % ( mu )
  print '  PDF parameter SIGMA = %g' % ( sigma )

  print ''
  print '       X              CDF'
  print ''

  for i in range ( -20, +21 ):

    x = mu + sigma * float ( i ) / 10.0
    cdf = normal_ms_cdf ( x, mu, sigma )
    print '  %14.6g  %24.16g' % ( x, cdf )

  print ''
  print 'NORMAL_MS_CDF_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  normal_ms_cdf_test ( )
  timestamp ( )
