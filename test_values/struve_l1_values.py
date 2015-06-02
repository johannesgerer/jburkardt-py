#!/usr/bin/env python
#
def struve_l1_values ( n_data ):

#*****************************************************************************80
#
## STRUVE_L1_VALUES returns some values of the Struve L1 function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      StruveL[1,x]
#
#    The data was reported by McLeod.
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
     0.80950410749865126939E-06, \
     0.20724649092571514607E-03, \
     0.33191834066894516744E-02, \
     0.53942182623522663292E-01, \
     0.22676438105580863683E+00, \
     0.11027597873677158176E+01, \
     0.91692778117386847344E+01, \
     0.15541656652426660966E+03, \
     0.26703582852084829694E+04, \
     0.86505880175304633906E+06, \
     0.11026046613094942620E+07, \
     0.22846209494153934787E+07, \
     0.42454972750111979449E+08, \
     0.48869614587997695539E+09, \
     0.56578651292431051863E+10, \
     0.76853203893832108948E+12, \
     0.14707396163259352103E+17, \
     0.29030785901035567967E+21, \
     0.58447515883904682813E+25, \
     0.11929750788892311875E+30 ))

  x_vec = np.array ( ( \
        0.0019531250E+00, \
       -0.0078125000E+00, \
        0.0625000000E+00, \
       -0.2500000000E+00, \
        1.0000000000E+00, \
        1.2500000000E+00, \
        2.0000000000E+00, \
       -4.0000000000E+00, \
        7.5000000000E+00, \
       11.0000000000E+00, \
       11.5000000000E+00, \
      -16.0000000000E+00, \
       20.0000000000E+00, \
       25.0000000000E+00, \
      -30.0000000000E+00, \
       50.0000000000E+00, \
       75.0000000000E+00, \
      -80.0000000000E+00, \
      100.0000000000E+00, \
     -125.0000000000E+00 ))

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

def struve_l1_values_test ( ):

#*****************************************************************************80
#
## STRUVE_L1_VALUES_TEST demonstrates the use of STRUVE_L1_VALUES.
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
  print 'STRUVE_L1_VALUES_TEST:'
  print '  STRUVE_L1_VALUES stores values of the STRUVE_L1 function.'
  print ''
  print '      X         STRUVE_L1(X)'
  print ''

  n_data = 0

  while ( True ):

    n_data, x, f = struve_l1_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %12g  %24.16g' % ( x, f )

  print ''
  print 'STRUVE_L1_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  struve_l1_values_test ( )
  timestamp ( )

