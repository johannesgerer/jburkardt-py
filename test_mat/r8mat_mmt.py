#!/usr/bin/env python

def r8mat_mmt ( n1, n2, n3, a, b ):

#*****************************************************************************80
#
## R8MAT_MMT multiplies an R8MAT times a transposed R8MAT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N1, N2, N3, the order of the matrices.
#
#    Input, real A(N1,N2), B(N3,N2), the matrices to multiply.
#
#    Output, real  C(N1,N3), the product matrix C = A * B'.
#
  import numpy as np

  c = np.zeros ( ( n1, n3 ) )

  for j in range ( 0, n3 ):
    for i in range ( 0, n1 ):
      for k in range ( 0, n2 ):
        c[i,j] = c[i,j] + a[i,k] * b[j,k]

  return c

def r8mat_mmt_test ( ):

#*****************************************************************************80
#
## R8MAT_MMT_TEST tests R8MAT_MMT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from r8mat_print import r8mat_print

  n1 = 4
  n2 = 3
  n3 = n1

  print ''
  print 'R8MAT_MMT_TEST'
  print '  R8MAT_MMT computes a matrix-matrix product C = A * B\';'

  a = np.zeros ( ( n1, n2 ) )

  for i in range ( 0, n1 ): 
    for j in range ( 0, n2 ):
 
      if ( j == 0 ):
        a[i,j] = 1.0
      elif ( i == 0 ):
        a[i,j] = 0.0
      else:
        a[i,j] = a[i-1,j-1] + a[i-1,j]

  b = np.copy ( a )

  c = r8mat_mmt ( n1, n2, n3, a, b )

  r8mat_print ( n1, n2, a, '  A:' )
  r8mat_print ( n3, n2, b, '  B:' )
  r8mat_print ( n1, n3, c, '  C = A*B\':' )

  print ''
  print 'R8MAT_MMT_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8mat_mmt_test ( )
  timestamp ( )
