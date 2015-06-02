#!/usr/bin/env python
#
def fresnel_cos_values ( n_data ):

#*****************************************************************************80
#
## FRESNEL_COS_VALUES returns values of the Fresnel cosine integral function.
#
#  Discussion:
#
#    The Fresnel cosine integral is defined by:
#
#      C(X) = integral ( 0 <= T <= X ) cos ( PI * T^2 / 2 ) / T dT
#
#    In Mathematica, the function can be evaluated by:
#
#      FresnelC[x]
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
#    Output, real X, the argument of the function.
#
#    Output, real FX, the value of the function.
#
  import numpy as np

  n_max = 16

  fx_vec = np.array ( ( \
     0.0000000000000000E+00, \
     0.1999210575944531E+00, \
     0.3974807591723594E+00, \
     0.5810954469916523E+00, \
     0.7228441718963561E+00, \
     0.7798934003768228E+00, \
     0.7154377229230734E+00, \
     0.5430957835462564E+00, \
     0.3654616834404877E+00, \
     0.3336329272215571E+00, \
     0.4882534060753408E+00, \
     0.6362860449033195E+00, \
     0.5549614058564281E+00, \
     0.3889374961919690E+00, \
     0.4674916516989059E+00, \
     0.6057207892976856E+00 ))

  x_vec = np.array ( ( \
     0.0E+00, \
     0.2E+00, \
     0.4E+00, \
     0.6E+00, \
     0.8E+00, \
     1.0E+00, \
     1.2E+00, \
     1.4E+00, \
     1.6E+00, \
     1.8E+00, \
     2.0E+00, \
     2.2E+00, \
     2.4E+00, \
     2.6E+00, \
     2.8E+00, \
     3.0E+00 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    x = 0.0
    fx = 0.0
  else:
    x = x_vec[n_data]
    fx = fx_vec[n_data]
    n_data = n_data + 1

  return n_data, x, fx

def fresnel_cos_values_test ( ):

#*****************************************************************************80
#
## FRESNEL_COS_VALUES_TEST demonstrates the use of FRESNEL_COS_VALUES.
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
  print 'FRESNEL_COS_VALUES_TEST:'
  print '  FRESNEL_COS_VALUES stores values of the Fresnel cosine integral.'
  print ''
  print '        X              F'
  print ''

  n_data = 0

  while ( True ):

    n_data, x, fx = fresnel_cos_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %12f  %24.16f' % ( x, fx )

  print ''
  print 'FRESNEL_COS_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  fresnel_cos_values_test ( )
  timestamp ( )

