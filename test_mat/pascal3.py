#! /usr/bin/env python
#
def pascal3 ( n, alpha ):

#*****************************************************************************80
#
## PASCAL3 returns the PASCAL3 matrix.
#
#  Formula:
#
#    if ( J = 1 )
#      A(I,J) = 1
#    elseif ( I = 0 )
#      A(1,J) = 0
#    else
#      A(I,J) =  ALPHA * A(I-1,J) + A(I-1,J-1) )
#
#  Example:
#
#    N = 5, ALPHA = 2
#
#     1   0   0   0   0
#     2   1   0   0   0
#     4   4   1   0   0
#     8  12   6   1   0
#    16  32  24   8   1
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A[0] is the identity matrix.
#
#    A[1] is the usual (lower triangular) Pascal matrix.
#
#    A is nonsingular.
#
#    A is lower triangular.
#
#    If ALPHA is integral, then A is integral.
#    If A is integral, then det ( A ) is integral, and 
#    det ( A ) * inverse ( A ) is integral.
#
#    det ( A ) = 1.
#
#    A is unimodular.
#
#    LAMBDA(1:N) = 1.
#
#    (0, 0, ..., 0, 1) is an eigenvector.
#
#    The inverse of A[ALPHA] is A[-ALPHA].
#
#    A[ALPHA] * A[BETA] = A[ALPHA*BETA].
#
#    A[1/2] is the "square root" of A[1], and so on.
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Gregory Call, Daniel Velleman,
#    Pascal's Matrices,
#    American Mathematical Monthly,
#    Volume 100, Number 4, April 1993, pages 372-376.
#
#  Parameters:
#
#    Input, integer N, the order of A.
#
#    Input, real ALPHA, the parameter.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( i == 0 ):

        if ( j == 0 ):
          a[i,j] = 1.0
        else:
          a[i,j] = 0.0

      elif ( j == 0 ):

        a[i,j] = alpha * a[i-1,j]

      else:

        a[i,j] = a[i-1,j-1] + alpha * a[i-1,j]

  return a

def pascal3_condition ( n, alpha ):

#*****************************************************************************80
#
## PASCAL3_CONDITION returns the L1 condition of the PASCAL3 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, real ALPHA, the scalar defining A.  
#
#    Output, real VALUE, the L1 condition.
#
  from r8mat_norm_l1 import r8mat_norm_l1

  a = pascal3 ( n, alpha )
  a_norm = r8mat_norm_l1 ( n, n, a );
  b_norm = a_norm;
  value = a_norm * b_norm

  return value

def pascal3_determinant ( n, alpha ):

#*****************************************************************************80
#
## PASCAL3_DETERMINANT returns the determinant of the PASCAL3 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, real ALPHA, the scalar defining A.  
#
#    Output, real VALUE, the determinant.
#
  value = 1.0

  return value

def pascal3_determinant_test ( ):

#*****************************************************************************80
#
## PASCAL3_DETERMINANT_TEST tests PASCAL3_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
  from pascal3 import pascal3
  from r8mat_print import r8mat_print
  from r8_uniform_ab import r8_uniform_ab

  print ''
  print 'PASCAL3_DETERMINANT_TEST'
  print '  PASCAL3_DETERMINANT computes the determinant of the PASCAL3 matrix.'
  print ''

  m = 4
  n = m

  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )

  a = pascal3 ( n, alpha )
  r8mat_print ( m, n, a, '  PASCAL3 matrix:' )

  value = pascal3_determinant ( n, alpha )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'PASCAL3_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def pascal3_inverse ( n, alpha ):

#*****************************************************************************80
#
## PASCAL3_INVERSE returns the inverse of the PASCAL3 matrix.
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
#    Input, integer N, the order of A.
#
#    Input, real ALPHA, the parameter.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( i == 0 ):

        if ( j == 0 ):
          a[i,j] = 1.0

      elif ( j == 0 ):

        a[i,j] = - alpha * a[i-1,j]

      else:

        a[i,j] = a[i-1,j-1] - alpha * a[i-1,j]

  return a

def pascal3_test ( ):

#*****************************************************************************80
#
## PASCAL3_TEST tests PASCAL3.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print
  from r8_uniform_ab import r8_uniform_ab

  print ''
  print 'PASCAL3_TEST'
  print '  PASCAL3 computes the PASCAL3 matrix.'

  m = 4
  n = m

  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )

  a = pascal3 ( n, alpha )
  r8mat_print ( m, n, a, '  PASCAL3 matrix:' )

  print ''
  print 'PASCAL3_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  pascal3_test ( )
  timestamp ( )
