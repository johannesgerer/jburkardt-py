#!/usr/bin/env python
#
def debye3_values ( n_data ):

#*****************************************************************************80
#
## DEBYE3_VALUES returns some values of Debye's function of order 3.
#
#  Discussion:
#
#    The function is defined by:
#
#      DEBYE3(x) = 3 / x^3 * Integral ( 0 <= t <= x ) t^3 / ( exp ( t ) - 1 ) dt
#
#    The data was reported by McLeod.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 September 2004
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
      0.99926776885985461940E+00, \
      0.98833007755734698212E+00, \
      0.95390610472023510237E+00, \
      0.82496296897623372315E+00, \
      0.67441556407781468010E+00, \
      0.54710665141286285468E+00, \
      0.44112847372762418113E+00, \
      0.35413603481042394211E+00, \
      0.28357982814342246206E+00, \
      0.18173691382177474795E+00, \
      0.16277924385112436877E+00, \
      0.11759741179993396450E+00, \
      0.95240802723158889887E-01, \
      0.77581324733763020269E-01, \
      0.36560295673194845002E-01, \
      0.19295765690345489563E-01, \
      0.57712632276188798621E-02, \
      0.24352200674805479827E-02, \
      0.72154882216335666096E-03, \
      0.15585454565440389896E-03 ))

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

def debye3_values_test ( ):

#*****************************************************************************80
#
## DEBYE3_VALUES_TEST demonstrates the use of DEBYE3_VALUES.
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
  print 'DEBYE3_VALUES_TEST:'
  print '  DEBYE3_VALUES stores values of the Debye function of order 3.'
  print ''
  print '      X         F(X)'
  print ''

  n_data = 0

  while ( True ):

    n_data, x, fx = debye3_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %12f  %24.16f' % ( x, fx )

  print ''
  print 'DEBYE3_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  debye3_values_test ( )
  timestamp ( )

