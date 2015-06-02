#! /usr/bin/env python
#
def aegerter ( n ):

#*****************************************************************************80
#
## AEGERTER returns the AEGERTER matrix.
#
#  Formula:
#
#    if ( I == N )
#      A(I,J) = J
#    else if ( J == N )
#      A(I,J) = I
#    else if ( I == J )
#      A(I,J) = 1
#    else
#      A(I,J) = 0
#
#  Example:
#
#    N = 5
#
#    1  0  0  0  1
#    0  1  0  0  2
#    0  0  1  0  3
#    0  0  0  1  4
#    1  2  3  4  5
#
#  Square Properties:
#
#    A is integral: int ( A ) = A.
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A is border-banded.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of rows and columns of A.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )
 
  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( i == n - 1 ):
        a[i,j] = j + 1
      elif ( j == n - 1 ):
        a[i,j] = i + 1
      elif ( i == j ):
        a[i,j] = 1.0
      else:
        a[i,j] = 0.0

  return a

def aegerter_condition ( n ):

#*****************************************************************************80
#
## AEGERTER_CONDITION returns the L1 condition of the AEGERTER matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Output, real COND, the L1 condition.
#
  from r8mat_norm_l1 import r8mat_norm_l1

  a = aegerter ( n )
  a_norm = r8mat_norm_l1 ( n, n, a )

  b = aegerter_inverse ( n )
  b_norm = r8mat_norm_l1 ( n, n, b )

  rcond = a_norm * b_norm

  return rcond

def aegerter_condition_test ( ):

#*****************************************************************************80
#
## AEGERTER_CONDITION_TEST tests AEGERTER_CONDITION.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 December 2014
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'AEGERTER_CONDITION_TEST'
  print '  AEGERTER_CONDITION computes the condition of the Aegerter matrix.'
  print ''
  print '    N     Cond(Aergerter(N))'
  print ''

  for n in range ( 1, 11 ):
    c = aegerter_condition ( n )
    print '  %4d  %8g' % ( n, c )

  print ''
  print 'AEGERTER_CONDITION_TEST'
  print '  Normal end of execution.'

  return

def aegerter_determinant ( n ):

#*****************************************************************************80
#
## AEGERTER_DETERMINANT returns the determinant of the AEGERTER matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 October 2007
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of rows and columns of A.
#
#    Output, real DETERM, the determinant.
#
  determ = ( n - ( ( n - 1 ) * n * ( 2 * n - 1 ) ) / 6 );

  return determ

def aegerter_determinant_test ( ):

#*****************************************************************************80
#
## AEGERTER_DETERMINANT_TEST tests AEGERTER_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 December 2014
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'AEGERTER_DETERMINANT_TEST'
  print '  AEGERTER_DETERMINANT computes the Aegerter determinant.'

  for n in range ( 1, 11 ):
    d = aegerter_determinant ( n )
    print '  %4d  %8g' % ( n, d )

  print ''
  print 'AEGERTER_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def aegerter_eigenvalues ( n ):

#*****************************************************************************80
#
## AEGERTER_EIGENVALUES returns the eigenvalues of the AEGERTER matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of rows and columns of A.
#
#    Output, real LAM(N), the eigenvalues.
#
  import numpy as np
  from math import sqrt

  lam = np.zeros ( n )

  determ = n - ( ( n - 1 ) * n * ( 2 * n - 1 ) ) / 6

  lam[0] = 0.5 * ( n + 1 - sqrt ( ( n + 1 ) ** 2 - 4.0 * determ ) )

  for i in range ( 1, n - 1 ):
    lam[i] = 1.0

  lam[n-1] = 0.5 * ( n + 1 + sqrt ( ( n + 1 ) ** 2 - 4.0 * determ ) )

  return lam

def aegerter_eigenvalues_test ( ):

#*****************************************************************************80
#
## AEGERTER_EIGENVALUES_TEST tests AEGERTER_EIGENVALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 December 2014
#
#  Author:
#
#    John Burkardt
#
  from r8vec_print import r8vec_print

  print ''
  print 'AEGERTER_EIGENVALUES_TEST'
  print '  AEGERTER_EIGENVALUES computes the eigenvalues of the Aegerter matrix.'

  n = 5
  lam = aegerter_eigenvalues ( n )
  r8vec_print ( n, lam, '  Aergerter eigenvalues:' )

  print ''
  print 'AEGERTER_EIGENVALUES_TEST'
  print '  Normal end of execution.'

  return

def aegerter_inverse ( n ):

#*****************************************************************************80
#
## AEGERTER_INVERSE returns the inverse of the AEGERTER matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of rows and columns of A.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  v = np.zeros ( n )

  for i in range ( 0, n - 1 ):
    v[i] = i + 1

  for j in range ( 0, n - 1 ):
    a[j,j] = 1.0
    for i in range ( 0, n - 1 ):
      a[i,j] = a[i,j] - v[i] * v[j] / ( n * n )

  for i in range ( 0, n - 1 ):
    a[i,n-1] = v[i] / ( n * n )

  for j in range ( 0, n - 1 ):
    a[n-1,j] = v[j] / ( n * n )

  a[n-1,n-1] = - 1.0 / ( n * n )

  return a

def aegerter_inverse_test ( ):

#*****************************************************************************80
#
## AEGERTER_INVERSE_TEST tests AEGERTER_INVERSE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 December 2014
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'AEGERTER_INVERSE_TEST'
  print '  AEGERTER_INVERSE computes the inverse of the Aegerter matrix.'

  n = 5
  b = aegerter_inverse ( n )
  r8mat_print ( n, n, b, '  Aergerter inverse:' )

  print ''
  print 'AEGERTER_INVERSE_TEST'
  print '  Normal end of execution.'

  return

def aegerter_test ( ):

#*****************************************************************************80
#
## AEGERTER_TEST tests AEGERTER.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 December 2014
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'AEGERTER_TEST'
  print '  AEGERTER computes the Aegerter matrix.'

  n = 5
  b = aegerter ( n )
  r8mat_print ( n, n, b, '  Aergerter matrix:' )

  print ''
  print 'AEGERTER_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  aegerter_test ( )
  timestamp ( )
