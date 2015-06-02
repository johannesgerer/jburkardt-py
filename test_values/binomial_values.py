#!/usr/bin/env python
#
def binomial_values ( n_data ):

#*****************************************************************************80
#
## BINOMIAL_VALUES returns some values of the binomial coefficients.
#
#  Discussion:
#
#    The formula for the binomial coefficient is
#
#      C(N,K) = N! / ( K! * (N-K)! )
#
#    In Mathematica, the function can be evaluated by:
#
#      Binomial[n,k]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 January 2015
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
#    Output, integer A, B, the arguments of the function.
#
#    Output, integer F, the value of the function.
#
  import numpy as np

  n_max = 20

  a_vec = np.array ( ( \
     1,  6,  6,  6, 15, \
    15, 15, 15, 15, 15, \
    15, 25, 25, 25, 25, \
    25, 25, 25, 25, 25  ) )

  b_vec = np.array ( ( \
     0,  1,  3,  5,  1, \
     3,  5,  7,  9, 11, \
    13,  1,  3,  5,  7, \
     9, 11, 13, 15, 17  ) )

  f_vec = np.array ( ( \
           1, \
           6, \
          20, \
           6, \
          15, \
         455, \
        3003, \
        6435, \
        5005, \
        1365, \
         105, \
          25, \
        2300, \
       53130, \
      480700, \
     2042975, \
     4457400, \
     5200300, \
     3268760, \
     1081575 ) )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    a = 0
    b = 0
    f = 0
  else:
    a = a_vec[n_data]
    b = b_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, a, b, f

def binomial_values_test ( ):

#*****************************************************************************80
#
## BINOMIAL_VALUES_TEST demonstrates the use of BINOMIAL_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 January 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'BINOMIAL_VALUES_TEST:'
  print '  BINOMIAL_VALUES stores values of the BINOMIAL function.'
  print ''
  print '      A         B         BINOMIAL(A,B)'
  print ''

  n_data = 0

  while ( True ):

    n_data, a, b, f = binomial_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %12d  %12d  %12d' % ( a, b, f )

  print ''
  print 'BINOMIAL_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  binomial_values_test ( )
  timestamp ( )

