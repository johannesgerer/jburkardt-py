#! /usr/bin/env python
#
def gfpp ( n, alpha ):

#*****************************************************************************80
#
## GFPP returns the GFPP matrix.
#
#  Discussion:
#
#    The GFPP matrix has maximal growth factor for Gauss elimination.
#
#  Formula:
#
#    if ( I = J or J = N )
#      A(I,J) = 1.0
#    elseif ( J < I )
#      A(I,J) = - abs ( ALPHA )
#    else
#      A(I,J) = 0
#
#  Example:
#
#    N = 5, ALPHA = 1
#
#    A =
#
#    1     0     0     0     1
#   -1     1     0     0     1
#   -1    -1     1     0     1
#   -1    -1    -1     1     1
#   -1    -1    -1    -1     1
#
#    P = Identity
#
#    L =
#
#    1     0     0     0     0
#   -1     1     0     0     0
#   -1    -1     1     0     0
#   -1    -1    -1     1     0
#   -1    -1    -1    -1     1
#
#    U =
#
#    1     0     0     0     1
#    0     1     0     0     2
#    0     0     1     0     4
#    0     0     0     1     8
#    0     0     0     0    16
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    If ALPHA is between 0 and 1, then Gaussian elimination with partial
#    pivoting yields a controllable growth factor of (1+ALPHA)^(N-1).
#    and a P factor which is the identity, an L factor equal to the lower
#    triangle of A, and an U factor which is equal to the identity matrix,
#    except that the last column is
#
#      [ 1, ALPHA+1, (ALPHA+1)^2, ...(ALPHA+1)^N-1 ].
#
#    If ALPHA is not between 0 and 1, then Gauss elimination WITHOUT
#    pivoting will yield the same pivot growth factor and PLU factorization
#    just described, but Gauss elimination with partial pivoting will not.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Nicholas Higham, Desmond Higham,
#    Large growth factors in Gaussian elimination with pivoting,
#    SIAM Journal on Matrix Analysis and Applications,
#    Volume 10, 1989, pages 155-164.
#
#    Lloyd Trefethen, David Bau,
#    Numerical Linear Algebra,
#    SIAM, 1997, pages 165-166.
#
#  Parameters:
#
#    Input, integer N, the order of A.
#
#    Input, real ALPHA, determines subdiagonal elements.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( i == j or j == n - 1 ):
        a[i,j] = 1.0
      elif ( j < i ):
        a[i,j] = - abs ( alpha )

  return a

def gfpp_condition ( n, alpha ):

#*****************************************************************************80
#
## GFPP_CONDITION returns the L1 condition of the GFPP matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, real ALPHA, determines subdiagonal elements.
#
#    Output, real VALUE, the L1 condition.
#
  a_norm = 1.0 + ( float ) ( n - 1 ) * abs ( alpha )
  b_norm = 1.0
  value = a_norm * b_norm

  return value

def gfpp_determinant ( n, alpha ):

#*****************************************************************************80
#
## GFPP_DETERMINANT returns the determinant of the GFPP matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, real ALPHA, determines subdiagonal elements.
#
#    Output, real VALUE, the determinant.
#
  value = ( 1.0 + abs ( alpha ) ) ** ( n - 1 )

  return value

def gfpp_determinant_test ( ):

#*****************************************************************************80
#
## GFPP_DETERMINANT_TEST tests GFPP_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 February 2015
#
#  Author:
#
#    John Burkardt
#
  from gfpp import gfpp
  from r8mat_print import r8mat_print
  from r8_uniform_ab import r8_uniform_ab

  print ''
  print 'GFPP_DETERMINANT_TEST'
  print '  GFPP_DETERMINANT computes the determinant of the GFPP matrix.'
  print ''

  m = 4
  n = m

  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )

  a = gfpp ( n, alpha )
  r8mat_print ( m, n, a, '  GFPP matrix:' )

  value = gfpp_determinant ( n, alpha )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'GFPP_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def gfpp_inverse ( n, alpha ):

#*****************************************************************************80
#
## GFPP_INVERSE returns the inverse of the GFPP matrix.
#
#  Example:
#
#    N = 5, ALPHA = 1
#
#    0.5000   -0.2500   -0.1250   -0.0625   -0.0625
#         0    0.5000   -0.2500   -0.1250   -0.1250
#         0         0    0.5000   -0.2500   -0.2500
#         0         0         0    0.5000   -0.5000
#    0.5000    0.2500    0.1250    0.0625    0.0625
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, real ALPHA, determines subdiagonal elements.
#
#    Output, real A(N,N), the inverse matrix.
#
  import numpy as np
  from r8mat_mm import r8mat_mm
  from tri_l1_inverse import tri_l1_inverse
  from tri_u_inverse import tri_u_inverse

  p, l, u = gfpp_plu ( n, alpha )
  
  p_inverse = np.transpose ( p )

  l_inverse = tri_l1_inverse ( n, l )

  u_inverse = tri_u_inverse ( n, u )

  lp_inverse = r8mat_mm ( n, n, n, l_inverse, p_inverse )

  a = r8mat_mm ( n, n, n, u_inverse, lp_inverse )
  
  return a

def gfpp_plu ( n, alpha ):

#*****************************************************************************80
#
## GFPP_PLU returns the PLU factorization of the GFPP matrix.
#
#  Discussion
#
#    This factorization assumes that Gaussian elimination is performed
#    without pivoting.  If ALPHA is not between 0 and 1, then the
#    PLU factors returned here will not be the PLU factors derived
#    from Gaussian elimination with pivoting.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, real ALPHA, determines subdiagonal elements.
#
#    Output, real P(N,N), L(N,N), U(N,N), the P, L, U factors
#    of the matrix.
#
  import numpy as np

  p = np.zeros ( ( n, n ) )
  for i in range ( 0, n ):
    p[i,i] = 1.0

  l = np.zeros ( ( n, n ) )
  for i in range ( 0, n ):
    for j in range ( 0, i ):
      l[i,j] = - abs ( alpha )
    l[i,i] = 1.0

  u = np.zeros ( ( n, n ) )
  for i in range ( 0, n ):
    u[i,i] = 1.0
  
  s = 1.0
  u[0,n-1] = s
  for i in range ( 1, n ):
    u[i,n-1] = 1.0 + abs ( alpha ) * s
    s = s + u[i,n-1]

  return p, l, u

def gfpp_test ( ):

#*****************************************************************************80
#
## GFPP_TEST tests GFPP.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 February 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print
  from r8_uniform_ab import r8_uniform_ab

  print ''
  print 'GFPP_TEST'
  print '  GFPP computes the GFPP matrix.'

  m = 4
  n = m

  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )

  a = gfpp ( n, alpha )
  r8mat_print ( m, n, a, '  GFPP matrix:' )

  print ''
  print 'GFPP_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  gfpp_test ( )
  timestamp ( )
