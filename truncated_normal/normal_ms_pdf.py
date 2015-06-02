#!/usr/bin/env python
#
def normal_ms_pdf ( x, mu, sigma ):

#*****************************************************************************80
#
## NORMAL_MS_PDF evaluates the Normal MS PDF.
#
#  Discussion:
#
#    The Normal MS PDF is also called the Gaussian PDF.
#
#  Formula:
#
#    PDF(X)(MU,SIGMA) = EXP ( - 0.5 * ( ( X - MU ) / SIGMA )^2 ) 
#      / SQRT ( 2 * PI * SIGMA^2 )
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
#    Input, real X, the argument of the PDF.
#
#    Input, real MU, SIGMA, the parameters of the PDF.
#    0.0 < SIGMA.
#
#    Output, real VALUE, the value of the PDF.
# 
  import numpy as np

  value = np.exp ( - 0.5 * ( ( x - mu ) / sigma ) ** 2 ) \
    / np.sqrt ( 2.0 * np.pi * sigma ** 2 )

  return value

def normal_ms_pdf_test ( ):

#*****************************************************************************80
#
## NORMAL_MS_PDF_TEST tests NORMAL_MS_PDF.
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
  print 'NORMAL_MS_PDF_TEST'
  print '  NORMAL_MS_PDF evaluates the PDF'
  print '  for the Normal MS distribution.'

  mu = 100.0;
  sigma = 15.0;
  seed = 123456789

  print ''
  print '  PDF parameter MU = %g' % ( mu )
  print '  PDF parameter SIGMA = %g' % ( sigma )

  print ''
  print '       X              PDF'
  print ''

  for i in range ( -20, +21 ):

    x = mu + sigma * float ( i ) / 10.0
    pdf = normal_ms_pdf ( x, mu, sigma )
    print '  %14.6g  %24.16g' % ( x, pdf )

  print ''
  print 'NORMAL_MS_PDF_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  normal_ms_pdf_test ( )
  timestamp ( )
