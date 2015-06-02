#!/usr/bin/env python
#
def tran02_values ( n_data ):

#*****************************************************************************80
#
## TRAN02_VALUES returns some values of the order 2 transportation function.
#
#  Discussion:
#
#    The function is defined by:
#
#      TRAN02(x) = Integral ( 0 <= t <= x ) t^2 exp(t) / ( exp(t) - 1 )^2 dt
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 February 2015
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
#    special functions,
#    ACM Transactions on Mathematical Software,
#    Volume 22, Number 3, September 1996, pages 288-301.
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
#    Output, real X, the argument of the function.
#
#    Output, real F, the value of the function.
#
  import numpy as np

  n_max = 20

  f_vec = np.array ( ( \
     0.19531247930394515480E-02, \
     0.31249152314331109004E-01, \
     0.12494577194783451032E+00, \
     0.49655363615640595865E+00, \
     0.97303256135517012845E+00, \
     0.14121978695932525805E+01, \
     0.18017185674405776809E+01, \
     0.21350385339277043015E+01, \
     0.24110500490169534620E+01, \
     0.28066664045631179931E+01, \
     0.28777421863296234131E+01, \
     0.30391706043438554330E+01, \
     0.31125074928667355940E+01, \
     0.31656687817738577185E+01, \
     0.32623520367816009184E+01, \
     0.32843291144979517358E+01, \
     0.32897895167775788137E+01, \
     0.32898672226665499687E+01, \
     0.32898681336064325400E+01, \
     0.32898681336964528724E+01 ))

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
    f = 0.0
  else:
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, x, f

def tran02_values_test ( ):

#*****************************************************************************80
#
## TRAN02_VALUES_TEST demonstrates the use of TRAN02_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'TRAN02_VALUES_TEST:'
  print '  TRAN02_VALUES stores values of the TRAN02 function.'
  print ''
  print '      X         TRAN02(X)'
  print ''

  n_data = 0

  while ( True ):

    n_data, x, f = tran02_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %12g  %24.16g' % ( x, f )

  print ''
  print 'TRAN02_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  tran02_values_test ( )
  timestamp ( )

