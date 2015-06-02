#!/usr/bin/env python
#
def normal_ms_cdf_inv ( cdf, mu, sigma ):

#*****************************************************************************80
#
## NORMAL_MS_CDF_INV inverts the CDF of the Normal MS distribution.
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
#    Input, real CDF, the value of the CDF.
#    0.0 <= CDF <= 1.0.
#
#    Input, real MU, SIGMA, the parameters of the PDF.
#    0.0 < SIGMA.
#
#    Output, real VALUE, the corresponding argument.
#
  from normal_01_cdf_inv import normal_01_cdf_inv

  if ( cdf < 0.0 or 1.0 < cdf ):
    print ''
    print 'NORMAL_MS_CDF_INV - Fatal error!'
    print '  CDF < 0 or 1 < CDF.'
    error ( 'NORMAL_MS_CDF_INV - Fatal error!' )

  y = normal_01_cdf_inv ( cdf )

  value = mu + sigma * y

  return value

def normal_ms_cdf_inv_test ( ):

#*****************************************************************************80
#
## NORMAL_MS_CDF_INV_TEST tests NORMAL_MS_CDF_INV.
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
  from normal_ms_cdf import normal_ms_cdf

  print ''
  print 'NORMAL_MS_CDF_INV_TEST'
  print '  NORMAL_MS_CDF_INV inverts the CDF'
  print '  of the Normal MS distribution.'

  mu = 100.0
  sigma = 15.0

  print ''
  print '  PDF parameter MU = %g' % ( mu )
  print '  PDF parameter SIGMA = %g' % ( sigma )

  print ''
  print '       X              CDF            CDF_INV'
  print ''

  for i in range ( -20, +21 ):

    x = mu + sigma * float ( i ) / 10.0
    cdf = normal_ms_cdf ( x, mu, sigma )
    x2 = normal_ms_cdf_inv ( cdf, mu, sigma )
    print '  %14.6g  %14.6g  %14.6g' % ( x, cdf, x2 )

  print ''
  print 'NORMAL_MS_CDF_INV_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  normal_ms_cdf_inv_test ( )
  timestamp ( )
