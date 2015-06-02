#!/usr/bin/env python
#
def legendre_symbol ( q, p ):

#*****************************************************************************80
#
## LEGENDRE_SYMBOL evaluates the Legendre symbol (Q/P).
#
#  Definition:
#
#    Let P be an odd prime.  Q is a QUADRATIC RESIDUE modulo P
#    if there is an integer R such that R^2 = Q ( mod P ).
#    The Legendre symbol ( Q / P ) is defined to be:
#
#      + 1 if Q ( mod P ) /= 0 and Q is a quadratic residue modulo P,
#      - 1 if Q ( mod P ) /= 0 and Q is not a quadratic residue modulo P,
#        0 if Q ( mod P ) == 0.
#
#    We can also define ( Q / P ) for P = 2 by:
#
#      + 1 if Q ( mod P ) /= 0
#        0 if Q ( mod P ) == 0
#
#  Example:
#
#    (0/7) =   0
#    (1/7) = + 1  ( 1^2 = 1 mod 7 )
#    (2/7) = + 1  ( 3^2 = 2 mod 7 )
#    (3/7) = - 1
#    (4/7) = + 1  ( 2^2 = 4 mod 7 )
#    (5/7) = - 1
#    (6/7) = - 1
#
#  Note:
#
#    For any prime P, exactly half of the integers from 1 to P-1
#    are quadratic residues.
#
#    ( 0 / P ) = 0.
#
#    ( Q / P ) = ( mod ( Q, P ) / P ).
#
#    ( Q / P ) = ( Q1 / P ) * ( Q2 / P ) if Q = Q1 * Q2.
#
#    If Q is prime, and P is prime and greater than 2, then:
#
#      if ( Q == 1 ) then
#
#        ( Q / P ) = 1
#
#      else if ( Q == 2 ) then
#
#        ( Q / P ) = + 1 if mod ( P, 8 ) = 1 or mod ( P, 8 ) = 7,
#        ( Q / P ) = - 1 if mod ( P, 8 ) = 3 or mod ( P, 8 ) = 5.
#
#      else
#
#        ( Q / P ) = - ( P / Q ) if Q = 3 ( mod 4 ) and P = 3 ( mod 4 ),
#                  =   ( P / Q ) otherwise.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Charles Pinter,
#    A Book of Abstract Algebra,
#    McGraw Hill, 1982, pages 236-237.
#
#    Daniel Zwillinger,
#    CRC Standard Mathematical Tables and Formulae,
#    30th Edition,
#    CRC Press, 1996, pages 86-87.
#
#  Parameters:
#
#    Input, integer Q, an integer whose Legendre symbol with
#    respect to P is desired.
#
#    Input, integer P, a prime number, greater than 1, with respect
#    to which the Legendre symbol of Q is desired.
#
#    Output, integer L, the Legendre symbol (Q/P).
#    Ordinarily, L will be -1, 0 or 1.
#    L = -2, P is less than or equal to 1.
#    L = -3, P is not prime.
#    L = -4, the internal stack of factors overflowed.
#    L = -5, not enough factorization space.
#
  import numpy as np
  from i4_factor import i4_factor
  from i4_is_prime import i4_is_prime
  from sys import exit

  l = 0
#
#  P must be greater than 1.
#
  if ( p <= 1 ):
    print ''
    print 'LEGENDRE_SYMBOL - Fatal error!'
    print '  P must be greater than 1.'
    l = -2
    exit ( 'LEGENDRE_SYMBOL - Fatal error!' )
#
#  P must be prime.
#
  if ( not ( i4_is_prime ( p ) ) ):
    print ''
    print 'LEGENDRE_SYMBOL - Fatal error!'
    print '  P is not prime.'
    l = -3
    exit ( 'LEGENDRE_SYMBOL - Fatal error!' )
#
#  ( k*P / P ) = 0.
#
  if ( ( q % p ) == 0 ):
    l = 0
    return l
#
#  For the special case P = 2, (Q/P) = 1 for all odd numbers.
#
  if ( p == 2 ):
    l = 1
    return l

#
#  Make a copy of Q, and force it to be nonnegative.
#
  qq = q

  while ( qq < 0 ):
    qq = qq + p

  nstack = 0
  pstack = np.zeros ( 100 )
  qstack = np.zeros ( 100 )
  pp = p
  l = 1

  while ( True ):

    qq = ( qq % pp )
#
#  Decompose QQ into factors of prime powers.
#
    nfactor, factor, power, nleft = i4_factor ( qq )

    if ( nleft != 1 ):
      print ''
      print 'LEGENDRE_SYMBOL - Fatal error!'
      print '  Not enough factorization space.'
      exit ( 'LEGENDRE_SYMBOL - Fatal error!' )
#
#  Each factor which is an odd power is added to the stack.
#
    nmore = 0

    for i in range ( 0, nfactor ):

      if ( ( power[i] % 2 ) == 1 ):

        nmore = nmore + 1
        pstack[nstack] = pp
        qstack[nstack] = factor[i]
        nstack = nstack + 1

    hop = False

    if ( nmore != 0 ):

      nstack = nstack - 1
      qq = qstack[nstack]
#
#  Check for a QQ of 1 or 2.
#
      if ( qq == 1 ):

        l = + 1 * l

      elif ( qq == 2 and ( ( pp % 8 ) == 1 or ( pp % 8 ) == 7 ) ):

        l = + 1 * l

      elif ( qq == 2 and ( ( pp % 8 ) == 3 or ( pp % 8 ) == 5 ) ):

        l = - 1 * l

      else:

        if ( ( pp % 4 ) == 3 and ( qq % 4 ) == 3 ):
          l = - 1 * l

        rr = pp
        pp = qq
        qq = rr

        hop = True
#
#  If the stack is empty, we're done.
#
    if ( not hop ):

      if ( nstack == 0 ):
        break
#
#  Otherwise, get the last P and Q from the stack, and process them.
#
      nstack = nstack - 1
      pp = pstack[nstack]
      qq = qstack[nstack]

  return l

def legendre_symbol_test ( ):

#*****************************************************************************80
#
## LEGENDRE_SYMBOL_TEST_TEST tests LEGENDRE_SYMBOL_TEST.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  ntest = 4;
  ptest = [ 7, 11, 13, 17 ];

  print ''
  print 'LEGENDRE_SYMBOL_TEST'
  print '  LEGENDRE_SYMBOL computes the Legendre'
  print '  symbol (Q/P) which records whether Q is'
  print '  a quadratic residue modulo the prime P.'

  for i in range ( 0, ntest ):
    p = ptest[i]
    print ''
    print '  Legendre Symbols for P = %d' % ( p )
    print ''
    for q in range ( 0, p + 1 ):
      l = legendre_symbol ( q, p )
      print '  %6d  %6d  %6d' % ( p, q, l )
 
  print ''
  print 'LEGENDRE_SYMBOL_TEST_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  legendre_symbol_test ( )
  timestamp ( )
