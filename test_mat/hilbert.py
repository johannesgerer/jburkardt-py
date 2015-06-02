#! /usr/bin/env python
#
def hilbert ( m, n ):

#*****************************************************************************80
#
## HILBERT returns the HILBERT matrix.
#
#  Formula:
#
#    A(I,J) = 1 / ( I + J - 1 )
#
#  Example:
#
#    N = 5
#
#    1/1 1/2 1/3 1/4 1/5
#    1/2 1/3 1/4 1/5 1/6
#    1/3 1/4 1/5 1/6 1/7
#    1/4 1/5 1/6 1/7 1/8
#    1/5 1/6 1/7 1/8 1/9
#
#  Rectangular Properties:
#
#    A is a Hankel matrix: constant along anti-diagonals.
#
#  Square Properties:
#
#    A is positive definite.
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A is totally positive.
#
#    A is a Cauchy matrix.
#
#    A is nonsingular.
#
#    A is very ill-conditioned.
#
#    The entries of the inverse of A are all integers.
#
#    The sum of the entries of the inverse of A is N*N.
#
#    The ratio of the absolute values of the maximum and minimum
#    eigenvalues is roughly EXP(3.5*N).
#
#    The determinant of the Hilbert matrix of order 10 is
#    2.16417... * 10^(-53).
#
#    If the (1,1) entry of the 5 by 5 Hilbert matrix is changed
#    from 1 to 24/25, the matrix is exactly singular.  And there
#    is a similar rule for larger Hilbert matrices.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    MD Choi,
#    Tricks or treats with the Hilbert matrix,
#    American Mathematical Monthly,
#    Volume 90, 1983, pages 301-312.
#
#    Robert Gregory, David Karney,
#    Example 3.8,
#    A Collection of Matrices for Testing Computational Algorithms,
#    Wiley, New York, 1969, page 33,
#    LC: QA263.G68.
#
#    Nicholas Higham,
#    Accuracy and Stability of Numerical Algorithms,
#    Society for Industrial and Applied Mathematics, Philadelphia, PA,
#    USA, 1996; section 26.1.
#
#    Donald Knuth,
#    The Art of Computer Programming,
#    Volume 1, Fundamental Algorithms, Second Edition
#    Addison-Wesley, Reading, Massachusetts, 1973, page 37.
#
#    Morris Newman and John Todd,
#    Example A13,
#    The evaluation of matrix inversion programs,
#    Journal of the Society for Industrial and Applied Mathematics,
#    Volume 6, 1958, pages 466-476.
#
#    Joan Westlake,
#    Test Matrix A12,
#    A Handbook of Numerical Matrix Inversion and Solution of Linear Equations,
#    John Wiley, 1968.
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
      a[i,j] = 1.0 / float ( i + j + 1 )

  return a

def hilbert_determinant ( n ):

#*****************************************************************************80
#
## HILBERT_DETERMINANT computes the determinant of the HILBERT matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 February 2015
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
  top = 1.0
  for i in range ( 1, n + 1 ):
    for j in range ( i + 1, n + 1 ):
      top = top * float ( ( j - i ) * ( j - i ) )

  bottom = 1.0
  for i in range ( 1, n + 1 ):
    for j in range ( 1, n + 1 ):
      bottom = bottom * float ( i + j - 1 )

  value = top / bottom

  return value

def hilbert_determinant_test ( ):

#*****************************************************************************80
#
## HILBERT_DETERMINANT_TEST tests HILBERT_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 February 2015
#
#  Author:
#
#    John Burkardt
#
  from hilbert import hilbert
  from r8mat_print import r8mat_print

  print ''
  print 'HILBERT_DETERMINANT_TEST'
  print '  HILBERT_DETERMINANT computes the HILBERT determinant.'

  m = 5
  n = m
 
  a = hilbert ( m, n )

  r8mat_print ( m, n, a, '  HILBERT matrix:' )

  value = hilbert_determinant ( n )

  print '  Value =  %g' % ( value )

  print ''
  print 'HILBERT_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def hilbert_inverse ( n ):

#*****************************************************************************80
#
## HILBERT_INVERSE returns the inverse of the Hilbert matrix.
#
#  Formula:
#
#    A(I,J) =  (-1)^(I+J) * (N+I-1)! * (N+J-1)! /
#           [ (I+J-1) * ((I-1)!*(J-1)!)^2 * (N-I)! * (N-J)! ]
#
#  Example:
#
#    N = 5
#
#       25    -300     1050    -1400     630
#     -300    4800   -18900    26880  -12600
#     1050  -18900    79380  -117600   56700
#    -1400   26880  -117600   179200  -88200
#      630  -12600    56700   -88200   44100
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A is almost impossible to compute accurately by general routines
#    that compute the inverse.
#
#    A is the exact inverse of the Hilbert matrix; however, if the
#    Hilbert matrix is stored on a finite precision computer, and
#    hence rounded, A is actually a poor approximation
#    to the inverse of that rounded matrix.  Even though Gauss elimination
#    has difficulty with the Hilbert matrix, it can compute an approximate
#    inverse matrix whose residual is lower than that of the
#    "exact" inverse.
#
#    All entries of A are integers.
#
#    The sum of the entries of A is N^2.
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 March 2015
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
#
#  Set the (1,1) entry.
#
  a[0,0] = n * n
#
#  Define Row 1, Column J by recursion on Row 1 Column J-1
#
  i = 0
  for j in range ( 1, n ):
    a[i,j] = - a[i,j-1] * float ( ( n + j ) * ( i + j ) * ( n - j ) ) \
      / float ( ( i + j + 1 ) * j * j )
#
#  Define Row I by recursion on row I-1
#
  for i in range ( 1, n ):
    for j in range ( 0, n ):

      a[i,j] = - a[i-1,j] * float ( ( n + i ) * ( i + j ) * ( n- i ) ) \
        / float ( ( i + j + 1 ) * i * i )

  return a

def hilbert_test ( ):

#*****************************************************************************80
#
## HILBERT_TEST tests HILBERT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 February 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'HILBERT_TEST'
  print '  HILBERT computes the HILBERT matrix.'

  m = 5
  n = m

  a = hilbert ( m, n )
 
  r8mat_print ( m, n, a, '  HILBERT matrix:' )

  print ''
  print 'HILBERT_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  hilbert_test ( )
  timestamp ( )
