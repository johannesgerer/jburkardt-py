#!/usr/bin/env python
#
def r8_rise_values ( n_data ):

#*****************************************************************************80
#
## R8_RISE_VALUES returns values of the rising factorial function.
#
#  Discussion:
#
#    The rising factorial function is sometimes symbolized by (m)_n.
#
#    The definition is
#
#      (m)_n = (m-1+n)! / (m-1)!
#            = ( m ) * ( m + 1 ) * ( m + 2 ) \ * ( m - 1 + n )
#            = Gamma ( m + n ) / Gamma ( m )
#
#    We assume 0 <= N <= M.
#
#    In Mathematica, the function can be evaluated by:
#
#      Pochhammer[m,n]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 December 2014
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
#    Output, real X, integer N, the arguments of the function.
#
#    Output, real F, the value of the function.
#
  import numpy as np

  n_max = 15

  f_vec = np.array ( [ 
       1680.000000000000, \
       1962.597656250000, \
       2279.062500000000, \
       2631.972656250000, \
       3024.000000000000, \
       1.000000000000000, \
       7.500000000000000, \
       63.75000000000000, \
       605.6250000000000, \
       6359.062500000000, \
       73129.21875000000, \
       914115.2343750000, \
       1.234055566406250E+07, \
       1.789380571289063E+08, \
       2.773539885498047E+09 ] )

  n_vec = np.array ( [ 
       4, \
       4, \
       4, \
       4, \
       4, \
       0, \
       1, \
       2, \
       3, \
       4, \
       5, \
       6, \
       7, \
       8, \
       9 ] )

  x_vec = np.array ( [ 
       5.00, \
       5.25, \
       5.50, \
       5.75, \
       6.00, \
       7.50, \
       7.50, \
       7.50, \
       7.50, \
       7.50, \
       7.50, \
       7.50, \
       7.50, \
       7.50, \
       7.50 ] )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    x = 0.0
    n = 0
    f = 0.0
  else:
    x = x_vec[n_data]
    n = n_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, x, n, f

def r8_rise_values_test ( ):

#*****************************************************************************80
#
## R8_RISE_VALUES_TEST tests R8_RISE_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 December 2014
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'R8_RISE_VALUES_TEST:'
  print '  R8_RISE_VALUES returns values of the rising factorial.'
  print ''
  print '          X         N          R8_RISE(X,N)'
  print ''

  n_data = 0

  while ( True ):

    n_data, x, n, f = r8_rise_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %8.4f  %8d  %24.16g' % ( x, n, f )

  print ''
  print 'R8_RISE_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_rise_values_test ( )
  timestamp ( )

