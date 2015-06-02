#! /usr/bin/env python
#
def pds_random ( n, key ):

#*****************************************************************************80
#
## PDS_RANDOM returns a random positive definite symmetric matrix.
#
#  Discussion:
#
#    The matrix returned will have eigenvalues in the range [0,1].
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#    A is positive definite: 0 < x'*A*x for nonzero x.
#
#    The eigenvalues of A will be real.
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
#    Input, integer N, the order of A.
#
#    Input, integer KEY, a positive value that selects the data.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np
  from orth_random import orth_random
  from r8vec_uniform_01 import r8vec_uniform_01
#
#  Get a random set of eigenvalues.
#
  seed = key
  lam, seed = r8vec_uniform_01 ( n, seed )
#
#  Get a random orthogonal matrix Q.
#
  q = orth_random ( n, key )
#
#  Set A = Q * Lambda * Q'.
#
  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      for k in range ( 0, n ):
        a[i,j] = a[i,j] + q[i,k] * lam[k] * q[j,k]

  return a

def pds_random_determinant ( n, key ):

#*****************************************************************************80
#
## PDS_RANDOM_DETERMINANT returns the determinant of the PDS_RANDOM matrix.
#
#  Discussion:
#
#    This routine will only work properly if the SAME value of SEED
#    is input that was input to PDS_RANDOM.
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
#    Input, integer N, the order of A.
#
#    Input, integer KEY, a positive value that selects the data.
#
#    Output, real VALUE, the determinant.
#
  import numpy as np
  from r8vec_uniform_01 import r8vec_uniform_01

  seed = key
  lam, seed = r8vec_uniform_01 ( n, seed )

  value = np.prod ( lam )

  return value

def pds_random_eigen_right ( n, key ):

#*****************************************************************************80
#
## PDS_RANDOM_EIGEN_RIGHT returns the right eigenvectors of the PDS_RANDOM matrix.
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
#    Input, integer N, the order of A.
#
#    Input, integer KEY, a positive value that selects the data.
#
#    Output, real Q(N,N), the matrix.
#
  from orth_random import orth_random
  from r8vec_uniform_01 import r8vec_uniform_01
#
#  Get a random set of eigenvalues.
#
  seed = key
  lam, seed = r8vec_uniform_01 ( n, seed )
#
#  Get a random orthogonal matrix Q.
#
  q = orth_random ( n, key )

  return q

def pds_random_eigenvalues ( n, key ):

#*****************************************************************************80
#
## PDS_RANDOM_EIGENVALUES returns the eigenvalues of the PDS_RANDOM matrix.
#
#  Discussion:
#
#    This routine will only work properly if the SAME value of SEED
#    is input that was input to PDS_RANDOM.
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
#    Input, integer N, the order of A.
#
#    Input, integer KEY, a positive value that selects the data.
#
#    Output, real LAM(N), the eigenvalues.
#
  from r8vec_uniform_01 import r8vec_uniform_01

  seed = key
  lam, seed = r8vec_uniform_01 ( n, seed )

  return lam

def pds_random_inverse ( n, key ):

#*****************************************************************************80
#
## PDS_RANDOM_INVERSE returns the inverse of the PDS_RANDOM matrix.
#
#  Discussion:
#
#    The matrix returned will have eigenvalues in the range [0,1].
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#    A is positive definite: 0 < x'*A*x for nonzero x.
#
#    The eigenvalues of A will be real.
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
#    Input, integer N, the order of A.
#
#    Input, integer KEY, a positive value that selects the data.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np
  from orth_random import orth_random
  from r8vec_uniform_01 import r8vec_uniform_01

  a = np.zeros ( ( n, n ) )
#
#  Get a random set of eigenvalues.
#
  seed = key
  lam, seed = r8vec_uniform_01 ( n, seed )
#
#  Get a random orthogonal matrix Q.
#
  q = orth_random ( n, key )
#
#  Set A = Q * Lambda * Q'.
#
  for i in range ( 0, n ):
    for j in range ( 0, n ):
      for k in range ( 0, n ):
        a[i,j] = a[i,j] + q[i,k] * ( 1.0 / lam[k] ) * q[j,k]

  return a

def pds_random_test ( ):

#*****************************************************************************80
#
## PDS_RANDOM_TEST tests PDS_RANDOM.
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
  from r8mat_print import r8mat_print

  print ''
  print 'PDS_RANDOM_TEST'
  print '  PDS_RANDOM computes the PDS_RANDOM matrix.'

  n = 5
  key = 123456789
  a = pds_random ( n, key )

  r8mat_print ( n, n, a, '  PDS_RANDOM matrix:' )

  print ''
  print 'PDS_RANDOM_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  pds_random_test ( )
  timestamp ( )
