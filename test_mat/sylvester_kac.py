#! /usr/bin/env python
#
def sylvester_kac ( n ):

#*****************************************************************************80
#
## SYLVESTER_KAC returns the SYLVESTER_KAC matrix.
#
#  Formula:
#
#    If J = I - 1
#      A(I,J) = N + 1 - I
#    If J = I + 1
#      A(I,J) = I
#
#  Example:
#
#    N = 5,
#
#    0 1 0 0 0
#    4 0 2 0 0
#    0 3 0 3 0
#    0 0 2 0 4
#    0 0 0 1 0
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is tridiagonal.
#
#    If N is odd, the eigenvalues are:
#      -(N-1), -(N-3), ..., -2, 0, 2, ... (N-3), (N-1).
#
#    If N is even, the eigenvalues are:
#      -(N-1), -(N-3), ..., -1, +1, ..., (N-3), (N-1).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Paul Clement,
#    A class of triple-diagonal matrices for test purposes,
#    SIAM Review,
#    Volume 1, 1959, pages 50-52.
#
#  Parameters:
#
#    Input, integer N, the number of rows and columns of A.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n - 1 ):
    a[i,i+1] = float (     i + 1 )
    a[i+1,i] = float ( n - i - 1 )

  return a

def sylvester_kac_determinant ( n ):

#*****************************************************************************80
#
## SYLVESTER_KAC_DETERMINANT computes the determinant of the SYLVESTER_KAC matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 April 2015
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
  if ( ( n % 2 ) == 1 ):
    value = 0.0
  else:
    value = 1.0
    for i in range ( - n + 1, n + 1, 2 ):
      value = value * float ( i )

  return value

def sylvester_kac_eigen_right ( n ):

#*****************************************************************************80
#
## SYLVESTER_KAC_EIGEN_RIGHT: right eigenvectors of the SYLVESTER_KAC matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Output, real V(N,N), the right eigenvectors.
#
  import numpy as np
  from r8_mop import r8_mop

  b = np.zeros ( n - 1 )
  for i in range ( 0, n - 1 ):
    b[i] = float ( i + 1 )

  c = np.zeros ( n - 1 )
  for i in range ( 0, n - 1 ):
    c[i] = float ( n - 1 - i )

  v = np.zeros ( ( n, n ) )

  for j in range ( 0, n ):

    lam = - n + 1 + 2 * j

    a = np.zeros ( n )
    a[0] = 1.0
    a[1] = - lam
    for i in range ( 2, n ):
      a[i] = - lam * a[i-1] - b[i-2] * c[i-2] * a[i-2]

    bot = 1.0
    v[0,j] = 1.0
    for i in range ( 1, n ):
      bot = bot * b[i-1]
      v[i,j] = r8_mop ( i ) * a[i] / bot

  return v

def sylvester_kac_eigenvalues ( n ):

#*****************************************************************************80
#
## SYLVESTER_KAC_EIGENVALUES returns the eigenvalues of the SYLVESTER_KAC matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 April 2015
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

  i = 0
  for i in range ( 0, n ):
    lam[i] = float ( - n + 1 + 2 * i )

  return lam

def sylvester_kac_inverse ( n ):

#*****************************************************************************80
#
## SYLVESTER_KAC_INVERSE returns the inverse of the SYLVESTER_KAC matrix.
#
#  Example:
#
#    N = 6:
#
#      0     1/5    0  -2/15  0   8/15
#      1      0     0    0    0    0
#      0      0     0   1/3   0  -4/3
#    -4/3     0    1/3   0    0    0
#      0      0     0    0    0    1
#     8/15    0   -2/15  0   1/5   0
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 April 2015
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
  from sys import exit

  if ( ( n % 2 ) == 1 ):
    print ''
    print 'SYLVESTER_KAC_INVERSE - Fatal error!'
    print '  The matrix is singular for odd N.'
    exit ( 'SYLVESTER_KAC - Fatal error!' )

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):

    if ( ( i % 2 ) == 0 ):

      for j in range ( i, n - 1, 2 ):

        if ( j == i ):
          prod1 = 1.0 / float ( n - 1 - j )
          prod2 = 1.0 / float (     1 + j )
        else:
          prod1 = - prod1 * float (     j ) / float ( n - 1 - j )
          prod2 = - prod2 * float ( n - j ) / float (     1 + j )

        a[i,j+1] = prod1
        a[j+1,i] = prod2

  return a

def sylvester_kac_test ( ):

#*****************************************************************************80
#
## SYLVESTER_KAC_TEST tests SYLVESTER_KAC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 April 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'SYLVESTER_KAC_TEST'
  print '  SYLVESTER_KAC computes the SYLVESTER_KAC matrix.'

  m = 5
  n = m
  a = sylvester_kac ( n )
  r8mat_print ( m, n, a, '  SYLVESTER_KAC matrix:' )

  print ''
  print 'SYLVESTER_KAC_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  sylvester_kac_test ( )
  timestamp ( )
