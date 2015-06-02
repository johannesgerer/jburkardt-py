#! /usr/bin/env python
#
def change_greedy ( total, coin_num, coin_value ):

#*****************************************************************************80
#
## CHANGE_GREEDY makes change for a given total using the biggest coins first.
#
#  Discussion:
#
#    The algorithm is simply to use as many of the largest coin first,
#    then the next largest, and so on.
#
#    It is assumed that there is always a coin of value 1.  The
#    algorithm will otherwise fail!
#
#  Example:
#
#    Total = 17
#    COIN_NUM = 3
#    COIN_VALUE = (/ 1, 5, 10 /)
#
#
#    #  CHANGE              COIN_VALUE(CHANGE)
#
#    4  3 2 1 1             10 5 1 1
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 May 2015
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
#    The values should be in ascending order, and if they are not,
#    they will be sorted.
#
#    Output, integer CHANGE_NUM, the number of coins given in change.
#
#    Output, integer CHANGE(TOTAL), the indices of the coins will be
#    in entries 1 through CHANGE_NUM.
#
  import numpy as np

  change_num = 0
  change = np.zeros ( total )
#
#  Find the largest coin smaller than the total.
#
  j = coin_num

  while ( 0 < j ):
    if ( coin_value[j-1] <= total ):
      break
    j = j - 1

  if ( j <= 0 ):
    return change_num, change
#
#  Subtract the current coin from the total.
#  Once that coin is too big, use the next coin.
#
  total_copy = total

  while ( 0 < total_copy ):

    if ( coin_value[j-1] <= total_copy ):

      total_copy = total_copy - coin_value[j-1]
      change_num = change_num + 1
      change[change_num-1] = j - 1

    else:

      j = j - 1
      if ( j <= 0 ):
        break

  return change_num, change

def change_greedy_test ( ):

#*****************************************************************************80
#
## CHANGE_GREEDY_TEST tests CHANGE_GREEDY.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  coin_num = 6
  coin_value = np.array ( [ 1, 5, 10, 25, 50, 100 ] )

  print ''
  print 'CHANGE_GREEDY_TEST'
  print '  CHANGE_GREEDY makes change using the biggest'
  print '  coins first.'

  total = 73

  print ''
  print '  The total for which change is to be made: %d' % ( total )
  print ''
  print '  The available coins are:'
  print ''
  for i in range ( 0, coin_num ):
    print '  %6d  %6d' % ( i, coin_value[i] )

  change_num, change = change_greedy ( total, coin_num, coin_value )

  print ''
  print '  %4d: ' % (change_num ),
  for i in range ( 0, change_num ):
    print '  %3d' % ( change[i] ),
  print ''

  total2 = 0
  for i in range ( 0, change_num ):
    total2 = total2 + coin_value[change[i]]
 
  print '  %4d: ' % ( total2 ),
  for i in range ( 0, change_num ):
    print '  %3d' % ( coin_value[change[i]] ),
  print ''
#
#  Terminate.
#
  print ''
  print 'CHANGE_GREEDY_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  change_greedy_test ( )
  timestamp ( )

