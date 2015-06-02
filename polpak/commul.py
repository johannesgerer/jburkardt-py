#!/usr/bin/env python

def commul ( n, nfactor, iarray ):

#*****************************************************************************80
#
## COMMUL computes a multinomial combinatorial coefficient.
#
#  Discussion:
#
#    The multinomial coefficient is a generalization of the binomial
#    coefficient.  It may be interpreted as the number of combinations of
#    N objects, where IARRAY(1) objects are indistinguishable of type 1,
#    ... and IARRAY(K) are indistinguishable of type NFACT.
#
#    The formula is
#
#      NCOMB = N! / ( IARRAY(1)! IARRAY(2)! ... IARRAY(NFACT)! )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, determines the numerator.
#
#    Input, integer NFACTOR, the number of factors in the numerator.
#
#    Input, integer IARRAY(NFACTOR).
#    IARRAY contains the NFACT values used in the denominator.
#    Note that the sum of these entries should be N,
#    and that all entries should be nonnegative.
#
#    Output, integer NCOMB, the value of the multinomial coefficient.
#
  import numpy as np
  from r8_gamma_log import r8_gamma_log
  from sys import exit

  for i in range ( 0, nfactor ):

    if ( iarray[i] < 0 ):
      print ''
      print 'COMMUL - Fatal error!'
      print '  Entry %d of IARRAY = %d' % ( i, iarray[i] )
      print 1, '  But this value must be nonnegative.'
      exit ( 'COMMUL - Fatal error!' )

  isum = np.sum ( iarray )

  if ( isum != n ):
    print ''
    print 'COMMUL - Fatal error!'
    print '  The sum of the IARRAY entries is %d' % (isum )
    print '  But it must equal N = %d' % ( n )
    exit ( 'COMMUL - Fatal error!' )
 
  facn = r8_gamma_log ( float ( n + 1 ) )
 
  for i in range ( 0, nfactor ):
 
    fack = r8_gamma_log ( float ( iarray[i] + 1 ) )
    facn = facn - fack

  ncomb = int ( np.round ( np.exp ( facn ) ) )

  return ncomb

def commul_test ( ):

#*****************************************************************************80
#
## COMMUL_TEST tests COMMUL.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    26 January 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ''
  print 'COMMUL_TEST'
  print '  COMMUL computes a multinomial coefficient.'

  n = 8
  nfactor = 2
  factor = np.array ( [ 6, 2 ] )
  ncomb = commul ( n, nfactor, factor )
  print ''
  print '  N = %d' % ( n )
  print '  Number of factors = %d' % ( nfactor )
  for i in range ( 0, nfactor ):
    print '  %2d  %2d' % ( i, factor[i] )
  print '  Value of coefficient = %d' % ( ncomb )

  n = 8
  nfactor = 3
  factor = np.array ( [ 2, 2, 4 ] )
  ncomb = commul ( n, nfactor, factor )
  print ''
  print '  N = %d' % ( n )
  print '  Number of factors = %d' % ( nfactor )
  for i in range ( 0, nfactor ):
    print '  %2d  %2d' % ( i, factor[i] )
  print '  Value of coefficient = %d' % ( ncomb )

  n = 13
  nfactor = 4
  factor = np.array ( [ 5, 3, 3, 2 ] )
  ncomb = commul ( n, nfactor, factor )
  print ''
  print '  N = %d' % ( n )
  print '  Number of factors = %d' % ( nfactor )
  for i in range ( 0, nfactor ):
    print '  %2d  %2d' % ( i, factor[i] )
  print '  Value of coefficient = %d' % ( ncomb )

  print ''
  print 'COMMUL_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  commul_test ( )
  timestamp ( )
