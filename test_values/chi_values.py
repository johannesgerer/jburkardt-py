#!/usr/bin/env python
#
def chi_values ( n_data ):

#*****************************************************************************80
#
## CHI_VALUES returns some values of the hyperbolic cosine integral function.
#
#  Discussion:
#
#      CHI(X) = gamma + log ( x ) 
#        + integral ( 0 <= T < X ) ( cosh ( T ) - 1 ) / T  dT
#
#    where gamma is Euler's constant.
#
#    In Mathematica, the function can be evaluated by:
#
#      CoshIntegral[x]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz, Irene Stegun,
#    Handbook of Mathematical Functions,
#    National Bureau of Standards, 1964,
#    ISBN: 0-486-61272-4,
#    LC: QA47.A34.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Cambridge University Press, 1999,
#    ISBN: 0-521-64314-7,
#    LC: QA76.95.W65.
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
    -0.05277684495649362, \
     0.1577508933739787, \
     0.3455691756953907, \
     0.5183999848333915, \
     0.6813138871854339, \
     0.8378669409802082, \
     1.141841924170595, \
     1.445494075789644, \
     1.759505807660965, \
     2.092577214062032, \
     2.452666922646915, \
     3.524425488354165, \
     4.960392094765610, \
     6.959191927647393, \
     9.813547558823186, \
    13.96581164859243 ) )

  x_vec = np.array ( ( \
      0.5E+00, \
      0.6E+00, \
      0.7E+00, \
      0.8E+00, \
      0.9E+00, \
      1.0E+00, \
      1.2E+00, \
      1.4E+00, \
      1.6E+00, \
      1.8E+00, \
      2.0E+00, \
      2.5E+00, \
      3.0E+00, \
      3.5E+00, \
      4.0E+00, \
      4.5E+00 ) )

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

def chi_values_test ( ):

#*****************************************************************************80
#
## CHI_VALUES_TEST demonstrates the use of CHI_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 January 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'CHI_VALUES_TEST:'
  print '  CHI_VALUES stores values of the hyperbolic cosine integral function.'
  print ''
  print '      X         CHI(X)'
  print ''

  n_data = 0

  while ( True ):

    n_data, x, fx = chi_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %12f  %24.16f' % ( x, fx )

  print ''
  print 'CHI_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  chi_values_test ( )
  timestamp ( )

