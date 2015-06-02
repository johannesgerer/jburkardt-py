#!/usr/bin/env python
#
def student_noncentral_cdf_values ( n_data ):

#*****************************************************************************80
#
## STUDENT_NONCENTRAL_CDF_VALUES returns values of the noncentral Student CDF.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      Needs["Statistics`ContinuousDistributions`"]
#      dist = NoncentralStudentTDistribution [ df, lambda ]
#      CDF [ dist, x ]
#
#    Mathematica seems to have some difficulty computing this function
#    to the desired number of digits.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 February 2015
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
#    Output, integer DF, real LAM, the parameters of the
#    function.
#
#    Output, real X, the argument of the function.
#
#    Output, real F, the value of the function.
#
  import numpy as np

  n_max = 30

  df_vec = np.array ( ( \
     1,  2,  3, \
     1,  2,  3, \
     1,  2,  3, \
     1,  2,  3, \
     1,  2,  3, \
    15, 20, 25, \
     1,  2,  3, \
    10, 10, 10, \
    10, 10, 10, \
    10, 10, 10 ))

  f_vec = np.array ( ( \
     0.8975836176504333E+00, \
     0.9522670169E+00, \
     0.9711655571887813E+00, \
     0.8231218864E+00, \
     0.9049021510E+00, \
     0.9363471834E+00, \
     0.7301025986E+00, \
     0.8335594263E+00, \
     0.8774010255E+00, \
     0.5248571617E+00, \
     0.6293856597E+00, \
     0.6800271741E+00, \
     0.20590131975E+00, \
     0.2112148916E+00, \
     0.2074730718E+00, \
     0.9981130072E+00, \
     0.9994873850E+00, \
     0.9998391562E+00, \
     0.168610566972E+00, \
     0.16967950985E+00, \
     0.1701041003E+00, \
     0.9247683363E+00, \
     0.7483139269E+00, \
     0.4659802096E+00, \
     0.9761872541E+00, \
     0.8979689357E+00, \
     0.7181904627E+00, \
     0.9923658945E+00, \
     0.9610341649E+00, \
     0.8688007350E+00 ))

  lam_vec = np.array ( ( \
     0.0E+00, \
     0.0E+00, \
     0.0E+00, \
     0.5E+00, \
     0.5E+00, \
     0.5E+00, \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     2.0E+00, \
     2.0E+00, \
     2.0E+00, \
     4.0E+00, \
     4.0E+00, \
     4.0E+00, \
     7.0E+00, \
     7.0E+00, \
     7.0E+00, \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     2.0E+00, \
     3.0E+00, \
     4.0E+00, \
     2.0E+00, \
     3.0E+00, \
     4.0E+00, \
     2.0E+00, \
     3.0E+00, \
     4.0E+00 ))

  x_vec = np.array ( ( \
      3.00E+00, \
      3.00E+00, \
      3.00E+00, \
      3.00E+00, \
      3.00E+00, \
      3.00E+00, \
      3.00E+00, \
      3.00E+00, \
      3.00E+00, \
      3.00E+00, \
      3.00E+00, \
      3.00E+00, \
      3.00E+00, \
      3.00E+00, \
      3.00E+00, \
     15.00E+00, \
     15.00E+00, \
     15.00E+00, \
      0.05E+00, \
      0.05E+00, \
      0.05E+00, \
      4.00E+00, \
      4.00E+00, \
      4.00E+00, \
      5.00E+00, \
      5.00E+00, \
      5.00E+00, \
      6.00E+00, \
      6.00E+00, \
      6.00E+00 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    df = 0
    lam = 0.0
    x = 0.0
    f = 0.0
  else:
    df = df_vec[n_data]
    lam = lam_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, df, lam, x, f

def student_noncentral_cdf_values_test ( ):

#*****************************************************************************80
#
## STUDENT_NONCENTRAL_CDF_VALUES_TEST demonstrates the use of STUDENT_NONCENTRAL_CDF_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'STUDENT_NONCENTRAL_CDF_VALUES_TEST:'
  print '  STUDENT_NONCENTRAL_CDF_VALUES stores values of the STUDENT_NONCENTRAL_CDF function.'
  print ''
  print '      DF          LAM             X         CDF(DF,LAM,X)'
  print ''

  n_data = 0

  while ( True ):

    n_data, df, lam, x, f = student_noncentral_cdf_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %6d  %12g  %12g  %24.16g' % ( df, lam, x, f )

  print ''
  print 'STUDENT_NONCENTRAL_CDF_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  student_noncentral_cdf_values_test ( )
  timestamp ( )

