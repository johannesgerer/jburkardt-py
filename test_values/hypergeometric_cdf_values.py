#!/usr/bin/env python

def hypergeometric_cdf_values ( n_data ):

#*****************************************************************************80
#
## HYPERGEOMETRIC_CDF_VALUES returns some values of the hypergeometric CDF.
#
#  Discussion:
#
#    CDF(X)(A,B) is the probability of at most X successes in A trials,
#    given that the probability of success on a single trial is B.
#
#    In Mathematica, the function can be evaluated by:
#
#      Needs["Statistics`DiscreteDistributions`]
#      dist = HypergeometricDistribution [ sam, suc, pop ]
#      CDF [ dist, n ]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 February 2015
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
#    Output, integer SAM, integer SUC, integer POP, the sample size, 
#    success size, and population parameters of the function.
#
#    Output, integer N, the argument of the function.
#
#    Output, real F, the value of the function.
#
  import numpy as np

  n_max = 16

  f_vec = np.array ( (\
     0.6001858177500578E-01, \
     0.2615284665839845E+00, \
     0.6695237889132748E+00, \
     0.1000000000000000E+01, \
     0.1000000000000000E+01, \
     0.5332595856827856E+00, \
     0.1819495964117640E+00, \
     0.4448047017527730E-01, \
     0.9999991751316731E+00, \
     0.9926860896560750E+00, \
     0.8410799901444538E+00, \
     0.3459800113391901E+00, \
     0.0000000000000000E+00, \
     0.2088888139634505E-02, \
     0.3876752992448843E+00, \
     0.9135215248834896E+00 ))

  n_vec = np.array ( (\
     7,  8,  9, 10, \
     6,  6,  6,  6, \
     6,  6,  6,  6, \
     0,  0,  0,  0 ))

  pop_vec = np.array ( (\
    100, 100, 100, 100, \
    100, 100, 100, 100, \
    100, 100, 100, 100, \
    90,  200, 1000, 10000 ))

  sam_vec = np.array ( (\
    10, 10, 10, 10, \
     6,  7,  8,  9, \
    10, 10, 10, 10, \
    10, 10, 10, 10 ))

  suc_vec = np.array ( (\
    90, 90, 90, 90, \
    90, 90, 90, 90, \
    10, 30, 50, 70, \
    90, 90, 90, 90 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    sam = 0
    suc = 0
    pop = 0
    n = 0
    f = 0.0
  else:
    sam = sam_vec[n_data]
    suc = suc_vec[n_data]
    pop = pop_vec[n_data]
    n = n_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, sam, suc, pop, n, f

def hypergeometric_cdf_values_test ( ):

#*****************************************************************************80
#
## HYPERGEOMETRIC_CDF_VALUE_TEST demonstrates the use of HYPERGEOMETRIC_CDF_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'HYPERGEOMETRIC_CDF_VALUES:'
  print '  HYPERGEOMETRIC_CDF_VALUES stores values of the hypergeometric CDF.'
  print ''
  print '    Sam    Suc    Pop    X     F'
  print ''

  n_data = 0

  while ( True ):

    n_data, sam, suc, pop, n, f = hypergeometric_cdf_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %6d  %6d  %6d  %6d  %24.16f' % ( sam, suc, pop, n, f )

  print ''
  print 'HYPERGEOMETRIC_CDF_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  hypergeometric_cdf_values_test ( )
  timestamp ( )


