#!/usr/bin/env python

def pentagon_num ( n ) :

#*****************************************************************************80
#
## PENTAGON_NUM computes the N-th pentagonal number.
#
#  Definition:
#
#    The pentagonal number P(N) counts the number of dots in a figure of
#    N nested pentagons.  The pentagonal numbers are defined for both
#    positive and negative N.
#
#  First values:
#
#    N   P
#
#   -5  40
#   -4  26
#   -3  15
#   -2   7
#   -1   2
#    0   0
#    1   1
#    2   5
#    3  12
#    4  22
#    5  35
#
#  Formula:
#
#    P(N) = ( N * ( 3 * N - 1 ) ) / 2
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the index of the pentagonal number desired.
#
#    Output, integer P, the value of the N-th pentagonal number.
#
  value = ( n * ( 3 * n - 1 ) ) / 2

  return value

def pentagon_num_test ( ):

#*****************************************************************************80
#
## PENTAGON_NUM_TEST tests PENTAGON_NUM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    24 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'PENTAGON_NUM_TEST'
  print '  PENTAGON_NUM computes the pentagonal numbers.'
  print ''
  print '     N      PENTAGON_NUM(N)'
  print ''

  for n in range ( 1, 11 ):
    value = pentagon_num ( n )
    print '  %4d  %12d' % ( n, value )      
 
  print ''
  print 'PENTAGON_NUM_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  pentagon_num_test ( )
  timestamp ( )
