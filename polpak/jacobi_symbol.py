#!/usr/bin/env python
#
def jacobi_symbol ( q, p ):

#*****************************************************************************80
#
## JACOBI_SYMBOL evaluates the Jacobi symbol (Q/P).
#
#  Definition:
#
#    If P is prime, then
#
#      Jacobi Symbol (Q/P) = Legendre Symbol (Q/P)
#
#    Else 
#
#      let P have the prime factorization
#
#        P = Product ( 1 <= I <= N ) P(I)^E(I)
#
#      Jacobi Symbol (Q/P) =
#
#        Product ( 1 <= I <= N ) Legendre Symbol (Q/P(I))^E(I)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Daniel Zwillinger,
#    CRC Standard Mathematical Tables and Formulae,
#    30th Edition,
#    CRC Press, 1996, pages 86-87.
#
#  Parameters:
#
#    Input, integer Q, an integer whose Jacobi symbol with
#    respect to P is desired.
#
#    Input, integer P, the number with respect to which the Jacobi
#    symbol of Q is desired.  P should be 2 or greater.
#
#    Output, integer J, the Jacobi symbol (Q/P).
#    Ordinarily, J will be -1, 0 or 1.
#    -2, not enough factorization space.
#    -3, an error during Legendre symbol calculation.
#
  from i4_factor import i4_factor
  from legendre_symbol import legendre_symbol
#
#  P must be greater than 1.
#
  if ( p <= 1 ):
    print ''
    print 'JACOBI_SYMBOL - Fatal error!'
    print '  P must be greater than 1.'
    j = -2
    return l
#
#  Decompose P into factors of prime powers.
#
  nfactor, factor, power, nleft = i4_factor ( p )

  if ( nleft != 1 ):
    print ''
    print 'JACOBI_SYMBOL - Fatal error!'
    print '  Not enough factorization space.'
    j = -2
    return j
#
#  Force Q to be nonnegative.
#
  qq = q

  while ( qq < 0 ):
    qq = qq + p
#
#  For each prime factor, compute the Legendre symbol, and
#  multiply the Jacobi symbol by the appropriate factor.
#
  j = 1
  for i in range ( 0, nfactor ):
    pp = factor[i]
    l = legendre_symbol ( qq, pp )
    if ( l < -1 ):
      print ''
      print 'JACOBI_SYMBOL - Fatal error!'
      print '  Error during Legendre symbol calculation.'
      j = -3

    j = j * l ** power[i]

  return j

def jacobi_symbol_test ( ):

#*****************************************************************************80
#
## JACOBI_SYMBOL_TEST_TEST tests JACOBI_SYMBOL_TEST.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  ntest = 4;
  ptest = [ 3, 9, 10, 12 ];

  print ''
  print 'JACOBI_SYMBOL_TEST'
  print '  JACOBI_SYMBOL computes the Jacobi symbol'
  print '  (Q/P) which records whether Q is'
  print '  a quadratic residue modulo the number P.'

  for i in range ( 0, ntest ):
    p = ptest[i]
    print ''
    print '  Jacobi Symbols for P = %d' % ( p )
    print ''
    for q in range ( 0, p + 1 ):
      l = jacobi_symbol ( q, p )
      print '  %6d  %6d  %6d' % ( p, q, l )
 
  print ''
  print 'JACOBI_SYMBOL_TEST_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  jacobi_symbol_test ( )
  timestamp ( )
