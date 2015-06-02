#! /usr/bin/env python
#
def multiperm_enum ( n, k, counts ):

#*****************************************************************************80
#
## MULTIPERM_ENUM enumerates multipermutations.
#
#  Discussion:
#
#    A multipermutation is a permutation of objects, some of which are
#    identical.
#
#    While there are 6 permutations of the distinct objects A,B,C, there
#    are only 3 multipermutations of the objects A,B,B.
#
#    In general, there are N! permutations of N distinct objects, but
#    there are N! / ( ( M1! ) ( M2! ) ... ( MK! ) ) multipermutations
#    of N objects, in the case where the N objects consist of K
#    types, with M1 examples of type 1, M2 examples of type 2 and so on,
#    and for which objects of the same type are indistinguishable.
#
#  Example:
#
#    Input:
#
#      N = 5, K = 3, COUNTS = (/ 1, 2, 2 /)
#
#    Output:
#
#      Number = 30
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of items in the multipermutation.
#
#    Input, integer K, the number of types of items.
#    1 <= K.  Ordinarily, K <= N, but we allow any positive K, because
#    we also allow entries in COUNTS to be 0.
#
#    Input, integer COUNTS(K), the number of items of each type.
#    0 <= COUNTS(1:K) <= N and sum ( COUNTS(1:K) ) = N.
#
#    Output, integer VALUE, the number of multipermutations.
#
  if ( n < 0 ):
    value = -1
    return value

  if ( n == 0 ):
    value = 1
    return value

  if ( k < 1 ):
    value = -1
    return value

  if ( any ( counts < 0 ) ):
    value = -1
    return value

  if ( sum ( counts ) != n ):
    number = -1
    return value
#
#  Ready for computation.
#  By design, the integer division should never have a remainder.
#
  top = 0
  value = 1

  for i in range ( 0, k ):

    for j in range ( 1, counts[i] + 1 ):
      top = top + 1
      value = round ( ( value * top ) / j )

  return value

def multiperm_enum_test ( ):

#*****************************************************************************80
#
## MULTIPERM_ENUM_TEST tests MULTIPERM_ENUM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    19 December 2014
#
#  Author:
#
#    John Burkardt
#
  from compnz_random import compnz_random
  from i4_uniform_ab import i4_uniform_ab

  n = 5
  seed = 123456789
  test_num = 5
  
  print ''
  print 'MULTIPERM_ENUM_TEST:'
  print '  MULTIPERM_ENUM enumerates multipermutations.'
  print ''
  print '  N is the number of objects to be permuted.'
  print '  K is the number of distinct types of objects.'
  print '  COUNTS is the number of objects of each type.'
  print '  NUMBER is the number of multipermutations.'
  print ''
  print '  Number       N       K       Counts(1:K)'
  print ''

  for test in range ( 0, test_num ):

    k, seed = i4_uniform_ab ( 1, n, seed )

    counts, seed = compnz_random ( n, k, seed )

    number = multiperm_enum ( n, k, counts )

    print '  %6d  %6d  %6d' % ( number, n, k ),
    for i in range ( 0, k ):
      print '  %4d' % ( counts[i] ),
    print ''
#
#  Terminate.
#
  print ''
  print 'MULTIPERM_ENUM_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  multiperm_enum_test ( )
  timestamp ( )
