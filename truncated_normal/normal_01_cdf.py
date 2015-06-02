#!/usr/bin/env python
#
def normal_01_cdf ( x ):

#*****************************************************************************80
#
## NORMAL_01_CDF evaluates the Normal 01 CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    A G Adams,
#    Areas Under the Normal Curve,
#    Algorithm 39,
#    Computer j.,
#    Volume 12, pages 197-198, 1969.
#
#  Parameters:
#
#    Input, real X, the argument of the CDF.
#
#    Output, real VALUE, the value of the CDF.
# 
  import numpy as np

  a1 = 0.398942280444
  a2 = 0.399903438504
  a3 = 5.75885480458
  a4 = 29.8213557808
  a5 = 2.62433121679
  a6 = 48.6959930692
  a7 = 5.92885724438
  b0 = 0.398942280385
  b1 = 3.8052E-08
  b2 = 1.00000615302
  b3 = 3.98064794E-04
  b4 = 1.98615381364
  b5 = 0.151679116635
  b6 = 5.29330324926
  b7 = 4.8385912808
  b8 = 15.1508972451
  b9 = 0.742380924027
  b10 = 30.789933034
  b11 = 3.99019417011
#
#  |X| <= 1.28.
#
  if ( abs ( x ) <= 1.28 ):

    y = 0.5 * x * x

    q = 0.5 - abs ( x ) * ( a1 - a2 * y / ( y + a3 \
      - a4 / ( y + a5 \
      + a6 / ( y + a7 ) ) ) )
#
#  1.28 < |X| <= 12.7
#
  elif ( abs ( x ) <= 12.7 ):

    y = 0.5 * x * x

    q = np.exp ( - y ) \
      * b0  / ( abs ( x ) - b1 \
      + b2  / ( abs ( x ) + b3 \
      + b4  / ( abs ( x ) - b5 \
      + b6  / ( abs ( x ) + b7 \
      - b8  / ( abs ( x ) + b9 \
      + b10 / ( abs ( x ) + b11 ) ) ) ) ) )
#
#  12.7 < |X|
#
  else:

    q = 0.0
#
#  Take account of negative X.
#
  if ( x < 0.0 ):
    value = q
  else:
    value = 1.0 - q

  return value

def normal_01_cdf_test ( ):

#*****************************************************************************80
#
## NORMAL_01_CDF_TEST tests NORMAL_01_CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 February 2015
#
#  Author:
#
#    John Burkardt
#
  from normal_01_cdf_values import normal_01_cdf_values

  print ''
  print 'NORMAL_01_CDF_TEST'
  print '  NORMAL_01_CDF evaluates the CDF;'
  print ''
  print '       X              CDF                       CDF'
  print '                     (exact)                   (computed)'
  print ''

  n_data = 0

  while ( True ):

    n_data, x, cdf1 = normal_01_cdf_values ( n_data )

    if ( n_data == 0 ):
      break

    cdf2 = normal_01_cdf ( x )

    print '  %14.6g  %24.16g  %24.16g' % ( x, cdf1, cdf2 )

  print ''
  print 'NORMAL_01_CDF_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  normal_01_cdf_test ( )
  timestamp ( )


