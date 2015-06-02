#!/usr/bin/env python
#
def f_noncentral_cdf_values ( n_data ):

#*****************************************************************************80
#
## F_NONCENTRAL_CDF_VALUES: values of the noncentral F CDF.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      Needs["Statistics`ContinuousDistributions`"]
#      dist = NoncentralFRatioDistribution [ n1, n2, lambda ]
#      CDF [ dist, x ]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 February 2015
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
#    Output, integer A, integer B, the numerator and denominator
#    degrees of freedom.
#
#    Output, real LAM, the noncentrality parameter.
#
#    Output, real X, the argument of the function.
#
#    Output, real FX, the value of the function.
#
  import numpy as np

  n_max = 22

  a_vec = np.array ( ( \
     1,  1,  1,  1, \
     1,  1,  1,  1, \
     1,  1,  2,  2, \
     3,  3,  4,  4, \
     5,  5,  6,  6, \
     8, 16 ))

  b_vec = np.array ( ( \
     1,  5,  5,  5, \
     5,  5,  5,  5, \
     5,  5,  5, 10, \
     5,  5,  5,  5, \
     1,  5,  6, 12, \
    16,  8 ))

  f_vec = np.array ( ( \
     0.5000000000000000E+00, \
     0.6367825323508774E+00, \
     0.5840916116305482E+00, \
     0.3234431872392788E+00, \
     0.4501187879813550E+00, \
     0.6078881441188312E+00, \
     0.7059275551414605E+00, \
     0.7721782003263727E+00, \
     0.8191049017635072E+00, \
     0.3170348430749965E+00, \
     0.4327218008454471E+00, \
     0.4502696915707327E+00, \
     0.4261881186594096E+00, \
     0.6753687206341544E+00, \
     0.4229108778879005E+00, \
     0.6927667261228938E+00, \
     0.3632174676491226E+00, \
     0.4210054012695865E+00, \
     0.4266672258818927E+00, \
     0.4464016600524644E+00, \
     0.8445888579504827E+00, \
     0.4339300273343604E+00 ))

  lam_vec = np.array ( ( \
     0.00E+00, \
     0.00E+00, \
     0.25E+00, \
     1.00E+00, \
     1.00E+00, \
     1.00E+00, \
     1.00E+00, \
     1.00E+00, \
     1.00E+00, \
     2.00E+00, \
     1.00E+00, \
     1.00E+00, \
     1.00E+00, \
     2.00E+00, \
     1.00E+00, \
     1.00E+00, \
     0.00E+00, \
     1.00E+00, \
     1.00E+00, \
     1.00E+00, \
     1.00E+00, \
     1.00E+00 ))

  x_vec = np.array ( ( \
     1.00E+00, \
     1.00E+00, \
     1.00E+00, \
     0.50E+00, \
     1.00E+00, \
     2.00E+00, \
     3.00E+00, \
     4.00E+00, \
     5.00E+00, \
     1.00E+00, \
     1.00E+00, \
     1.00E+00, \
     1.00E+00, \
     1.00E+00, \
     1.00E+00, \
     2.00E+00, \
     1.00E+00, \
     1.00E+00, \
     1.00E+00, \
     1.00E+00, \
     2.00E+00, \
     2.00E+00 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    a = 0
    b = 0
    lam = 0.0
    x = 0.0
    f = 0.0
  else:
    a = a_vec[n_data]
    b = b_vec[n_data]
    lam = lam_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, a, b, lam, x, f

def f_noncentral_cdf_values_test ( ):

#*****************************************************************************80
#
## F_NONCENTRAL_CDF_VALUES_TEST demonstrates the use of F_NONCENTRAL_CDF_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'F_NONCENTRAL_CDF_VALUES_TEST:'
  print '  F_NONCENTRAL_CDF_VALUES stores values of the noncentral F CDF.'
  print ''
  print '     A     B        LAM           X               F'
  print ''

  n_data = 0

  while ( True ):

    n_data, a, b, lam, x, f = f_noncentral_cdf_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %4d  %4d  %12f  %12f  %24.16g' % ( a, b, lam, x, f )

  print ''
  print 'F_NONCENTRAL_CDF_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  f_noncentral_cdf_values_test ( )
  timestamp ( )
