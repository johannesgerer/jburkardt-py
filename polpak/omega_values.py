#!/usr/bin/env python
#
def omega_values ( n_data ):

#*****************************************************************************80
#
## OMEGA_VALUES returns some values of the OMEGA function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by
#
#      Length [ FactorInteger [ n ] ]
#
#  First values:
#
#     N   OMEGA(N)
#
#     1    0
#     2    1
#     3    1
#     4    1
#     5    1
#     6    2
#     7    1
#     8    1
#     9    1
#    10    2
#    11    1
#    12    2
#    13    1
#    14    2
#    15    2
#    16    1
#    17    1
#    18    2
#    19    1
#    20    2
#
#  Formula:
#
#    If N = 1, then
#
#      OMEGA(N) = 0
#
#    else if the prime factorization of N is
#
#      N = P1^E1 * P2^E2 * \ * PM^EM,
#
#    then
#
#      OMEGA(N) = M
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
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
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
#    Output, integer N, the argument of the OMEGA function.
#
#    Output, integer C, the value of the OMEGA function.
#
  import numpy as np

  n_max = 23

  c_vec = np.array ( ( \
      0,   1,   1,   1,   1, \
      2,   1,   1,   1,   2, \
      3,   1,   4,   4,   3, \
      1,   5,   2,   2,   1, \
      6,   7,   8 ))

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
          30, \
         101, \
         210, \
        1320, \
        1764, \
        2003, \
        2310, \
        2827, \
        8717, \
       12553, \
       30030, \
      510510, \
     9699690 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    c = 0
  else:
    n = n_vec[n_data]
    c = c_vec[n_data]
    n_data = n_data + 1

  return n_data, n, c

def omega_values_test ( ):

#*****************************************************************************80
#
## OMEGA_VALUES_TEST demonstrates the use of OMEGA_VALUES.
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
  print 'OMEGA_VALUES_TEST:'
  print '  OMEGA_VALUES stores values of the OMEGA function.'
  print ''
  print '             N    OMEGA(N)'
  print ''

  n_data = 0

  while ( True ):

    n_data, n, c = omega_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %12d  %12d' % ( n, c )

  print ''
  print 'OMEGA_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  omega_values_test ( )
  timestamp ( )

