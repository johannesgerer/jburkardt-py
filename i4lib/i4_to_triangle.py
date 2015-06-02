#!/usr/bin/env python

def i4_to_triangle ( k ):

#*****************************************************************************80
#
## I4_TO_TRIANGLE converts an integer to triangular coordinates.
#
#  Discussion:
#
#    Triangular coordinates are handy when storing a naturally triangular
#    array (such as the lower half of a matrix) in a linear array.
#
#    Thus, for example, we might consider storing
#
#    (1,1)
#    (2,1) (2,2)
#    (3,1) (3,2) (3,3)
#    (4,1) (4,2) (4,3) (4,4)
#
#    as the linear array
#
#    (1,1) (2,1) (2,2) (3,1) (3,2) (3,3) (4,1) (4,2) (4,3) (4,4)
#
#    Here, the quantities in parenthesis represent the natural row and
#    column indices of a single number when stored in a rectangular array.
#
#    In this routine, we are given the location K of an item in the
#    linear array, and wish to determine the row I and column J
#    of the item when stored in the triangular array.
#
#  First Values:
#
#     K  I  J
#
#     0  0  0
#     1  1  1
#     2  2  1
#     3  2  2
#     4  3  1
#     5  3  2
#     6  3  3
#     7  4  1
#     8  4  2
#     9  4  3
#    10  4  4
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer K, the linear index of the (I,J) element, which
#    must be nonnegative.
#
#    Output, integer I, J, the row and column indices.
#
  from math import sqrt
  from sys import exit

  if ( k < 0 ):
    print ''
    print 'I4_TO_TRIANGLE - Fatal error!'
    print '  K < 0.'
    print '  K = %d' % ( k )
    exit ( 'I4_TO_TRIANGLE - Fatal error!' )

  if ( k == 0 ):
    i = 0
    j = 0
  else:
    i = int ( sqrt ( float ( 2 * k ) ) )

    if ( i * i + i < 2 * k ):
      i = i + 1

    j = k - ( i * ( i - 1 ) ) // 2

  return i, j

def i4_to_triangle_test ( ):

#*****************************************************************************80
#
## I4_TO_TRIANGLE_TEST tests I4_TO_TRIANGLE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    13 April 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'I4_TO_TRIANGLE_TEST'
  print '  I4_TO_TRIANGLE converts a linear index to a triangular one.'
  print ''
  print '     K  ==>  ( I  J )'
  print ''

  for k in range ( 1, 21 ):
 
    i, j = i4_to_triangle ( k )

    print '  %4d    %4d  %4d' % ( k, i, j )      
#
#  Terminate.
#
  print ''
  print 'I4_TO_TRIANGLE_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_to_triangle_test ( )
  timestamp ( )
