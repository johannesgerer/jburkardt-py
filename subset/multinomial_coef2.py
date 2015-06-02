#! /usr/bin/env python
#
def multinomial_coef2 ( nfactor, factor ):

#*****************************************************************************80
#
## MULTINOMIAL_COEF2 computes a multinomial coefficient.
#
#  Discussion:
#
#    The multinomial coefficient is a generalization of the binomial
#    coefficient.  It may be interpreted as the number of combinations of
#    N objects, where FACTOR(1) objects are indistinguishable of type 1,
#    ... and FACTOR(NFACTOR) are indistinguishable of type NFACTOR,
#    and N is the sum of FACTOR(1) through FACTOR(NFACTOR).
#
#    NCOMB = N! / ( FACTOR(1)! FACTOR(2)! ... FACTOR(NFACTOR)! )
#
#    A direct method is used, which should be exact.  However, there
#    is a possibility of intermediate overflow of the result.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer NFACTOR, the number of factors.
#
#    Input, integer FACTOR(NFACTOR), contains the factors.
#    0 <= FACTOR(I)
#
#    Output, integer NCOMB, the value of the multinomial coefficient.
#
  from sys import exit
#
#  Each factor must be nonnegative.
#
  for i in range ( 0, nfactor ): 

    if ( factor[i] < 0 ):
      print ''
      print 'MULTINOMIAL_COEF2 - Fatal error!'
      print '  Factor %d = %d' % ( i, factor[i] )
      print '  But this value must be nonnegative.'
      exit  ( 'MULTINOMIAL_COEF2 - Fatal error!' )

  ncomb = 1
  k = 0

  for i in range ( 0, nfactor ):

    for j in range ( 1, factor[i] + 1 ):
      k = k + 1
      ncomb = ( ncomb * k ) // j

  return ncomb

def multinomial_coef2_test ( ):

#*****************************************************************************80
#
#% MULTINOMIAL_COEF2_TEST tests MULTINOMIAL_COEF2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  maxfactor = 5

  print ''
  print 'MULTINOMIAL_COEF2_TEST'
  print '  MULTINOMIAL_COEF2 computes multinomial'
  print '  coefficients directly.'

  print ''
  print '  Line 10 of the BINOMIAL table:'
  print ''

  n = 10
  nfactor = 2
  factor = np.zeros ( nfactor, dtype = np.int32 )

  for i in range ( 0, n + 1 ):

    factor[0] = i
    factor[1] = n - i

    ncomb = multinomial_coef2 ( nfactor, factor )

    print '  %2d  %2d   %3d' % ( factor[0], factor[1], ncomb )

  print ''
  print '  Level 5 of the TRINOMIAL coefficients:'

  n = 5
  nfactor = 3
  factor = np.zeros ( nfactor, dtype = np.int32 )

  for i in range ( 0, n + 1 ):

    factor[0] = i

    print ''

    for j in range ( 0, n - factor[0] + 1 ):

      factor[1] = j
      factor[2] = n - factor[0] - factor[1]

      ncomb = multinomial_coef2 ( nfactor, factor )

      print '  %2d  %2d  %2d   %3d' % ( factor[0], factor[1], factor[2], ncomb )
#
#  Terminate.
#
  print ''
  print 'MULTINOMIAL_COEF2_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  multinomial_coef2_test ( )
  timestamp ( )
