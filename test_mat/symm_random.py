#! /usr/bin/env python
#
def symm_random ( n, d, key ):

#*****************************************************************************80
#
## SYMM_RANDOM returns the SYMM_RANDOM matrix.
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#    The eigenvalues of A will be real.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of A.
#
#    Input, real D(N), the desired eigenvalues for the matrix.
#
#    Input, integer KEY, a positive integer that selects the data.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np
  from orth_random import orth_random
#
#  Get a random orthogonal matrix Q.
#
  q = orth_random ( n, key )
#
#  Set A = Q * Lambda * Q'.
#
  a = np.zeros ( ( n, n ) )

  for j in range ( 0, n ):
    for i in range ( 0, n ):
      for k in range ( 0, n ):
        a[i,j] = a[i,j] + q[i,k] * d[k] * q[j,k]

  return a

def symm_random_determinant ( n, d, key ):

#*****************************************************************************80
#
## SYMM_RANDOM_DETERMINANT computes the determinant of the SYMM_RANDOM matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of A.
#
#    Input, real D(N), the desired eigenvalues for the matrix.
#
#    Input, integer KEY, a positive integer that selects the data.
#
#    Output, real VALUE, the determinant.
#
  import numpy as np

  value = np.prod ( d )

  return value

def symm_random_eigen_left ( n, d, key ):

#*****************************************************************************80
#
## SYMM_RANDOM_EIGEN_LEFT returns left eigenvectors for the SYMM_RANDOM matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of A.
#
#    Input, real D(N), the desired eigenvalues for the matrix.
#
#    Input, integer KEY, a positive integer that selects the data.
#
#    Output, real V(N,N), the vectors.
#
  from orth_random import orth_random
#
#  Get a random orthogonal matrix Q.
#
  x = orth_random ( n, key )
#
#  Transpose.
#
  for i in range ( 0, n ):
    for j in range ( 0, i ):
      t      = x[i,j]
      x[i,j] = x[j,i]
      x[j,i] = t

  return x

def symm_random_eigen_right ( n, d, key ):

#*****************************************************************************80
#
## SYMM_RANDOM_EIGEN_RIGHT returns right eigenvectors for the SYMM_RANDOM matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of A.
#
#    Input, real D(N), the desired eigenvalues for the matrix.
#
#    Input, integer KEY, a positive integer that selects the data.
#
#    Output, real V(N,N), the vectors.
#
  from orth_random import orth_random
#
#  Get a random orthogonal matrix Q.
#
  x = orth_random ( n, key )

  return x

def symm_random_eigenvalues ( n, d, key ):

#*****************************************************************************80
#
## SYMM_RANDOM_EIGENVALUES returns eigenvalues for the SYMM_RANDOM matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of A.
#
#    Input, real D(N), the desired eigenvalues for the matrix.
#
#    Input, integer KEY, a positive integer that selects the data.
#
#    Output, real LAM(N), the eigenvalues.
#
  import numpy as np

  lam = np.copy ( d )

  return lam

def symm_random_inverse ( n, d, key ):

#*****************************************************************************80
#
## SYMM_RANDOM_INVERSE returns the inverse of the SYMM_RANDOM matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of A.
#
#    Input, real D(N), the desired eigenvalues for the matrix.
#
#    Input, integer KEY, a positive integer that selects the data.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np
  from orth_random import orth_random
#
#  Get a random orthogonal matrix Q.
#
  q = orth_random ( n, key )
#
#  Set A = Q * 1/Lambda * Q'.
#
  a = np.zeros ( ( n, n ) )

  for j in range ( 0, n ):
    for i in range ( 0, n ):
      for k in range ( 0, n ):
        a[i,j] = a[i,j] + q[i,k] * ( 1.0 / d[k] ) * q[j,k]

  return a

def symm_random_test ( ):

#*****************************************************************************80
#
## SYMM_RANDOM_TEST tests SYMM_RANDOM.
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
  from r8mat_print import r8mat_print

  print ''
  print 'SYMM_RANDOM_TEST'
  print '  SYMM_RANDOM computes the SYMM_RANDOM matrix.'

  n = 3
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  d, seed = r8vec_uniform_ab ( r8_lo, r8_hi, seed )

  key = 123456789
  a = symm_random ( n, d, key )
  r8mat_print ( n, n, a, '  SYMM_RANDOM matrix:' )

  print ''
  print 'SYMM_RANDOM_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  symm_random_test ( )
  timestamp ( )
