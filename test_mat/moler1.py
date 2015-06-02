#! /usr/bin/env python
#
def moler1 ( alpha, m, n ):

#*****************************************************************************80
#
## MOLER1 returns the MOLER1 matrix.
#
#  Formula:
#
#    If ( I = J )
#      A(I,J) = min ( I-1, J-1 ) * ALPHA^2 + 1
#    else
#      A(I,J) = min ( I-1, J-1 ) * ALPHA^2 + ALPHA
#
#  Example:
#
#    ALPHA = 2, N = 5
#
#    1 2  2  2  2
#    2 5  6  6  6
#    2 6  9 10 10
#    2 6 10 13 14
#    2 6 10 14 17
#
#  Properties:
#
#    Successive elements of each diagonal increase by an increment of ALPHA^2.
#
#    A is the product of B' * B, where B is the matrix returned by
#
#      B = TRIW ( ALPHA, N-1, N ).
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A is positive definite.
#
#    If ALPHA = -1, A(I,J) = min ( I, J ) - 2, A(I,I)=I.
#
#    A has one small eigenvalue.
#
#    If ALPHA is integral, then A is integral.
#    If A is integral, then det ( A ) is integral, and 
#    det ( A ) * inverse ( A ) is integral.
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
#  Reference:
#
#    John Nash,
#    Compact Numerical Methods for Computers: Linear Algebra and
#    Function Minimisation,
#    John Wiley, 1979,
#    pages 76 and 210.
#
#  Parameters:
#
#    Input, real ALPHA, the scalar that defines the Moler matrix.
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
        a[i,j] = min ( i, j ) * alpha * alpha + 1.0
      else:
        a[i,j] = min ( i, j ) * alpha * alpha + alpha

  return a

def moler1_determinant ( alpha, n ):

#*****************************************************************************80
#
## MOLER1_DETERMINANT returns the determinant of the MOLER1 matrix.
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
#    Input, real ALPHA, the scalar defining A.  
#
#    Input, integer N, the order of the matrix.
#
#    Output, real VALUE, the determinant.
#
  value = 1.0

  return value

def moler1_determinant_test ( ):

#*****************************************************************************80
#
## MOLER1_DETERMINANT_TEST tests MOLER1_DETERMINANT.
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
  from moler1 import moler1
  from r8mat_print import r8mat_print
  from r8_uniform_ab import r8_uniform_ab

  print ''
  print 'MOLER1_DETERMINANT_TEST'
  print '  MOLER1_DETERMINANT computes the determinant of the MOLER1 matrix.'
  print ''

  m = 4
  n = m

  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )

  a = moler1 ( alpha, n )
  r8mat_print ( m, n, a, '  MOLER1 matrix:' )

  value = moler1_determinant ( alpha, n )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'MOLER1_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def moler1_inverse ( alpha, n ):

#*****************************************************************************80
#
## MOLER1_INVERSE returns the inverse of the MOLER1 matrix.
#
#  Formula:
#
#    if ( I = J )
#      A(I,J) =              min ( N-I, N-J ) * ALPHA^2 + 1
#    else
#      A(I,J) = (-1)^(I+J) * min ( N-I, N-J ) * ALPHA^2 + ALPHA
#
#  Example:
#
#    ALPHA = 2, N = 5
#
#     17 -14  10 -6  2
#    -14  13 -10  6 -2
#     10 -10   9 -6  2
#     -6   6  -6  5 -2
#      2  -2   2 -2  1
#
#  Properties:
#
#    The matrix is symmetric.
#
#    Successive elements of each diagonal decrease by ALPHA**2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real ALPHA, the scalar that defines the inverse 
#    Moler matrix.
#
#    Input, integer N, the order of A.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  v = np.zeros ( n )

  v[0] = 1.0
  v[1] = - alpha
  for i in range ( 2, n ):
    v[i] = - ( alpha - 1.0 ) * v[i-1]

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      if ( i <= j ):
        t = 0.0
        for k in range ( 0, n - j ):
          t = t + v[j-i+k] * v[k]
        a[i,j] = t
      else:
        t = 0.0
        for k in range ( 0, n - i ):
          t = t + v[k] * v[i-j+k]
        a[i,j] = t

  return a

def moler1_llt ( alpha, n ):

#*****************************************************************************80
#
## MOLER1_LLT returns the Cholesky factor of the MOLER1 matrix.
#
#  Example:
#
#    ALPHA = 2, N = 5
#
#    1  0  0  0  0
#    2  1  0  0  0
#    2  2  1  0  0
#    2  2  2  1  0
#    2  2  2  2  1
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

  for j in range ( 0, n ):
    a[j,j] = 1.0
    for i in range ( j + 1, n ):
      a[i,j] = alpha
 
  return a

def moler1_plu ( alpha, n ):

#*****************************************************************************80
#
## MOLER1_PLU returns the PLU factors of the MOLER1 matrix.
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
#  Reference:
#
#    John Nash,
#    Compact Numerical Methods for Computers: Linear Algebra and
#    Function Minimisation,
#    Second Edition,
#    Taylor & Francis, 1990,
#    ISBN: 085274319X,
#    LC: QA184.N37.
#
#  Parameters:
#
#    Input, real ALPHA, the parameter.
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
    for i in range ( 0, n ):
      if ( i == j ):
        l[i,j] = 1.0
      elif ( j < i ):
        l[i,j] = alpha

  u = np.zeros ( ( n, n ) )
  for j in range ( 0, n ):
    for i in range ( 0, j ):
      u[i,j] = alpha
    u[j,j] = 1.0

  return p, l, u

def moler1_test ( ):

#*****************************************************************************80
#
## MOLER1_TEST tests MOLER1.
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
  from r8mat_print import r8mat_print
  from r8_uniform_ab import r8_uniform_ab

  print ''
  print 'MOLER1_TEST'
  print '  MOLER1 computes the MOLER1 matrix.'

  m = 5
  n = m

  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )

  a = moler1 ( alpha, m, n )
  r8mat_print ( m, n, a, '  MOLER1 matrix:' )

  print ''
  print 'MOLER1_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  moler1_test ( )
  timestamp ( )
