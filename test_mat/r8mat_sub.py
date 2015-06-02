#!/usr/bin/env python

def r8mat_sub ( m, n, a, b ):

#*****************************************************************************80
#
## R8MAT_SUB computes the difference of two matrices.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the order of the matrices.
#
#    Input, real A(M,N), B(M,N), the matrices.
#
#    Output, real C(M,N), the difference C = A - B.
#
  import numpy as np

  c = np.zeros ( ( m, n ) )

  for j in range ( 0, n ):
    for i in range ( 0, m):
      c[i,j] = a[i,j] - b[i,j]

  return c

def r8mat_sub_test ( ):

#*****************************************************************************80
#
## R8MAT_SUB_TEST tests R8MAT_SUB.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 March 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from r8mat_indicator import r8mat_indicator
  from r8mat_print import r8mat_print
  from r8mat_transpose import r8mat_transpose

  m = 4
  n = 4

  print ''
  print 'R8MAT_SUB_TEST'
  print '  R8MAT_SUB computes C = A - B;'

  a = r8mat_indicator ( m, n )

  b = r8mat_transpose ( m, n, a )

  c = r8mat_sub ( m, n, a, b )

  r8mat_print ( m, n, a, '  A:' )
  r8mat_print ( m, n, b, '  B:' )
  r8mat_print ( m, n, c, '  C = A - B:' )

  print ''
  print 'R8MAT_SUB_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8mat_sub_test ( )
  timestamp ( )
