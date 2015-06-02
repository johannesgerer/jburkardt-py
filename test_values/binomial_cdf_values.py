#!/usr/bin/env python
#
def binomial_cdf_values ( n_data ):

#*****************************************************************************80
#
## BINOMIAL_CDF_VALUES returns some values of the binomial CDF.
#
#  Discussion:
#
#    CDF(X)(A,B) is the probability of at most X successes in A trials,
#    given that the probability of success on a single trial is B.
#
#    In Mathematica, the function can be evaluated by:
#
#      Needs["Statistics`DiscreteDistributions`]
#      dist = BinomialDistribution [ n, p ]
#      CDF [ dist, x ]
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
#    Daniel Zwillinger,
#    CRC Standard Mathematical Tables and Formulae,
#    30th Edition, CRC Press, 1996, pages 651-652.
#
#  Parameters:
#
#    Input/output, integer N_DATA.  The user sets N_DATA to 0 before the
#    first call.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, integer A, a parameter of the function.
#
#    Output, real B, a parameter of the function.
#
#    Output, integer X, the argument of the function.
#
#    Output, real F, the value of the function.
#
  import numpy as np

  n_max = 17

  a_vec = np.array ( ( \
     2,  2,  2,  2, \
     2,  4,  4,  4, \
     4, 10, 10, 10, \
    10, 10, 10, 10, \
    10 ))

  b_vec = np.array ( ( \
     0.05E+00, \
     0.05E+00, \
     0.05E+00, \
     0.50E+00, \
     0.50E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.05E+00, \
     0.10E+00, \
     0.15E+00, \
     0.20E+00, \
     0.25E+00, \
     0.30E+00, \
     0.40E+00, \
     0.50E+00 ))

  f_vec = np.array ( ( \
     0.9025000000000000E+00, \
     0.9975000000000000E+00, \
     0.1000000000000000E+01, \
     0.2500000000000000E+00, \
     0.7500000000000000E+00, \
     0.3164062500000000E+00, \
     0.7382812500000000E+00, \
     0.9492187500000000E+00, \
     0.9960937500000000E+00, \
     0.9999363101685547E+00, \
     0.9983650626000000E+00, \
     0.9901259090013672E+00, \
     0.9672065024000000E+00, \
     0.9218730926513672E+00, \
     0.8497316674000000E+00, \
     0.6331032576000000E+00, \
     0.3769531250000000E+00 ) )

  x_vec = np.array ( ( \
     0, 1, 2, 0, \
     1, 0, 1, 2, \
     3, 4, 4, 4, \
     4, 4, 4, 4, \
     4  ) )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    a = 0.0
    b = 0.0
    x = 0.0
    f = 0.0
  else:
    a = a_vec[n_data]
    b = b_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, a, b, x, f

def binomial_cdf_values_test ( ):

#*****************************************************************************80
#
## BINOMIAL_CDF_VALUES_TEST demonstrates the use of BINOMIAL_CDF_VALUES.
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
  print 'BINOMIAL_CDF_VALUES_TEST:'
  print '  BINOMIAL_CDF_VALUES stores values of the BINOMIAL CDF.'
  print ''
  print '      A         B         X        BINOMIAL_CDF(A,B,X)'
  print ''

  n_data = 0

  while ( True ):

    n_data, a, b, x, f = binomial_cdf_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %12f  %12f  %12d  %24.16g' % ( a, b, x, f )

  print ''
  print 'BINOMIAL_CDF_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  binomial_cdf_values_test ( )
  timestamp ( )

