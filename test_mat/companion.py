#! /usr/bin/env python
#
def companion ( n, x ):

#*****************************************************************************80
#
## COMPANION returns the companion matrix A for a monic polynomial.
#
#  Formula:
#
#    Let the monic N-th degree polynomial be defined by
#
#      P(t) = t^N + X(N)*t^(N-1) + X(N-1)*t^(N-2) + ... + X(2)*t + X(1)
#
#    Then
#
#      A(1,J) = X(N+1-J) for J=1 to N
#      A(I,I-1) = 1      for I=2 to N
#      A(I,J) = 0        otherwise
#
#    A is called the companion matrix of the polynomial P(t), and the
#    characteristic equation of A is P(t) = 0.
#
#    Matrices of this form are also called Frobenius matrices.
#
#    The determinant of a matrix is unaffected by being transposed,
#    and only possibly changes sign if the rows are "reflected", so
#    there are actually many possible ways to write a companion matrix:
#
#    A B C D  A 1 0 0  0 1 0 0  0 0 1 0  0 0 1 A
#    1 0 0 0  B 0 1 0  0 0 1 0  0 1 0 0  0 1 0 B
#    0 1 0 0  C 0 0 1  0 0 0 1  1 0 0 0  1 0 0 C
#    0 0 1 0  D 0 0 0  D C B A  A B C D  0 0 0 D
#
#  Example:
#
#    N = 5, X = ( 1, 2, 3, 4, 5 )
#
#    5 4 3 2 1
#    1 0 0 0 0
#    0 1 0 0 0
#    0 0 1 0 0
#    0 0 0 1 0
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is nonsingular if and only if X(1) is nonzero.
#
#    The eigenvalues of A are the roots of P(t) = 0.
#
#    If LAMBDA is an eigenvalue of A, then a corresponding eigenvector is
#      ( 1, LAMBDA, LAMBDA^2, ..., LAMBDA^(N-1) ).
#
#    If LAMBDA is an eigenvalue of multiplicity 2, then a second 
#    corresponding generalized eigenvector is
#
#      ( 0, 1, 2 * LAMBDA, ..., (N-1)*LAMBDA^(N-2) ).
#
#    For higher multiplicities, repeatedly differentiate with respect to LAMBDA.
#
#    Any matrix with characteristic polynomial P(t) is similar to A.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Gene Golub, Charles Van Loan,
#    Matrix Computations, second edition,
#    Johns Hopkins University Press, Baltimore, Maryland, 1989,
#    section 7.4.6.
#
#    Charles Kenney, Alan Laub,
#    Controllability and stability radii for companion form systems,
#    Math. Control Signals Systems, 1 (1988), pages 239-256.
#    (Gives explicit formulas for the singular values.)
#
#    James Wilkinson,
#    The Algebraic Eigenvalue Problem,
#    Oxford University Press,
#    1965, page 12.
#
#  Parameters:
#
#    Input, integer N, the order of A.
#
#    Input, real X(N), the coefficients of the polynomial 
#    which define A.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ n, n ] )

  for j in range ( 0, n ):
    for i in range ( 0, n ):

      if ( i == 0 ):
        a[i,j] = x[n-1-j]
      elif ( i == j + 1 ):
        a[i,j] = 1.0
      else:
        a[i,j] = 0.0

  return a

def companion_condition ( n, x ):

#*****************************************************************************80
#
## COMPANION_CONDITION computes the L1 condition of the COMPANION matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, real X(N), the polynomial coefficients.
#
#    Output, real VALUE, the L1 condition.
#
  a_norm = abs ( x[0] )
  for i in range ( 1, n ):
    a_norm = max ( a_norm, 1.0 + abs ( x[i] ) )

  b_norm = 1.0 / abs ( x[0] )
  for i in range ( 1, n ):
    b_norm = max ( b_norm, 1.0 + abs ( x[i] ) / abs ( x[0] ) )

  value = a_norm * b_norm
 
  return value

def companion_condition_test ( ):

