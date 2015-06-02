#!/usr/bin/env python
#
def truncated_normal_a_moment ( order, mu, sigma, a ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_A_MOMENT: moments of the truncated Normal distribution.
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
#    Input, real A, the lower truncation limit.
#
#    Output, real VALUE, the moment of the PDF.
#
  from r8_mop import r8_mop
  from truncated_normal_b_moment import truncated_normal_b_moment

  value = r8_mop ( order ) \
    * truncated_normal_b_moment ( order, -mu, sigma, -a );

  return value

def truncated_normal_a_moment_test ( ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_A_MOMENT_TEST tests TRUNCATED_NORMAL_A_MOMENT.
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
  
  test_num = 6
  mu_test =    np.array ( [  0.0,  0.0,   0.0,   0.0,  0.0,  -5.0 ] )
  sigma_test = np.array ( [  1.0,  1.0,   1.0,   2.0,  2.0,   1.0 ] )
  a_test =     np.array ( [  0.0, -10.0, 10.0, -10.0, 10.0, -10.0 ] )

  print ''
  print 'TRUNCATED_NORMAL_A_MOMENT_TEST'
  print '  TRUNCATED_NORMAL_A_MOMENT evaluates moments'
  print '  of the lower Truncated Normal distribution.'

  for test in range ( 0, test_num ):

    mu = mu_test[test]
    sigma = sigma_test[test]
    a = a_test[test]
    print ''
    print '  Test = %d, Mu = %g, Sigma = %g, A = %g' \
      % ( test, mu, sigma, a )
    print ' Order  Moment'
    print '\n'

    for order in range ( 0, 9 ):
      value = truncated_normal_a_moment ( order, mu, sigma, a )
      print '  %2d  %12g' % ( order, value )

  print ''
  print 'TRUNCATED_NORMAL_A_MOMENT_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  truncated_normal_a_moment_test ( )
  timestamp ( )
