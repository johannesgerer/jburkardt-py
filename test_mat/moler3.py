#! /usr/bin/env python
#
def moler3 ( m, n ):

#*****************************************************************************80
#
## MOLER3 returns the MOLER3 matrix.
#
#  Formula:
#
#    if ( I == J )
#      A(I,J) = I
#    else
#      A(I,J) = min(I,J) - 2
#
#  Example:
#
#    N = 5
#
#     1 -1 -1 -1 -1
#    -1  2  0  0  0
#    -1  0  3  1  1
#    -1  0  1  4  2
#    -1  0  1  2  5
#
#  Properties:
#
#    A is integral, therefore det ( A ) is integral, and 
#    det ( A ) * inverse ( A ) is integral.
#
#    A is positive definite.
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A has a simple Cholesky factorization.
#
#    A has one small eigenvalue.
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns of A.
#
#    Output, real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( m, n ) )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      if ( i == j ):
        a[i,j] = i + 1
      else:
        a[i,j] = min ( i, j ) - 1

  return a

def moler3_determinant ( n ):

#*****************************************************************************80
#
## MOLER3_DETERMINANT returns the determinant of the MOLER3 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Output, real VALUE, the determinant.
#
  value = 1.0

  return value

def moler3_determinant_test ( ):

#*****************************************************************************80
#
## MOLER3_DETERMINANT_TEST tests MOLER3_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 February 2015
#
#  Author:
#
#    John Burkardt
#
  from moler3 import moler3
  from r8mat_print import r8mat_print
 
  print ''
  print 'MOLER3_DETERMINANT_TEST'
  print '  MOLER3_DETERMINANT computes the determinant of the MOLER3 matrix.'
  print ''

  m = 5
  n = m

  a = moler3 ( m, n )
  r8mat_print ( m, n, a, '  MOLER3 matrix:' )

  value = moler3_determinant ( n )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'MOLER3_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def moler3_inverse ( n ):

#*****************************************************************************80
#
## MOLER3_INVERSE returns the inverse of the MOLER3 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of A.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np
  from r8mat_mtm import r8mat_mtm

  l = np.zeros ( ( n, n ) )

  for j in range ( 0, n ):
    l[j,j] = 1.0
    value = 1.0
    for i in range ( j + 1, n ):
      l[i,j] = value
      value = value * 2.0

  a = r8mat_mtm ( n, n, n, l, l )

  return a

def moler3_llt ( n ):

#*****************************************************************************80
#
## MOLER3_LLT returns the Cholesky factor of the MOLER3 matrix.
#
#  Example:
#
#    N = 5
#
#    1  0  0  0  0
#   -1  1  0  0  0
#   -1 -1  1  0  0
#   -1 -1 -1  1  0
#   -1 -1 -1 -1  1
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of A.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, i ):
      a[i,j] = -1.0
    a[i,i] =  1.0
 
  return a

def moler3_plu ( n ):

#*****************************************************************************80
#
## MOLER3_PLU returns the PLU factors of the MOLER3 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Output, real P(N,N), L(N,N), U(N,N) the PLU factors.
#
  import numpy as np

  p = np.zeros ( ( n, n ) )

  for j in range ( 0, n ):
    p[j,j] = 1.0

  l = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, i ):
      l[i,j] = -1.0
    l[i,i] =  1.0

  u = np.zeros ( ( n, n ) )

  for j in range ( 0, n ):
    for i in range ( 0, j ):
      u[i,j] = -1.0
    u[j,j] =  1.0

  return p, l, u

def moler3_test ( ):

#*****************************************************************************80
#
## MOLER3_TEST tests MOLER3.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 January 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'MOLER3_TEST'
  print '  MOLER3 computes the MOLER3 matrix.'

  m = 5
  n = m

  a = moler3 ( m, n )
  r8mat_print ( m, n, a, '  MOLER3 matrix:' )

  print ''
  print 'MOLER3_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  moler3_test ( )
  timestamp ( )
