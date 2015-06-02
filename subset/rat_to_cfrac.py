#! /usr/bin/env python
#
def rat_to_cfrac ( p, q ):

#*****************************************************************************80
#
## RAT_TO_CFRAC converts a rational value to a continued fraction.
#
#  Discussion:
#
#    The routine is given a rational number represented by P/Q, and
#    computes the monic or "simple" continued fraction representation
#    with integer coefficients of the number:
#
#      A(1) + 1/ (A(2) + 1/ (A(3) + ... + 1/A(N) ...))
#
#    The user must dimension A to a value M which is "large enough".
#    The actual number of terms needed in the continued fraction
#    representation cannot be known beforehand.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    17 August 2004
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Hart, Cheney, Lawson, Maehly, Mesztenyi, Rice, Thacher, Witzgall,
#    Computer Approximations,
#    Wiley, 1968.
#
#  Parameters:
#
#    Input, integer P, Q, the numerator and denominator of the
#    rational value whose continued fraction representation is
#    desired.
#
#    Output, integer N, the number of entries in A.
#
#    Output, integer A(N), contains the continued fraction
#    representation of the number.
#
  import numpy as np

  b = []

  n = 0

  while ( True ):

    b.append ( p // q )
    n = n + 1
    p = ( p % q )

    if ( p == 0 ):
      break

    b.append ( q // p )
    n = n + 1
    q = ( q % p )

    if ( q == 0 ):
      break

  a = np.zeros ( n )
  for i in range ( 0, n ):
    a[i] = b[i]

  return n, a

def rat_to_cfrac_test ( ):

#*****************************************************************************80
#
## RAT_TO_CFRAC_TEST tests RAT_TO_CFRAC.
#
#  Discussion:
#
#    Compute the continued fraction form of 4096/15625.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 April 2009
#
#  Author:
#
#    John Burkardt
#
  from cfrac_to_rat import cfrac_to_rat
  from i4vec_print import i4vec_print

  m = 10

  print ''
  print 'RAT_TO_CFRAC_TEST'
  print '  RAT_TO_CFRAC fraction => continued fraction,'
  print ''

  top = 4096
  bot = 15625

  print '  Regular fraction is %6d / %6d' % ( top, bot )
 
  n, a = rat_to_cfrac ( top, bot )
 
  i4vec_print ( n, a, '  Continued fraction coefficients:' )

  p, q = cfrac_to_rat ( n, a )
 
  print ''
  print '  The continued fraction convergents.'
  print '  The last row contains the value of the continued'
  print '  fraction, written as a common fraction.'
  print ''
  print '  I, P(I), Q(I), P(I)/Q(I)'
  print ''

  for i in range ( 0, n ):
    print '  %3d  %6d  %6d  %14f' % ( i, p[i], q[i], p[i] / q[i] )
#
#  Terminate.
#
  print ''
  print 'RAT_TO_CFRAC_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  rat_to_cfrac_test ( )
  timestamp ( )

