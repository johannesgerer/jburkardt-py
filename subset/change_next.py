#! /usr/bin/env python
#
def change_next ( total, coin_num, coin_value, change_num, change, done  ):

#*****************************************************************************80
#
## CHANGE_NEXT computes the next set of change for a given sum.
#
#  Examples:
#
#    Total = 17
#    COIN_NUM = 3
#    COIN_VALUE = (/ 1, 5, 10 /)
#
#
#        #  CHANGE              COIN_VALUE(CHANGE)
#
#    1   4  3 2 1 1             10 5 1 1
#    2   8  3 1 1 1 1 1 1 1     10 1 1 1 1 1 1 1
#    3   5  2 2 2 1 1            5 5 5 1 1
#    4   9  2 2 1 1 1 1 1 1 1    5 5 1 1 1 1 1 1 1
#    5  13  2 1 1 1 1 1 1 1 1 1  5 1 1 1 1 1 1 1 1 1
#           1 1 1                1 1 1
#    6  17  1 1 1 1 1 1 1 1 1 1  1 1 1 1 1 1 1 1 1 1 1
#           1 1 1 1 1 1 1        1 1 1 1 1 1
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer TOTAL, the total for which change is to be made.
#
#    Input, integer COIN_NUM, the number of types of coins.
#
#    Input, integer COIN_VALUE(COIN_NUM), the value of each coin.
#    The values should be in ascending order.
#
#    Input, integer CHANGE_NUM, the output value of CHANGE_NUM
#    from the previous call.  This value is not needed on a startup call.
#
#    Input, integer CHANGE(CHANGE_NUM), the output value of CHANGE
#    from the previous call.  This value is not needed on a startup call.
#
#    Input, logical DONE.  The user sets DONE = TRUE on the
#    first call to tell the routine this is the beginning of a computation.
#    Thereafter, DONE should be set to the output value of DONE from]
#    the previous call.
#
#    Output, integer CHANGE_NUM, the number of coins given in change
#    for the next set of change.
#
#    Output, integer CHANGE(CHANGE_NUM), the indices of the coins
#    used in this set of change.
#
#    Output, logical DONE, is FALSE until the last possible set of change
#    has been made.
#
  from sys import exit
  from change_greedy import change_greedy
  from i4vec_ascends import i4vec_ascends

  if ( done ):
#
#  Make sure the coin values are sorted.
#
    if ( not i4vec_ascends ( coin_num, coin_value ) ):
      print ''
      print 'CHANGE_NEXT - Fatal error!'
      print '  The array COIN_VALUE is not in ascending order.'
      exit ( 'CHANGE_NEXT - Fatal error!' )
#
#  Start with the greedy change.
#
    change_num, change = change_greedy ( total, coin_num, coin_value )
#
#  In a few cases, like change for 4 cents, we're done after the first call.
#
    if ( change_num == total ):
      done = True
    else:
      done = False

    return change_num, change, done
#
#  Find the last location in the input change which is NOT a penny.
#
  else:

    last = -1

    for i in range ( change_num - 1, -1, -1 ):

      if ( change[i] != 0 ):
        last = i
        break
#
#  If that location is still 0, an error was made.
#
    if ( last == -1 ):
      done = True
      return change_num, change, done
#
#  Sum the entries from that point to the end.
#
    total2 = 0
    for i in range ( last, change_num ):
      total2 = total2 + coin_value[change[i]]
#
#  Make greedy change for the partial sum using coins smaller than that one.
#
    coin_num2 = change[last]

    change_num2, change2 = change_greedy ( total2, coin_num2, coin_value )

    for i in range ( 0, change_num2 ):
      change[last+i] = change2[i]

    change_num = last + change_num2

  return change_num, change, done

def change_next_test ( ):

#*****************************************************************************80
#
## CHANGE_NEXT_TEST tests CHANGE_NEXT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  coin_num = 6
  coin_value = np.array ( [ 1, 5, 10, 25, 50, 100 ] )

  print ''
  print 'CHANGE_NEXT_TEST'
  print '  CHANGE_NEXT displays the next possible way to make'
  print '  change for a given total'

  total = 50

  print ''
  print '  The total for which change is to be made: %d' % ( total )
  print ''
  print '  The available coins are:'
  print ''
  for i in range ( 0, coin_num ):
    print '  %6d' % ( coin_value[i] )

  i = 0
  change_num = 0
  change = np.zeros ( 0 )
  done = True

  print ''

  while ( True ):

    [ change_num, change, done ] = change_next ( total, coin_num, coin_value, \
      change_num, change, done )

    if ( done or 9 < i ):
      break
 
    i = i + 1
    print '  %3d:' % ( i ),
    for j in range ( 0, change_num ):
      print '  %3d' % ( coin_value[change[j]] ),
    print ''
#
#  Terminate.
#
  print ''
  print 'CHANGE_NEXT_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  change_next_test ( )
  timestamp ( )
