#!/usr/bin/env python

def hypergeometric_pdf_values ( n_data ):

#*****************************************************************************80
#
## HYPERGEOMETRIC_PDF_VALUES returns some values of the hypergeometric PDF.
#
#  Discussion:
#
#    PDF(X)(A,B) is the probability of X successes in A trials,
#    given that the probability of success on a single trial is B.
#
#    In Mathematica, the function can be evaluated by:
#
#      dist = HypergeometricDistribution [ sam, suc, pop ]
#      PDF [ dist, n ]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 February 2015
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
    0.05179370533242827E+00, \
    0.2015098848089788E+00, \
    0.4079953223292903E+00, \
    0.3304762110867252E+00, \
    0.5223047493549780E+00, \
    0.3889503452643453E+00, \
    0.1505614239732950E+00, \
    0.03927689321042477E+00, \
    0.00003099828465518108E+00, \
    0.03145116093938197E+00, \
    0.2114132170316862E+00, \
    0.2075776621999210E+00, \
    0.0000000000000000E+00, \
    0.002088888139634505E+00, \
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

def hypergeometric_pdf_values_test ( ):

#*****************************************************************************80
#
## HYPERGEOMETRIC_PDF_VALUE_TEST demonstrates the use of HYPERGEOMETRIC_PDF_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'HYPERGEOMETRIC_PDF_VALUES:'
  print '  HYPERGEOMETRIC_PDF_VALUES stores values of the hypergeometric PDF.'
  print ''
  print '     Sam     Suc     Pop       X          F'
  print ''

  n_data = 0

  while ( True ):

    n_data, sam, suc, pop, n, f = hypergeometric_pdf_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %6d  %6d  %6d  %6d  %24.16f' % ( sam, suc, pop, n, f )

  print ''
  print 'HYPERGEOMETRIC_PDF_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  hypergeometric_pdf_values_test ( )
  timestamp ( )


