#! /usr/bin/env python
#
def kershawtri ( n, x ):

#*****************************************************************************80
#
## KERSHAWTRI returns the KERSHAWTRI matrix.
#
#  Discussion:
#
#    A(I,I) = X(I)     for I <= (N+1)/2
#    A(I,I) = X(N+1-I) for (N+1)/2 < I
#    A(I,J) = 1        for I = J + 1 or I = J - 1.
#    A(I,J) = 0        otherwise.
#
#  Example:
#
#    N = 5,
#    X = ( 10, 20, 30 )
#    A = 
#      10   1   0   0   0
#       1  20   1   0   0
#       0   1  30   1   0
#       0   0   1  20   1
#       0   0   0   1  10
#
#  Properties:
#
#    A is tridiagonal.
#
#    A is symmetric.
#
#    If the entries in X are integers, then det(A) is an integer.
#
#    If det(A) is an integer, then det(A) * inv(A) is an integer matrix.
#
#    A is persymmetric: A(I,J) = A(N+1-J,N+1-I).
#
#    A is centrosymmetric: A(I,J) = A(N+1-I,N+1-J).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    P Schlegel,
#    The Explicit Inverse of a Tridiagonal Matrix,
#    Mathematics of Computation,
#    Volume 24, Number 111, July 1970, page 665.
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, real X((N+1)/2), defines the diagonal of the matrix.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  nh = ( n // 2 )

  for i in range ( 0, nh ):
    a[i,i]         = x[i]
    a[n-1-i,n-1-i] = x[i]

  if ( ( n % 2 ) == 1 ):
    a[nh,nh] = x[nh]

  for i in range ( 0, n - 1 ):  
    a[i,i+1] = 1.0
    a[i+1,i] = 1.0

  return a

def kershawtri_determinant ( n, x ):

#*****************************************************************************80
#
## KERSHAWTRI_DETERMINANT computes the determinant of the KERSHAWTRI matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, real X((N+1)/2), defines the diagonal of the matrix.
#
#    Output, real VALUE, the determinant.
#
  import numpy as np

  nh = ( n // 2 )

  r = np.zeros ( n + 1 )

  r[0] = 1.0
  r[1] = - x[0]
  for i in range ( 3, n + 1 ):
    if ( i - 1 <= nh ):
      xim1 = x[i-2]
    else:
      xim1 = x[n+1-i]
    r[i-1] = - ( xim1 * r[i-2] + r[i-3] )

  value = x[0] * r[n-1] + r[n-2]
 
  return value

def kershawtri_determinant_test ( ):

#*****************************************************************************80
#
## KERSHAWTRI_DETERMINANT_TEST tests KERSHAWTRI_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 February 2015
#
#  Author:
#
#    John Burkardt
#
  from kershawtri import kershawtri
  from r8vec_uniform_ab import r8vec_uniform_ab
  from r8mat_print import r8mat_print

  print ''
  print 'KERSHAWTRI_DETERMINANT_TEST'
  print '  KERSHAWTRI_DETERMINANT computes the KERSHAWTRI determinant.'

  n = 5

  x_n = ( ( n + 1 ) // 2 )
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( x_n, r8_lo, r8_hi, seed )

  a = kershawtri ( n, x )
  m = n
  r8mat_print ( m, n, a, '  KERSHAWTRI matrix:' )

  value = kershawtri_determinant ( n, x )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'KERSHAWTRI_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def kershawtri_inverse ( n, x ):

#*****************************************************************************80
#
## KERSHAWTRI_INVERSE returns the inverse of the KERSHAWTRI matrix.
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
#    Input, integer N, the order of the matrix.
#
#    Input, real X((N+1)/2), defines the diagonal of the matrix.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  nh = ( n // 2 )

  r = np.zeros ( n + 1 )
 
  r[0] = 1.0
  r[1] = - x[0]
  for i in range ( 2, n ):
    if ( i <= nh ):
      xim1 = x[i-1]
    else:
      xim1 = x[n-i]
    r[i] = - ( xim1 * r[i-1] + r[i-2] )
  r[n] = x[0] * r[n-1] + r[n-2]

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, i ):
      a[i,j] = r[j] * r[n-1-i] / r[n]
    a[i,i] = r[i] * r[n-1-i] / r[n]
    for j in range ( i + 1, n ):
      a[i,j] = r[i] * r[n-1-j] / r[n]

  return a

def kershawtri_test ( ):

#*****************************************************************************80
#
## KERSHAWTRI_TEST tests KERSHAWTRI.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 February 2015
#
#  Author:
#
#    John Burkardt
#
  from r8vec_uniform_ab import r8vec_uniform_ab
  from r8mat_print import r8mat_print

  print ''
  print 'KERSHAWTRI_TEST'
  print '  KERSHAWTRI computes the KERSHAWTRI matrix.'

  n = 5
  x_n = ( ( n + 1 ) // 2 )
  x_lo = -5.0
  x_hi = +5.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( x_n, x_lo, x_hi, seed )

  a = kershawtri ( n, x )
  m = n
  r8mat_print ( m, n, a, '  KERSHAWTRI matrix:' )

  print ''
  print 'KERSHAWTRI_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  kershawtri_test ( )
  timestamp ( )
