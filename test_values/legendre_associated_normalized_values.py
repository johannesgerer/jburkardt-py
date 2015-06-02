#!/usr/bin/env python
#
def legendre_associated_normalized_values ( n_data ):

#*****************************************************************************80
#
## LEGENDRE_ASSOCIATED_NORMALIZED_VALUES returns values of associated Legendre functions.
#
#  Discussion:
#
#    The function considered is the associated Legendre polynomial P^M_N(X).
#
#    In Mathematica, the function can be evaluated by:
#
#      LegendreP [ n, m, x ]
#
#    The function is normalized by dividing by
#
#      sqrt ( 2 * ( n + m )! / ( 2 * n + 1 ) / ( n - m )! )
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
    0.7071067811865475E+00, \
    0.6123724356957945E+00, \
   -0.7500000000000000E+00, \
   -0.1976423537605237E+00, \
   -0.8385254915624211E+00, \
    0.7261843774138907E+00, \
   -0.8184875533567997E+00, \
   -0.1753901900050285E+00, \
    0.9606516343087123E+00, \
   -0.6792832849776299E+00, \
   -0.6131941618102092E+00, \
    0.6418623720763665E+00, \
    0.4716705890038619E+00, \
   -0.1018924927466445E+01, \
    0.6239615396237876E+00, \
    0.2107022704608181E+00, \
    0.8256314721961969E+00, \
   -0.3982651281554632E+00, \
   -0.7040399320721435E+00, \
    0.1034723155272289E+01, \
   -0.5667412129155530E+00 ))

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

def legendre_associated_normalized_values_test ( ):

#*****************************************************************************80
#
## LEGENDRE_ASSOCIATED_NORMALIZED_VALUES_TEST demonstrates LEGENDRE_ASSOCIATED_NORMALIZED_VALUES.
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
  print 'LEGENDRE_ASSOCIATED_NORMALIZED_VALUES_TEST:'
  print '  LEGENDRE_ASSOCIATED_NORMALIZED_VALUES stores values of the '
  print '  normalized associated Legendre function.'
  print ''
  print '      N       M            X            F'
  print ''

  n_data = 0

  while ( True ):

    n_data, n, m, x, f = legendre_associated_normalized_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %6d  %6d  %12f  %24.16g' % ( n, m, x, f )

  print ''
  print 'LEGENDRE_ASSOCIATED_NORMALIZED_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  legendre_associated_normalized_values_test ( )
  timestamp ( )

