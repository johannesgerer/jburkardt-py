#!/usr/bin/env python

def asm_triangle ( n ):

#*****************************************************************************80
#
## ASM_TRIANGLE returns a row of the alternating sign matrix triangle.
#
#  Discussion:
#
#    The first seven rows of the triangle are as follows:
#
#          1      2      3      4      5      6     7
#
#    0     1
#    1     1      1
#    2     2      3      2
#    3     7     14     14      7
#    4    42    105    135    105     42
#    5   429   1287   2002   2002   1287    429
#    6  7436  26026  47320  56784  47320  26026  7436
#
#    For a given N, the value of A(J) represents entry A(I,J) of
#    the triangular matrix, and gives the number of alternating sign matrices
#    of order N in which the (unique) 1 in row 1 occurs in column J.
#
#    Thus, of alternating sign matrices of order 3, there are
#    2 with a leading 1 in column 1:
#
#      1 0 0  1 0 0
#      0 1 0  0 0 1
#      0 0 1  0 1 0
#
#    3 with a leading 1 in column 2, and
#
#      0 1 0  0 1 0  0 1 0
#      1 0 0  0 0 1  1-1 1
#      0 0 1  1 0 0  0 1 0
#
#    2 with a leading 1 in column 3:
#
#      0 0 1  0 0 1
#      1 0 0  0 1 0
#      0 1 0  1 0 0
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 June 2004
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the desired row.
#
#    Output, integer A(N+1), the entries of the row.
#
  import numpy as np
  from i4vec_sum import i4vec_sum

  a = np.zeros ( n + 1 );
  b = np.zeros ( n + 1 );
  c = np.zeros ( n + 1 );
#
#  Row 1
#
  a[0] = 1;

  if ( n + 1 == 1 ):
    return a
#
#  Row 2
#
  nn = 2
  b[0] = 2
  c[0] = nn

  a[0] = i4vec_sum ( nn - 1, a )
  for i in range ( 1, nn ):
    a[i] = a[i-1] * c[i-1] / b[i-1]

  if ( n + 1 == 2 ):
    return a
#
#  Row 3 and on.
#
  for nn in range ( 3, n + 2 ):

    b[nn-2] = nn
    for i in range ( nn - 3, 0, -1 ):
      b[i] = b[i] + b[i-1]
    b[0] = 2

    c[nn-2] = 2
    for i in range ( nn - 3, 0, -1 ):
      c[i] = c[i] + c[i-1]
    c[0] = nn

    a[0] = i4vec_sum ( nn - 1, a )
    for i in range ( 1, nn ):
      a[i] = a[i-1] * c[i-1] / b[i-1]

  return a

def asm_triangle_test ( ):

#*****************************************************************************80
#
## ASM_TRIANGLE_TEST tests ASM_TRIANGLE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 April 2009
#
#  Author:
#
#    John Burkardt
#
  max_n = 7

  print ''
  print 'ASM_TRIANGLE_TEST'
  print '  ASM_TRIANGLE returns a row of the alternating sign'
  print '  matrix triangle.'
  print ''

  for n  in range ( 0, max_n + 1 ):
    a = asm_triangle ( n )
    print '  %2d' % ( n ),
    for i in range ( 0, n + 1 ):
      print '  %8d' % ( a[i] ),
    print ''
#
#  Terminate.
#
  print ''
  print 'ASM_TRIANGLE_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp

  timestamp ( )
  asm_triangle_test ( )
  timestamp ( )
