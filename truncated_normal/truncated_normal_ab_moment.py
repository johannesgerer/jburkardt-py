#!/usr/bin/env python
#
def truncated_normal_ab_moment ( order, mu, sigma, a, b ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_AB_MOMENT: moments of the truncated Normal distribution.
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
#  Reference:
#
#    Phoebus Dhrymes,
#    Moments of Truncated Normal Distributions,
#    May 2005.
#
#  Parameters:
#
#    Input, integer ORDER, the order of the moment.
#    0 <= ORDER.
#
#    Input, real MU, SIGMA, the mean and standard deviation of the
#    parent Normal distribution.
#    0 < S.
#
#    Input, real A, B, the lower and upper truncation limits.
#    A < B.
#
#    Output, real VALUE, the moment of the PDF.
#
  from normal_01_cdf import normal_01_cdf
  from normal_01_pdf import normal_01_pdf
  from r8_choose import r8_choose
  from sys import exit

  if ( order < 0 ):
    print ''
    print 'TRUNCATED_NORMAL_AB_MOMENT - Fatal error!'
    print '  ORDER < 0.'
    exit ( 'TRUNCATED_NORMAL_AB_MOMENT - Fatal error!' )

  if ( sigma <= 0.0 ):
    print ''
    print 'TRUNCATED_NORMAL_AB_MOMENT - Fatal error!'
    print '  SIGMA <= 0.0.'
    exit ( 'TRUNCATED_NORMAL_AB_MOMENT - Fatal error!' )

  if ( b <= a ):
    print ''
    print 'TRUNCATED_NORMAL_AB_MOMENT - Fatal error!'
    print '  B <= A.'
    exit ( 'TRUNCATED_NORMAL_AB_MOMENT - Fatal error!' )

  a_h = ( a - mu ) / sigma
  a_pdf = normal_01_pdf ( a_h )
  a_cdf = normal_01_cdf ( a_h )

  if ( a_cdf == 0.0 ):
    print ''
    print 'TRUNCATED_NORMAL_AB_MOMENT - Fatal error!'
    print '  PDF/CDF ratio fails, because A_CDF is too small.'
    print '  A_PDF = %g' % ( a_pdf )
    print '  A_CDF = %g' % ( a_cdf )
    exit ( 'TRUNCATED_NORMAL_AB_MOMENT - Fatal error!' )

  b_h = ( b - mu ) / sigma
  b_pdf = normal_01_pdf ( b_h )
  b_cdf = normal_01_cdf ( b_h )

  if ( b_cdf == 0.0 ):
    print ''
    print 'TRUNCATED_NORMAL_AB_MOMENT - Fatal error!'
    print '  PDF/CDF ratio fails, because B_CDF too small.'
    print '  B_PDF = %g' % ( b_pdf )
    print '  B_CDF = %g' % ( b_cdf )
    exit ( 'TRUNCATED_NORMAL_AB_MOMENT - Fatal error!' )

  value = 0.0
  irm2 = 0.0
  irm1 = 0.0

  for r in range ( 0, order + 1 ):

    if ( r == 0 ):
      ir = 1.0
    elif ( r == 1 ):
      ir = - ( b_pdf - a_pdf ) / ( b_cdf - a_cdf )
    else:
      ir = ( r - 1 ) * irm2 \
        - ( b_h ** ( r - 1 ) * b_pdf - a_h ** ( r - 1 ) * a_pdf ) \
        / ( b_cdf - a_cdf )

    value = value + r8_choose ( order, r ) \
      * mu ** ( order - r ) \
      * sigma ** r * ir

    irm2 = irm1
    irm1 = ir

  return value

def truncated_normal_ab_moment_test ( ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_AB_MOMENT_TEST tests TRUNCATED_NORMAL_AB_MOMENT.
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
  import numpy as np
  
  test_num = 9
  mu_test =    np.array ( [  0.0, 0.0,  0.0,  0.0,  1.0, 0.0,  0.0,  0.0, 5.0 ] )
  sigma_test = np.array ( [  1.0, 1.0,  1.0,  2.0,  1.0, 1.0,  1.0,  1.0, 0.5 ] )
  a_test =     np.array ( [ -1.0, 0.0, -1.0, -1.0,  0.0, 0.5, -2.0, -4.0, 4.0 ] )
  b_test =     np.array ( [  1.0, 1.0,  0.0,  1.0,  2.0, 2.0,  2.0,  4.0, 7.0 ] )

  print ''
  print 'TRUNCATED_NORMAL_AB_MOMENT_TEST'
  print '  TRUNCATED_NORMAL_AB_MOMENT evaluates moments'
  print '  of the Truncated Normal distribution.'

  for test in range ( 0, test_num ):

    mu = mu_test[test]
    sigma = sigma_test[test]
    a = a_test[test]
    b = b_test[test]
    print ''
    print '  Test = %d, Mu = %g, Sigma = %g, A = %g, B = %g' \
      % ( test, mu, sigma, a, b )
    print ' Order  Moment'
    print '\n'

    for order in range ( 0, 9 ):
      value = truncated_normal_ab_moment ( order, mu, sigma, a, b )
      print '  %2d  %12g' % ( order, value )
#
#  Terminate.
#
  print ''
  print 'TRUNCATED_NORMAL_AB_MOMENT_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  truncated_normal_ab_moment_test ( )
  timestamp ( )
