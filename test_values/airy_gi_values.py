#!/usr/bin/env python
#
def airy_gi_values ( n_data ):

#*****************************************************************************80
#
## AIRY_GI_VALUES returns some values of the Airy Gi(x) function.
#
#  Discussion:
#
#    The function is defined by:
#
#      AIRY_GI(x) = Integral ( 0 <= t < infinity ) sin ( x*t+t^3/3) dt / pi
#
#    The data was reported by McLeod.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 December 2014
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
      0.20468308070040542435E+00, \
      0.18374662832557904078E+00, \
     -0.11667221729601528265E+00, \
      0.31466934902729557596E+00, \
     -0.37089040722426257729E+00, \
     -0.25293059772424019694E+00, \
      0.28967410658692701936E+00, \
     -0.34644836492634090590E+00, \
      0.28076035913873049496E+00, \
      0.21814994508094865815E+00, \
      0.20526679000810503329E+00, \
      0.22123695363784773258E+00, \
      0.23521843981043793760E+00, \
      0.82834303363768729338E-01, \
      0.45757385490989281893E-01, \
      0.44150012014605159922E-01, \
      0.39951133719508907541E-01, \
      0.35467706833949671483E-01, \
      0.31896005100679587981E-01, \
      0.26556892713512410405E-01 ) )

  x_vec = np.array ( ( \
      -0.0019531250E+00, \
      -0.1250000000E+00, \
      -1.0000000000E+00, \
      -4.0000000000E+00, \
      -8.0000000000E+00, \
      -8.2500000000E+00, \
      -9.0000000000E+00, \
     -10.0000000000E+00, \
     -11.0000000000E+00, \
     -13.0000000000E+00, \
       0.0019531250E+00, \
       0.1250000000E+00, \
       1.0000000000E+00, \
       4.0000000000E+00, \
       7.0000000000E+00, \
       7.2500000000E+00, \
       8.0000000000E+00, \
       9.0000000000E+00, \
      10.0000000000E+00, \
      12.0000000000E+00 ) )

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

def airy_gi_values_test ( ):

#*****************************************************************************80
#
## AIRY_GI_VALUES_TEST demonstrates the use of AIRY_GI_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 December 2014
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'AIRY_GI_VALUES_TEST:'
  print '  AIRY_GI_VALUES stores values of'
  print '  the Airy function Gi(x).'
  print ''
  print '      X           Gi(X)'
  print ''

  n_data = 0

  while ( True ):

    n_data, x, ai = airy_gi_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %12f  %24.16g' % ( x, ai )

  print ''
  print 'AIRY_GI_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  airy_gi_values_test ( )
  timestamp ( )

