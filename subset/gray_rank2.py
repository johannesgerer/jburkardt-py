#! /usr/bin/env python
#
def gray_rank2 ( gray ):

#*****************************************************************************80
#
## GRAY_RANK2 ranks a Gray code.
#
#  Discussion:
#
#    In contrast to GRAY_RANK, this routine is entirely arithmetical,
#    and does not require access to bit testing and setting routines.
#
#
#    Given the number GRAY, its ranking is the order in which it would be
#    visited in the Gray code ordering.  The Gray code ordering begins
#
#    Rank  Gray  Gray
#          (Dec) (Bin)
#
#       0     0  0000
#       1     1  0001
#       2     3  0011
#       3     2  0010
#       4     6  0110
#       5     7  0111
#       6     5  0101
#       7     4  0100
#       8    12  0110
#       etc
#
#   This routine is given a Gray code, and has to return the rank.
#
#  Example:
#
#    Gray  Gray  Rank
#    (Dec) (Bin)
#
#     0       0     0
#     1       1     1
#     2      10     3
#     3      11     2
#     4     100     7
#     5     101     6
#     6     110     4
#     7     111     5
#     8    1000    15
#     9    1001    14
#    10    1010    12
#    11    1011    13
#    12    1100     8
#    13    1101     9
#    14    1110    11
#    15    1111    10
#    16   10000    31
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
#    Input, integer GRAY, the Gray code to be ranked.
#
#    Output, integer RANK, the rank of GRAY, and the integer whose Gray
#    code is GRAY.
#
  from sys import exit

  if ( gray < 0 ):
    print ''
    print 'GRAY_RANK2 - Fatal error!'
    print '  Input value of GRAY < 0.'
    exit ( 'GRAY_RANK2 - Fatal error!' )

  if ( gray == 0 ):
    rank = 0
    return rank
#
#  Find TWO_K, the largest power of 2 less than or equal to GRAY.
#
  k = 0
  two_k = 1
  while ( 2 * two_k <= gray ):
    two_k = two_k * 2
    k = k + 1

  rank = two_k
  last = 1
  gray = gray - two_k

  while ( 0 < k ):

    two_k = ( two_k // 2 )
    k = k - 1

    next = ( two_k <= gray and gray < two_k * 2 )

    if ( next ):
      gray = gray - two_k

    if ( next != last ):
      rank = rank + two_k
      last = 1
    else:
      last = 0

  return rank

def gray_rank2_test ( ):

#*****************************************************************************80
#
## GRAY_RANK2_TEST tests GRAY_RANK2.
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
  from gray_unrank2 import gray_unrank2

  print ''
  print 'GRAY_RANK2_TEST'
  print '  GRAY_RANK2 ranks a Gray code;'
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
  print 'GRAY_RANK2_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  gray_rank2_test ( )
  timestamp ( )
