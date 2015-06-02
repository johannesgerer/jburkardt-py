#! /usr/bin/env python
#
def orth_symm ( n ):

#*****************************************************************************80
#
## ORTH_SYMM returns an orthogonal symmetric matrix.
#
#  Formula:
#
#    A(I,J) = sqrt ( 2 ) * sin ( I * J * pi / ( N + 1 ) ) / sqrt ( N + 1 )
#
#  Example:
#
#    N = 5
#
#    0.326019   0.548529   0.596885   0.455734   0.169891
#    0.548529   0.455734  -0.169891  -0.596885  -0.326019
#    0.596885  -0.169891  -0.548529   0.326019   0.455734
#    0.455734  -0.596885   0.326019   0.169891  -0.548528
#    0.169891  -0.326019   0.455734  -0.548528   0.596885
#
#  Properties:
#
#    A is orthogonal: A' * A = A * A' = I.
#
#    A is symmetric: A' = A.
#
#    A is not positive definite (unless N = 1 ).
#
#    Because A is symmetric, it is normal.
#
#    Because A is symmetric, its eigenvalues are real.
#
#    Because A is orthogonal, its eigenvalues have unit norm.
#
#    Only +1 and -1 can be eigenvalues of A.
#
#    Because A is normal, it is diagonalizable.
#
#    A is involutional: A * A = I.
#
#    If N is even, trace ( A ) = 0; if N is odd, trace ( A ) = 1.
#
#    LAMBDA(1:(N+1)/2) = 1; LAMBDA((N+1)/2+1:N) = -1.
#
#    A is the left and right eigenvector matrix for the
#    second difference matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 October 2007
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Morris Newman, John Todd,
#    The evaluation of matrix inversion programs,
#    Journal of the Society for Industrial and Applied Mathematics,
#    Volume 6, Number 4, pages 466-476, 1958.
#
#  Parameters:
#
#    Input, integer N, the order of A.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  r8_pi = 3.141592653589793

  a = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      angle = 2.0 * float ( i + 1 ) * float ( j + 1 ) * r8_pi / float ( 2 * n + 1 )
      a[i,j] = 2.0 * np.sin ( angle ) / np.sqrt ( float ( 2 * n + 1 ) )

  return a

def orth_symm_condition ( n ):

#*****************************************************************************80
#
## ORTH_SYMM_CONDITION returns the L1 condition of the ORTH_SYMM matrix.
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
#    Output, real VALUE, the L1 condition.
#
  import numpy as np

  r8_pi = 3.141592653589793

  a_norm = 0.0
  j = 0
  for i in range ( 0, n ): 
    angle = 2.0 * float ( i + 1 ) * float ( j + 1 ) * r8_pi / float ( 2 * n + 1 )
    a_norm = a_norm + 2.0 * abs ( np.sin ( angle ) ) / np.sqrt ( 2 * n + 1 )
  b_norm = a_norm
  value = a_norm * b_norm

  return value

def orth_symm_condition_test ( ):

#*****************************************************************************80
#
## ORTH_SYMM_CONDITION_TEST tests ORTH_SYMM_CONDITION.
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
  from orth_symm import orth_symm
  from r8mat_print import r8mat_print

  print ''
  print 'ORTH_SYMM_CONDITION_TEST'
  print '  ORTH_SYMM_CONDITION computes the condition of the ORTH_SYMM matrix.'
  print ''

  n = 4
  a = orth_symm ( n )
  r8mat_print ( n, n, a, '  ORTH_SYMM matrix:' )

  value = orth_symm_condition ( n )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'ORTH_SYMM_CONDITION_TEST'
  print '  Normal end of execution.'

  return

def orth_symm_determinant ( n ):

#*****************************************************************************80
#
## ORTH_SYMM_DETERMINANT returns the determinant of the ORTH_SYMM matrix.
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
#    Output, real VALUE, the determinant.
#
  value = 1.0

  return value

def orth_symm_determinant_test ( ):

#*****************************************************************************80
#
## ORTH_SYMM_DETERMINANT_TEST tests ORTH_SYMM_DETERMINANT.
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
  from orth_symm import orth_symm
  from r8mat_print import r8mat_print

  print ''
  print 'ORTH_SYMM_DETERMINANT_TEST'
  print '  ORTH_SYMM_DETERMINANT computes the determinant of the ORTH_SYMM matrix.'
  print ''

  n = 4
  a = orth_symm ( n )
  r8mat_print ( n, n, a, '  ORTH_SYMM matrix:' )

  value = orth_symm_determinant ( n )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'ORTH_SYMM_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def orth_symm_inverse ( n ):

#*****************************************************************************80
#
## ORTH_SYMM_INVERSE returns the inverse of the ORTH_SYMM matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 March 2015
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
  from orth_symm import orth_symm

  a = orth_symm ( n )

  return a

def orth_symm_test ( ):

#*****************************************************************************80
#
## ORTH_SYMM_TEST tests ORTH_SYMM.
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
  from r8mat_print import r8mat_print

  print ''
  print 'ORTH_SYMM_TEST'
  print '  ORTH_SYMM computes the ORTH_SYMM matrix.'

  m = 5
  n = 5
  a = orth_symm ( n )
  r8mat_print ( m, n, a, '  ORTH_SYMM matrix:' )

  print ''
  print 'ORTH_SYMM_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  orth_symm_test ( )
  timestamp ( )
