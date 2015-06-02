#!/usr/bin/env python
#
def normal_ms_moment_central ( order, mu, sigma ):

#*****************************************************************************80
#
## NORMAL_MS_MOMENT_CENTRAL evaluates central moments of the Normal MS distribution.
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
#    Output, real VALUE, the value of the central moment.
#
  from r8_factorial2 import r8_factorial2

  if ( ( order % 2 ) == 0 ):
    value = r8_factorial2 ( order - 1 ) * sigma ** order
  else:
    value = 0.0

  return value

def normal_ms_moment_central_values ( order, mu, sigma ):

#*****************************************************************************80
#
## NORMAL_MS_MOMENT_CENTRAL_VALUES evaluates central moments 0 through 8 of the Normal PDF.
#
#  Discussion:
#
#    The formula was posted by John D Cook.
#
#    Order  Moment
#    -----  ------
#      0    1
#      1    0
#      2    sigma^2
#      3    0
#      4    3 sigma^4
#      5    0
#      6    15 sigma^6
#      7    0
#      8    105 sigma^8
#      9    0
#     10    945 sigma^10
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
    value = 0.0
  elif ( order == 2 ):
    value = sigma ** 2
  elif ( order == 3 ):
    value = 0.0
  elif ( order == 4 ):
    value = 3.0 * sigma ** 4
  elif ( order == 5 ):
    value = 0.0
  elif ( order == 6 ):
    value = 15.0 * sigma ** 6
  elif ( order == 7 ):
    value = 0.0
  elif ( order == 8 ):
    value = 105.0 * sigma ** 8
  elif ( order == 9 ):
    value = 0.0
  elif ( order == 10 ):
    value = 945.0 * sigma ** 10
  else:
    print ''
    print 'NORMAL_MS_MOMENT_CENTRAL_VALUES - Fatal error!'
    print '  Only ORDERS 0 through 8 are available.'
    exit ( 'NORMAL_MS_MOMENT_CENTRAL_VALUES - Fatal error!' )

  return value

def normal_ms_moment_central_test ( ):

#*****************************************************************************80
#
## NORMAL_MS_MOMENT_CENTRAL_TEST tests NORMAL_MS_MOMENT_CENTRAL.
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
  print 'NORMAL_MS_MOMENT_CENTRAL_TEST'
  print '  NORMAL_MS_MOMENT_CENTRAL evaluates central moments'
  print '  of the Normal MS distribution.'

  for test in range ( 0, test_num ):

    mu = mu_test[test]
    sigma = sigma_test[test]
    print ''
    print '  Mu = %g, Sigma = %g' % ( mu, sigma )
    print ' Order  Moment'
    print '\n'

    for order in range ( 0, 9 ):
      moment1 = normal_ms_moment_central ( order, mu, sigma )
      moment2 = normal_ms_moment_central_values ( order, mu, sigma )
      print '  %2d  %12g  %12g' % ( order, moment1, moment2 )

  print ''
  print 'NORMAL_MS_MOMENT_CENTRAL_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  normal_ms_moment_central_test ( )
  timestamp ( )
