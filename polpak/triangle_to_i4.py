#!/usr/bin/env python

def triangle_to_i4 ( i, j ):

#*****************************************************************************80
#
## TRIANGLE_TO_I4 converts a triangular coordinate to an integer.
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
#    Thus, our goal is, given the row I and column J of the data,
#    to produce the value K which indicates its position in the linear
#    array.
#
#    The triangular numbers are the indices associated with the
#    diagonal elements of the original array, T(1,1), T(2,2), T(3,3)
#    and so on.
#
#  Formula:
#
#    K = J + ( (I-1) * I ) / 2
#
#  First Values:
#
#     I  J  K
#
#     0  0  0
#     1  1  1
#     2  1  2
#     2  2  3
#     3  1  4
#     3  2  5
#     3  3  6
#     4  1  7
#     4  2  8
#     4  3  9
#     4  4 10
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer I, J, the row and column indices.  I and J must
#    be nonnegative, and J must not be greater than I.
#
#    Output, integer VALUE, the linear index of the (I,J) element.
#
  from sys import exit

  if ( i < 0 ):
    print ''
    print 'TRIANGLE_TO_I4 - Fatal error!'
    print '  I < 0.'
    print '  I = %d' % ( i )
    exit ( 'TRIANGLE_TO_I4 - Fatal error!' )

  if ( j < 0 ):
    print ''
    print 'TRIANGLE_TO_I4 - Fatal error!'
    print '  J < 0.'
    print '  J = %d' % ( j )
    exit ( 'TRIANGLE_TO_I4 - Fatal error!' )

  if ( i < j ):
    print ''
    print 'TRIANGLE_TO_I4 - Fatal error!'
    print '  I < J.'
    print '  I = %d' % ( i )
    print '  J = %d' % ( j )
    exit ( 'TRIANGLE_TO_I4 - Fatal error!' )

  value = j + ( ( i - 1 ) * i ) / 2

  return value

def triangle_to_i4_test ( ):

#*****************************************************************************80
#
## TRIANGLE_TO_I4_TEST tests TRIANGLE_TO_I4.
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
  from i4_to_triangle import i4_to_triangle

  print ''
  print 'TRIANGLE_TO_I4_TEST'
  print '  TRIANGLE_TO_I4 converts a triangular index to a linear one.'
  print ''
  print '   ( I,    J ) ==> K'
  print ''

  for i in range ( 1, 5 ):
    for j in range ( 1, i + 1 ):
      k = triangle_to_i4 ( i,j )  
      print '  %4d  %4d    %4d' % ( i, j, k )

  print ''
  print 'TRIANGLE_TO_I4_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  triangle_to_i4_test ( )
  timestamp ( )
