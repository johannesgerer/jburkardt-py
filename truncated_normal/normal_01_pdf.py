#!/usr/bin/env python
#
def normal_01_pdf ( x ):

#*****************************************************************************80
#
## NORMAL_01_PDF evaluates the Normal 01 PDF.
#
#  Discussion:
#
#    The Normal 01 PDF is also called the "Standard Normal" PDF, or
#    the Normal PDF with 0 mean and standard deviation 1.
#
#  Formula:
#
#    PDF(x) = exp ( - 0.5 * x^2 ) / sqrt ( 2 * pi )
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
#    Input, real X, the argument of the PDF.
#
#    Output, real VALUE, the value of the PDF.
# 
  import numpy as np

  value = np.exp ( - 0.5 * x * x ) / np.sqrt ( 2.0 * np.pi )

  return value

def normal_01_pdf_test ( ):

#*****************************************************************************80
#
## NORMAL_01_PDF_TEST tests NORMAL_01_PDF.
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
  print ''
  print 'NORMAL_01_PDF_TEST'
  print '  NORMAL_01_PDF evaluates the PDF;'
  print ''
  print '       X              PDF'
  print ''

  for i in range ( -20, +21 ):

    x = float ( i ) / 10.0
    pdf = normal_01_pdf ( x )
    print '  %14.6g  %24.16g' % ( x, pdf )

  print ''
  print 'NORMAL_01_PDF_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  normal_01_pdf_test ( )
  timestamp ( )

