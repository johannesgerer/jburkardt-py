#! /usr/bin/env python
#
def pascal_to_i4 ( i, j ):

#*****************************************************************************80
#
## PASCAL_TO_I4 converts Pacal triangle coordinates to a linear index.
#
#  Discussion:
#
#    We describe the grid points in a Pascal triangle in two ways:
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
#    Input, integer I, J, the row and column indices.  I and J must
#    be nonnegative.
#
#    Output, integer K, the linear index of the (I,J) element.
#
  from sys import exit

  if ( i < 0 ):
    print ''
    print 'PASCAL_TO_I4 - Fatal error!'
    print '  I < 0.'
    print '  I = %d' % ( i )
    exit ( 'PASCAL_TO_I4 - Fatal error!' );
  elif ( j < 0 ):
    print ''
    print 'PASCAL_TO_I4 - Fatal error!'
    print '  J < 0.'
    print '  J = %d' % ( j )
    exit ( 'PASCAL_TO_I4 - Fatal error!' )

  d = i + j

  k = ( d * ( d + 1 ) ) / 2 + j + 1

  return k

def pascal_to_i4_test ( ):

#*****************************************************************************80
#
#% PASCAL_TO_I4_TEST tests PASCAL_TO_I4.
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
  print 'PASCAL_TO_I4_TEST'
  print '  PASCAL_TO_I4 converts Pascal triangle indices to a'
  print '  linear index.'
  print ''
  print '     I     J =>    K'
  print ''

  for d in range ( 0, 5 ):
    for i in range ( d, -1, -1 ):
      j = d - i;
      k = pascal_to_i4 ( i, j )
      print '  %4d  %4d    %4d' % ( i, j, k )
    print ''
#
#  Terminate.
#
  print ''
  print 'PASCAL_TO_I4_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  pascal_to_i4_test ( )
  timestamp ( )
