#! /usr/bin/env python
#
def carry ( n, alpha ):

#*****************************************************************************80
#
## CARRY returns the CARRY matrix.
#
#  Discussion:
#
#    We assume that arithmetic is being done in base ALPHA.  We are adding
#    a column of N digits base ALPHA, as part of adding N random numbers.
#    We know the carry digit, between 0 and N-1, that is being carried into the
#    column sum (the incarry digit), and we want to know the probability of
#    the various carry digits 0 through N-1 (the outcarry digit) that could
#    be carried out of the column sum.
#
#    The carry matrix summarizes this data.  The entry A(I,J) represents
#    the probability that, given that the incarry digit is I-1, the
#    outcarry digit will be J-1.
#
#  Formula:
#
#    A(I,J) = ( 1 / ALPHA )^N * sum ( 0 <= K <= J-1 - floor ( I-1 / ALPHA ) )
#      (-1)^K * C(N+1,K) * C(N-I+(J-K)*ALPHA, N )
#
#  Example:
#
#    ALPHA = 10, N = 4
#
#    0.0715 0.5280 0.3795 0.0210
#    0.0495 0.4840 0.4335 0.0330
#    0.0330 0.4335 0.4840 0.0495
#    0.0210 0.3795 0.5280 0.0715
#
#  Square Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is a Markov matrix.
#
#    A is centrosymmetric: A(I,J) = A(N+1-I,N+1-J).
#
#    LAMBDA(I) = 1 / ALPHA^(I-1)
#
#    det ( A ) = 1 / ALPHA^((N*(N-1))/2)
#
#    The eigenvectors do not depend on ALPHA.
#
#    A is generally not normal: A' * A /= A * A'.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John Holte,
#    Carries, Combinatorics, and an Amazing Matrix,
#    The American Mathematical Monthly,
#    February 1997, pages 138-149.
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, integer ALPHA, the numeric base used in the addition.
#
#    Output, real A(N,N), the matrix.
#
  from r8_choose import r8_choose
  import numpy as np

  a = np.zeros ( [ n, n ] )

  for j in range ( 0, n ):
    for i in range ( 0, n ):

      temp = 0.0
      s = -1.0

      for k in range ( 0, j - ( i // alpha ) + 1 ):
        s = - s
        c1 = r8_choose ( n + 1, k )
        c2 = r8_choose ( n - i - 1 + ( j + 1 - k ) * alpha, n )
        temp = temp + s * c1 * c2

      a[i,j] = temp / alpha ** n

  return a

def carry_determinant ( n, alpha ):

#*****************************************************************************80
#
## CARRY_DETERMINANT computes the determinant of the CARRY matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, integer ALPHA, the numeric base used in the addition.
#
#    Output, real DETERM, the determinant.
#
  power = ( n * ( n - 1 ) ) // 2
  determ = 1.0 / alpha ** power
 
  return determ

def carry_determinant_test ( ):

#*****************************************************************************80
#
## CARRY_DETERMINANT_TEST tests CARRY_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 December 2014
#
#  Author:
#
#    John Burkardt
#
  from carry import carry
  from r8mat_print import r8mat_print

  print ''
  print 'CARRY_DETERMINANT_TEST'
  print '  CARRY_DETERMINANT computes the CARRY determinant.'

  m = 4
  n = m
  alpha = 10
  a = carry ( n, alpha )

  r8mat_print ( m, n, a, '  CARRY matrix:' )

  value = carry_determinant ( n, alpha )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'CARRY_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def carry_eigen_left ( n, alpha  ):

#*****************************************************************************80
#
#% CARRY_EIGEN_LEFT returns the left eigenvectors for the CARRY matrix.
#
#  Formula:
#
#    A(I,J) = sum ( 0 <= K <= J-1 )
#      (-1)^K * C(N+1,K) * ( J - K )^(N+1-I)
#
#  Example:
#
#    N = 4
#
#    1  11  11   1
#    1   3  -3  -1
#    1  -1  -1   1
#    1  -3   3  -1
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    Column 1 is all 1's, and column N is (-1)^(I+1).
#
#    The top row is proportional to a row of Eulerian numbers, and
#    can be normalized to represent the stationary probablities
#    for the carrying process when adding N random numbers.
#
#    The bottom row is proportional to a row of Pascal's triangle,
#    with alternating signs.
#
#    The product of the left and right eigenvector matrices of
#    order N is N! times the identity.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John Holte,
#    Carries, Combinatorics, and an Amazing Matrix,
#    The American Mathematical Monthly,
#    February 1997, pages 138-149.
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, integer ALPHA, the numeric base used in the addition.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np
  from r8_choose import r8_choose

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      s = -1.0
      for k in range ( 0, j + 1 ):
        s = - s
        a[i,j] = a[i,j] + s * r8_choose ( n + 1, k ) * ( j + 1 - k ) ** ( n - i )

  return a

def carry_eigen_right ( n, alpha ):

#*****************************************************************************80
#
#% CARRY_EIGEN_RIGHT returns the right eigenvectors of the CARRY matrix.
#
#  Formula:
#
#    A(I,J) = sum ( N+1-J) <= K <= N )
#      S1(N,K) * C(K,N+1-J) ( N - I )^(K-N+J-1)
#
#    where S1(N,K) is a signed Sterling number of the first kind.
#
#  Example:
#
#    N = 4
#
#    1   6  11   6
#    1   2  -1  -2
#    1  -2  -1   2
#    1  -6  11  -6
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    The first column is all 1's.
#
#    The last column is reciprocals of binomial coefficients with
#    alternating sign multiplied by (N-1).
#
#    The top and bottom rows are the unsigned and signed Stirling numbers
#    of the first kind.
#
#    The entries in the J-th column are a degree (J-1) polynomial
#    in the row index I.  (Column 1 is constant, the first difference
#    in column 2 is constant, the second difference in column 3 is
#    constant, and so on.)
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
#    John Holte,
#    Carries, Combinatorics, and an Amazing Matrix,
#    The American Mathematical Monthly,
#    February 1997, pages 138-149.
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, integer ALPHA, the numeric base used in the addition.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np
  from r8_choose import r8_choose
  from stirling import stirling

  s1 = stirling ( n, n )

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      for k in range ( n - j, n + 1 ):
        if ( n - 1 - i == 0 and k - n + j == 0 ):
          a[i,j] = a[i,j] + s1[n-1,k-1] * r8_choose ( k, n - j )
        else:
          a[i,j] = a[i,j] + s1[n-1,k-1] * r8_choose ( k, n - j ) \
            * ( n - i - 1 ) ** ( k - n + j )

  return a

def carry_eigenvalues ( n, alpha ):

#*****************************************************************************80
#
#% CARRY_EIGENVALUES returns the eigenvalues of the CARRY matrix.
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
#    Input, integer N, the order of the matrix.
#
#    Input, integer ALPHA, the numeric base used in the addition.
#
#    Output, real LAM(N), the eigenvalues.
#
  import numpy as np

  lam = np.zeros ( n )

  for i in range ( 0, n ):
    lam[i] = 1.0 / alpha ** i

  return lam

def carry_inverse ( n, alpha ):

#*****************************************************************************80
#
## CARRY_INVERSE returns the inverse of the CARRY matrix.
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
#    Input, integer ALPHA, the numeric base used in the addition.
#
#    Input, integer ALPHA, the numeric base used in the addition.
#
#    Output, real A(N,N), the matrix.
#
  from diagonal import diagonal
  from r8_factorial import r8_factorial
  from r8mat_mm import r8mat_mm

  v = carry_eigen_left ( n, alpha )

  d = carry_eigenvalues ( n, alpha )
  for i in range ( 0, n ):
    d[i] = 1.0 / d[i]
  d_inv = diagonal ( n, n, d )

  u = carry_eigen_right ( n, alpha )

  dv = r8mat_mm ( n, n, n, d_inv, v )

  a = r8mat_mm ( n, n, n, u, dv )

  t = r8_factorial ( n )
  for j in range ( 0, n ):
    for i in range ( 0, n ):
      a[i,j] = a[i,j] / t

  return a

def carry_test ( ):

#*****************************************************************************80
#
## CARRY_TEST tests CARRY.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 December 2014
#
#  Author:
#
#    John Burkardt
#
  from r8_uniform_01 import r8_uniform_01
  from r8mat_print import r8mat_print

  print ''
  print 'CARRY_TEST'
  print '  cARRY computes the CARRY matrix.'

  m = 4
  n = m
  alpha = 10
  a = carry ( alpha, n )
  r8mat_print ( m, n, a, '  CARRY matrix:' )

  print ''
  print 'CARRY_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  carry_test ( )
  timestamp ( )
