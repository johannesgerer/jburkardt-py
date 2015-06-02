#! /usr/bin/env python
#
def i4mat_u1_inverse ( n, a ):

#*****************************************************************************80
#
## I4MAT_U1_INVERSE inverts a unit upper triangular I4MAT.
#
#  Discussion:
#
#    A unit upper triangular matrix is a matrix with only 1's on the main
#    diagonal, and only 0's below the main diagonal.
#
#    The inverse of an integer unit upper triangular matrix is also
#    an integer unit upper triangular matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Albert Nijenhuis, Herbert Wilf,
#    Combinatorial Algorithms,
#    Academic Press, 1978, second edition,
#    ISBN 0-12-519260-6.
#
#  Parameters:
#
#    Input, integer N, number of rows and columns in the matrix.
#
#    Input, integer A(N,N), the unit upper triangular matrix.
#
#    Output, integer B(N,N), the inverse matrix.
#
  import numpy as np

  b = np.zeros ( [ n, n ], dtype = np.int32 )

  for j in range ( n - 1, -1, -1 ):

    b[j,j] = 1

    for i in range ( j - 1, -1, -1 ):
      for k in range ( i + 1, j + 1 ):
        b[i,j] = b[i,j] - a[i,k] * b[k,j]

  return b

def i4mat_u1_inverse_test ( ):

#*****************************************************************************80
#
## I4MAT_U1_INVERSE_TEST tests I4MAT_U1_INVERSE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from i4mat_mm import i4mat_mm
  from i4mat_print import i4mat_print

  n = 6
#
#  Each row of this definition is a COLUMN of the matrix.
#
  a = np.array ( [
   [  1,  2,  0,  5,  0, 75 ], \
   [  0,  1,  0,  0,  0,  0 ], \
   [  0,  0,  1,  3,  0,  0 ], \
   [  0,  0,  0,  1,  0,  6 ], \
   [  0,  0,  0,  0,  1,  4 ], \
   [  0,  0,  0,  0,  0,  1 ] ] )

  print ''
  print 'I4MAT_U1_INVERSE_TEST'
  print '  I4MAT_U1_INVERSE inverts a unit upper triangular matrix.'

  i4mat_print ( n, n, a, '  The original matrix:' )
 
  b = i4mat_u1_inverse ( n, a )
 
  i4mat_print ( n, n, b, '  The inverse matrix:' )

  c = i4mat_mm ( n, n, n, a, b )

  i4mat_print ( n, n, c, '  The product:' )
#
#  Terminate.
#
  print ''
  print 'I4MAT_U1_INVERSE_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4mat_u1_inverse_test ( )
  timestamp ( )

