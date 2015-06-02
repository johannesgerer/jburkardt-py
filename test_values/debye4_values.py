#!/usr/bin/env python
#
def debye4_values ( n_data ):

#*****************************************************************************80
#
## returns some values of Debye's function of order 4.
#
#  Discussion:
#
#    The function is defined by:
#
#      DEBYE4(x) = 4 / x^4 * Integral ( 0 <= t <= x ) t^4 / ( exp ( t ) - 1 ) dt
#
#    The data was reported by McLeod.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
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
      0.99921896192761576256E+00, \
      0.98755425280996071022E+00, \
      0.95086788606389739976E+00, \
      0.81384569172034042516E+00, \
      0.65487406888673697092E+00, \
      0.52162830964878715188E+00, \
      0.41189273671788528876E+00, \
      0.32295434858707304628E+00, \
      0.25187863642883314410E+00, \
      0.15185461258672022043E+00, \
      0.13372661145921413299E+00, \
      0.91471377664481164749E-01, \
      0.71227828197462523663E-01, \
      0.55676547822738862783E-01, \
      0.21967566525574960096E-01, \
      0.96736755602711590082E-02, \
      0.19646978158351837850E-02, \
      0.62214648623965450200E-03, \
      0.12289514092077854510E-03, \
      0.15927210319002161231E-04 ))

  x_vec = np.array ( ( \
       0.0019531250E+00, \
       0.0312500000E+00, \
       0.1250000000E+00, \
       0.5000000000E+00, \
       1.0000000000E+00, \
       1.5000000000E+00, \
       2.0000000000E+00, \
       2.5000000000E+00, \
       3.0000000000E+00, \
       4.0000000000E+00, \
       4.2500000000E+00, \
       5.0000000000E+00, \
       5.5000000000E+00, \
       6.0000000000E+00, \
       8.0000000000E+00, \
      10.0000000000E+00, \
      15.0000000000E+00, \
      20.0000000000E+00, \
      30.0000000000E+00, \
      50.0000000000E+00 ))

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

def debye4_values_test ( ):

#*****************************************************************************80
#
## DEBYE4_VALUES_TEST demonstrates the use of DEBYE4_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'DEBYE4_VALUES_TEST:'
  print '  DEBYE4_VALUES stores values of the Debye function of order 4.'
  print ''
  print '      X         F(X)'
  print ''

  n_data = 0

  while ( True ):

    n_data, x, fx = debye4_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %12f  %24.16f' % ( x, fx )

  print ''
  print 'DEBYE4_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  debye4_values_test ( )
  timestamp ( )

