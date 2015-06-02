#!/usr/bin/env python
#
def airy_ai_prime_values ( n_data ):

#*****************************************************************************80
#
## AIRY_AI_PRIME_VALUES returns some values of the Airy function Ai'(x).
#
#  Discussion:
#
#    The Airy functions Ai(X) and Bi(X) are a pair of linearly independent
#    solutions of the differential equation:
#
#      W'' - X * W = 0
#
#    In Mathematica, the function can be evaluated by:
#
#      AiryAiPrime[x]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 September 2004
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
#    Output, real AIP, the derivative of the Airy AI function.
#
  import numpy as np

  n_max = 11

  fx_vec = np.array ( ( \
     -0.2588194037928068E+00, \
     -0.2571304219075862E+00, \
     -0.2524054702856195E+00, \
     -0.2451463642190548E+00, \
     -0.2358320344192082E+00, \
     -0.2249105326646839E+00, \
     -0.2127932593891585E+00, \
     -0.1998511915822805E+00, \
     -0.1864128638072717E+00, \
     -0.1727638434616347E+00, \
     -0.1591474412967932E+00 ) )

  x_vec = np.array ( ( \
     0.0E+00, \
     0.1E+00, \
     0.2E+00, \
     0.3E+00, \
     0.4E+00, \
     0.5E+00, \
     0.6E+00, \
     0.7E+00, \
     0.8E+00, \
     0.9E+00, \
     1.0E+00 ) )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    x = 0.0
    fx = 0.0
  else:
    x = x_vec[n_data]
    fx = fx_vec[n_data]
    n_data =n_data + 1

  return n_data, x, fx

def airy_ai_prime_values_test ( ):

#*****************************************************************************80
#
## AIRY_AI_PRIME_VALUES_TEST demonstrates the use of AIRY_AI_PRIME_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 December 2014
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'AIRY_AI_PRIME_VALUES_TEST:'
  print '  AIRY_AI_PRIME_VALUES stores values of'
  print '  the derivative of the Airy Ai function.'
  print ''
  print '      X           FX'
  print ''

  n_data = 0

  while ( True ):

    n_data, x, fx = airy_ai_prime_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %12f  %24.16f' % ( x, fx )

  print ''
  print 'AIRY_AI_PRIME_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  airy_ai_prime_values_test ( )
  timestamp ( )

