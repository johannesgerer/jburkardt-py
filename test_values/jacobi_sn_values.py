#!/usr/bin/env python
#
def jacobi_sn_values ( n_data ):

#*****************************************************************************80
#
## JACOBI_SN_VALUES returns some values of the Jacobi elliptic function SN(A,X).
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      JacobiSN[ x, a ]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 February 2015
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
#    Output, real A, the parameter of the function.
#
#    Output, real X, the argument of the function.
#
#    Output, real F, the value of the function.
#
  import numpy as np

  n_max = 20

  a_vec = np.array ( ( \
     0.0E+00, \
     0.0E+00, \
     0.0E+00, \
     0.0E+00, \
     0.0E+00, \
     0.5E+00, \
     0.5E+00, \
     0.5E+00, \
     0.5E+00, \
     0.5E+00, \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     1.0E+00 ))

  f_vec = np.array ( ( \
      0.9983341664682815E-01, \
      0.1986693307950612E+00, \
      0.4794255386042030E+00, \
      0.8414709848078965E+00, \
      0.9092974268256817E+00, \
      0.9975068547462484E-01, \
      0.1980217429819704E+00, \
      0.4707504736556573E+00, \
      0.8030018248956439E+00, \
      0.9946623253580177E+00, \
      0.9966799462495582E-01, \
      0.1973753202249040E+00, \
      0.4621171572600098E+00, \
      0.7615941559557649E+00, \
      0.9640275800758169E+00, \
      0.9993292997390670E+00, \
     -0.1973753202249040E+00, \
     -0.4621171572600098E+00, \
     -0.7615941559557649E+00, \
     -0.9640275800758169E+00 ))

  x_vec = np.array ( ( \
      0.1E+00, \
      0.2E+00, \
      0.5E+00, \
      1.0E+00, \
      2.0E+00, \
      0.1E+00, \
      0.2E+00, \
      0.5E+00, \
      1.0E+00, \
      2.0E+00, \
      0.1E+00, \
      0.2E+00, \
      0.5E+00, \
      1.0E+00, \
      2.0E+00, \
      4.0E+00, \
     -0.2E+00, \
     -0.5E+00, \
     -1.0E+00, \
     -2.0E+00 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    a = 0.0
    x = 0.0
    f = 0.0
  else:
    a = a_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, a, x, f

def jacobi_sn_values_test ( ):

#*****************************************************************************80
#
## JACOBI_SN_VALUES_TEST demonstrates the use of JACOBI_SN_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'JACOBI_SN_VALUES_TEST:'
  print '  JACOBI_SN_VALUES stores values of the Jacobi SN function.'
  print ''
  print '      A         X        JACOBI_SN(A,X)'
  print ''

  n_data = 0

  while ( True ):

    n_data, a, x, f = jacobi_sn_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %12f  %12f  %24.16g' % ( a, x, f )

  print ''
  print 'JACOBI_SN_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  jacobi_sn_values_test ( )
  timestamp ( )

