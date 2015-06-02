#!/usr/bin/env python
#
def sphere_unit_volume_values ( n_data ):

#*****************************************************************************80
#
## SPHERE_UNIT_VOLUME_VALUES returns some volumes of the unit sphere in ND.
#
#  Discussion:
#
#    The formula for the volume of the unit sphere in N dimensions is
#
#      Volume(N) = 2 * PI^(N/2) / ( N * Gamma ( N / 2 ) )
#
#    This function satisfies the relationships:
#
#      Volume(N) = 2 * PI * Volume(N-2) / N
#      Volume(N) = Area(N) / N
#
#    Some values of the function include:
#
#       N  Volume
#
#       1    1
#       2    1        * PI
#       3  ( 4 /   3) * PI
#       4  ( 1 /   2) * PI^2
#       5  ( 8 /  15) * PI^2
#       6  ( 1 /   6) * PI^3
#       7  (16 / 105) * PI^3
#       8  ( 1 /  24) * PI^4
#       9  (32 / 945) * PI^4
#      10  ( 1 / 120) * PI^5
#
#    In Mathematica, the function can be evaluated by:
#
#      2 * Pi^(n/2) / ( n * Gamma[n/2] )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 February 2015
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
#    Input/output, integer N_DATA.
#    On input, if N_DATA is 0, the first test data is returned, and
#    N_DATA is set to the index of the test data.  On each subsequent
#    call, N_DATA is incremented and that test data is returned.  When
#    there is no more test data, N_DATA is set to 0.
#
#    Output, integer N, the spatial dimension.
#
#    Output, real VOLUME, the volume of the unit 
#    sphere in that dimension.
#
  import numpy as np

  n_max = 20

  n_vec = np.array ( ( \
     1, \
     2, \
     3, \
     4, \
     5, \
     6, \
     7, \
     8, \
     9, \
    10, \
    11, \
    12, \
    13, \
    14, \
    15, \
    16, \
    17, \
    18, \
    19, \
    20 ))

  volume_vec = np.array ( ( \
     0.2000000000000000E+01, \
     0.3141592653589793E+01, \
     0.4188790204786391E+01, \
     0.4934802200544679E+01, \
     0.5263789013914325E+01, \
     0.5167712780049970E+01, \
     0.4724765970331401E+01, \
     0.4058712126416768E+01, \
     0.3298508902738707E+01, \
     0.2550164039877345E+01, \
     0.1884103879389900E+01, \
     0.1335262768854589E+01, \
     0.9106287547832831E+00, \
     0.5992645293207921E+00, \
     0.3814432808233045E+00, \
     0.2353306303588932E+00, \
     0.1409811069171390E+00, \
     0.8214588661112823E-01, \
     0.4662160103008855E-01, \
     0.2580689139001406E-01  ))

  n_vec = np.array ( ( \
     1, \
     2, \
     3, \
     4, \
     5, \
     6, \
     7, \
     8, \
     9, \
    10, \
    11, \
    12, \
    13, \
    14, \
    15, \
    16, \
    17, \
    18, \
    19, \
    20 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0.0
    volume = 0.0
  else:
    n = n_vec[n_data]
    volume = volume_vec[n_data]
    n_data = n_data + 1

  return n_data, n, volume

def sphere_unit_volume_values_test ( ):

#*****************************************************************************80
#
## SPHERE_UNIT_VOLUME_VALUES_TEST demonstrates the use of SPHERE_UNIT_VOLUME_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'SPHERE_UNIT_VOLUME_VALUES_TEST:'
  print '  SPHERE_UNIT_VOLUME_VALUES stores values of the SPHERE_UNIT_VOLUME function.'
  print ''
  print '      N         SPHERE_UNIT_VOLUME(X)'
  print ''

  n_data = 0

  while ( True ):

    n_data, n, volume = sphere_unit_volume_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %12d  %24.16f' % ( n, volume )

  print ''
  print 'SPHERE_UNIT_VOLUME_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  sphere_unit_volume_values_test ( )
  timestamp ( )

