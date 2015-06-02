#! /usr/bin/env python
#
def cheby_diff1 ( n ):

#*****************************************************************************80
#
## CHEBY_DIFF1 returns the CHEBY_DIFF1 matrix.
#
#  Discussion:
#
#    CHEBY_DIFF1 is the Chebyshev Differentiation matrix.
#
#  Example:
#
#    N = 6
#
#    8.5000 -10.4721   2.8944  -1.5279   1.1056  -0.5000
#    2.6180  -1.1708  -2.0000   0.8944  -0.6810   0.2764
#   -0.7236   2.0000  -0.1708   1.6180   0.8944  -0.3820
#    0.3820  -0.8944   1.6180   0.1708  -2.0000   0.7236
#   -0.2764   0.6180  -0.8944   2.0000   1.1708  -2.6180
#    0.5000  -1.1056   1.5279  -2.8944  10.4721  -8.5000
#
#  Properties:
#
#    A is antisymmetric.
#
#    If N is odd, then det ( A ) = 0.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Lloyd Trefethen,
#    Spectral Methods in MATLAB,
#    SIAM, 2000, page 54.
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

  if ( n == 1 ):
    a[0,0] = 1.0
    return a

  c = np.zeros ( n );
  c[0] = 2.0;
  for i in range ( 1, n - 1 ):
    c[i] = 1.0
  c[n-1] = 2.0
#
#  Get the Chebyshev points.
#
  x = np.zeros ( n + 1 )
  for i in range ( 0, n + 1 ):
    x[i] = np.cos ( r8_pi * float ( i ) / float ( n - 1 ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
 
      if ( i != j ):
        a[i,j] = ( -1.0 ) ** ( i + j ) * c[i] / ( c[j] * ( x[i] - x[j] ) )
      elif ( i == 0 ):
        a[i,i] = ( 2 * ( n - 1 ) ** 2 + 1 ) / 6.0
      elif ( i == n - 1 ):
        a[i,i] = - ( 2 * ( n - 1 ) ** 2 + 1 ) / 6.0
      else:
        a[i,i] = - 0.5 * x[i] / ( 1.0 - x[i] ** 2 )

  return a

def cheby_diff1_determinant ( n ):

#*****************************************************************************80
#
## CHEBY_DIFF1_DETERMINANT computes the determinant of the CHEBY_DIFF1 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 December 2014
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
  determ = 0.0

  return determ

def cheby_diff1_determinant_test ( ):

#*****************************************************************************80
#
## CHEBY_DIFF1_DETERMINANT_TEST tests CHEBY_DIFF1_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 December 2014
#
#  Author:
#
#    John Burkardt
#
  from cheby_diff1 import cheby_diff1
  from r8mat_print import r8mat_print

  print ''
  print 'CHEBY_DIFF1_DETERMINANT_TEST'
  print '  CHEBY_DIFF1_DETERMINANT computes the CHEBY_DIFF1 determinant.'

  m = 5
  n = 5
  a = cheby_diff1 ( n )
  r8mat_print ( n, n, a, '  CHEBY_DIFF1 matrix:' )

  value = cheby_diff1_determinant ( n )
  print '  Value =  %g' % ( value )

  print ''
  print 'CHEBY_DIFF1_DETERMINANT_TEST'
  print '  Normal end of execution.'

def cheby_diff1_null_left ( m, n ):

#*****************************************************************************80
#
## CHEBY_DIFF1_NULL_LEFT returns a left null vector for the CHEBY_DIFF1 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the order of the matrix.
#
#    Output, real X(M), the vector.
#
  import numpy as np

  if ( ( m % 2 ) == 1 ):

    x = np.zeros ( m )
    x[0] = 1.0
    t = -2.0
    for i in range ( 1, m - 1 ):
      x[i] = t
      t = -t
    x[m-1] = 1.0

  else:

    x = np.zeros ( m )

  return x

def cheby_diff1_null_right ( m, n ):

#*****************************************************************************80
#
## CHEBY_DIFF1_NULL_RIGHT returns a right null vector for the CHEBY_DIFF1 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the order of the matrix.
#
#    Output, real X(N), the vector.
#
  import numpy as np

  if ( n % 2 == 1 ):
    x = np.ones ( n )
  else:
    x = np.zeros ( n )

  return x

def cheby_diff1_test ( ):

#*****************************************************************************80
#
## CHEBY_DIFF1_TEST tests CHEBY_DIFF1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 December 2014
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'CHEBY_DIFF1_TEST'
  print '  CHEBY_DIFF1 computes the CHEBY_DIFF1 matrix.'

  m = 5
  n = 5
  a = cheby_diff1 ( n )
  r8mat_print ( m, n, a, '  CHEBY_DIFF1 matrix:' )

  print ''
  print 'CHEBY_DIFF1_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  cheby_diff1_test ( )
  cheby_diff1_determinant_test ( )
  timestamp ( )
