#!/usr/bin/env python
#
def average_length():

#*****************************************************************************80
#
## AVERAGE_LENGTH estimates the average length of a one-player game.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    15 September 2014
#
#  Author:
#
#    John Burkardt
#
  from game_length import game_length

  games = 0
  total = 0

  while ( games < 1000 ):
    games = games + 1
    n = game_length ( )
    total = total + n

  average = total / 1000
  print 'Average number of moves is ' + repr ( average )

if ( __name__ == '__main__' ):
  average_length ( )
      
