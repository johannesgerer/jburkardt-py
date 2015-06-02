#!/usr/bin/env python
#
def log10_values ( n_data ):

#*****************************************************************************80
#
## LOG10_VALUES returns some values of the logarithm 10 function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      Log10[x]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 February 2015
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
#    Input/output, integer N_DATA.  The user sets N_DATA to 0 
#    before the first call.  On each call, the routine increments N_DATA by 1,
#    and returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, real X, the argument of the function.
#
#    Output, real F, the value of the function.
#
  import numpy as np

  n_max = 20

  f_vec = np.array ( ( \
   -5.0000000000000000000, \
   -2.0000000000000000000, \
   -1.0000000000000000000, \
   -0.69897000433601880479, \
   -0.52287874528033756270, \
   -0.39794000867203760957, \
   -0.30102999566398119521, \
   -0.22184874961635636749, \
   -0.15490195998574316929, \
   -0.096910013008056414359, \
   -0.045757490560675125410, \
    0.000000000000000000000, \
    0.30102999566398119521, \
    0.47712125471966243730, \
    0.49714987269413385435, \
    0.69897000433601880479, \
    1.0000000000000000000, \
    1.3010299956639811952, \
    2.0000000000000000000, \
    8.0915149771692704475 ))

  x_vec = np.array ( ( \
   1.0E-05,  \
   1.0E-02,  \
   0.1,  \
   0.2,  \
   0.3,  \
   0.4,  \
   0.5,  \
   0.6,  \
   0.7,  \
   0.8,  \
   0.9,  \
   1.0,  \
   2.0,  \
   3.0,  \
   3.1415926535897932385,  \
   5.0,  \
   10.0,  \
   20.0, \
   100.0, \
   123456789.0 ))

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

def log10_values_test ( ):

#*****************************************************************************80
#
## LOG10_VALUES_TEST demonstrates the use of LOG10_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'LOG10_VALUES_TEST:'
  print '  LOG10_VALUES stores values of the LOG10 function.'
  print ''
  print '      X         LOG10(X)'
  print ''

  n_data = 0

  while ( True ):

    n_data, x, f = log10_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %12f  %24.16f' % ( x, f )

  print ''
  print 'LOG10_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  log10_values_test ( )
  timestamp ( )

