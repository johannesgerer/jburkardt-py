#!/usr/bin/env python
#
def log_values ( n_data ):

#*****************************************************************************80
#
## LOG_VALUES returns some values of the logarithm function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      Log[x]
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
    -11.512925464970228420E+00, \
     -4.6051701859880913680E+00, \
     -2.3025850929940456840E+00, \
     -1.6094379124341003746E+00, \
     -1.2039728043259359926E+00, \
     -0.91629073187415506518E+00, \
     -0.69314718055994530942E+00, \
     -0.51082562376599068321E+00, \
     -0.35667494393873237891E+00, \
     -0.22314355131420975577E+00, \
     -0.10536051565782630123E+00, \
      0.00000000000000000000E+00, \
      0.69314718055994530942E+00, \
      1.0986122886681096914E+00, \
      1.1447298858494001741E+00, \
      1.6094379124341003746E+00, \
      2.3025850929940456840E+00, \
      2.9957322735539909934E+00, \
      4.6051701859880913680E+00, \
      18.631401766168018033E+00 ))

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

def log_values_test ( ):

#*****************************************************************************80
#
## LOG_VALUES_TEST demonstrates the use of LOG_VALUES.
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
  print 'LOG_VALUES_TEST:'
  print '  LOG_VALUES stores values of the LOG function.'
  print ''
  print '      X         LOG(X)'
  print ''

  n_data = 0

  while ( True ):

    n_data, x, f = log_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %12f  %24.16f' % ( x, f )

  print ''
  print 'LOG_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  log_values_test ( )
  timestamp ( )

