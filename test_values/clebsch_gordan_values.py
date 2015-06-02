#!/usr/bin/env python
#
def clebsch_gordan_values ( n_data ):

#*****************************************************************************80
#
## CLEBSCH_GORDAN_VALUES returns some values of the Clebsch-Gordan function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      ClebschGordan[{j1,m1},{j2,m2},{j3,m3}]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 January 2015
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
#    Output, real J1, J2, J3, M1, M2, M3, the arguments
#    of the function.
#
#    Output, real F, the value of the function.
#
  import numpy as np

  n_max = 12

  f_vec = np.array ( ( \
     0.7071067811865475, \
     1.000000000000000, \
     0.5773502691896258, \
    -0.2581988897471611, \
    -0.6324555320336759, \
    -0.7745966692414834, \
     0.4082482904638630, \
     0.8164965809277260, \
     0.5345224838248488, \
     0.2672612419124244, \
     0.8944271909999159, \
     0.3380617018914066 ))
  j1_vec = np.array ( ( \
    0.5, \
    0.5, \
    0.5, \
    1.0, \
    1.0, \
    1.0, \
    1.0, \
    1.0, \
    2.0, \
    2.0, \
    1.5, \
    1.5 ))
  j2_vec = np.array ( ( \
    0.5, \
    0.5, \
    1.0, \
    1.5, \
    1.5, \
    1.5, \
    1.0, \
    1.0, \
    2.0, \
    2.0, \
    2.0, \
    2.0 ))
  j3_vec = np.array ( ( \
    1.0, \
    1.0, \
    1.5, \
    1.5, \
    1.5, \
    1.5, \
    2.0, \
    2.0, \
    2.0, \
    2.0, \
    2.5, \
    3.5 ))
  m1_vec = np.array ( ( \
    0.5, \
    0.5, \
   -0.5, \
    0.0, \
   -1.0, \
    0.0, \
    1.0, \
    0.0, \
    2.0, \
    1.0, \
    0.5, \
    1.5 ))
  m2_vec = np.array ( ( \
   -0.5, \
    0.5, \
    1.0, \
    0.5, \
    1.5, \
    1.5, \
   -1.0, \
    0.0, \
   -2.0, \
   -1.0, \
    1.0, \
   -1.0 ))
  m3_vec = np.array ( ( \
    0.0, \
    1.0, \
    0.5, \
    0.5, \
    0.5, \
    1.5, \
    0.0, \
    0.0, \
    0.0, \
    0.0, \
    1.5, \
    0.5 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    j1 = 0
    j2 = 0
    j3 = 0
    m1 = 0
    m2 = 0
    m3 = 0
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

def clebsch_gordan_values_test ( ):

#*****************************************************************************80
#
## CLEBSCH_GORDAN_VALUES_TEST demonstrates the use of CI_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 January 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'CLEBSCH_GORDAN_VALUES_TEST:'
  print '  CLEBSCH_GORDAN_VALUES returns value of the Clebsch-Gordan coefficient.'
  print ''
  print '      J1      J2      J3      M1      M2      M3        CG'
  print ''

  n_data = 0

  while ( True ):

    n_data, j1, j2, j3, m1, m2, m3, f = clebsch_gordan_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %6.2f  %6.2f  %6.2f  %6.2f  %6.2f  %6.2f  %24.16f' % ( j1, j2, j3, m1, m2, m3, f )

  print ''
  print 'CLEBSCH_GORDAN_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  clebsch_gordan_values_test ( )
  timestamp ( )

