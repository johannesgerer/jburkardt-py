#!/usr/bin/env python

def r8mat_nint ( m, n, a ):

#*****************************************************************************80
#
## R8MAT_NINT rounds the entries of an R8MAT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns of A.
#
#    Input, real A(M,N), the matrix to be rounded.
#
#    Output, real A(M,N), the rounded matrix.
#
  for j in range ( 0, n ):
    for i in range ( 0, m ):
      a[i,j] = round ( a[i,j] )

  return a

def r8mat_nint_test ( ):

#*****************************************************************************80
#
## R8MAT_NINT_TEST tests R8MAT_NINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 December 2014
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print
  from r8mat_uniform_ab import r8mat_uniform_ab

  m = 5
  n = 4

  print ''
  print 'R8MAT_NINT_TEST'
  print '  R8MAT_NINT rounds an R8MAT.'

  x1 = -5.0
  x2 = +5.0
  seed = 123456789
  a, seed = r8mat_uniform_ab ( m, n, x1, x2, seed )
  r8mat_print ( m, n, a, '  Matrix A:' )
  a = r8mat_nint ( m, n, a )
  r8mat_print ( m, n, a, '  Rounded matrix A:' )

  print ''
  print 'R8MAT_NINT_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8mat_nint_test ( )
  timestamp ( )
