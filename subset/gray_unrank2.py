#! /usr/bin/env python
#
def gray_unrank2 ( rank ):

#*****************************************************************************80
#
## GRAY_UNRANK2 unranks a Gray code.
#
#  Discussion:
#
#    In contrast to GRAY_UNRANK, this routine is entirely arithmetical,
#    and does not require access to bit testing and setting routines.
#
#    The binary values of the Gray codes of successive integers differ in
#    just one bit.
#
#    The sequence of Gray codes for 0 to (2**N)-1 can be interpreted as a
#    Hamiltonian cycle on a graph of the cube in N dimensions.
#
#  Example:
#
#    Rank  Gray  Gray
#          (Dec) (Bin)
#
#     0     0       0
#     1     1       1
#     2     3      11
#     3     2      10
#     4     6     110
#     5     7     111
#     6     5     101
#     7     4     100
#     8    12    1100
#     9    14    1001
#    10    12    1010
#    11    13    1011
#    12     8    1100
#    13     9    1101
#    14    11    1110
#    15    10    1111
#    16    31   10000
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer RANK, the integer whose Gray code is desired.
#
#    Output, integer GRAY, the Gray code of the given rank.
#
  if ( rank <= 0 ):
    gray = 0
    return gray

  k = 0
  two_k = 1
  while ( 2 * two_k <= rank ):
    two_k = two_k * 2
    k = k + 1

  gray = two_k
  rank = rank - two_k
  next = 1

  while ( 0 < k ):

    two_k = ( two_k // 2 )
    k = k - 1

    last = next
    next = ( two_k <= rank and rank <= two_k * 2 )

    if ( next != last ):
      gray = gray + two_k

    if ( next ):
      rank = rank - two_k

  return gray

def gray_unrank2_test ( ):

#*****************************************************************************80
#
## GRAY_UNRANK2_TEST tests GRAY_UNRANK2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 May 2015
#
#  Author:
#
#    John Burkardt
#
  from gray_rank2 import gray_rank2

  print ''
  print 'GRAY_UNRANK2_TEST'
  print '  GRAY_UNRANK2 unranks a Gray code.'
  print ''
  print '    R  =                         RANK'
  print '    G  =            GRAY_UNRANK2(RANK)'
  print '    R2 = GRAY_RANK2(GRAY_UNRANK2(RANK))'
  print ''
  print '       R       G       R2'
  print ''

  for rank in range ( 0, 25 ):
    gray = gray_unrank2 ( rank )
    rank2 = gray_rank2 ( gray )
    print '  %6d  %6d  %6d' % ( rank, gray, rank2 )
#
#  Terminate.
#
  print ''
  print 'GRAY_UNRANK2_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  gray_unrank2_test ( )
  timestamp ( )
