#! /usr/bin/env python
#
def frank ( n ):

#*****************************************************************************80
#
## FRANK returns the FRANK matrix.
#
#  Formula:
#
#    if ( I <= J )
#      A(I,J) = N+1-J
#    elseif ( J = I-1 )
#      A(I,J) = N-J
#    else
#      A(I,J) = 0.0
#
#  Example:
#
#    N = 5
#
#    5 4 3 2 1
#    4 4 3 2 1
#    . 3 3 2 1
#    . . 2 2 1
#    . . . 1 1
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is upper Hessenberg.
#
#    A is integral: int ( A ) = A.
#
#    det ( A ) = 1.
#
#    A is unimodular.
#
#    The eigenvalues of A are related to the zeros of the Hermite
#    polynomials.
#
#    The eigenvalues of A are real and positive, and occur in reciprocal
#    pairs, LAMBDA and 1/LAMBDA.
#
#    For N = 12, the eigenvalues of A range from 32.2 to 0.031, with
#    the smaller eigenvalues having a condition number of 10^7,
#    meaning that a change in the matrix of order 10^(-7) can
#    result in a change in the eigenvalue of order 1.  The actual
#    eigenvalues are:
#
#      0.031028060644010
#      0.049507429185278
#      0.081227659240405
#      0.143646519769220
#      0.284749720558478
#      0.6435053190048555
#      1.55398870913210790
#      3.511855948580757194
#      6.961533085567122113
#     12.311077408868526120
#     20.198988645877079428
#     32.228891501572160750
#
#    If N is odd, 1 is an eigenvalue of A.
#
#    The (N/2) smaller eigenvalues of A are ill-conditioned.
#
#    For large N, the computation of the determinant of A
#    comes out very far from its correct value of 1.
#
#    Simple linear systems:
#      x = (0,0,0,...,1),   A*x = (1,1,1,...,1)
#      x = (1,1,1,...,1),   A*x = n * ( (n+1)/2, (n+3)/2, (n+3)/2, ..., (n+3)/2)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Patricia Eberlein,
#    A note on the matrices denoted by $B n$,
#    SIAM Journal on Applied Mathematics,
#    Volume 20, 1971, pages 87-92.
#
#    Werner Frank,
#    Computing eigenvalues of complex matrices by determinant
#    evaluation, and by methods of Danilewski and Wielandt,
#    Journal of the Society for Industrial and Applied Mathematics,
#    Volume 6, 1958, pages 378-392.
#
#    Gene Golub, James Wilkinson,
#    Ill-conditioned eigensystems and the computation of the Jordan
#    canonical form,
#    SIAM Review,
#    Volume 18, Number 4, 1976, pages 578-619.
#
#    Robert Gregory, David Karney,
#    Example 5.14,
#    A Collection of Matrices for Testing Computational Algorithms,
#    Wiley, New York, 1969, page 92,
#    LC: QA263.G68.
#
#    H Rutishauser,
#    On test matrices,
#    Programmation en Mathematiques
#    Numeriques, Editions Centre Nat. Recherche Sci., Paris, 165,
#    1966, pages 349-365.  Section 9.
#
#    J M Varah,
#    A generalization of the Frank matrix,
#    SIAM Journal on Scientific and Statistical Computing,
#    Volume 7, Number 3, August 1986, pages 835-839.
#
#    Joan Westlake,
#    Test Matrix A37,
#    A Handbook of Numerical Matrix Inversion and Solution of Linear Equations,
#    John Wiley, 1968.
#
#    James Wilkinson,
#    Error analysis of floating-point computation,
#    Numerische Mathematik,
#    Volume 2, 1960, pages 319-340.
#
#    James Wilkinson,
#    The Algebraic Eigenvalue Problem,
#    Oxford University Press, 1965, pages 92-93.
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
    for j in range ( 0, n ):

      if ( i <= j ):
        a[i,j] = ( n - j )
      elif ( j == i - 1 ):
        a[i,j] = ( n - j - 1 )

  return a

def frank_determinant ( n ):

#*****************************************************************************80
#
## FRANK_DETERMINANT computes the determinant of the FRANK matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Output, real DETERM, the determinant.
#
  determ = 1.0
 
  return determ

def frank_determinant_test ( ):

#*****************************************************************************80
#
## FRANK_DETERMINANT_TEST tests FRANK_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 February 2015
#
#  Author:
#
#    John Burkardt
#
  from frank import frank
  from r8mat_print import r8mat_print

  print ''
  print 'FRANK_DETERMINANT_TEST'
  print '  FRANK_DETERMINANT computes the FRANK determinant.'

  m = 4
  n = 4
  a = frank ( n )

  r8mat_print ( m, n, a, '  FRANK matrix:' )

  value = frank_determinant ( n )

  print '  Value =  %g' % ( value )

  print ''
  print 'FRANK_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def frank_inverse ( n ):

#*****************************************************************************80
#
## FRANK_INVERSE returns the inverse of the FRANK matrix.
#
#  Formula:
#
#    if ( I = J-1 )
#      A(I,J) = -1
#    elseif ( I = J )
#      if ( I = 1 )
#        A(I,J) = 1
#      else
#        A(I,J) = N + 2 - I
#    elseif ( J < I )
#      A(I,J) = - (N+1-I) * A(I-1,J)
#    else
#      A(I,J) = 0
#
#  Example:
#
#    N = 5
#
#     1  -1  0  0  0
#    -4   5 -1  0  0
#    12 -15  4 -1  0
#   -24  30 -8  3 -1
#    24 -30  8 -3  2
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is lower Hessenberg.
#
#    det ( A ) = 1.
#
#    A is unimodular.
#
#    A is integral: int ( A ) = A.
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

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( i == j - 1 ):
        a[i,j] = - 1.0
      elif ( i == j ):
        if ( i == 0 ):
          a[i,j] = 1.0
        else:
          a[i,j] = float ( n + 1 - i )
      elif ( j < i ):
        a[i,j] = - float ( n - i ) * a[i-1,j]

  return a

def frank_rhs ( m, k ):

#*****************************************************************************80
#
## FRANK_RHS returns the FRANK right hand side.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the row dimension.
#
#    Input, integer K, the column dimension ( should be 2).
#
#    Output, real B(M,K), the right hand side matrix.
#
  import numpy as np

  b = np.zeros ( ( m, k ) )

  if ( 1 <= k ):
    for i in range ( 0, m ):
      b[i,0] = 1.0

    if ( 2 <= k ):
      b[0,1] = float ( ( m * ( m + 1 ) ) // 2 )
      for i in range ( 1, m ):
        b[i,1] = float ( ( ( m - i ) * ( m + 3 - i ) ) // 2 )

  return b

def frank_solution ( n, k ):

#*****************************************************************************80
#
## FRANK_SOLUTION returns the FRANK solution matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 November 2007
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the row dimension.
#
#    Input, integer K, the column dimension ( should be 2).
#
#    Output, real X(N,K), the solution matrix.
#
  import numpy as np

  x = np.zeros ( ( n, k ) )

  if ( 1 <= k ):
    x[n-1,0] = 1.0

    if ( 2 <= k ):
      for i in range ( 0, n ):
        x[i,1] = 1.0

  return x

def frank_test ( ):

#*****************************************************************************80
#
## FRANK_TEST tests FRANK.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 March 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'FRANK_TEST'
  print '  FRANK computes the FRANK matrix.'

  m = 5
  n = m
  a = frank ( n )
  r8mat_print ( m, n, a, '  FRANK matrix:' )

  print ''
  print 'FRANK_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  frank_test ( )
  timestamp ( )
