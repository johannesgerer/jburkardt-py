#!/usr/bin/env python
#
def hermite_function_values ( n_data ):

#*****************************************************************************80
#
## HERMITE_FUNCTION_VALUES: values of the Hermite function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      Hf(n,x) = HermiteH[n,x] 
#        * Exp [ -1/2 * x^2] / Sqrt [ 2^n * n! * Sqrt[Pi] ]
#
#    The Hermite functions are orthonormal:
#
#      Integral ( -oo < x < +oo ) Hf(m,x) Hf(n,x) dx = delta ( m, n )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 February 2015
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
#    Output, integer N, the order of the polynomial.
#
#    Output, real X, the point where the polynomial is evaluated.
#
#    Output, real F, the value of the function.
#
  import numpy as np

  n_max = 23

  f_vec = np.array ( ( \
    0.7511255444649425E+00,  0.0000000000000000E+00, -0.5311259660135985E+00, \
    0.0000000000000000E+00,  0.4599685791773266E+00,  0.0000000000000000E+00, \
    0.4555806720113325E+00,  0.6442883651134752E+00,  0.3221441825567376E+00, \
   -0.2630296236233334E+00, -0.4649750762925110E+00, -0.5881521185179581E-01, \
    0.3905052515434106E+00,  0.2631861423064045E+00, -0.2336911435996523E+00, \
   -0.3582973361472840E+00,  0.6146344487883041E-01,  0.3678312067984882E+00, \
    0.9131969309166278E-01,  0.4385750950032321E+00, -0.2624689527931006E-01, \
    0.5138426125477819E+00,  0.09355563118061758E+00 ))

  n_vec = np.array ( ( \
    0,  1,  2,  \
    3,  4,  5,  \
    0,  1,  2,  \
    3,  4,  5,  \
    6,  7,  8,  \
    9, 10, 11,  \
   12,  5,  5,  \
    5,  5  ))

  x_vec = np.array ( ( \
    0.0E+00, 0.0E+00, 0.0E+00, \
    0.0E+00, 0.0E+00, 0.0E+00, \
    1.0E+00, 1.0E+00, 1.0E+00, \
    1.0E+00, 1.0E+00, 1.0E+00, \
    1.0E+00, 1.0E+00, 1.0E+00, \
    1.0E+00, 1.0E+00, 1.0E+00, \
    1.0E+00, 0.5E+00, 2.0E+00, \
    3.0E+00, 4.0E+00 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    x = 0.0
    f = 0.0
  else:
    n = n_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, n, x, f

def hermite_function_values_test ( ):

#*****************************************************************************80
#
## HERMITE_FUNCTION_VALUES_TEST demonstrates the use of HERMITE_FUNCTION_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'HERMITE_FUNCTION_VALUES_TEST:'
  print '  HERMITE_FUNCTION_VALUES stores values of the Hermite function.'
  print ''
  print '      N            X            F'
  print ''

  n_data = 0

  while ( True ):

    n_data, n, x, f = hermite_function_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %6d  %12g  %24.16g' % ( n, x, f )

  print ''
  print 'HERMITE_FUNCTION_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  hermite_function_values_test ( )
  timestamp ( )

