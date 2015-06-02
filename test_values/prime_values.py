#!/usr/bin/env python
#
def prime_values ( n_data ):

#*****************************************************************************80
#
## PRIME_VALUES returns values of the prime function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      Prime[n]
#
#    Thanks to Morten Welinder for pointing out that the index of 145253029
#    is 8192000, 12 April 2013.
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
#    Output, integer N, the index of the prime.
#
#    Output, integer P, the value of the prime.
#
  import numpy as np

  n_max = 24

  n_vec = np.array ( ( \
          1, \
          2, \
          4, \
          8, \
         16, \
         32, \
         64, \
        128, \
        256, \
        512, \
       1000, \
       2000, \
       4000, \
       8000, \
      16000, \
      32000, \
      64000, \
     128000, \
     256000, \
     512000, \
    1024000, \
    2048000, \
    4096000, \
    8192000 ))

  p_vec = np.array ( ( \
            2, \
            3, \
            7, \
           19, \
           53, \
          131, \
          311, \
          719, \
         1619, \
         3671, \
         7919, \
        17389, \
        37813, \
        81799, \
       176081, \
       376127, \
       800573, \
      1698077, \
      3588941, \
      7559173, \
     15881419, \
     33283031, \
     69600977, \
    145253029 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    p = 0
  else:
    n = n_vec[n_data]
    p = p_vec[n_data]
    n_data = n_data + 1

  return n_data, n, p

def prime_values_test ( ):

#*****************************************************************************80
#
## PRIME_VALUES_TEST demonstrates the use of PRIME_VALUES.
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
  print 'PRIME_VALUES_TEST:'
  print '  PRIME_VALUES stores values of the PRIME function.'
  print ''
  print '             N    PRIME(N)'
  print ''

  n_data = 0

  while ( True ):

    n_data, n, p = prime_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %12d  %12d' % ( n, p )

  print ''
  print 'PRIME_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  prime_values_test ( )
  timestamp ( )

