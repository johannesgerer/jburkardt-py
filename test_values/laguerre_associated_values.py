#!/usr/bin/env python
#
def laguerre_associated_values ( n_data ):

#*****************************************************************************80
#
## LAGUERRE_ASSOCIATED_VALUES returns some values of the associated Laguerre polynomials.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      LaguerreL[n,m,x]
#
#    The associated Laguerre polynomials may be generalized so that the 
#    parameter M is allowed to take on arbitrary noninteger values.
#    The resulting function is known as the generalized Laguerre function.
#    
#    The polynomials satisfy the differential equation:
#
#      X * Y'' + (M+1-X) * Y' + (N-M) * Y = 0
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
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
#    Output, integer N, the order of the function.
#
#    Output, integer M, the parameter.
#
#    Output, real X, the point where the function is evaluated.
#
#    Output, real F, the value of the function.
#
  import numpy as np

  n_max = 20

  f_vec = np.array ( ( \
     0.1000000000000000E+01, \
     0.1000000000000000E+01, \
     0.1000000000000000E+01, \
     0.1000000000000000E+01, \
     0.1000000000000000E+01, \
     0.1500000000000000E+01, \
     0.1625000000000000E+01, \
     0.1479166666666667E+01, \
     0.1148437500000000E+01, \
     0.4586666666666667E+00, \
     0.2878666666666667E+01, \
     0.8098666666666667E+01, \
     0.1711866666666667E+02, \
     0.1045328776041667E+02, \
     0.1329019368489583E+02, \
     0.5622453647189670E+02, \
     0.7484729341779436E+02, \
     0.3238912982762806E+03, \
     0.4426100000097533E+03, \
     0.1936876572288250E+04 ))

  m_vec = np.array ( ( \
    0, 0, 0, 0, \
    0, 1, 1, 1, \
    1, 0, 1, 2, \
    3, 2, 2, 3, \
    3, 4, 4, 5 ))

  n_vec = np.array ( ( \
    1,  2,  3,  4, \
    5,  1,  2,  3, \
    4,  3,  3,  3, \
    3,  4,  5,  6, \
    7,  8,  9, 10 ))

  x_vec = np.array ( ( \
     0.00E+00, \
     0.00E+00, \
     0.00E+00, \
     0.00E+00, \
     0.00E+00, \
     0.50E+00, \
     0.50E+00, \
     0.50E+00, \
     0.50E+00, \
     0.20E+00, \
     0.20E+00, \
     0.20E+00, \
     0.20E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00 ))

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

def laguerre_associated_values_test ( ):

#*****************************************************************************80
#
## LAGUERRE_ASSOCIATED_VALUES_TEST demonstrates the use of LAGUERRE_ASSOCIATED_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'LAGUERRE_ASSOCIATED_VALUES_TEST:'
  print '  LAGUERRE_ASSOCIATED_VALUES stores values of the associated Laguerre function.'
  print ''
  print '      N       M            X            F'
  print ''

  n_data = 0

  while ( True ):

    n_data, n, m, x, f = laguerre_associated_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %6d  %6d  %12f  %24.16g' % ( n, m, x, f )

  print ''
  print 'LAGUERRE_ASSOCIATED_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  laguerre_associated_values_test ( )
  timestamp ( )

