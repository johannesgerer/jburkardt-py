#!/usr/bin/env python

def r8mat_mtm ( n1, n2, n3, a, b ):

#*****************************************************************************80
#
## R8MAT_MTM computes A' * B for two R8MAT's.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N1, N2, N3, the order of the matrices.
#
#    Input, real A(N2,N1), B(N2,N3), the matrices to multiply.
#
#    Output, real  C(N1,N3), the product matrix C = A' * B.
#
  import numpy as np

  c = np.zeros ( ( n1, n3 ) )

  for j in range ( 0, n3 ):
    for i in range ( 0, n1 ):
      for k in range ( 0, n2 ):
        c[i,j] = c[i,j] + a[k,i] * b[k,j]

  return c

def r8mat_mtm_test ( ):

#*****************************************************************************80
#
## R8MAT_MTM_TEST tests R8MAT_MTM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 March 2015
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
  print 'R8MAT_MTM_TEST'
  print '  R8MAT_MTM computes a matrix-matrix product C = A\' * B;'

  a = np.zeros ( ( n2, n1 ) )

  for i in range ( 0, n2 ): 
    for j in range ( 0, n1 ):
 
      if ( j == 0 ):
        a[i,j] = 1.0
      elif ( i == 0 ):
        a[i,j] = 0.0
      else:
        a[i,j] = a[i-1,j-1] + a[i-1,j]

  b = a

  c = r8mat_mtm ( n1, n2, n3, a, b )

  r8mat_print ( n2, n1, a, '  A:' )
  r8mat_print ( n2, n3, b, '  B:' )
  r8mat_print ( n1, n3, c, '  C = A\'*B:' )

  print ''
  print 'R8MAT_MTM_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8mat_mtm_test ( )
  timestamp ( )
