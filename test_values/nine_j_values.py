#!/usr/bin/env python
#
def nine_j_values ( n_data ):

#*****************************************************************************80
#
## NINE_J_VALUES returns some values of the Wigner 9J function.
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
#    Milton Abramowitz, Irene Stegun,
#    Handbook of Mathematical Functions,
#    National Bureau of Standards, 1964,
#    ISBN: 0-486-61272-4,
#    LC: QA47.A34.
#
#  Parameters:
#
#    Input/output, integer N_DATA.  The user sets N_DATA to 0 before the
#    first call.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, real J1, J2, J3, J4, J5, J6, J7, J8, J9,
#    the arguments of the function.
#
#    Output, real F, the value of the function.
#
  import numpy as np

  n_max = 9

  f_vec = np.array ( ( \
     0.0004270039294528318, \
    -0.001228915451058514, \
    -0.0001944260688400887, \
     0.003338419923885592, \
    -0.0007958936865080434, \
    -0.004338208690251972, \
     0.05379143536399187, \
     0.006211299937499411, \
     0.03042903097250921 ))
  j1_vec = np.array ( ( \
    1.0, \
    1.5, \
    2.0, \
    1.0, \
    1.5, \
    2.0, \
    0.5, \
    1.0, \
    1.5  ))
  j2_vec = np.array ( ( \
    8.0, \
    8.0, \
    8.0, \
    3.0, \
    3.0, \
    3.0, \
    0.5, \
    0.5, \
    0.5  ))
  j3_vec = np.array ( ( \
    7.0, \
    7.0, \
    7.0, \
    2.0, \
    2.0, \
    2.0, \
    1.0, \
    1.0, \
    1.0 ))
  j4_vec = np.array ( ( \
    6.5, \
    6.5, \
    6.5, \
    4.0, \
    4.0, \
    4.0, \
    2.0, \
    2.0, \
    2.0 ))
  j5_vec = np.array ( ( \
    7.5, \
    7.5, \
    7.5, \
    1.5, \
    1.5, \
    1.5, \
    1.0, \
    1.0, \
    1.0 ))
  j6_vec = np.array ( ( \
    7.5, \
    7.5, \
    7.5, \
    3.0, \
    3.0, \
    3.0, \
    1.5, \
    1.5, \
    1.5 ))
  j7_vec = np.array ( ( \
    6.0, \
    6.0, \
    6.0, \
    3.5, \
    3.5, \
    3.5, \
    1.5, \
    1.5, \
    1.5 ))
  j8_vec = np.array ( ( \
    10.0, \
    10.0, \
    10.0, \
     2.0, \
     2.0, \
     2.0, \
     0.5, \
     0.5, \
     0.5 ))
  j9_vec = np.array ( ( \
    6.0, \
    6.0, \
    6.0, \
    2.0, \
    2.0, \
    2.0, \
    1.5, \
    1.5, \
    1.5 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    j1 = 0.0
    j2 = 0.0
    j3 = 0.0
    j4 = 0.0
    j5 = 0.0
    j6 = 0.0
    j7 = 0.0
    j8 = 0.0
    j9 = 0.0
    f = 0.0
  else:
    j1 = j1_vec[n_data]
    j2 = j2_vec[n_data]
    j3 = j3_vec[n_data]
    j4 = j4_vec[n_data]
    j5 = j5_vec[n_data]
    j6 = j6_vec[n_data]
    j7 = j7_vec[n_data]
    j8 = j8_vec[n_data]
    j9 = j9_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, j1, j2, j3, j4, j5, j6, j7, j8, j9, f

def nine_j_values_test ( ):

#*****************************************************************************80
#
## NINE_J_VALUES_TEST demonstrates the use of NINE_J_VALUES.
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
  print 'NINE_J_VALUES_TEST:'
  print '  NINE_J_VALUES stores values of the NINE_J function.'
  print ''
  print '    J1    J2    J3    J4    J5    J6    J7    J8    J9    NINE_J(X)'
  print ''

  n_data = 0

  while ( True ):

    n_data, j1, j2, j3, j4, j5, j6, j7, j8, j9, f = nine_j_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %4.1f  %4.1f  %4.1f  %4.1f  %4.1f  %4.1f  %4.1f  %4.1f  %4.1f  %24.16f' \
      % ( j1, j2, j3, j4, j5, j6, j7, j8, j9, f )

  print ''
  print 'NINE_J_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  nine_j_values_test ( )
  timestamp ( )

