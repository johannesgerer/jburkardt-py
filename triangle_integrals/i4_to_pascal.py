#! /usr/bin/env python
#
def i4_to_pascal ( k ):

#*****************************************************************************80
#
#% I4_TO_PASCAL converts a linear index to Pascal triangle coordinates.
#
#  Discussion:
#
#    We describe the grid points in Pascal's triangle in two ways:
#
#    As a linear index K:
#
#                     1
#                   2   3
#                 4   5   6
#               7   8   9   10
#
#    As elements (I,J) of Pascal's triangle:
#
#                     0,0
#                  1,0   0,1
#               2,0   1,1    0,2
#            3,0   2,1   1,2    0,3
#
#  Example:
#
#     K  I  J
#
#     1  0  0
#     2  1  0
#     3  0  1
#     4  2  0
#     5  1  1
#     6  0  2
#     7  3  0
#     8  2  1
#     9  1  2
#    10  0  3
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer K, the linear index of the (I,J) element.
#    1 <= K.
#
#    Output, integer I, J, the Pascal indices.
#
  from i4_to_pascal_degree import i4_to_pascal_degree
  from sys import exit

  if ( k <= 0 ):
    print ''
    print 'I4_TO_PASCAL - Fatal error!'
    print '  K must be positive.'
    exit ( 'I4_TO_PASCAL - Fatal error!' )

  d = i4_to_pascal_degree ( k )

  j = k - ( d * ( d + 1 ) ) / 2 - 1
  i = d - j

  return i, j

def i4_to_pascal_test ( ):

#*****************************************************************************80
#
## I4_TO_PASCAL_TEST tests I4_TO_PASCAL.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 April 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'I4_TO_PASCAL_TEST'
  print '  I4_TO_PASCAL converts a linear index to'
  print '  Pascal triangle indices.'
  print ''
  print '     K  =>   I     J'
  print ''

  for k in range ( 1, 21 ):

    i, j = i4_to_pascal ( k )

    print '  %4d    %4d  %4d' % ( k, i, j )
#
#  Terminate.
#
  print ''
  print 'I4_TO_PASCAL_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_to_pascal_test ( )
  timestamp ( )
