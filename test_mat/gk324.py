#! /usr/bin/env python
#
def gk324 ( m, n, x ):

#*****************************************************************************80
#
## GK324 returns the GK324 matrix.
#
#  Discussion:
#
#    This is Gregory and Karney example matrix 3.24.
#
#  Example:
#
#    M = N = 5
#
#    X = ( 11, 12, 13, 14 )
#
#     1  1  1  1  1
#    11  1  1  1  1
#    11 12  1  1  1
#    11 12 13  1  1
#    11 12 13 14  1
#
#  Properties:
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#   09 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Gregory, David Karney,
#    A Collection of Matrices for Testing Computational Algorithms,
#    Wiley, 1969, page 51, 
#    LC: QA263.G68.
#
#  Parameters:
#
#    Input, integer M, N, the order of the matrix.
#
#    Input, 
#    * real X(N-1), the first N-1 entries of the
#      last row, if M <= N, 
#    or 
#    * real X(N), the N entries of the last row,
#      if N < M.
#
#    Output, real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( m, n ) )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      if ( i <= j ):
        a[i,j] = 1.0
      else:
        a[i,j] = x[j]

  return a

def gk324_determinant ( n, x ):

#*****************************************************************************80
#
## GK324_DETERMINANT computes the determinant of the GK324 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, real X(N-1), the first N-1 entries of the last row.
#
#    Output, real VALUE, the determinant.
#
  value = 1.0

  for i in range ( 0, n - 1 ):
    value = value * ( 1.0 - x[i] )

  return value

def gk324_determinant_test ( ):

#*****************************************************************************80
#
## GK324_DETERMINANT_TEST tests GK324_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 February 2015
#
#  Author:
#
#    John Burkardt
#
  from gk324 import gk324
  from r8mat_print import r8mat_print
  from r8vec_uniform_ab import r8vec_uniform_ab

  print ''
  print 'GK324_DETERMINANT_TEST'
  print '  GK324_DETERMINANT computes the GK324 determinant.'

  m = 5
  n = m
 
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  if ( n < m ):
    x_n = n
  else:
    x_n = n - 1

  x, seed = r8vec_uniform_ab ( x_n, r8_lo, r8_hi, seed )

  a = gk324 ( m, n, x )

  r8mat_print ( m, n, a, '  GK324 matrix:' )

  value = gk324_determinant ( n, x )

  print '  Value =  %g' % ( value )

  print ''
  print 'GK324_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def gk324_inverse ( n, x ):

#*****************************************************************************80
#
## GK324_INVERSE returns the inverse of the GK324 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#   26 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Gregory, David Karney,
#    A Collection of Matrices for Testing Computational Algorithms,
#    Wiley, 1969, page 51, 
#    LC: QA263.G68.
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, real X(N-1), the first N-1 entries of the last row.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( i < n - 1 ):

        if ( j == i ):
          a[i,j] = 1.0 / ( 1.0 - x[i] )
        elif ( j == i + 1 ):
          a[i,j] = - 1.0 / ( 1.0 - x[i] )

      elif ( i == n - 1 ):

        if ( j == 0 ):

          a[i,j] = - x[0] / ( 1.0 - x[0] )

        elif ( j < n - 1 ):

          a[i,j] = ( x[j-1] - x[j] ) / ( 1.0 - x[j] ) / ( 1.0 - x[j-1] )

        elif ( j == n - 1 ):

          a[i,j] = 1.0 / ( 1.0 - x[n-2] )

  return a

def gk324_test ( ):

#*****************************************************************************80
#
## GK324_TEST tests GK324.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 February 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print
  from r8vec_uniform_ab import r8vec_uniform_ab

  print ''
  print 'GK324_TEST'
  print '  GK324 computes the GK324 matrix.'

  m = 5
  n = m

  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  if ( n < m ):
    x_n = n
  else:
    x_n = n - 1

  x, seed = r8vec_uniform_ab ( x_n, r8_lo, r8_hi, seed )

  a = gk324 ( m, n, x )
 
  r8mat_print ( m, n, a, '  GK324 matrix:' )

  print ''
  print 'GK324_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  gk324_test ( )
  timestamp ( )
