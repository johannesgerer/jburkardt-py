#! /usr/bin/env python
#
def power_mod ( a, n, m ):

#*****************************************************************************80
#
## POWER_MOD computes mod ( A^N, M ).
#
#  Discussion:
#
#    Some programming tricks are used to speed up the computation, and to
#    allow computations in which A^N is much too large to store in a
#    real word.
#
#    First, for efficiency, the power A^N is computed by determining
#    the binary expansion of N, then computing A, A^2, A^4, and so on
#    by repeated squaring, and multiplying only those factors that
#    contribute to A^N.
#
#    Secondly, the intermediate products are immediately "mod'ed", which
#    keeps them small.
#
#    For instance, to compute mod ( A^13, 11 ), we essentially compute
#
#       13 = 1 + 4 + 8
#
#       A^13 = A * A^4 * A^8
#
#       mod ( A^13, 11 ) = mod ( A, 11 ) * mod ( A^4, 11 ) * mod ( A^8, 11 ).
#
#    Fermat's little theorem says that if P is prime, and A is not divisible
#    by P, then ( A^(P-1) - 1 ) is divisible by P.
#
#  Example:
#
#     A  N  M  X
#
#    13  0 31  1
#    13  1 31 13
#    13  2 31 14
#    13  3 31 27
#    13  4 31 10
#    13  5 31  6
#    13  6 31 16
#    13  7 31 22
#    13  8 31  7 
#    13  9 31 29
#    13 10 31  5
#    13 11 31  3
#    13 12 31  8
#    13 13 31 11
#    13 14 31 19
#    13 15 31 30
#    13 16 31 18
#    13 17 31 17
#    13 18 31  4
#    13 19 31 21
#    13 20 31 25
#    13 21 31 15
#    13 22 31  9
#    13 23 31 24
#    13 24 31  2
#    13 25 31 26
#    13 26 31 28
#    13 27 31 23
#    13 28 31 20
#    13 29 31 12
#    13 30 31  1
#    13 31 31 13
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    15 November 2004
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer A, the base of the expression to be tested.
#    A should be nonnegative.
#
#    Input, integer N, the power to which the base is raised.
#    N should be nonnegative.
#
#    Input, integer M, the divisor against which the expression is tested.
#    M should be positive.
#
#    Output, integer X, the remainder when A^N is divided by M.
#
  if ( a < 0 ):
    x = -1
    return x

  if ( int ( a ) != a ):
    x = -1
    return x

  if ( n < 0 ):
    x = -1
    return x

  if ( int ( n ) != n ):
    x = -1
    return x

  if ( m <= 0 ):
    x = -1
    return x

  if ( int ( m ) != m ):
    x = -1
    return x
#
#  A contains the successive squares of A.
#
  x = 1

  while ( 0 < n ):

    d = ( n % 2 )

    if ( d == 1 ):
      x = ( ( x * a ) % m )

    a = ( ( a * a ) % m )
    n = ( ( n - d ) // 2 )
#
#  Ensure that 0 <= X.
#
  while ( x < 0 ):
    x = x + m

  return x

def power_mod_test ( ):

#*****************************************************************************80
#
## POWER_MOD_TEST tests POWER_MOD.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 May 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'POWER_MOD_TEST'
  print '  POWER_MOD computes the remainder of a power'
  print '  of an integer modulo another integer.'

  a = 7
  n = 50
  m = 11

  x = power_mod ( a, n, m )

  print ''
  print '  A = %d' % ( a )
  print '  N = %d' % ( n )
  print '  M = %d' % ( m )
  print '  mod ( A^N, M ) = %d' % ( x )

  a = 3
  n = 118
  m = 119

  x = power_mod ( a, n, m )

  print ''
  print '  A = %d' % ( a )
  print '  N = %d' % ( n )
  print '  M = %d' % ( m )
  print '  mod ( A^N, M ) = %d' % ( x )
#
#  Terminate.
#
  print ''
  print 'POWER_MOD_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  power_mod_test ( )
  timestamp ( )

