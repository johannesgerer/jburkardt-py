#! /usr/bin/env python
#
def integration ( alpha, n ):

#*****************************************************************************80
#
## INTEGRATION returns the INTEGRATION matrix.
#
#  Formula:
#
#    if ( I = J )
#      A(I,J) = 1
#    else if ( J = I + 1 )
#      A(I,J) = ALPHA / I
#    else
#      A(I,J) = 0
#
#  Example:
#
#    ALPHA = 2, N = 5
#
#    1  2   0   0   0
#    0  1  2/2  0   0
#    0  0   1  2/3  0
#    0  0   0   1  2/4
#    0  0   0   0   1
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is unit upper triangular.
#
#    A is bidiagonal.
#
#    Because A is bidiagonal, it has property A (bipartite).
#
#    A is nonsingular.
#
#    det ( A ) = 1.
#
#    A is unimodular.
#
#    LAMBDA(1:N) = 1.
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real ALPHA, the scalar which defines the first 
#    superdiagonal of the matrix.
#
#    Input, integer N, the number of rows and columns of A.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for j in range ( 0, n ):
    for i in range ( 0, n ):

      if ( j == i ):
        a[i,j] = 1.0
      elif ( j == i + 1 ):
        a[i,j] = alpha / float ( i + 1 )

  return a

def integration_determinant ( alpha, n ):

#*****************************************************************************80
#
## INTEGRATION_DETERMINANT returns the determinant of the INTEGRATION matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real ALPHA, the scalar defining A.  
#    A common value is -1.
#
#    Input, integer N, the order of the matrix.  N must be even.
#
#    Output, real VALUE, the determinant.
#
  value = 1.0

  return value

def integration_determinant_test ( ):

#*****************************************************************************80
#
## INTEGRATION_DETERMINANT_TEST tests INTEGRATION_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 February 2015
#
#  Author:
#
#    John Burkardt
#
  from integration import integration
  from r8mat_print import r8mat_print
  from r8_uniform_ab import r8_uniform_ab

  print ''
  print 'INTEGRATION_DETERMINANT_TEST'
  print '  INTEGRATION_DETERMINANT computes the determinant of the INTEGRATION matrix.'
  print ''

  m = 4
  n = m

  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )

  a = integration ( alpha, n )
  r8mat_print ( m, n, a, '  INTEGRATION matrix:' )

  value = integration_determinant ( alpha, n )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'INTEGRATION_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def integration_inverse ( alpha, n ):

#*****************************************************************************80
#
## INTEGRATION_INVERSE returns the inverse of the INTEGRATION matrix.
#
#  Formula:
#
#    if ( I = J )
#      A(I,J) = 1
#    else if ( I < J )
#      A(I,J) = (-ALPHA)^(J-I) / (I*...*J-1)
#    else
#      A(I,J) = 0
#
#  Example:
#
#    ALPHA = 2, N = 5
#
#    1 -2   2  -4/3   2/3
#    0  1  -1   2/3  -1/3
#    0  0   1  -2/3   1/3
#    0  0   0    1   -1/2
#    0  0   0    0     1
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is unit upper triangular.
#
#    A is nonsingular.
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
#    Input, real ALPHA, the scalar which defines the first
#    superdiagonal of the matrix.
#
#    Input, integer N, the number of rows and columns of A.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np
  from r8_rise import r8_rise

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( j == i ):
        a[i,j] = 1.0
      elif ( i < j ):
        a[i,j] = ( - alpha ) ** ( j - i ) / r8_rise ( i + 1, j - i )

  return a

def integration_test ( ):

#*****************************************************************************80
#
## INTEGRATION_TEST tests INTEGRATION.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 February 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print
  from r8_uniform_ab import r8_uniform_ab

  print ''
  print 'INTEGRATION_TEST'
  print '  INTEGRATION computes the INTEGRATION matrix.'

  m = 6
  n = m

  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )

  a = integration ( alpha, n )
  r8mat_print ( m, n, a, '  INTEGRATION matrix:' )

  print ''
  print 'INTEGRATION_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  integration_test ( )
  timestamp ( )