#*****************************************************************************80
#
## COMPANION_CONDITION_TEST tests COMPANION_CONDITION.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 January 2015
#
#  Author:
#
#    John Burkardt
#
  from r8vec_uniform_ab import r8vec_uniform_ab
  from r8mat_print import r8mat_print

  print ''
  print 'COMPANION_CONDITION_TEST'
  print '  COMPANION_CONDITION computes the COMPANION condition.'

  n = 5
  x_lo = -5.0
  x_hi = +5.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( n, x_lo, x_hi, seed )

  a = companion ( n, x )
  m = n
  r8mat_print ( m, n, a, '  COMPANION matrix:' )

  value = companion_condition ( n, x )

  print '  Value =  %g' % ( value )

  print ''
  print 'COMPANION_CONDITION_TEST'
  print '  Normal end of execution.'

  return

def companion_determinant ( n, x ):

#*****************************************************************************80
#
## COMPANION_DETERMINANT computes the determinant of the COMPANION matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, real X(N), the polynomial coefficients.
#
#    Output, real DETERM, the determinant.
#
  if ( ( n % 2 ) == 1 ):
    determ = + x[0]
  else:
    determ = - x[0]
 
  return determ

def companion_determinant_test ( ):

#*****************************************************************************80
#
## COMPANION_DETERMINANT_TEST tests COMPANION_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 January 2015
#
#  Author:
#
#    John Burkardt
#
  from r8vec_uniform_ab import r8vec_uniform_ab
  from r8mat_print import r8mat_print

  print ''
  print 'COMPANION_DETERMINANT_TEST'
  print '  COMPANION_DETERMINANT computes the COMPANION determinant.'

  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( n, r8_lo, r8_hi, seed )

  a = companion ( n, x )
  m = n
  r8mat_print ( m, n, a, '  COMPANION matrix:' )

  value = companion_determinant ( n, x )

  print '  Value =  %g' % ( value )

  print ''
  print 'COMPANION_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def companion_inverse ( n, x ):

#*****************************************************************************80
#
## COMPANION_INVERSE returns the inverse of the COMPANION matrix.
#
#  Example:
#
#    N = 5, X = ( 1, 2, 3, 4, 5 )
#
#    0    1    0    0    0
#    0    0    1    0    0
#    0    0    0    1    0
#    0    0    0    0    1
#   1/1 -5/1 -4/1 -3/1 -2/1
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
#  Reference:
#
#    Gene Golub, Charles Van Loan,
#    Matrix Computations, second edition,
#    Johns Hopkins University Press, Baltimore, Maryland, 1989,
#    section 7.4.6.
#
#    Charles Kenney, Alan Laub,
#    Controllability and stability radii for companion form systems,
#    Math. Control Signals Systems,
#    Volume 1, 1988, pages 239-256.
#
#    James Wilkinson,
#    The Algebraic Eigenvalue Problem,
#    Oxford University Press,
#    1965, page 12.
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, real X(N), the coefficients of the polynomial
#    which define the matrix.  X(1) must not be zero.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for j in range ( 0, n ):
    for i in range ( 0, n ):
 
      if ( i == n - 1 ):

        if ( j == 0 ):
          a[i,j] = 1.0 / x[0]
        else:
          a[i,j] = - x[n-j] / x[0]

      elif ( i == j - 1 ):
        a[i,j] = 1.0

  return a

def companion_test ( ):

#*****************************************************************************80
#
## COMPANION_TEST tests COMPANION.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 January 2015
#
#  Author:
#
#    John Burkardt
#
  from r8vec_uniform_ab import r8vec_uniform_ab
  from r8mat_print import r8mat_print

  print ''
  print 'COMPANION_TEST'
  print '  COMPANION computes the COMPANION matrix.'

  n = 5
  x_lo = -5.0
  x_hi = +5.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( n, x_lo, x_hi, seed )

  a = companion ( n, x )
  m = n
  r8mat_print ( m, n, a, '  COMPANION matrix:' )

  print ''
  print 'COMPANION_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  companion_test ( )
  timestamp ( )
