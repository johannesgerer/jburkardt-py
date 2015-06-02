#! /usr/bin/env python
#
def redheffer ( n ):

#*****************************************************************************80
#
## REDHEFFER returns the REDHEFFER matrix.
#
#  Formula:
#
#    if ( J = 1 or mod ( J, I ) == 0 )
#      A(I,J) = 1
#    else
#      A(I,J) = 0
#
#  Example:
#
#    N = 5
#
#     1  1  1  1  1
#     1  1  0  1  0
#     1  0  1  0  0
#     1  0  0  1  0
#     1  0  0  0  1
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is integral, therefore det ( A ) is integral, and 
#    det ( A ) * inverse ( A ) is integral.
#
#    The diagonal entries of A are all 1.
#
#    A is a zero/one matrix.
#
#    N - int ( log2 ( N ) ) - 1 eigenvalues are equal to 1.
#
#    There is a real eigenvalue of magnitude approximately sqrt ( N ),
#    which is the spectral radius of the matrix.
#
#    There is a negative eigenvalue of value approximately -sqrt ( N ).
#
#    The remaining eigenvalues are "small", and there is a conjecture
#    that they lie inside the unit circle in the complex plane.
#
#    The determinant is equal to the Mertens function M(N).
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Wayne Barrett, Tyler Jarvis,
#    Spectral Properties of a Matrix of Redheffer,
#    Linear Algebra and Applications,
#    Volume 162, 1992, pages 673-683.
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

      if ( j == 0 or ( ( j + 1 ) % ( i + 1 ) ) == 0 ):
        a[i,j] = 1.0

  return a

def redheffer_determinant ( n ):

#*****************************************************************************80
#
## REDHEFFER_DETERMINANT computes the determinant of the REDHEFFER matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 February 2015
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
  from mertens import mertens

  value = mertens ( n )

  return value

def redheffer_determinant_test ( ):

#*****************************************************************************80
#
## REDHEFFER_DETERMINANT_TEST tests REDHEFFER_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
  from redheffer import redheffer
  from r8mat_print import r8mat_print

  print ''
  print 'REDHEFFER_DETERMINANT_TEST'
  print '  REDHEFFER_DETERMINANT computes the REDHEFFER determinant.'

  m = 5
  n = m
 
  a = redheffer ( n )

  r8mat_print ( m, n, a, '  REDHEFFER matrix:' )

  value = redheffer_determinant ( n )

  print '  Value =  %g' % ( value )

  print ''
  print 'REDHEFFER_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def redheffer_test ( ):

#*****************************************************************************80
#
## REDHEFFER_TEST tests REDHEFFER.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'REDHEFFER_TEST'
  print '  REDHEFFER computes the REDHEFFER matrix.'

  m = 5
  n = m

  a = redheffer ( n )
 
  r8mat_print ( m, n, a, '  REDHEFFER matrix:' )

  print ''
  print 'REDHEFFER_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  redheffer_test ( )
  timestamp ( )
