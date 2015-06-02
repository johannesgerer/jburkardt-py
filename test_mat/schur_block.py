#! /usr/bin/env python
#
def schur_block ( n, x, y ):

#*****************************************************************************80
#
## SCHUR_BLOCK returns the SCHUR_BLOCK matrix.
#
#  Formula:
#
#    if ( i == j )
#      a(i,j) = x( (i+1)/2 )
#    else ( mod ( i, 2 ) == 1 & j == i + 1 )
#      a(i,j) = y( (i+1)/2 )
#    else ( mod ( i, 2 ) == 0 & j == i - 1 )
#      a(i,j) = -y( (i+1)/2 )
#    else
#      a(i,j) = 0.0
#
#  Example:
#
#    N = 5, X = ( 1, 2, 3 ), Y = ( 4, 5 )
#
#    1  4    0    0    0
#   -4  1    0    0    0
#    0  0    2    5    0
#    0  0   -5    2    0
#    0  0    0    0    3
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is block diagonal, with the blocks being 2 by 2 or 1 by 1 in size.
#
#    A is in real Schur form.
#
#    The eigenvalues of A are X(I) +/- sqrt ( - 1 ) * Y(I)
#
#    A is tridiagonal.
#
#    A is banded, with bandwidth 3.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Francoise Chatelin,
#    Section 4.2.7,
#    Eigenvalues of Matrices,
#    John Wiley, 1993.
#
#    Francoise Chatelin, Valerie Fraysse,
#    Qualitative computing: Elements of a theory for finite precision
#    computation, Lecture notes,
#    CERFACS, Toulouse, France and THOMSON-CSF, Orsay, France, June 1993.
#
#  Parameters:
#
#    Input, integer N, the order of A.
#
#    Input, real X( (N+1)/2 ), specifies the diagonal elements
#    of A.
#
#    Input, real Y( N/2 ), specifies the off-diagonal elements 
#    of the Schur blocks.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    ih = ( i // 2 )
    for j in range ( 0, n ):

      if ( i == j ):
        a[i,j] = x[ih]
      elif ( ( i % 2 ) == 0 and j == i + 1 ):
        a[i,j] = y[ih]
      elif ( ( i % 2 ) == 1 and j == i - 1 ):
        a[i,j] = - y[ih]

  return a

def schur_block_determinant ( n, x, y ):

#*****************************************************************************80
#
## SCHUR_BLOCK_DETERMINANT returns the determinant of the SCHUR_BLOCK matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of A.
#
#    Input, real X( (N+1)/2 ), specifies the diagonal 
#    elements of A.
#
#    Input, real Y( N/2 ), specifies the off-diagonal 
#    elements of the Schur blocks.
#
#    Output, real VALUE, the determinant of A.
#
  value = 1.0;

  ihi = ( n // 2 )
  for i in range ( 0, ihi ):
    value = value * ( x[i] ** 2 + y[i] ** 2 )

  if ( ( n % 2 ) == 1 ):
    value = value * x[ihi]

  return value

def schur_block_inverse ( n, x, y ):

#*****************************************************************************80
#
## SCHUR_BLOCK_INVERSE returns the inverse of the SCHUR_BLOCK matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of A.
#
#    Input, real X( (N+1)/2 ), specifies the diagonal elements
#    of A.
#
#    Input, real Y( N/2 ), specifies the off-diagonal elements 
#    of the Schur blocks.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      k = ( i // 2 )

      if ( i == j ):

        if ( i == n - 1 and ( n % 2 ) == 1 ):
          a[i,j] = 1.0 / x[k]
        else:
          a[i,j] = x[k] / ( x[k] ** 2 + y[k] ** 2 )

      elif ( ( i % 2 ) == 0 and j == i + 1 ):

        a[i,j] = - y[k] / ( x[k] ** 2 + y[k] ** 2 )

      elif ( ( i % 2 ) == 1 and j == i - 1 ):

        a[i,j] =   y[k] / ( x[k] ** 2 + y[k] ** 2 )

  return a

def schur_block_test ( ):

#*****************************************************************************80
#
## SCHUR_BLOCK_TEST tests SCHUR_BLOCK.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 March 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print
  from r8vec_uniform_ab import r8vec_uniform_ab

  print ''
  print 'SCHUR_BLOCK_TEST'
  print '  SCHUR_BLOCK computes the SCHUR_BLOCK matrix.'

  m = 5
  n = m
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  x_n = ( ( n + 1 ) // 2 )
  x, seed = r8vec_uniform_ab ( x_n, r8_lo, r8_hi, seed )
  y_n = ( n // 2 )
  y, seed = r8vec_uniform_ab ( y_n, r8_lo, r8_hi, seed )
  a = schur_block ( n, x, y )

  r8mat_print ( n, n, a, '  SCHUR_BLOCK matrix:' )

  print ''
  print 'SCHUR_BLOCK_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  schur_block_test ( )
  timestamp ( )
