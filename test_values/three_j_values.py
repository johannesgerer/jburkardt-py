#!/usr/bin/env python
#
def three_j_values ( n_data ):

#*****************************************************************************80
#
## THREE_J_VALUES returns some values of the Wigner 3J function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      ThreeJSymbol[{j1,m1},{j2,m2},{j3,m3}]
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
#    Input, integer N_DATA.  The user sets N_DATA to 0 before the
#    first call.  On each subsequent call, the input value should be
#    the output value from the previous call.
#
#    Output, integer N_DATA.  The routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, real  J1, J2, J3, M1, M2, M3, the arguments 
#    of the function.
#
#    Output, real F, the value of the function.
#
  import numpy as np

  n_max = 8

  f_vec = np.array ( ( \
     0.2788866755113585, \
    -0.09534625892455923, \
    -0.06741998624632421, \
     0.1533110351679666, \
    -0.1564465546936860, \
     0.1099450412156551, \
    -0.05536235693131719, \
     0.01799835451137786 ))
  j1_vec = np.array ( ( \
    1.0, \
    2.0, \
    3.0, \
    4.0, \
    5.0, \
    6.0, \
    7.0, \
    8.0 ))
  j2_vec = np.array ( ( \
    4.5, \
    4.5, \
    4.5, \
    4.5, \
    4.5, \
    4.5, \
    4.5, \
    4.5 ))
  j3_vec = np.array ( ( \
    3.5, \
    3.5, \
    3.5, \
    3.5, \
    3.5, \
    3.5, \
    3.5, \
    3.5 ))
  m1_vec = np.array ( ( \
    1.0, \
    1.0, \
    1.0, \
    1.0, \
    1.0, \
    1.0, \
    1.0, \
    1.0 ))
  m2_vec = np.array ( ( \
    -3.5, \
    -3.5, \
    -3.5, \
    -3.5, \
    -3.5, \
    -3.5, \
    -3.5, \
    -3.5 ))
  m3_vec = np.array ( ( \
    2.5, \
    2.5, \
    2.5, \
    2.5, \
    2.5, \
    2.5, \
    2.5, \
    2.5 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    j1 = 0.0
    j2 = 0.0
    j3 = 0.0
    m1 = 0.0
    m2 = 0.0
    m3 = 0.0
    f = 0.0
  else:
    j1 = j1_vec[n_data]
    j2 = j2_vec[n_data]
    j3 = j3_vec[n_data]
    m1 = m1_vec[n_data]
    m2 = m2_vec[n_data]
    m3 = m3_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, j1, j2, j3, m1, m2, m3, f

def three_j_values_test ( ):

#*****************************************************************************80
#
## THREE_J_VALUES_TEST demonstrates the use of THREE_J_VALUES.
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
  print 'THREE_J_VALUES_TEST:'
  print '  THREE_J_VALUES stores values of the THREE_J function.'
  print ''
  print '    J1    J2    J3    M1    M2    M3    THREE_J(X)'
  print ''

  n_data = 0

  while ( True ):

    n_data, j1, j2, j3, m1, m2, m3, f = three_j_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %4.1f  %4.1f  %4.1f  %4.1f  %4.1f  %4.1f  %24.16f' \
      % ( j1, j2, j3, m1, m2, m3, f )

  print ''
  print 'THREE_J_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  three_j_values_test ( )
  timestamp ( )

