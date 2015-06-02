#!/usr/bin/env python
#
def collatz_count_max ( n ):

#*****************************************************************************80
#
## COLLATZ_COUNT_MAX seeks the maximum Collatz count for 1 through N.
#
#  Discussion:
#
#    For each integer I, we compute a sequence of values that 
#    terminate when we reach 1.  The number of steps required to
#    reach 1 is the "rank" of I, and we are searching the numbers
#    from 1 to N for the number with maximum rank.
#
#    For a given I, the sequence is produced by:
#
#    1) J = 1, X(J) = I;
#    2) If X(J) = 1, stop.
#    3) J = J + 1; 
#       if X(J-1) was even, X(J) = X(J-1)/2;
#       else                X(J) = 3 * X(J-1) + 1;
#    4) Go to 3
#
#  Example:
#
#            N    I_MAX J_MAX
#
#           10        9    20
#          100       97   119
#        1,000      871   179
#       10,000    6,171   262
#      100,000   77,031   351
#    1,000,000  837,799   525
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 April 2009
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the maximum integer to check.
#
#    Output, integer I_MAX, J_MAX, an integer I with the maximum rank,
#    and the value of the maximum rank.
#
  i_max = -1
  j_max = -1

  for i in range ( 1, n + 1 ):

    j = 1
    x = i

    while ( x != 1 ):
      j = j + 1
      if ( ( x % 2 ) == 0 ):
        x = x // 2
      else:
        x = 3 * x + 1

    if ( j_max < j ):
      i_max = i
      j_max = j

  return i_max, j_max

def collatz_count_max_test ( ):

#*****************************************************************************80
#
## COLLATZ_COUNT_MAX_TEST tests COLLATZ_COUNT_MAX.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 January 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'COLLATZ_COUNT_MAX_TEST'
  print '  COLLATZ_COUNT_MAX(N) returns the maximum length of a'
  print '  Collatz sequence for starts between 1 an N.'
  print ''
  print '       N       I_MAX         J_MAX'
  print ''

  n = 10

  while ( n <= 100000 ):

    i_max, j_max = collatz_count_max ( n )

    print '  %8d  %8d  %8d' % ( n, i_max, j_max )

    n = n * 10
 
  print ''
  print 'COLLATZ_COUNT_MAX_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  collatz_count_max_test ( )
  timestamp ( )
