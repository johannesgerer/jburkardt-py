#! /usr/bin/env python
#
def fibonacci2 ( n ):

#*****************************************************************************80
#
## FIBONACCI2 returns the FIBONACCI2 matrix.
#
#  Example:
#
#    N = 5
#
#    0 1 0 0 0
#    1 1 0 0 0
#    0 1 1 0 0
#    0 0 1 1 0
#    0 0 0 1 1
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is tridiagonal.
#
#    Because A is tridiagonal, it has property A (bipartite).
#
#    A is banded, with bandwidth 3.
#
#    A is integral: int ( A ) = A.
#
#    A is a zero/one matrix.
#
#    If N = 1 then
#      det ( A ) = 0
#    else
#      det ( A ) = (-1)^(N-1)
#
#    If 1 < N, then A is unimodular.
#
#    For 2 <= N, A has the eigenvalues:
#
#      PHI   (once),
#      1     (N-2) times,
#      1-PHI (once).
#
#    When applied to a Fibonacci1 matrix B, the Fibonacci2 matrix
#    A produces the "next" Fibonacci1 matrix C = A*B.
#
#    Let PHI be the golden ratio (1+sqrt(5))/2.
#
#    For 2 <= N, the eigenvalues and eigenvectors are:
#
#    LAMBDA(1)     = PHI,     vector = (1,PHI,PHI^2,...PHI^(N-1));
#    LAMBDA(2:N-1) = 1        vector = (0,0,0,...,0,1);
#    LAMBDA(N)     = 1 - PHI. vector = ((-PHI)^(N-1),(-PHI)^(N-2),...,1)
#
#    Note that there is only one eigenvector corresponding to 1.
#    Hence, for 3 < N, the matrix is defective.  This fact means, 
#    for instance, that the convergence of the eigenvector in the power 
#    method will be very slow.
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 January 2015
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

  a = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( i == 0 ):

        if ( j == 1 ):
          a[i,j] = 1.0;

      else:

        if ( j == i - 1 or j == i ):
          a[i,j] = 1.0

  return a

def fibonacci2_condition ( n ):

#*****************************************************************************80
#
## FIBONACCI2_CONDITION returns the L1 condition of the FIBONACCI2 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Output, real VALUE, the L1 condition.
#
  from sys import exit

  if ( n == 1 ):
    print ''
    print 'FIBONACCI2_CONDITION - Fatal error!'
    print '  The condition number is infinite for N=1'
    exit ( 'FIBONACCI2_CONDITION - Fatal error!' )

  if ( n == 1 ):
    a_norm = 0.0
  elif ( n == 2 ):
    a_norm = 2.0
  else:
    a_norm = 3.0
  b_norm = float ( n )
  value = a_norm * b_norm;

  return value

def fibonacci2_determinant ( n ):

#*****************************************************************************80
#
## FIBONACCI2_DETERMINANT returns the determinant of the FIBONACCI2 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 January 2015
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
  if ( n == 1 ):
    determ = 0.0
  else:
    determ = -1.0

  return determ

def fibonacci2_determinant_test ( ):

#*****************************************************************************80
#
## FIBONACCI2_DETERMINANT_TEST tests FIBONACCI2_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 January 2015
#
#  Author:
#
#    John Burkardt
#
  from fibonacci2 import fibonacci2
  from r8mat_print import r8mat_print

  print ''
  print 'FIBONACCI2_DETERMINANT_TEST'
  print '  FIBONACCI2_DETERMINANT computes the determinant of the FIBONACCI2 matrix.'
  print ''

  m = 5
  n = m

  a = fibonacci2 ( n )
  r8mat_print ( m, n, a, '  FIBONACCI2 matrix:' )

  value = fibonacci2_determinant ( n )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'FIBONACCI2_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def fibonacci2_inverse ( n ):

#*****************************************************************************80
#
## FIBONACCI2_INVERSE returns the inverse of the FIBONACCI2 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 March 2015
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
  from sys import exit

  a = np.zeros ( ( n, n ) )

  if ( n == 1 ):
    print ''
    print 'FIBONACCI2_INVERSE - Fatal error!'
    print '  The inverse does not exist for N = 1.'
    exit ( 'FIBONACCI2_INVERSE - Fatal error!' )
#
#  Column 1.
#
  j = 0
  s = -1.0
  for i in range ( 0, n ):
    a[i,j] = s
    s = -s
#
#  Column 2
#
  j = 1
  a[0,j] = 1.0
#
#  Columns 3:N
#
  for j in range ( 2, n ):
    s = 1.0
    for i in range ( j, n ):
      a[i,j] = s
      s = -s

  return a

def fibonacci2_test ( ):

#*****************************************************************************80
#
## FIBONACCI2_TEST tests FIBONACCI2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 January 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'FIBONACCI2_TEST'
  print '  FIBONACCI2 computes the FIBONACCI2 matrix.'

  m = 5
  n = m

  a = fibonacci2 ( n )
  r8mat_print ( m, n, a, '  FIBONACCI2 matrix:' )

  print ''
  print 'FIBONACCI2_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  fibonacci2_test ( )
  timestamp ( )
