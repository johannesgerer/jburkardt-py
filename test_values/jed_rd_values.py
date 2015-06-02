#!/usr/bin/env python
#
def jed_rd_values ( n_data ):

#*****************************************************************************80
#
## JED_RD_VALUES returns the RD for Julian Ephemeris Dates.
#
#  Discussion:
#
#    The JED (Julian Ephemeris Date) is a calendrical system which counts days,
#    starting from noon on 1 January 4713 BCE.
#
#    The RD is the Reingold Dershowitz Date, which counts days from
#    midnight, 1 January year 1 in the Gregorian calendar.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Edward Reingold and Nachum Dershowitz,
#    Calendrical Calculations: The Millennium Edition,
#    Cambridge University Press, 2001,
#    ISBN: 0 521 77752 6
#
#  Parameters:
#
#    Input/output, integer N_DATA.  The user sets N_DATA to 0 before the
#    first call.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, real JED, the Julian Ephemeris Date.
#
#    Output, real RD, the Modified Julian Ephemeris Date.
#
  import numpy as np

  n_max = 33

  jed_vec = np.array ( ( \
     1507231.5E+00, \
     1660037.5E+00, \
     1746893.5E+00, \
     1770641.5E+00, \
     1892731.5E+00, \
     1931579.5E+00, \
     1974851.5E+00, \
     2091164.5E+00, \
     2121509.5E+00, \
     2155779.5E+00, \
     2174029.5E+00, \
     2191584.5E+00, \
     2195261.5E+00, \
     2229274.5E+00, \
     2245580.5E+00, \
     2266100.5E+00, \
     2288542.5E+00, \
     2290901.5E+00, \
     2323140.5E+00, \
     2334848.5E+00, \
     2348020.5E+00, \
     2366978.5E+00, \
     2385648.5E+00, \
     2392825.5E+00, \
     2416223.5E+00, \
     2425848.5E+00, \
     2430266.5E+00, \
     2430833.5E+00, \
     2431004.5E+00, \
     2448698.5E+00, \
     2450138.5E+00, \
     2465737.5E+00, \
     2486076.5E+00 ))

  rd_vec = np.array ( ( \
    -214193.0E+00, \
     -61387.0E+00, \
      25469.0E+00, \
      49217.0E+00, \
     171307.0E+00, \
     210155.0E+00, \
     253427.0E+00, \
     369740.0E+00, \
     400085.0E+00, \
     434355.0E+00, \
     452605.0E+00, \
     470160.0E+00, \
     473837.0E+00, \
     507850.0E+00, \
     524156.0E+00, \
     544676.0E+00, \
     567118.0E+00, \
     569477.0E+00, \
     601716.0E+00, \
     613424.0E+00, \
     626596.0E+00, \
     645554.0E+00, \
     664224.0E+00, \
     671401.0E+00, \
     694799.0E+00, \
     704424.0E+00, \
     708842.0E+00, \
     709409.0E+00, \
     709580.0E+00, \
     727274.0E+00, \
     728714.0E+00, \
     744313.0E+00, \
     764652.0E+00 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    jed = 0.0
    rd = 0.0
  else:
    jed = jed_vec[n_data]
    rd = rd_vec[n_data]
    n_data = n_data + 1

  return n_data, jed, rd

def jed_rd_values_test ( ):

#*****************************************************************************80
#
## JED_RD_VALUES_TEST demonstrates the use of JED_RD_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'JED_RD_VALUES_TEST:'
  print '  JED_RD_VALUES stores values of the Reingold Dershowitz Date.'
  print ''
  print '    JED         RD(JED)'
  print ''

  n_data = 0

  while ( True ):

    n_data, jed, rd = jed_rd_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %12f  %24.16f' % ( jed, rd )

  print ''
  print 'JED_RD_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  jed_rd_values_test ( )
  timestamp ( )

