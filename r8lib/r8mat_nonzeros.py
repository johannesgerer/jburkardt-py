#!/usr/bin/env python

def r8mat_nonzeros ( m, n, a ):

#*****************************************************************************80
#
## R8MAT_NONZEROS returns the number of nonzeros in an R8MAT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns.
#
#    Input, real A(M,N), the matrix.
#
#    Output, integer VALUE, the number of nonzeros.
#
  value = 0

  for j in range ( 0, n ):
    for i in range ( 0, m ):
      if ( a[i,j] != 0.0 ):
        value = value + 1

  return value

def r8mat_nonzeros_test ( ):

#*****************************************************************************80
#
## R8MAT_NONZEROS_TEST tests R8MAT_NONZEROS.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 December 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from r8mat_print import r8mat_print

  m = 5
  n = 4
  a = np.zeros ( ( m, n ) )

  print ''
  print 'R8MAT_NONZEROS_TEST'
  print '  R8MAT_NONZEROS counts nonzeros in an R8MAT.'

  c1 = 0
  for i in range ( 0, m ):
    for j in range ( 0, n ):
      if ( ( i % 2 ) == 0 and ( j % 2 ) == 0 ):
        a[i,j] = 1.0
        c1 = c1 + 1
      else:
        a[i,j] = 0.0

  r8mat_print ( m, n, a, '  Matrix A:' )

  c2 = r8mat_nonzeros ( m, n, a )

  print ''
  print '  Expected nonzeros = %d' % ( c1 )
  print '  Computed nonzeros = %d' % ( c2 )

  print ''
  print 'R8MAT_NONZEROS_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8mat_nonzeros_test ( )
  timestamp ( )
