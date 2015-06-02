#!/usr/bin/env python

def idem_random ( n, rank, key ):

#*****************************************************************************80
#
## IDEM_RANDOM returns a random idempotent matrix of rank K.
#
#  Properties:
#
#    A is idempotent: A * A = A
#
#    If A is invertible, then A must be the identity matrix.
#    In other words, unless A is the identity matrix, it is singular.
#
#    I - A is also idempotent.
#
#    All eigenvalues of A are either 0 or 1.
#
#    rank(A) = trace(A)
#
#    A is a projector matrix.
#
#    The matrix I - 2A is involutory, that is ( I - 2A ) * ( I - 2A ) = I.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Alston Householder, John Carpenter,
#    The singular values of involutory and of idempotent matrices,
#    Numerische Mathematik,
#    Volume 5, 1963, pages 234-237.
#
#  Parameters:
#
#    Input, integer N, the order of A.
#
#    Input, integer RANK, the rank of A.
#    0 <= RANK <= N.
#
#    Input, integer KEY, a positive value that selects the data.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np
  from orth_random import orth_random
  from sys import exit

  if ( rank < 0 or n < rank ):
    print ''
    print 'IDEM_RANDOM - Fatal error!'
    print '  RANK must be between 0 and N.'
    print '  Input value = %d' % ( rank )
    exit ( 'IDEM_RANDOM - Fatal error!' )
#
#  Get a random orthogonal matrix Q.
#
  q = orth_random ( n, key )
#
#  Compute Q' * D * Q, where D is the diagonal eigenvalue matrix
#  of RANK 1's followed by N-RANK 0's.
#
  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      t = 0.0
      for k in range ( 0, rank ):
        t = t + q[k,i] * q[k,j]
      a[i,j] =  t

  return a

def idem_random_determinant ( n, rank, key ):

#*****************************************************************************80
#
## IDEM_RANDOM_DETERMINANT returns the determinant of the IDEM_RANDOM matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, integer RANK, the rank.
#
#    Input, integer KEY, a positive value that selects the data.
#
#    Output, real VALUE, the determinant.
#
  if ( rank == n ):
    value = 1.0
  else:
    value = 0.0

  return value

def idem_random_determinant_test ( ):

#*****************************************************************************80
#
## IDEM_RANDOM_DETERMINANT_TEST tests IDEM_RANDOM_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#, 
#  Modified:
#
#    14 February 2015
#
#  Author:
#
#    John Burkardt
#
  from idem_random import idem_random
  from r8mat_print import r8mat_print
 
  print ''
  print 'IDEM_RANDOM_DETERMINANT_TEST'
  print '  IDEM_RANDOM_DETERMINANT computes the determinant of the IDEM_RANDOM matrix.'
  print ''

  n = 5
  i4_lo = 0
  i4_hi = n
  seed = 123456789

  rank, seed = i4_uniform_ab ( i4_lo, i4_hi, seed )

  print ''
  print '  Randomly chosen rank will be %d' % ( rank )

  key = 123456789
  a, seed = idem_random ( n, rank, key )

  m = n
  r8mat_print ( m, n, a, '  IDEM_RANDOM matrix:' )

  value = idem_random_determinant ( n, rank, key )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'IDEM_RANDOM_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def idem_random_eigen_right ( n, rank, key ):

#*****************************************************************************80
#
## IDEM_RANDOM_EIGEN_RIGHT returns the right eigenvectors of the IDEM_RANDOM matrix.
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
#    Alston Householder, John Carpenter,
#    The singular values of involutory and of idempotent matrices,
#    Numerische Mathematik,
#    Volume 5, 1963, pages 234-237.
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, integer RANK, the rank of A.
#    0 <= RANK <= N.
#
#    Input, integer KEY, a positive value that selects the data.
#
#    Output, real X(N,N), the matrix.
#
  import numpy as np
  from orth_random import orth_random

  x = orth_random ( n, key )

  x = np.transpose ( x )

  return x

def idem_random_eigenvalues ( n, rank, key ):

#*****************************************************************************80
#
## IDEM_RANDOM_EIGENVALUES returns the eigenvalues of the IDEM_RANDOM matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 October 2007
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of A.
#
#    Input, integer RANK, the rank of A.
#
#    Input, integer KEY, a positive value that selects the data.
#
#    Output, real LAM(N), the eigenvalues.
#
  import numpy as np

  lam = np.zeros ( n )

  for i in range ( 0, rank ):
    lam[i] = 1.0

  return lam

def idem_random_test ( ):

#*****************************************************************************80
#
## IDEM_RANDOM_TEST tests IDEM_RANDOM.
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
  import numpy as np

  n = 5
  i4_lo = 0
  i4_hi = n
  seed = 123456789

  print ''
  print 'IDEM_RANDOM_TEST'
  print '  IDEM_RANDOM computes a random idempotent matrix.'

  rank, seed = i4_uniform_ab ( i4_lo, i4_hi, seed )

  print ''
  print '  Randomly chosen rank will be %d' % ( rank )

  key = 123456789

  a = idem_random ( n, rank, key )

  m = n
  r8mat_print ( m, n, a, '  IDEM_RANDOM matrix:' )

  print ''
  print 'IDEM_RANDOM_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  idem_random_test ( )
  timestamp ( )

