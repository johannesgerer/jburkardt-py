#!/usr/bin/env python

def comp_enum ( n, k ):

#******************************************************************************/
#
## COMP_ENUM returns the number of compositions of the integer N into K parts.
#
#  Discussion:
#
#    A composition of the integer N into K parts is an ordered sequence
#    of K nonnegative integers which sum to N.  The compositions (1,2,1)
#    and (1,1,2) are considered to be distinct.
#
#    The 28 compositions of 6 into three parts are:
#
#      6 0 0,  5 1 0,  5 0 1,  4 2 0,  4 1 1,  4 0 2,
#      3 3 0,  3 2 1,  3 1 2,  3 0 3,  2 4 0,  2 3 1,
#      2 2 2,  2 1 3,  2 0 4,  1 5 0,  1 4 1,  1 3 2,
#      1 2 3,  1 1 4,  1 0 5,  0 6 0,  0 5 1,  0 4 2,
#      0 3 3,  0 2 4,  0 1 5,  0 0 6.
#
#    The formula for the number of compositions of N into K parts is
#
#      Number = ( N + K - 1 )! / ( N! * ( K - 1 )! )
#
#    Describe the composition using N '1's and K-1 dividing lines '|'.
#    The number of distinct permutations of these symbols is the number
#    of compositions.  This is equal to the number of permutations of
#    N+K-1 things, with N identical of one kind and K-1 identical of another.
#
#    Thus, for the above example, we have:
#
#      Number = ( 6 + 3 - 1 )! / ( 6! * (3-1)! ) = 28
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Albert Nijenhuis, Herbert Wilf,
#    Combinatorial Algorithms for Computers and Calculators,
#    Second Edition,
#    Academic Press, 1978,
#    ISBN: 0-12-519260-6,
#    LC: QA164.N54.
#
#  Parameters:
#
#    Input, integer N, the integer whose compositions are desired.
#
#    Input, integer K, the number of parts in the composition.
#
#    Output, integer VALUE, the number of compositions of N
#    into K parts.
#
  from i4_choose import i4_choose

  value = i4_choose ( n + k - 1, n )

  return value

def comp_enum_test ( ):

#*****************************************************************************80
#
## COMP_ENUM_TEST tests COMP_ENUM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    30 October 2014
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'COMP_ENUM_TEST'
  print '  COMP_ENUM counts compositions.'

  print ''
  for n in range ( 0, 11 ):
    for k in range ( 1, 11 ):
      num = comp_enum ( n, k )
      print '  %6d' % ( num ),
    print ''
#
#  Terminate.
#
  print ''
  print 'COMP_ENUM_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  comp_enum_test ( )
  timestamp ( )
