#!/usr/bin/env python
#
def si_values ( n_data ):

#*****************************************************************************80
#
## SI_VALUES returns some values of the sine integral function.
#
#  Discussion:
#
#    SI(X) = integral ( 0 <= T <= X ) sin ( T ) / T dt
#
#    In Mathematica, the function can be evaluated by:
#
#      SinIntegral[x]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 February 2015
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
#    Output, real F, the value of the function.
#
  import numpy as np

  n_max = 16

  f_vec = np.array ( ( \
     0.4931074180430667E+00, \
     0.5881288096080801E+00, \
     0.6812222391166113E+00, \
     0.7720957854819966E+00, \
     0.8604707107452929E+00, \
     0.9460830703671830E+00, \
     0.1108047199013719E+01, \
     0.1256226732779218E+01, \
     0.1389180485870438E+01, \
     0.1505816780255579E+01, \
     0.1605412976802695E+01, \
     0.1778520173443827E+01, \
     0.1848652527999468E+01, \
     0.1833125398665997E+01, \
     0.1758203138949053E+01, \
     0.1654140414379244E+01 ))

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
      4.5E+00 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    x = 0.0
    f = 0.0
  else:
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, x, f

def si_values_test ( ):

#*****************************************************************************80
#
## SI_VALUES_TEST demonstrates the use of SI_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 January 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'SI_VALUES_TEST:'
  print '  SI_VALUES stores values of the SI function.'
  print ''
  print '      X         SI(X)'
  print ''

  n_data = 0

  while ( True ):

    n_data, x, f = si_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %12f  %24.16f' % ( x, f )

  print ''
  print 'SI_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  si_values_test ( )
  timestamp ( )

