#!/usr/bin/env python
#
def abram1_values ( n_data ):

#*****************************************************************************80
#
## ABRAM1_VALUES returns some values of the Abramowitz1 function.
#
#  Discussion:
#
#    The function is defined by:
#
#      ABRAM1(x) = integral ( 0 <= t < infinity ) t * exp ( -t^2 - x / t ) dt
#
#    The data was reported by McLeod.
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
#    Allan McLeod,
#    Algorithm 757, MISCFUN: A software package to compute uncommon
#      special functions,
#    ACM Transactions on Mathematical Software,
#    Volume 22, Number 3, September 1996, pages 288-301.
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

  n_max = 20

  fx_vec = np.array ( ( \
     0.49828219848799921792E+00, \
     0.49324391773047288556E+00, \
     0.47431612784691234649E+00, \
     0.41095983258760410149E+00, \
     0.25317617388227035867E+00, \
     0.14656338138597777543E+00, \
     0.11421547056018366587E+00, \
     0.90026307383483764795E-01, \
     0.64088214170742303375E-01, \
     0.57446614314166191085E-01, \
     0.51581624564800730959E-01, \
     0.25263719555776416016E-01, \
     0.11930803330196594536E-01, \
     0.59270542280915272465E-02, \
     0.30609215358017829567E-02, \
     0.16307382136979552833E-02, \
     0.28371851916959455295E-03, \
     0.21122150121323238154E-04, \
     0.20344578892601627337E-05, \
     0.71116517236209642290E-09 ) )

  x_vec = np.array ( ( \
     0.0019531250E+00, \
     0.0078125000E+00, \
     0.0312500000E+00, \
     0.1250000000E+00, \
     0.5000000000E+00, \
     1.0000000000E+00, \
     1.2500000000E+00, \
     1.5000000000E+00, \
     1.8750000000E+00, \
     2.0000000000E+00, \
     2.1250000000E+00, \
     3.0000000000E+00, \
     4.0000000000E+00, \
     5.0000000000E+00, \
     6.0000000000E+00, \
     7.0000000000E+00, \
     10.0000000000E+00, \
     15.0000000000E+00, \
     20.0000000000E+00, \
     40.0000000000E+00 ) )

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

def abram1_values_test ( ):

#*****************************************************************************80
#
## ABRAM1_VALUES_TEST demonstrates the use of ABRAM1_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 April 2007
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'ABRAM1_VALUES_TEST:'
  print '  ABRAM1_VALUES stores values of'
  print '  the Abramowitz function of order 1.'
  print ''
  print '      X           FX'
  print ''

  n_data = 0

  while ( True ):

    n_data, x, fx = abram1_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %12f  %24.16f' % ( x, fx )

  print ''
  print 'ABRAM1_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  abram1_values_test ( )
  timestamp ( )
