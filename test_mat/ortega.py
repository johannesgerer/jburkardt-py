#! /usr/bin/env python
#
def ortega ( n, u, v, d ):

#*****************************************************************************80
#
## ORTEGA returns the ORTEGA matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    James Ortega,
#    Generation of Test Matrices by Similarity Transformations,
#    Communications of the ACM,
#    Volume 7, 1964, pages 377-378.
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#    2 <= N.
#
#    Input, real U(N), V(N), vectors which define the matrix.
#    U'V must not equal -1.0.  If, in fact, U'V = 0, and U, V and D are
#    integers, then the matrix, inverse, eigenvalues, and eigenvectors 
#    will be integers.
#
#    Input, real D(N), the desired eigenvalues.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np
  
  vtu = np.dot ( v, u )

  beta = 1.0 / ( 1.0 + vtu )

  a = np.zeros ( ( n, n ) )

  for j in range ( 0, n ):
    for i in range ( 0, n ):
      for k in range ( 0, n ):

        if ( i == k ):
          bik = 1.0 + u[i] * v[k]
        else:
          bik =       u[i] * v[k]

        if ( k == j ):
          ckj = 1.0 - beta * u[k] * v[j]
        else:
          ckj =     - beta * u[k] * v[j]

        a[i,j] = a[i,j] + bik * d[k] * ckj
 
  return a

def ortega_determinant ( n, u, v, d ):

#*****************************************************************************80
#
## ORTEGA_DETERMINANT returns the determinant of the ORTEGA matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, real U(N), V(N), vectors which define the matrix.
#    U'V must not equal -1.0.  If, in fact, U'V = 0, and U, V and D are
#    integers, then the matrix, inverse, eigenvalues, and eigenvectors 
#    will be integers.
#
#    Input, real D(N), the desired eigenvalues
#
#    Output, real VALUE, the determinant.
#
  import numpy as  np

  value = np.prod ( d )

  return value

def ortega_determinant_test ( ):

#*****************************************************************************80
#
## ORTEGA_DETERMINANT_TEST tests ORTEGA_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 February 2015
#
#  Author:
#
#    John Burkardt
#
  from ortega import ortega
  from r8mat_print import r8mat_print
  from r8vec_uniform_ab import r8vec_uniform_ab
 
  print ''
  print 'ORTEGA_DETERMINANT_TEST'
  print '  ORTEGA_DETERMINANT computes the determinant of the ORTEGA matrix.'
  print ''

  m = 5
  n = m
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  v1, seed = r8vec_uniform_ab ( n, r8_lo, r8_hi, seed )
  v2, seed = r8vec_uniform_ab ( n, r8_lo, r8_hi, seed )
  v3, seed = r8vec_uniform_ab ( n, r8_lo, r8_hi, seed )

  a = ortega ( n, v1, v2, v3 )

  r8mat_print ( m, n, a, '  ORTEGA matrix:' )

  value = ortega_determinant ( n )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'ORTEGA_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def ortega_eigen_right ( n, u, v, d ):

#*****************************************************************************80
#
## ORTEGA_EIGEN_RIGHT returns the right eigenvectors of the ORTEGA matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    James Ortega,
#    Generation of Test Matrices by Similarity Transformations,
#    Communications of the ACM,
#    Volume 7, 1964, pages 377-378.
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#    2 <= N.
#
#    Input, real U(N), V(N), vectors which define the matrix.
#    U'V must not equal -1.0.  If, in fact, U'V = 0, and U, V and D are
#    integers, then the matrix, inverse, eigenvalues, and eigenvectors 
#    will be integers.
#
#    Input, real D(N), the desired eigenvalues.
#
#    Output, real X(N,N), the determinant.
#
  import numpy as np

  x = np.zeros ( ( n, n ) )
 
  for j in range ( 0, n ):
    for i in range ( 0, n ):

      if ( i == j ):
        x[i,j] = 1.0 + u[i] * v[j]
      else:
        x[i,j] =       u[i] * v[j]

  return x

def ortega_eigenvalues ( n, u, v, d ):

#*****************************************************************************80
#
## ORTEGA_EIGENVALUES returns the eigenvalues of the ORTEGA matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    James Ortega,
#    Generation of Test Matrices by Similarity Transformations,
#    Communications of the ACM,
#    Volume 7, 1964, pages 377-378.
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#    2 <= N.
#
#    Input, real U(N), V(N), vectors which define the matrix.
#    U'V must not equal -1.0.  If, in fact, U'V = 0, and U, V and D are
#    integers, then the matrix, inverse, eigenvalues, and eigenvectors 
#    will be integers.
#
#    Input, real D(N), the desired eigenvalues.
#
#    Output, real LAM(N), the determinant.
#
  import numpy as np

  lam = np.copy ( d )

  return lam

def ortega_inverse ( n, u, v, d ):

#*****************************************************************************80
#
## ORTEGA_INVERSE returns the inverse of the ORTEGA matrix.
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
#  Reference:
#
#    James Ortega,
#    Generation of Test Matrices by Similarity Transformations,
#    Communications of the ACM,
#    Volume 7, 1964, pages 377-378.
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#    2 <= N.
#
#    Input, real U(N), V(N), vectors which define the matrix.
#    U'V must not equal -1.0.  If, in fact, U'V = 0, and U, V and D are
#    integers, then the matrix, inverse, eigenvalues, and eigenvectors 
#    will be integers.
#
#    Input, real D(N), the desired eigenvalues.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  vtu = 0.0
  for i in range ( 0, n):
    vtu = vtu + v[i] * u[i]

  beta = 1.0 / ( 1.0 + vtu )

  for j in range ( 0, n ):
    for i in range ( 0, n ):
      for k in range ( 0, n ):

        if ( i == k ):
          bik = 1.0 + u[i] * v[k]
        else:
          bik =     + u[i] * v[k]

        if ( k == j ):
          ckj = 1.0 - beta * u[k] * v[j]
        else:
          ckj =     - beta * u[k] * v[j]

        a[i,j] = a[i,j] + ( bik / d[k] ) * ckj

  return a

def ortega_test ( ):

#*****************************************************************************80
#
## ORTEGA_TEST tests ORTEGA.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 February 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print
  from r8vec_uniform_ab import r8vec_uniform_ab

  print ''
  print 'ORTEGA_TEST'
  print '  ORTEGA computes the ORTEGA matrix.'

  m = 5
  n = m
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  v1, seed = r8vec_uniform_ab ( n, r8_lo, r8_hi, seed )
  v2, seed = r8vec_uniform_ab ( n, r8_lo, r8_hi, seed )
  v3, seed = r8vec_uniform_ab ( n, r8_lo, r8_hi, seed )

  a = ortega ( n, v1, v2, v3 )

  r8mat_print ( m, n, a, '  ORTEGA matrix:' )

  print ''
  print 'ORTEGA_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  ortega_test ( )
  timestamp ( )
