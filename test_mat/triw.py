#! /usr/bin/env python
#
def triw ( alpha, k, n ):

#*****************************************************************************80
#
## TRIW returns the TRIW matrix.
#
#  Discussion:
#
#    TRIW is the Wilkinson banded upper triangular matrix.
#
#  Formula:
#
#    if ( I = J )
#      A(I,J) = 1
#    elseif ( I < J and J <= K + I )
#      A(I,J) = ALPHA
#    else
#      A(I,J) = 0
#
#  Example:
#
#    ALPHA = 3, K = 2, N = 5
#
#    1 3 3 0 0
#    0 1 3 3 0
#    0 0 1 3 3
#    0 0 0 1 3
#    0 0 0 0 1
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is nonsingular.
#
#    A is upper triangular.
#
#    det ( A ) = 1.
#
#    A is unimodular.
#
#    LAMBDA(1:N) = 1.
#
#    A is Toeplitz: constant along diagonals.
#
#    A is persymmetric: A(I,J) = A(N+1-J,N+1-I).
#
#    Adding -2^(2-N) to the (N,1) element makes the matrix singular.
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Gene Golub, James Wilkinson,
#    Ill-conditioned eigensystems and the computation of the Jordan
#    canonical form,
#    SIAM Review,
#    Volume 18, Number 4, 1976, pages 578-619.
#
#    W Kahan,
#    Numerical linear algebra,
#    Canadian Mathematical Bulletin,
#    Volume 9, 1966, pages 757-801.
#
#    AM Ostrowski,
#    On the spectrum of a one-parametric family of matrices,
#    Journal fuer Reine und Angewandte Mathematik,
#    Volume 193, Number (3/4), 1954, pages 143-160.
#
#    James Wilkinson,
#    Singular-value decomposition - basic aspects,
#    in Numerical Software - Needs and Availability,
#    edited by DAH Jacobs,
#    Academic Press, London, 1978, pages 109-135.
#
#  Parameters:
#
#    Input, real ALPHA, the superdiagonal value. 
#    A typical value is -1.
#
#    Input, integer K, the number of nonzero superdiagonals.  
#    A typical value is N-1.
#
#    Input, integer N, the order of A.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( i == j ):
        a[i,j] = 1.0
      elif ( i < j and j - i <= k ):
        a[i,j] = alpha
 
  return a

def triw_determinant ( alpha, k, n ):

#*****************************************************************************80
#
## TRIW_DETERMINANT returns the determinant of the TRIW matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real ALPHA, value used on the superdiagonals.
#
#    Input, integer K, the number of nonzero superdiagonals.
#
#    Input, integer N, the order of the matrix.
#
#    Output, real VALUE, the determinant.
#
  value = 1.0

  return value

def triw_determinant_test ( ):

#*****************************************************************************80
#
## TRIW_DETERMINANT_TEST tests TRIW_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 February 2015
#
#  Author:
#
#    John Burkardt
#
  from triw import triw
  from r8_uniform_01 import r8_uniform_01
  from r8mat_print import r8mat_print

  print ''
  print 'TRIW_DETERMINANT_TEST'
  print '  TRIW_DETERMINANT computes the determinant of the TRIW matrix.'
  print ''

  m = 5
  n = m

  i4_lo = 0
  i4_hi = n - 1
  seed = 123456789
  k, seed = i4_uniform_ab ( i4_lo, i4_hi, seed )

  r8_lo = -5.0
  r8_hi = +5.0
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )

  a = triw ( alpha, k, n )

  r8mat_print ( m, n, a, '  TRIW matrix:' )

  value = triw_determinant ( alpha, k, n )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'TRIW_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def triw_inverse ( alpha, k, n ):

#*****************************************************************************80
#
#% TRIW_INVERSE sets the inverse of the TRIW matrix.
#
#  Example:
#
#    ALPHA = 3, K = 2, N = 5
#
#    1      -3       6      -9       9
#    0       1      -3       6      -9
#    0       0       1      -3       6
#    0       0       0       1      -3
#    0       0       0       0       1
#
#  Properties:
#
#    A is nonsingular.
#
#    A is upper triangular.
#
#    A is Toeplitz: constant along diagonals.
#
#    A is persymmetric: A(I,J) = A(N+1-J,N+1-I).
#
#    det ( A ) = 1.
#
#    A is unimodular.
#
#    LAMBDA(1:N) = 1.
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
#    Input, real ALPHA, value used on the superdiagonals.
#
#    Input, integer K, the number of nonzero superdiagonals.
#
#    Input, integer N, the order of A.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    a[i,i] = 1.0
#
#  Compute the product of row 1 of the inverse with columns 2,
#  3,..., N of the original matrix, up to, but not including,
#  the next unknown entry of the inverse.  That unknown entry
#  is multiplied by 1, and the resulting sum must be zero.
#  So the unknown entry equals minus the sum of all the
#  other products.  And all the entries along its superdiagonal
#  have the same value.
#
  for j in range ( 1, n ):

    prod = 0.0
    klo = max ( 0, j - k )
    for kk in range ( klo, j ):
      prod = prod + a[0,kk] * alpha

    for i in range ( 0, n - j ):
      a[i,i+j] = - prod

  return a

def triw_test ( ):

#*****************************************************************************80
#
## TRIW_TEST tests TRIW.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 February 2015
#
#  Author:
#
#    John Burkardt
#
  from r8_uniform_01 import r8_uniform_01
  from r8mat_print import r8mat_print

  print ''
  print 'TRIW_TEST'
  print '  TRIW computes the TRIW matrix.'

  m = 5
  n = m

  i4_lo = 0
  i4_hi = n - 1
  seed = 123456789
  k, seed = i4_uniform_ab ( i4_lo, i4_hi, seed )

  r8_lo = -5.0
  r8_hi = +5.0
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )

  a = triw ( alpha, k, n )

  r8mat_print ( m, n, a, '  TRIW matrix:' )

  print ''
  print 'TRIW_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  triw_test ( )
  timestamp ( )
