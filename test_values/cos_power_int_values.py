#!/usr/bin/env python
#
def cos_power_int_values ( n_data ):

#*****************************************************************************80
#
## COS_POWER_INT_VALUES returns some values of the cosine power integral.
#
#  Discussion:
#
#    The function has the form
#
#      COS_POWER_INT(A,B,N) = Integral ( A <= T <= B ) ( cos(T) )^N dt
#
#    In Mathematica, the function can be evaluated by:
#
#      Integrate [ ( Cos[x] )^n, { x, a, b } ]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 January 2015
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
#    Output, real A, B, the limits of integration.
#
#    Output, integer N, the power.
#
#    Output, real F, the function value.
#
  import numpy as np

  n_max = 11

  a_vec = np.array ( ( \
     0.00, \
     0.00, \
     0.00, \
     0.00, \
     0.00, \
     0.00, \
     0.00, \
     0.00, \
     0.00, \
     0.00, \
     0.00 ))

  b_vec = np.array ( ( \
     3.141592653589793, \
     3.141592653589793, \
     3.141592653589793, \
     3.141592653589793, \
     3.141592653589793, \
     3.141592653589793, \
     3.141592653589793, \
     3.141592653589793, \
     3.141592653589793, \
     3.141592653589793, \
     3.141592653589793  ) )

  f_vec = np.array ( ( \
     3.141592653589793, \
     0.0, \
     1.570796326794897, \
     0.0, \
     1.178097245096172, \
     0.0, \
     0.9817477042468104, \
     0.0, \
     0.8590292412159591, \
     0.0, \
     0.7731263170943632 ) )

  n_vec = np.array ( ( \
     0, \
     1, \
     2, \
     3, \
     4, \
     5, \
     6, \
     7, \
     8, \
     9, \
    10  ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    a = 0.0
    b = 0.0
    f = 0.0
    n = 0
  else:
    a = a_vec[n_data]
    b = b_vec[n_data]
    f = f_vec[n_data]
    n = n_vec[n_data]
    n_data = n_data + 1

  return n_data, a, b, n, f

def cos_power_int_values_test ( ):

#*****************************************************************************80
#
## COS_POWER_INT_VALUES_TEST tests COS_POWER_INT_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 January 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'COS_POWER_INT_VALUES_TEST:'
  print '  COS_POWER_INT_VALUES stores values of the cosine power integral.'
  print ''
  print '        A             B            N           F'
  print ''

  n_data = 0

  while ( True ):

    n_data, a, b, n, f = cos_power_int_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %12f  %12f  %6d  %24.16g' % ( a, b, n, f )

  print ''
  print 'COS_POWER_INT_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  cos_power_int_values_test ( )
  timestamp ( )
