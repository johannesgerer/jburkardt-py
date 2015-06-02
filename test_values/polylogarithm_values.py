#!/usr/bin/env python
#
def polylogarithm_values ( n_data ):

#*****************************************************************************80
#
## POLYLOGARITHM_VALUES returns some values of the polylogarithm.
#
#  Discussion:
#
#    The polylogarithm of n and z is defined as
#
#      f[n,z] = Sum ( 1 <= k < infinity ) z^k / k^n
#
#    In Mathematica, the function can be evaluated by:
#
#      PolyLog[n,z]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 February 2015
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
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Parameters:
#
#    Input/output, integer N_DATA.  The user sets N_DATA to 0 before the
#    first call.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, integer N, the exponent of the denominator.
#
#    Output, real Z, the base of the numerator.
#
#    Output, real F, the value of the function.
#
  import numpy as np

  n_max = 12

  f_vec = np.array ( ( \
     0.1644934066848226E+01, \
     0.1202056903159594E+01, \
     0.1000994575127818E+01, \
     0.5822405264650125E+00, \
     0.5372131936080402E+00, \
     0.5002463206060068E+00, \
     0.3662132299770635E+00, \
     0.3488278611548401E+00, \
     0.3334424797228716E+00, \
     0.1026177910993911E+00, \
     0.1012886844792230E+00, \
     0.1000097826564961E+00 ))

  n_vec = np.array ( ( \
     2, 3, 10, 2, 3, 10, 2, 3, 10, 2, 3, 10 ))

  z_vec = np.array ( ( \
     0.1000000000000000E+01, \
     0.1000000000000000E+01, \
     0.1000000000000000E+01, \
     0.5000000000000000E+00, \
     0.5000000000000000E+00, \
     0.5000000000000000E+00, \
     0.3333333333333333E+00, \
     0.3333333333333333E+00, \
     0.3333333333333333E+00, \
     0.1000000000000000E+00, \
     0.1000000000000000E+00, \
     0.1000000000000000E+00 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    z = 0.0
    f = 0.0
  else:
    n = n_vec[n_data]
    z = z_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, n, z, f

def polylogarithm_values_test ( ):

#*****************************************************************************80
#
## POLYLOGARITHM_VALUES_TEST demonstrates the use of POLYLOGARITHM_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'POLYLOGARITHM_VALUES_TEST:'
  print '  POLYLOGARITHM_VALUES stores values of the Gegenbauer polynomials.'
  print ''
  print '      N         Z            F'
  print ''

  n_data = 0

  while ( True ):

    n_data, n, z, f = polylogarithm_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %6d  %12f  %24.16g' % ( n, z, f )

  print ''
  print 'POLYLOGARITHM_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  polylogarithm_values_test ( )
  timestamp ( )

