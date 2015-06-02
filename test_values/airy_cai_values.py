#!/usr/bin/env python
#
def airy_cai_values ( n_data ):

#*****************************************************************************80
#
## AIRY_CAI_VALUES returns some values of the Airy Ai(x) with complex argument.
#
#  Discussion:
#
#    The Airy functions Ai(X) and Bi(X) are a pair of linearly independent
#    solutions of the differential equation:
#
#      W'' - X * W = 0
#
#    In Mathematica, the function can be evaluated by:
#
#      AiryAi[x]
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
#    Input/output, integer N_DATA.  The user sets N_DATA to 0 before the
#    first call.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, complex X, the argument of the function.
#
#    Output, complex CAI, the value of the Airy AI function.
#
  import numpy as np

  n_max = 10

  cai_vec = np.array ( ( \
    0.1352924163128814 + 0.0000000000000000j, \
    0.1433824486882056 - 0.1092193342707378j, \
    0.2215404472324631 - 0.2588711788891803j, \
    0.4763929771766866 - 0.3036484220291284j, \
    0.5983692170633874 - 0.08154602160771214j, \
    0.5355608832923521 + 0.00000000000000000j, \
    0.5983692170633874 + 0.08154602160771214j, \
    0.4763929771766866 + 0.3036484220291284j, \
    0.2215404472324631 + 0.2588711788891803j, \
    0.1433824486882056 + 0.1092193342707378j ) )

  x_vec = np.array ( ( \
     1.0000000000000000 + 0.0000000000000000j, \
     0.8090169943749474 + 0.5877852522924731j, \
     0.3090169943749474 + 0.9510565162951536j, \
    -0.3090169943749474 + 0.9510565162951536j, \
    -0.8090169943749474 + 0.5877852522924731j, \
    -1.0000000000000000 + 0.0000000000000000j, \
    -0.8090169943749474 - 0.5877852522924731j, \
    -0.3090169943749474 - 0.9510565162951536j, \
     0.3090169943749474 - 0.9510565162951536j, \
     0.8090169943749474 - 0.5877852522924731j ) )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    x = 0.0
    cai = 0.0
  else:
    x = x_vec[n_data]
    cai = cai_vec[n_data]
    n_data = n_data + 1

  return n_data, x, cai

def airy_cai_values_test ( ):

#*****************************************************************************80
#
## AIRY_CAI_VALUES_TEST demonstrates the use of AIRY_CAI_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 January 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'AIRY_CAI_VALUES_TEST:'
  print '  AIRY_CAI_VALUES stores values of'
  print '  the complex Airy function Ai(x).'
  print ''
  print '        X.real        X.imag          Ai.real(X)                Ai.imag(X)'
  print ''

  n_data = 0

  while ( True ):

    n_data, x, cai = airy_cai_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %12f  %12f  %24.16f  %24.16g' % ( x.real, x.imag, cai.real, cai.imag )

  print ''
  print 'AIRY_CAI_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  airy_cai_values_test ( )
  timestamp ( )

