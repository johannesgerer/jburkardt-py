#! /usr/bin/env python
#
def forsythe ( alpha, beta, n ):

#*****************************************************************************80
#
## FORSYTHE returns the FORSYTHE matrix.
#
#  Discussion:
#
#    The Forsythe matrix represents a Jordan canonical matrix, perturbed
#    by a rank one update.
#
#  Formula:
#
#    If ( I = J )
#      A(I,J) = BETA
#    else if ( J = I+1 )
#      A(I,J) = 1
#    else if ( I = N and J = 1 ) then
#      A(I,J) = ALPHA
#    else
#      A(I,J) = 0
#
#  Example:
#
#    ALPHA = 2, BETA = 3, N = 5
#
#    3 1 0 0 0
#    0 3 1 0 0
#    0 0 3 1 0
#    0 0 0 3 1
#    2 0 0 0 3
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is Toeplitz: constant along diagonals.
#
#    A is persymmetric: A(I,J) = A(N+1-J,N+1-I).
#
#    The characteristic equation of A is
#
#      ( BETA - LAMBDA )^N - (-1)^N*ALPHA = 0
#
#    The eigenvalues of A are
#
#      LAMBDA(I) = BETA
#        + abs ( ALPHA )^1/N * exp ( 2 * I * PI * sqrt ( - 1 ) / N )
#
#    Gregory and Karney consider the special case where BETA is 0,
#    and ALPHA is a "small" value.  In that case, the characteristic
#    equation is LAMBDA^N - ALPHA = 0, and the eigenvalues are the
#    N-th root of ALPHA times the N roots of unity.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 October 2007
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Gregory, David Karney,
#    Example 5.22,
#    A Collection of Matrices for Testing Computational Algorithms,
#    Wiley, New York, 1969, page 103, 
#    LC: QA263.G68.
#
#  Parameters:
#
#    Input, real ALPHA, BETA, define the matrix.  A typical 
#    value of ALPHA is the square root of the machine precision; a typical
#    value of BETA is 0.0.
#
#    Input, integer N, the order of A.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( j == i ):
        a[i,j] = beta
      elif ( j == i + 1 ):
        a[i,j] = 1.0
      elif ( i == n - 1 and j == 0 ):
        a[i,j] = alpha

  return a

def forsythe_determinant ( alpha, beta, n ):

#*****************************************************************************80
#
## FORSYTHE_DETERMINANT computes the determinant of the FORSYTHE matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real ALPHA, BETA, parameters that define the matrix.
#
#    Input, integer N, the order of the matrix.
#
#    Output, real VALUE, the determinant.
#
  from r8_mop import r8_mop

  value = r8_mop ( n - 1 ) * alpha + beta ** n

  return value

def forsythe_determinant_test ( ):

#*****************************************************************************80
#
## FORSYTHE_DETERMINANT_TEST tests FORSYTHE_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 February 2015
#
#  Author:
#
#    John Burkardt
#
  from forsythe import forsythe
  from r8_uniform_ab import r8_uniform_ab
  from r8mat_print import r8mat_print

  print ''
  print 'FORSYTHE_DETERMINANT_TEST'
  print '  FORSYTHE_DETERMINANT computes the FORSYTHE determinant.'

  seed = 123456789

  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  beta, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  a = forsythe ( alpha, beta,  n )
  r8mat_print ( n, n, a, '  FORSYTHE matrix:' )

  value = forsythe_determinant ( alpha, beta, n )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'FORSYTHE_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def forsythe_inverse ( alpha, beta, n ):

#*****************************************************************************80
#
## FORSYTHE_INVERSE returns the inverse of the Forsythe matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Gregory, David Karney,
#    A Collection of Matrices for Testing Computational Algorithms,
#    Wiley, 1969,
#    ISBN: 0882756494,
#    LC: QA263.G68.
#
#  Parameters:
#
#    Input, real ALPHA, BETA, define the matrix.  
#    The Forsythe matrix does not have an inverse if both ALPHA and BETA are zero.
#
#    Input, integer N, the order of A.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np
 
  a = np.zeros ( ( n, n ) )

  if ( beta == 0.0 and alpha == 0.0 ):

    fprintf ( 1, '\n' );
    fprintf ( 1, 'FORSYTHE_INVERSE - Fatal error!\n' );
    fprintf ( 1, '  The Forsythe matrix is not invertible if\n' );
    fprintf ( 1, '  both ALPHA and BETA are 0.\n' );
    error ( 'FORSYTHE_INVERSE - Fatal error!' );

  elif ( beta == 0.0 ):

    for j in range ( 0, n ):
      for i in range ( 0, n ):
 
        if ( j == n - 1 ):
          a[i,j] = 1.0 / alpha
        elif ( j == i - 1 ):
          a[i,j] = 1.0
#
#  Set up the original Jordan matrix as B.
#
  else:
#
#  Compute inverse of unperturbed Jordan matrix.
#
    for j in range ( 0, n ):
      for i in range ( 0, n ):

        if ( i <= j ):
          a[i,j] =  - ( - 1.0 / beta ) ** ( j + 1 - i )
#
#  Add rank one perturbation.
#
    z = - 1.0 / beta

    for j in range ( 0, n ):
      for i in range ( 0, n ):
        a[i,j] = a[i,j] - alpha * z ** ( n + 1 + j - i ) \
                / ( 1.0 - alpha * z ** n )

  return a

def forsythe_test ( ):

#*****************************************************************************80
#
## FORSYTHE_TEST tests FORSYTHE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 February 2015
#
#  Author:
#
#    John Burkardt
#
  from r8_uniform_ab import r8_uniform_ab
  from r8mat_print import r8mat_print

  print ''
  print 'FORSYTHE_TEST'
  print '  FORSYTHE computes the FORSYTHE matrix.'

  seed = 123456789

  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  beta, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  a = forsythe ( alpha, beta, n )
  r8mat_print ( n, n, a, '  FORSYTHE matrix:' )

  print ''
  print 'FORSYTHE_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  forsythe_test ( )
  timestamp ( )
