#!/usr/bin/env python

def orth_random ( n, key ):

#*****************************************************************************80
#
## ORTH_RANDOM returns an ORTH_RANDOM matrix.
#
#  Properties:
#
#    The inverse of A is equal to A'.
#
#    A is orthogonal: A * A'  = A' * A = I.
#
#    Because A is orthogonal, it is normal: A' * A = A * A'.
#
#    Columns and rows of A have unit Euclidean norm.
#
#    Distinct pairs of columns of A are orthogonal.
#
#    Distinct pairs of rows of A are orthogonal.
#
#    The L2 vector norm of A*x = the L2 vector norm of x for any vector x.
#
#    The L2 matrix norm of A*B = the L2 matrix norm of B for any matrix B.
#
#    det ( A ) = +1 or -1.
#
#    A is unimodular.
#
#    All the eigenvalues of A have modulus 1.
#
#    All singular values of A are 1.
#
#    All entries of A are between -1 and 1.
#
#  Discussion:
#
#    Thanks to Eugene Petrov, B I Stepanov Institute of Physics,
#    National Academy of Sciences of Belarus, for convincingly
#    pointing out the severe deficiencies of an earlier version of
#    this routine.
#
#    Essentially, the computation involves saving the Q factor of the
#    QR factorization of a matrix whose entries are normally distributed.
#    However, it is only necessary to generate this matrix a column at
#    a time, since it can be shown that when it comes time to annihilate
#    the subdiagonal elements of column K, these (transformed) elements of
#    column K are still normally distributed random values.  Hence, there
#    is no need to generate them at the beginning of the process and
#    transform them K-1 times.
#
#    For computational efficiency, the individual Householder transformations
#    could be saved, as recommended in the reference, instead of being
#    accumulated into an explicit matrix format.
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
#    Pete Stewart,
#    Efficient Generation of Random Orthogonal Matrices With an Application
#    to Condition Estimators,
#    SIAM Journal on Numerical Analysis,
#    Volume 17, Number 3, June 1980, pages 403-409.
#
#  Parameters:
#
#    Input, integer N, the order of A.
#
#    Input, integer KEY, a positive value that selects the data.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np
  from r8_normal_01 import r8_normal_01
  from r8mat_house_axh import r8mat_house_axh
  from r8vec_house_column import r8vec_house_column
#
#  Start with A = the identity matrix.
#
  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    a[i,i] = 1.0
#
#  Now behave as though we were computing the QR factorization of
#  some other random matrix.  Generate the N elements of the first column,
#  compute the Householder matrix H1 that annihilates the subdiagonal elements,
#  and set A := A * H1' = A * H.
#
#  On the second step, generate the lower N-1 elements of the second column,
#  compute the Householder matrix H2 that annihilates them,
#  and set A := A * H2' = A * H2 = H1 * H2.
#
#  On the N-1 step, generate the lower 2 elements of column N-1,
#  compute the Householder matrix HN-1 that annihilates them, and
#  and set A := A * H(N-1)' = A * H(N-1) = H1 * H2 * ... * H(N-1).
#  This is our random orthogonal matrix.
#
  x_col = np.zeros ( n )
 
  seed = key

  for j in range ( 0, n - 1 ):

    for i in range ( 0, j ):
      x_col[i] = 0.0

    for i in range ( j, n ):
      x_col[i], seed = r8_normal_01 ( seed )
#
#  Compute the vector V that defines a Householder transformation matrix
#  H(V) that annihilates the subdiagonal elements of X.
#
    v = r8vec_house_column ( n, x_col, j )
#
#  Postmultiply the matrix A by H'(V) = H(V).
#
    a = r8mat_house_axh ( n, a, v )

  return a

def orth_random_determinant ( n, key ):

#*****************************************************************************80
#
## ORTH_RANDOM_DETERMINANT returns the determinant of the ORTH_RANDOM matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, integer KEY, a positive value that selects the data.
#
#    Output, real VALUE, the determinant.
#
  value = 1.0

  return value

def orth_random_test ( ):

#*****************************************************************************80
#
## ORTH_RANDOM_TEST tests ORTH_RANDOM.
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
  import numpy as np
  from r8mat_mm import r8mat_mm
  from r8mat_print import r8mat_print

  print ''
  print 'ORTH_RANDOM_TEST'
  print '  ORTH_RANDOM computes a random orthogal matrix.'

  m = 5
  n = m
  key = 123456789

  a = orth_random ( n, key )

  r8mat_print ( m, n, a, '  ORTH_RANDOM matrix:' )

  print ''
  print 'ORTH_RANDOM_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  orth_random_test ( )
  timestamp ( )

