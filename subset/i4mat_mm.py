#! /usr/bin/env python
#
def i4mat_mm ( n1, n2, n3, a, b ):

#*****************************************************************************80
#
## I4MAT_MM computes the product of two I4MAT's.
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
#  Parameters:
#
#    Input, integer N1, N2, N3, matrix dimensions.
#
#    Input, integer A(N1,N2), factor 1.
#
#    Output, integer B(N2,N3), factor 2.
#
#    Output, integer C(N1,N3), the product.
#
  import numpy as np

  c = np.zeros ( [ n1, n3 ], dtype = np.int32 )

  for k in range ( 0, n3 ):
    for i in range ( 0, n1 ):
      for j in range ( 0, n2 ):
        c[i,k] = c[i,k] + a[i,j] * b[j,k]

  return c

def i4mat_mm_test ( ):

#*****************************************************************************80
#
## I4MAT_MM_TEST tests I4MAT_MM.
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
  from i4mat_print import i4mat_print

  n1 = 3
  n2 = 2
  n3 = 4
#
#  Each row of this definition is a COLUMN of the matrix.
#
  a = np.array ( [
   [  11,  12 ], \
   [  21,  22 ], \
   [  31,  32 ] ] )

  b = np.array ( [
   [  11,  12, 13, 14 ], \
   [  21,  22, 23, 24 ] ] )

  print ''
  print 'I4MAT_MM_TEST'
  print '  I4MAT_MM multiplies two I4MAT\'s'

  i4mat_print ( n1, n2, a, '  Matrix A:' )
  i4mat_print ( n2, n3, b, '  Matrix B:' )

  c = i4mat_mm ( n1, n2, n3, a, b )
 
  i4mat_print ( n1, n3, c, '  C = A*B:' )
#
#  Terminate.
#
  print ''
  print 'I4MAT_MM_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4mat_mm_test ( )
  timestamp ( )

