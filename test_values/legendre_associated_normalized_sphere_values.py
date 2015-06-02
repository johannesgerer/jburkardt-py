#!/usr/bin/env python
#
def legendre_associated_normalized_sphere_values ( n_data ):

#*****************************************************************************80
#
## LEGENDRE_ASSOCIATED_NORMALIZED_SPHERE_VALUES does what it says.
#
#  Discussion:
#
#    The function considered is the associated Legendre polynomial P^M_N(X).
#
#    In Mathematica, the function can be evaluated by:
#
#      LegendreP [ n, m, x ]
#
#    The function is normalized for the unit sphere by dividing by
#
#      sqrt ( 4 * pi * ( n + m )! / ( 2 * n + 1 ) / ( n - m )! )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Parameters:
#
#    Input/output, integer N_DATA.  The user sets N_DATA to 0 before the
#    first call.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, integer N, integer M, real X, 
#    the arguments of the function.
#
#    Output, real F, the value of the function.
#
  import numpy as np

  n_max = 21

  f_vec = np.array ( ( \
     0.2820947917738781, \
     0.2443012559514600, \
    -0.2992067103010745, \
    -0.07884789131313000, \
    -0.3345232717786446, \
     0.2897056515173922, \
    -0.3265292910163510, \
    -0.06997056236064664, \
     0.3832445536624809, \
    -0.2709948227475519, \
    -0.2446290772414100, \
     0.2560660384200185, \
     0.1881693403754876, \
    -0.4064922341213279, \
     0.2489246395003027, \
     0.08405804426339821, \
     0.3293793022891428, \
    -0.1588847984307093, \
    -0.2808712959945307, \
     0.4127948151484925, \
    -0.2260970318780046  ))

  m_vec = np.array ( ( \
    0, 0, 1, 0, \
    1, 2, 0, 1, \
    2, 3, 0, 1, \
    2, 3, 4, 0, \
    1, 2, 3, 4, \
    5 ))

  n_vec = np.array ( ( \
    0,  1,  1,  2, \
    2,  2,  3,  3, \
    3,  3,  4,  4, \
    4,  4,  4,  5, \
    5,  5,  5,  5, \
    5 ))

  x_vec = np.array ( ( \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    m = 0
    x = 0.0
    f = 0.0
  else:
    n = n_vec[n_data]
    m = m_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, n, m, x, f

def legendre_associated_normalized_sphere_values_test ( ):

#*****************************************************************************80
#
## LEGENDRE_ASSOCIATED_NORMALIZED_SPHERE_VALUES_TEST demonstrates LEGENDRE_ASSOCIATED_NORMALIZED_SPHERE_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'LEGENDRE_ASSOCIATED_NORMALIZED_SPHERE_VALUES_TEST:'
  print '  LEGENDRE_ASSOCIATED_NORMALIZED_SPHERE_VALUES stores values of the '
  print '  associated Legendre function normalized for the surface of a sphere.'
  print ''
  print '      N       M            X            F'
  print ''

  n_data = 0

  while ( True ):

    n_data, n, m, x, f = legendre_associated_normalized_sphere_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %6d  %6d  %12f  %24.16g' % ( n, m, x, f )

  print ''
  print 'LEGENDRE_ASSOCIATED_NORMALIZED_SPHERE_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  legendre_associated_normalized_sphere_values_test ( )
  timestamp ( )

