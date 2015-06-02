#!/usr/bin/env python
#
def hypergeometric_u_values ( n_data ):

#*****************************************************************************80
#
## HYPERGEOMETRIC_U_VALUES: some values of the hypergeometric function U(a,b,x).
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      fx = HypergeometricU [ a, b, x ]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    15 February 2015
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
#    Daniel Zwillinger, editor,
#    CRC Standard Mathematical Tables and Formulae,
#    30th Edition,
#    CRC Press, 1996,
#    ISBN: 0-8493-2479-3,
#    LC: QA47.M315.
#
#  Parameters:
#
#    Input/output, integer N_DATA.  The user sets N_DATA to 0 
#    before the first call.  On each call, the routine increments N_DATA by 1,
#    and returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, real A, B, X, the parameters.
#
#    Output, real F, the value of the function.
#
  import numpy as np

  n_max = 24

  a_vec = np.array ( (\
    -2.500, \
    -0.500, \
     0.500, \
     2.500, \
    -2.500, \
    -0.500, \
     0.500, \
     2.500, \
    -2.500, \
    -0.500, \
     0.500, \
     2.500, \
     0.825, \
     1.100, \
     1.650, \
     3.300, \
     0.825, \
     1.100, \
     1.650, \
     3.300, \
     0.825, \
     1.100, \
     1.650, \
     3.300 ))

  b_vec = np.array ( (\
     3.3, \
     1.1, \
     1.1, \
     3.3, \
     3.3, \
     1.1, \
     1.1, \
     3.3, \
     3.3, \
     1.1, \
     1.1, \
     3.3, \
     6.7, \
     6.7, \
     6.7, \
     6.7, \
     6.7, \
     6.7, \
     6.7, \
     6.7, \
     6.7, \
     6.7, \
     6.7, \
     6.7 ))

  f_vec = np.array ( (\
         -68.693628728078601389E+00, \
          -0.0029710551374761070801E+00, \
           1.5008631742177797301E+00, \
          20.614688244200596134E+00, \
           7.4563815469305551938E+00, \
           1.0155793767749293733E+00, \
           0.73446538936622668912E+00, \
           0.28046404941879399225E+00, \
           3.4508153741446547607E+00, \
           1.5156637368753063495E+00, \
           0.56042118587934993510E+00, \
           0.064897147735134223341E+00, \
      223432.02356977463356E+00, \
      263079.25980740811495E+00, \
      269802.90319351274132E+00, \
       82809.311335606553425E+00, \
          26.465684783131844524E+00, \
          28.093506172516056560E+00, \
          23.889164624518872504E+00, \
           4.5338847857070388229E+00, \
           3.0224469362694842535E+00, \
           2.8040650913713359934E+00, \
           1.9262578111480172682E+00, \
           0.23020518115860909098E+00 ))

  x_vec = np.array ( (\
     0.25, \
     0.25, \
     0.25, \
     0.25, \
     1.55, \
     1.55, \
     1.55, \
     1.55, \
     2.85, \
     2.85, \
     2.85, \
     2.85, \
     0.25, \
     0.25, \
     0.25, \
     0.25, \
     1.55, \
     1.55, \
     1.55, \
     1.55, \
     2.85, \
     2.85, \
     2.85, \
     2.85 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    a = 0.0
    b = 0.0
    x = 0.0
    f = 0.0
  else:
    a = a_vec[n_data]
    b = b_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, a, b, x, f

def hypergeometric_u_values_test ( ):

#*****************************************************************************80
#
## HYPERGEOMETRIC_U_VALUES_TEST demonstrates the use of HYPERGEOMETRIC_U_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'HYPERGEOMETRIC_U_VALUES_TEST:'
  print '  HYPERGEOMETRIC_U_VALUES stores values of the Hypergeometric U function.'
  print ''
  print '        A             B             X              F'
  print ''

  n_data = 0

  while ( True ):

    n_data, a, b, x, f = hypergeometric_u_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %12f  %12f  %12f  %24.16g' % ( a, b, x, f )

  print ''
  print 'HYPERGEOMETRIC_U_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  hypergeometric_u_values_test ( )
  timestamp ( )

