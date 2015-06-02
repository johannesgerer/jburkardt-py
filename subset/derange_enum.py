#! /usr/bin/env python
#
def derange_enum ( n ):

#*****************************************************************************80
#
## DERANGE_ENUM returns the number of derangements of N objects.
#
#  Discussion:
#
#    A derangement of N objects is a permutation which leaves no object
#    unchanged.
#
#    A derangement of N objects is a permutation with no fixed
#    points.  If we symbolize the permutation operation by "P",
#    then for a derangment, P(I) is never equal to I.
#
#    The number of derangements of N objects is sometimes called
#    the subfactorial function, or the derangement number D(N).
#
#  Recursion:
#
#      D(0) = 1
#      D(1) = 0
#      D(2) = 1
#      D(N) = (N-1) * ( D(N-1) + D(N-2) )
#
#    or
#
#      D(0) = 1
#      D(1) = 0
#      D(N) = N * D(N-1) + (-1)^N
#
#  Formula:
#
#    D(N) = N! * ( 1 - 1/1! + 1/2! - 1/3! ... 1/N! )
#
#    Based on the inclusion/exclusion law.
#
#    D(N) is the number of ways of placing N non-attacking rooks on
#    an N by N chessboard with one diagonal deleted.
#
#    Limit ( N -> Infinity ) D(N)/N! = 1 / e.
#
#    The number of permutations with exactly K items in the right
#    place is COMB(N,K) * D(N-K).
#
#  First values:
#
#     N         D(N)
#     0           1
#     1           0
#     2           1
#     3           2
#     4           9
#     5          44
#     6         265
#     7        1854
#     8       14833
#     9      133496
#    10     1334961
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of objects to be permuted.
#
#    Output, integer VALUE, the number of derangements of N objects.
#
  if ( n < 0 ):

    dn = -1

  elif ( n == 0 ):

    dn = 1

  elif ( n == 1 ):

    dn = 0

  elif ( n == 2 ):

    dn = 1

  else:

    dnm1 = 0
    dn = 1

    for i in range ( 3, n + 1 ):
      dnm2 = dnm1
      dnm1 = dn
      dn = ( i - 1 ) * ( dnm1 + dnm2 )

  value = dn

  return value

def derange_enum_test ( ):

#*****************************************************************************80
#
## DERANGE_ENUM_TEST tests DERANGE_ENUM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    16 December 2014
#
#  Author:
#
#    John Burkardt
#
  n = 10

  print ''
  print 'DERANGE_ENUM_TEST'
  print '  DERANGE_ENUM counts derangements;'
  print ''
  print '  N    # of derangements'
  print ''

  for i in range ( 0, n + 1 ):
    print '  %8d  %8d' % ( i, derange_enum ( i ) )
#
#  Terminate.
#
  print ''
  print 'DERANGE_ENUM_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  derange_enum_test ( )
  timestamp ( )

