#!/usr/bin/env python
#
def truncated_normal_ab_pdf ( x, mu, sigma, a, b ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_AB_PDF evaluates the Truncated Normal PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the argument of the PDF.
#
#    Input, real MU, SIGMA, the mean and standard deviation of the
#    parent Normal distribution.
#
#    Input, real A, B, the lower and upper truncation limits.
#
#    Output, real VALUE, the value of the PDF.
# 
  from normal_01_cdf import normal_01_cdf
  from normal_01_pdf import normal_01_pdf

  alpha = ( a - mu ) / sigma
  beta = ( b - mu ) / sigma
  xi = ( x - mu ) / sigma

  alpha_cdf = normal_01_cdf ( alpha )
  beta_cdf = normal_01_cdf ( beta )
  xi_pdf = normal_01_pdf ( xi )

  value = xi_pdf / ( beta_cdf - alpha_cdf ) / sigma

  return value

def truncated_normal_ab_pdf_test ( ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_AB_PDF_TEST tests TRUNCATED_NORMAL_AB_PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 March 2015
#
#  Author:
#
#    John Burkardt
#
  from truncated_normal_ab_pdf_values import truncated_normal_ab_pdf_values

  print ''
  print 'TRUNCATED_NORMAL_AB_PDF_TEST'
  print '  TRUNCATED_NORMAL_AB_PDF evaluates the PDF'
  print '  of the Truncated Normal distribution.'
  print ''
  print '  The "parent" normal distribution has'
  print '    mean = mu'
  print '    standard deviation = sigma'
  print '  The parent distribution is truncated to'
  print '  the interval [a,b]'

  print ''
  print '                                                           Stored         Computed'
  print '       X        Mu         S         A         B             PDF             PDF'
  print ''

  n_data = 0

  while ( True ):

    n_data, mu, sigma, a, b, x, pdf1 = truncated_normal_ab_pdf_values ( n_data )

    if ( n_data == 0 ):
      break

    pdf2 = truncated_normal_ab_pdf ( x, mu, sigma, a, b )

    print '  %8.1f  %8.1f  %8.1f  %8.1f  %8.1f  %14g  %14g' \
      % ( x, mu, sigma, a, b, pdf1, pdf2 )

  print ''
  print 'TRUNCATED_NORMAL_AB_PDF_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  truncated_normal_ab_pdf_test ( )
  timestamp ( )

