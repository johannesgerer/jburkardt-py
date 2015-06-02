#!/usr/bin/env python
#
def normal_ms_moment ( order, mu, sigma ):

#*****************************************************************************80
#
## NORMAL_MS_MOMENT evaluates the moments of the Normal MS distribution.
#
#  Discussion:
#
#    The formula was posted by John D Cook.
#
#    Order  Moment
#    -----  ------
#      0    1
#      1    mu
#      2    mu ** 2 +         sigma ** 2
#      3    mu ** 3 +  3 mu   sigma ** 2
#      4    mu ** 4 +  6 mu ** 2 sigma ** 2 +   3      sigma ** 4
#      5    mu ** 5 + 10 mu ** 3 sigma ** 2 +  15 mu   sigma ** 4
#      6    mu ** 6 + 15 mu ** 4 sigma ** 2 +  45 mu ** 2 sigma ** 4 +  15      sigma ** 6
#      7    mu ** 7 + 21 mu ** 5 sigma ** 2 + 105 mu ** 3 sigma ** 4 + 105 mu   sigma ** 6
#      8    mu ** 8 + 28 mu ** 6 sigma ** 2 + 210 mu ** 4 sigma ** 4 + 420 mu ** 2 sigma ** 6 + 105 sigma ** 8
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
#    Input, integer ORDER, the order of the moment.
#
#    Input, real MU, the mean of the distribution.
#
#    Input, real SIGMA, the standard deviation of the distribution.
#
#    Output, real VALUE, the value of the moment.
#
  from r8_choose import r8_choose
  from r8_factorial2 import r8_factorial2

  j_hi = ( order // 2 )

  value = 0.0
  for j in range ( 0, j_hi + 1 ):
    value = value \
      + r8_choose ( order, 2 * j ) \
      * r8_factorial2 ( 2 * j - 1 ) \
      * mu ** ( order - 2 * j ) * sigma ** ( 2 * j )

  return value

def normal_ms_moment_values ( order, mu, sigma ):

#*****************************************************************************80
#
## NORMAL_MS_MOMENT_VALUES evaluates moments 0 through 8 of the Normal PDF.
#
#  Discussion:
#
#    The formula was posted by John D Cook.
#
#    Order  Moment
#    -----  ------
#      0    1
#      1    mu
#      2    mu ** 2 +         sigma ** 2
#      3    mu ** 3 +  3 mu   sigma ** 2
#      4    mu ** 4 +  6 mu ** 2 sigma ** 2 +   3      sigma ** 4
#      5    mu ** 5 + 10 mu ** 3 sigma ** 2 +  15 mu   sigma ** 4
#      6    mu ** 6 + 15 mu ** 4 sigma ** 2 +  45 mu ** 2 sigma ** 4 +  15      sigma ** 6
#      7    mu ** 7 + 21 mu ** 5 sigma ** 2 + 105 mu ** 3 sigma ** 4 + 105 mu   sigma ** 6
#      8    mu ** 8 + 28 mu ** 6 sigma ** 2 + 210 mu ** 4 sigma ** 4 + 420 mu ** 2 sigma ** 6 + 105 sigma ** 8
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
#    Input, integer ORDER, the order of the moment.
#    0 <= ORDER <= 8.
#
#    Input, real MU, the mean of the distribution.
#
#    Input, real SIGMA, the standard deviation of the distribution.
#
#    Output, real VALUE, the value of the central moment.
#
  from sys import exit

  if ( order == 0 ):
    value = 1.0
  elif ( order == 1 ):
    value = mu
  elif ( order == 2 ):
    value = mu ** 2 + sigma ** 2
  elif ( order == 3 ):
    value = mu ** 3 + 3.0 * mu * sigma ** 2
  elif ( order == 4 ):
    value = mu ** 4 + 6.0 * mu ** 2 * sigma ** 2 + 3.0 * sigma ** 4
  elif ( order == 5 ):
    value = mu ** 5 + 10.0 * mu ** 3 * sigma ** 2 + 15.0 * mu * sigma ** 4
  elif ( order == 6 ):
    value = mu ** 6 + 15.0 * mu ** 4 * sigma ** 2 + 45.0 * mu ** 2 * sigma ** 4 \
      + 15.0 * sigma ** 6
  elif ( order == 7 ):
    value = mu ** 7 + 21.0 * mu ** 5 * sigma ** 2 + 105.0 * mu ** 3 * sigma ** 4 \
      + 105.0 * mu * sigma ** 6
  elif ( order == 8 ):
    value = mu ** 8 + 28.0 * mu ** 6 * sigma ** 2 + 210.0 * mu ** 4 * sigma ** 4 \
      + 420.0 * mu ** 2 * sigma ** 6 + 105.0 * sigma ** 8
  else:
    print ''
    print 'NORMAL_MS_MOMENT_VALUES - Fatal error!'
    print '  Only ORDERS 0 through 8 are available.'
    exit ( 'NORMAL_MS_MOMENT_VALUES - Fatal error!' )

  return value

def normal_ms_moment_test ( ):

#*****************************************************************************80
#
## NORMAL_MS_MOMENT_TEST tests NORMAL_MS_MOMENT.
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
  
  test_num = 4
  mu_test = np.array ( [ 0.0, 2.0, 10.0, 0.0 ] )
  sigma_test = np.array ( [ 1.0, 1.0, 2.0, 2.0 ] )

  print ''
  print 'NORMAL_MS_MOMENT_TEST'
  print '  NORMAL_MS_MOMENT evaluates moments of the Normal MS distribution.'

  for test in range ( 0, test_num ):

    mu = mu_test[test]
    sigma = sigma_test[test]
    print ''
    print '  Mu = %g, Sigma = %g' % ( mu, sigma )
    print ' Order  Moment'
    print '\n'

    for order in range ( 0, 9 ):
      moment1 = normal_ms_moment ( order, mu, sigma )
      moment2 = normal_ms_moment_values ( order, mu, sigma )
      print '  %2d  %12g  %12g' % ( order, moment1, moment2 )
#
#  Terminate.
#
  print ''
  print 'NORMAL_MS_MOMENT_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  normal_ms_moment_test ( )
  timestamp ( )
