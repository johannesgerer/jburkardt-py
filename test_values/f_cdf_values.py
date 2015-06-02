#!/usr/bin/env python
#
def f_cdf_values ( n_data ):

#*****************************************************************************80
#
## F_CDF_VALUES returns some values of the F CDF test function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      Needs["Statistics`ContinuousDistributions`"]
#      dist = FRatioDistribution [ dfn, dfd ]
#      CDF [ dist, x ]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 February 2015
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
#    Output, integer A, integer B, the parameters of the function.
#
#    Output, real X, the argument of the function.
#
#    Output, real F, the value of the function.
#
  import numpy as np

  n_max = 20

  a_vec = np.array ( ( \
    1, \
    1, \
    5, \
    1, \
    2, \
    4, \
    1, \
    6, \
    8, \
    1, \
    3, \
    6, \
    1, \
    1, \
    1, \
    1, \
    2, \
    3, \
    4, \
    5 ))

  b_vec = np.array ( ( \
     1, \
     5, \
     1, \
     5, \
    10, \
    20, \
     5, \
     6, \
    16, \
     5, \
    10, \
    12, \
     5, \
     5, \
     5, \
     5, \
     5, \
     5, \
     5, \
     5 ))

  f_vec = np.array ( ( \
     0.5000000000000000E+00, \
     0.4999714850534485E+00, \
     0.4996034370170990E+00, \
     0.7496993658293228E+00, \
     0.7504656462757382E+00, \
     0.7514156325324275E+00, \
     0.8999867031372156E+00, \
     0.8997127554259699E+00, \
     0.9002845660853669E+00, \
     0.9500248817817622E+00, \
     0.9500574946122442E+00, \
     0.9501926400000000E+00, \
     0.9750133887312993E+00, \
     0.9900022327445249E+00, \
     0.9949977837872073E+00, \
     0.9989999621122122E+00, \
     0.5687988496283079E+00, \
     0.5351452100063650E+00, \
     0.5143428032407864E+00, \
     0.5000000000000000E+00 ))

  x_vec = np.array ( ( \
      1.00E+00, \
      0.528E+00, \
      1.89E+00, \
      1.69E+00, \
      1.60E+00, \
      1.47E+00, \
      4.06E+00, \
      3.05E+00, \
      2.09E+00, \
      6.61E+00, \
      3.71E+00, \
      3.00E+00, \
     10.01E+00, \
     16.26E+00, \
     22.78E+00, \
     47.18E+00, \
      1.00E+00, \
      1.00E+00, \
      1.00E+00, \
      1.00E+00 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    a = 0
    b = 0
    x = 0.0
    f = 0.0
  else:
    a = a_vec[n_data]
    b = b_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, a, b, x, f

def f_cdf_values_test ( ):

#*****************************************************************************80
#
## F_CDF_VALUES_TEST demonstrates the use of F_CDF_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'F_CDF_VALUES_TEST:'
  print '  F_CDF_VALUES stores values of the F CDF.'
  print ''
  print '      A         B         X        F_CDF(A,B,X)'
  print ''

  n_data = 0

  while ( True ):

    n_data, a, b, x, f = f_cdf_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %12d  %12d  %12f  %24.16g' % ( a, b, x, f )

  print ''
  print 'F_CDF_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  f_cdf_values_test ( )
  timestamp ( )
