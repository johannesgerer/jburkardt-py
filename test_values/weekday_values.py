#!/usr/bin/env python
#
def weekday_values ( n_data ):

#*****************************************************************************80
#
## WEEKDAY_VALUES returns the day of the week for various dates.
#
#  Discussion:
#
#    The CE or Common Era calendar is used, under the
#    hybrid Julian/Gregorian Calendar, with a transition from Julian
#    to Gregorian.  The day after 04 October 1582 was 15 October 1582.  
#
#    The year before 1 AD or CE is 1 BC or BCE.  In this data set,
#    years BC/BCE are indicated by a negative year value.  
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
#    Edward Reingold, Nachum Dershowitz,
#    Calendrical Calculations: The Millennium Edition,
#    Cambridge University Press, 2001,
#    ISBN: 0 521 77752 6
#    LC: CE12.R45.
#
#  Parameters:
#
#    Input/output, integer N_DATA.  The user sets N_DATA to 0 
#    before the first call.  On each call, the routine increments N_DATA by 1,
#    and returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, integer Y, M, D, the Common Era date.
#
#    Output, integer W, the day of the week.  Sunday = 1.
#
  import numpy as np

  n_max = 34

  d_vec = np.array ( ( \
    30, \
     8, \
    26, \
     3, \
     7, \
    18, \
     7, \
    19, \
    14, \
    18, \
    16, \
     3, \
    26, \
    20, \
     4, \
    25, \
    31, \
     9, \
    24, \
    10, \
    30, \
    24, \
    19, \
     2, \
    27, \
    19, \
    25, \
    29, \
    19, \
     7, \
    17, \
    25, \
    10, \
    18 ))

  m_vec = np.array ( ( \
     7, \
    12, \
     9, \
    10, \
     1, \
     5, \
    11, \
     4, \
    10, \
     5, \
     3, \
     3, \
     3, \
     4, \
     6, \
     1, \
     3, \
     9, \
     2, \
     6, \
     6, \
     7, \
     6, \
     8, \
     3, \
     4, \
     8, \
     9, \
     4, \
    10, \
     3, \
     2, \
    11, \
     7 ))

  w_vec = np.array ( ( \
    1, \
    4, \
    4, \
    1, \
    4, \
    2, \
    7, \
    1, \
    7, \
    1, \
    6, \
    7, \
    6, \
    1, \
    1, \
    4, \
    7, \
    7, \
    7, \
    4, \
    1, \
    6, \
    1, \
    2, \
    4, \
    1, \
    1, \
    2, \
    2, \
    5, \
    3, \
    1, \
    4, \
    1 ))

  y_vec = np.array ( ( \
    - 587, \
    - 169, \
       70, \
      135, \
      470, \
      576, \
      694, \
     1013, \
     1066, \
     1096, \
     1190, \
     1240, \
     1288, \
     1298, \
     1391, \
     1436, \
     1492, \
     1553, \
     1560, \
     1648, \
     1680, \
     1716, \
     1768, \
     1819, \
     1839, \
     1903, \
     1929, \
     1941, \
     1943, \
     1943, \
     1992, \
     1996, \
     2038, \
     2094 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    y = 0
    m = 0
    d = 0
    w = 0
  else:
    y = y_vec[n_data]
    m = m_vec[n_data]
    d = d_vec[n_data]
    w = w_vec[n_data]
    n_data = n_data + 1

  return n_data, y, m, d, w

def weekday_values_test ( ):

#*****************************************************************************80
#
## WEEKDAY_VALUES_TEST demonstrates the use of WEEKDAY_VALUES.
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
  print 'WEEKDAY_VALUES_TEST:'
  print '  WEEKDAY_VALUES stores values of'
  print '  the weekday for a given Y/M/D date'
  print ''
  print '         Y       M       D           W'
  print ''

  n_data = 0

  while ( True ):

    n_data, y, m, d, w = weekday_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %6d  %6d  %6d  %6d' % ( y, m, d, w )

  print ''
  print 'WEEKDAY_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  weekday_values_test ( )
  timestamp ( )

