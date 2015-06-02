#!/usr/bin/env python
#
def gamma_inc_q_values ( n_data ):

#*****************************************************************************80
#
## GAMMA_INC_Q_VALUES: values of the normalized incomplete Gamma function Q(A,X).
#
#  Discussion:
#
#    The (normalized) incomplete Gamma function is defined as:
#
#      Q(A,X) = 1/Gamma(A) * Integral ( X <= T < oo ) T^(A-1) * exp(-T) dT.
#
#    With this definition, for all A and X,
#
#      0 <= Q(A,X) <= 1
#
#    and
#
#      Q(A,INFINITY) = 0.0
#
#    In Mathematica, the function can be evaluated by:
#
#      GammaRegularized[A,X]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 February 2015
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
     0.10E+00, \
     0.10E+00, \
     0.10E+00, \
     0.50E+00, \
     0.50E+00, \
     0.50E+00, \
     0.10E+01, \
     0.10E+01, \
     0.10E+01, \
     0.11E+01, \
     0.11E+01, \
     0.11E+01, \
     0.20E+01, \
     0.20E+01, \
     0.20E+01, \
     0.60E+01, \
     0.60E+01, \
     0.11E+02, \
     0.26E+02, \
     0.41E+02  ))

  f_vec = np.array ( ( \
    0.2617649467660649, \
    0.09164201026996572, \
    0.01134401663780527, \
    0.6985353583033387, \
    0.2206713619198468, \
    0.008150971593502700, \
    0.9048374180359596, \
    0.3678794411714423, \
    0.006737946999085467, \
    0.9279402542394568, \
    0.4108190381293515, \
    0.008463184015447498, \
    0.9898141728888165, \
    0.5578254003710746, \
    0.007295055724436130, \
    0.9579789618046939, \
    0.02034102941692837, \
    0.07739601577035708, \
    0.5529214200244148, \
    0.2555450779281301 ))

  x_vec = np.array ( ( \
     0.30E-01, \
     0.30E+00, \
     0.15E+01, \
     0.75E-01, \
     0.75E+00, \
     0.35E+01, \
     0.10E+00, \
     0.10E+01, \
     0.50E+01, \
     0.10E+00, \
     0.10E+01, \
     0.50E+01, \
     0.15E+00, \
     0.15E+01, \
     0.70E+01, \
     0.25E+01, \
     0.12E+02, \
     0.16E+02, \
     0.25E+02, \
     0.45E+02 ))

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

def gamma_inc_q_values_test ( ):

#*****************************************************************************80
#
## GAMMA_INC_Q_VALUES_TEST demonstrates the use of GAMMA_INC_Q_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'GAMMA_INC_Q_VALUES_TEST:'
  print '  GAMMA_INC_Q_VALUES stores values of an incomplete Gamma function.'
  print ''
  print '      A         X        GAMMA_INC_Q(A,X)'
  print ''

  n_data = 0

  while ( True ):

    n_data, a, x, f = gamma_inc_q_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %12f  %12f  %24.16g' % ( a, x, f )

  print ''
  print 'GAMMA_INC_Q_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  gamma_inc_q_values_test ( )
  timestamp ( )

