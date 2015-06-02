#! /usr/bin/env python
#
def count_pose_random ( seed ):

#*****************************************************************************80
#
## COUNT_POSE_RANDOM poses a problem for the game "The Count is Good"
#
#  Discussion:
#
#    The French television show "The Count is Good" has a game that goes
#    as follows:
#
#      A number is chosen at random between 100 and 999.  This is the GOAL.
#
#      Six numbers are randomly chosen from the set 1, 2, 3, 4, 5, 6, 7, 8,
#      9, 10, 25, 50, 75, 100.  These numbers are the BLOCKS.
#
#      The player must construct a formula, using some or all of the blocks,
#      (but not more than once), and the operations of addition, subtraction,
#      multiplication and division.  Parentheses should be used to remove
#      all ambiguity.  However, it is forbidden to use subtraction in a
#      way that produces a negative result, and all division must come out
#      exactly, with no remainder.
#
#    This routine poses a sample problem from the show.  The point is,
#    to determine how to write a program that can solve such a problem.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Raymond Seroul,
#    Programming for Mathematicians,
#    Springer Verlag, 2000, page 355-357.
#
#  Parameters:
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, integer BLOCKS(6), the six numbers available for the formula.
#
#    Output, integer GOAL, the goal number.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  import numpy as np
  from i4_uniform_ab import i4_uniform_ab
  from ksub_random2 import ksub_random2

  stuff = np.array ( [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 25, 50, 75, 100 ] )

  i4_lo = 100
  i4_hi = 999
  goal, seed = i4_uniform_ab ( i4_lo, i4_hi, seed )

  m = 14
  n = 6
  ind, seed = ksub_random2 ( m, n, seed )

  blocks = np.zeros ( 6 )

  for i in range ( 0, 6 ):
    blocks[i] = stuff[ind[i]-1]

  return blocks, goal, seed

def count_pose_random_test ( ):

#*****************************************************************************80
#
## COUNT_POSE_RANDOM_TEST tests COUNT_POSE_RANDOM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 May 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'COUNT_POSE_RANDOM_TEST'
  print '  COUNT_POSE_RANDOM poses a random problem for'
  print '  the game "The Count is Good".'

  seed = 123456789

  for i in range ( 0, 5 ):

    blocks, goal, seed = count_pose_random ( seed )

    print ''
    print '  Problem #%d' % ( i )
    print ''
    print '    The goal number:'
    print ''
    print '      %d' % ( goal )
    print ''
    print '    The available numbers are'
    print ''
    print '    ',
    for j in range ( 0, 6 ):
      print '  %4d' % ( blocks[j] ),
    print ''
#
#  Terminate.
#
  print ''
  print 'COUNT_POSE_RANDOM_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  count_pose_random_test ( )
  timestamp ( )
