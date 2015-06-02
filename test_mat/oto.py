#! /usr/bin/env python
#
def oto ( m, n ):

#*****************************************************************************80
#
## OTO returns the OTO matrix.
#
#  Example:
#
#    N = 5
#
#    2  1  .  .  .
#    1  2  1  .  .
#    .  1  2  1  .
#    .  .  1  2  1
#    .  .  .  1  2
#
#  Properties:
#
#    A is banded, with bandwidth 3.
#
#    A is tridiagonal.
#
#    Because A is tridiagonal, it has property A (bipartite).
#
#    A is integral: int ( A ) = A.
#
#    A is Toeplitz: constant along diagonals.
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A is persymmetric: A(I,J) = A(N+1-J,N+1-I).
#
#    A is weakly diagonally dominant, but not strictly diagonally dominant.
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 December 2014
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
      if ( j == i - 1 ):
        a[i,j] = 1.0
      elif ( j == i ):
        a[i,j] = 2.0
      elif ( j == i + 1 ):
        a[i,j] = 1.0
      else:
        a[i,j] = 0.0

  return a

def oto_condition ( n ):

#*****************************************************************************80
#
## OTO_CONDITION returns the L1 condition of the OTO matrix.
#
#  Discussion:
#
#    I knew it had to be possible to work out this condition number!
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Output, real VALUE, the L1 condition.
#
  if ( n == 1 ):
    a_norm = 2.0
  elif ( n == 2 ):
    a_norm = 3.0
  else:
    a_norm = 4.0

  n1 = ( n + 1 ) // 2
  n2 = ( n + 2 ) // 2

  s = 0
  i1 = n1
  i2 = 0

  while ( i2 < n2 ):
    i2 = i2 + 1
    s = s + i1 * i2

  while ( 1 < i1 ):
    i1 = i1 - 1
    s = s + i1 * i2

  b_norm = ( float ) ( s ) / ( float ) ( n + 1 )

  value = a_norm * b_norm

  return value

def oto_determinant ( n ):

#*****************************************************************************80
#
## OTO_DETERMINANT computes the determinant of the OTO matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 December 2014
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
  value = n + 1

  return value

def oto_determinant_test ( ):

#*****************************************************************************80
#
## OTO_DETERMINANT_TEST tests OTO_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 December 2014
#
#  Author:
#
#    John Burkardt
#
  from oto import oto
  from r8mat_print import r8mat_print

  print ''
  print 'OTO_DETERMINANT_TEST'
  print '  OTO_DETERMINANT computes the OTO determinant.'

  seed = 123456789

  m = 5
  n = 5
  a = oto ( m, n )
  r8mat_print ( n, n, a, '  OTO matrix:' )

  value = oto_determinant ( n )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'OTO_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def oto_eigen_right ( n ):

#*****************************************************************************80
#
## OTO_EIGEN_RIGHT returns the right eigenvectors of the OTO matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of A.
#
#    Output, real A(N,N), the right eigenvector matrix.
#
  import numpy as np
  from r8_mop import r8_mop

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      angle = float ( ( i + 1 ) * ( j + 1 ) ) * np.pi / float ( n + 1 )
      a[i,j] = r8_mop ( i + j ) * np.sqrt ( 2.0 / float ( n + 1 ) ) * np.sin ( angle )

  return a

def oto_eigenvalues ( n ):

#*****************************************************************************80
#
## OTO_EIGENVALUES returns the eigenvalues of the OTO matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Output, real LAM(N), the eigenvalues.
#
  import numpy as np

  lam = np.zeros ( n )

  for i in range ( 0, n ):
    angle = float ( i + 1 ) * np.pi / float ( 2 * ( n + 1 ) )
    lam[i] = 4.0 * ( np.sin ( angle ) ) ** 2

  return lam

def oto_inverse ( n ):

#*****************************************************************************80
#
## OTO_INVERSE returns the inverse of the OTO matrix.
#
#  Formula:
#
#    if ( I <= J )
#      A(I,J) = (-1)^(I+J) * I * (N-J+1) / (N+1)
#    else
#      A(I,J) = (-1)^(I+J) * J * (N-I+1) / (N+1)
#
#  Example:
#
#    N = 4
#
#             4 -3  2 -1
#    (1/5) * -3  6 -4  2
#             2 -4  6 -3
#            -1  2 -3  4
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 March 2015
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
  from r8_mop import r8_mop

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      if ( i <= j ):
        a[i,j] = r8_mop ( i + j ) * float ( ( i + 1 ) * ( n - j ) ) / float ( n + 1 )
      else:
        a[i,j] = r8_mop ( i + j ) * float ( ( j + 1 ) * ( n - i ) ) / float ( n + 1 )


  return a

def oto_llt ( n ):

#*****************************************************************************80
#
## OTO_LLT returns the Cholesky factor of the OTO matrix.
#
#  Example:
#
#    N = 5
#
#   1.4142         0         0         0         0
#   0.7071    1.2247         0         0         0
#        0    0.8165    1.1547         0         0
#        0         0    0.8660    1.1180         0
#        0         0         0    0.8944    1.0954
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np
  
  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    a[i,i] = np.sqrt ( float ( i + 2 ) / float ( i + 1 ) )

  for i in range ( 1, n ):
    a[i,i-1] = np.sqrt ( float ( i ) / float ( i + 1 ) )

  return a

def oto_plu ( n ):

#*****************************************************************************80
#
## OTO_PLU returns the PLU factors of the OTO matrix.
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
#    Output, real P(N,N), L(N,N), U(N,N), the PLU factors.
#
  import numpy as np

  p = np.zeros ( ( n, n ) )
  for j in range ( 0, n ):
    p[j,j] = 1.0

  l = np.zeros ( ( n, n ) )
  for j in range ( 0, n ):
    l[j,j] = 1.0
  for j in range ( 0, n - 1 ):
    l[j+1,j] = float ( j + 1 ) / float ( j + 2 )

  u = np.zeros ( ( n, n ) )
  for j in range ( 0, n ):
    u[j,j] = float ( j + 2 ) / float ( j + 1 )
  for j in range ( 1, n ):
    u[j-1,j] = 1.0

  return p, l, u

def oto_test ( ):

#*****************************************************************************80
#
## OTO_TEST tests OTO.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 December 2014
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'OTO_TEST'
  print '  OTO computes the OTO matrix.'

  m = 5
  n = m
  a = oto ( m, n )
  r8mat_print ( m, n, a, '  OTO matrix:' )

  print ''
  print 'OTO_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  oto_test ( )
  oto_determinant_test ( )
  timestamp ( )
