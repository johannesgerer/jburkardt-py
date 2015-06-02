#! /usr/bin/env python
#
def i4_to_pascal_degree ( k ):

#*****************************************************************************80
#
## I4_TO_PASCAL_DEGREE converts a linear index to a Pascal triangle degree.
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
#    The quantity D represents the "degree" of the corresponding monomial,
#    that is, D = I + J.
#
#    We can compute D directly from K using the quadratic formula.
#
#  Example:
#
#     K  I  J  D
#
#     1  0  0  0
#
#     2  1  0  1
#     3  0  1  1
#
#     4  2  0  2
#     5  1  1  2
#     6  0  2  2
#
#     7  3  0  3
#     8  2  1  3
#     9  1  2  3
#    10  0  3  3
#
#    11  4  0  4
#    12  3  1  4
#    13  2  2  4
#    14  1  3  4
#    15  0  4  4
#
#    16  5  0  5
#    17  4  1  5
#    18  3  2  5
#    19  2  3  5
#    20  1  4  5
#    21  0  5  5
#
#    22  6  0  6
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
#    Output, integer D, the degree (sum) of the corresponding Pascal indices.
#
  import numpy as np
  from sys import exit

  if ( k <= 0 ):
    print ''
    print 'I4_TO_PASCAL_DEGREE - Fatal error!'
    print '  K must be positive.'
    exit ( 'I4_TO_PASCAL_DEGREE - Fatal error!' )

  d = int ( 0.5 * ( -1.0 + np.sqrt ( 1.0 + 8.0 * ( k - 1 ) ) ) )

  return d

def i4_to_pascal_degree_test ( ):

#*****************************************************************************80
#
#% I4_TO_PASCAL_DEGREE_TEST tests I4_TO_PASCAL_DEGREE.
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
  print 'I4_TO_PASCAL_DEGREE_TEST'
  print '  I4_TO_PASCAL_DEGREE converts a linear index to'
  print '  the degree of the corresponding Pascal triangle indices.'
  print ''
  print '     K  =>   D'
  print ''

  for k in range ( 1, 21 ):

    d = i4_to_pascal_degree ( k )

    print '  %4d    %4d' % ( k, d )
#
#  Terminate.
#
  print ''
  print 'I4_TO_PASCAL_DEGREE_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_to_pascal_degree_test ( )
  timestamp ( )

