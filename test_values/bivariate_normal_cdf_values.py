#!/usr/bin/env python
#
def bivariate_normal_cdf_values ( n_data ):

#*****************************************************************************80
#
## BIVARIATE_NORMAL_CDF_VALUES returns some values of the bivariate normal CDF.
#
#  Discussion:
#
#    FXY is the probability that two variables A and B, which are
#    related by a bivariate normal distribution with correlation R,
#    respectively satisfy A <= X and B <= Y.
#
#    Mathematica can evaluate the bivariate normal CDF via the commands:
#
#      <<MultivariateStatistics`
#      cdf = CDF[MultinormalDistribution[{0,0}{{1,r},{r,1}}],{x,y}]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    National Bureau of Standards,
#    Tables of the Bivariate Normal Distribution and Related Functions,
#    NBS, Applied Mathematics Series, Number 50, 1959.
#
#  Parameters:
#
#    Input, integer N_DATA.  The user sets N_DATA to 0 before the
#    first call.
#
#    Output, integer N_DATA, the routine increments the input value of N_DATA
#    by 1, and returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, real X, Y, the parameters of the function.
#
#    Output, real R, the correlation value.
#
#    Output, real F, the value of the function.
#
  import numpy as np

  n_max = 41

  f_vec = np.array ( ( \
  0.02260327218569867, \
  0.1548729518584100, \
  0.4687428083352184, \
  0.7452035868929476, \
  0.8318608306874188, \
  0.8410314261134202, \
  0.1377019384919464, \
  0.1621749501739030, \
  0.1827411243233119, \
  0.2010067421506235, \
  0.2177751155265290, \
  0.2335088436446962, \
  0.2485057781834286, \
  0.2629747825154868, \
  0.2770729823404738, \
  0.2909261168683812, \
  0.3046406378726738, \
  0.3183113449213638, \
  0.3320262544108028, \
  0.3458686754647614, \
  0.3599150462310668, \
  0.3742210899871168, \
  0.3887706405282320, \
  0.4032765198361344, \
  0.4162100291953678, \
  0.6508271498838664, \
  0.8318608306874188, \
  0.0000000000000000, \
  0.1666666666539970, \
  0.2500000000000000, \
  0.3333333333328906, \
  0.5000000000000000, \
  0.7452035868929476, \
  0.1548729518584100, \
  0.1548729518584100, \
  0.06251409470431653, \
  0.7452035868929476, \
  0.1548729518584100, \
  0.1548729518584100, \
  0.06251409470431653, \
  0.6337020457912916 ) )

  r_vec = np.array ( ( \
     0.500,  0.500,  0.500,  0.500,  0.500, \
     0.500, -0.900, -0.800, -0.700, -0.600, \
    -0.500, -0.400, -0.300, -0.200, -0.100, \
     0.000,  0.100,  0.200,  0.300,  0.400, \
     0.500,  0.600,  0.700,  0.800,  0.900, \
     0.673,  0.500, -1.000, -0.500,  0.000, \
     0.500,  1.000,  0.500,  0.500,  0.500, \
     0.500,  0.500,  0.500,  0.500,  0.500, \
     0.500  ) )

  x_vec = np.array ( ( \
    -2.0, -1.0,  0.0,  1.0,  2.0, \
     3.0, -0.2, -0.2, -0.2, -0.2, \
    -0.2, -0.2, -0.2, -0.2, -0.2, \
    -0.2, -0.2, -0.2, -0.2, -0.2, \
    -0.2, -0.2, -0.2, -0.2, -0.2, \
     1.0,  2.0,  0.0,  0.0,  0.0, \
     0.0,  0.0,  1.0,  1.0, -1.0, \
    -1.0,  1.0,  1.0, -1.0, -1.0, \
     0.7071067811865475 ))

  y_vec = np.array ( ( \
     1.0,  1.0,  1.0,  1.0,  1.0, \
     1.0,  0.5,  0.5,  0.5,  0.5, \
     0.5,  0.5,  0.5,  0.5,  0.5, \
     0.5,  0.5,  0.5,  0.5,  0.5, \
     0.5,  0.5,  0.5,  0.5,  0.5, \
     0.5,  1.0,  0.0,  0.0,  0.0, \
     0.0,  0.0,  1.0, -1.0,  1.0, \
    -1.0,  1.0, -1.0,  1.0, -1.0, \
     0.7071067811865475 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    x = 0.0
    y = 0.0
    r = 0.0
    f = 0.0
  else:
    x = x_vec[n_data]
    y = y_vec[n_data]
    r = r_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, x, y, r, f

def bivariate_normal_cdf_values_test ( ):

#*****************************************************************************80
#
## BIVARIATE_NORMAL_CDF_VALUES_TEST tests BIVARIATE_NORMAL_CDF_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 January 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'BIVARIATE_NORMAL_CDF_VALUES_TEST:'
  print '  BIVARIATE_NORMAL_CDF_VALUES stores values of the bivariate normal CDF.'
  print ''
  print '      X         Y         R        BIVARIATE_NORMAL_CDF(X,Y,R)'
  print ''

  n_data = 0

  while ( True ):

    n_data, x, y, r, f = bivariate_normal_cdf_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %12f  %12f  %12f  %24.16g' % ( x, y, r, f )

  print ''
  print 'BIVARIATE_NORMAL_CDF_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  bivariate_normal_cdf_values_test ( )
  timestamp ( )

