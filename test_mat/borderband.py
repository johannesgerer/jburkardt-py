#! /usr/bin/env python
#
def borderband ( n ):

#*****************************************************************************80
#
## BORDERBAND returns the BORDERBAND matrix.
#
#  Formula:
#
#    If ( I = J )
#      A(I,I) = 1
#    else if ( I = N )
#      A(N,J) = 2^(1-J)
#    else if ( J = N )
#      A(I,N) = 2^(1-I)
#    else
#      A(I,J) = 0
#
#  Example:
#
#    N = 5
#
#     1  0   0   0   1
#     0  1   0   0  1/2
#     0  0   1   0  1/4
#     0  0   0   1  1/8
#     1 1/2 1/4 1/8  1
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#    A is border-banded.
#
#    A has N-2 eigenvalues of 1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 December 2014
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

      if ( i == j ):
        a[i,j] = 1.0
      elif ( j == n - 1 ):
        a[i,j] = 1.0 / ( 2 ** i )
      elif ( i == n - 1 ):
        a[i,j] = 1.0 / ( 2 ** j )
      else:
        a[i,j] = 0.0

  return a

def borderband_determinant ( n ):

#*****************************************************************************80
#
## BORDERBAND_DETERMINANT computes the determinant of the BORDERBAND matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 December 2014
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
  for i in range ( 1, n ):
    determ = determ - 2 ** ( 2 - 2 * i )
  determ = determ + 1

  return determ

def borderband_determinant_test ( ):

#*****************************************************************************80
#
## BORDERBAND_DETERMINANT_TEST tests BORDERBAND_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 December 2014
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'BORDERBAND_DETERMINANT_TEST'
  print '  BORDERBAND_DETERMINANT computes the BORDERBAND determinant.'

  m = 5
  n = m
  a = borderband ( n )
  r8mat_print ( m, n, a, '  BORDERBAND matrix:' )

  value = borderband_determinant ( n )
  print '  Value =  %g' % ( value )

  print ''
  print 'BORDERBAND_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def borderband_inverse ( n ):

#*****************************************************************************80
#
## BORDERBAND_INVERSE returns the inverse of the BORDERBAND matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Output, real A(N,N), the inverse matrix.
#
  import numpy as np
  from r8mat_mm import r8mat_mm
  from tri_l1_inverse import tri_l1_inverse
  from tri_u_inverse import tri_u_inverse

  p, l, u = borderband_plu ( n )

  p_inverse = np.transpose ( p )

  l_inverse = tri_l1_inverse ( n, l )

  u_inverse = tri_u_inverse ( n, u )

  lipi = r8mat_mm ( n, n, n, l_inverse, p_inverse )
  
  a = r8mat_mm ( n, n, n, u_inverse, lipi )

  return a

def borderband_plu ( n ):

#*****************************************************************************80
#
## BORDERBAND_PLU returns the PLU factors of the BORDERBAND matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 June 2011
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Output, real P(N,N), L(N,N), U(N,N), the PLU factors.
#
  import numpy as np

  p = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    p[i,i] = 1.0

  l = np.zeros ( ( n, n ) )

  for j in range ( 0, n ):
    for i in range ( 0, n ):
      if ( i == j ):
        l[i,j] = 1.0
      elif ( i == n - 1 ):
        l[i,j] = 1.0 / 2.0 ** j

  u = np.zeros ( ( n, n ) )

  for j in range ( 0, n ):
    for i in range ( 0, n ):
      if ( i == n - 1 and j == n - 1 ):
        u[i,j] = 0.0
        for k in range ( 2, n ):
          u[i,j] = u[i,j] - 2.0 ** ( 2 - 2 * k )
      elif ( i == j ):
        u[i,j] = 1.0
      elif ( j == n - 1 ):
        u[i,j] = 1.0 / 2.0 ** i

  return p, l, u

def borderband_test ( ):

#*****************************************************************************80
#
## BORDERBAND_TEST tests BORDERBAND.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 December 2014
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'BORDERBAND_TEST'
  print '  BORDERBAND computes the BORDERBAND matrix.'

  m = 5
  n = m
  a = borderband ( n )
  r8mat_print ( m, n, a, '  BORDERBAND matrix:' )

  print ''
  print 'BORDERBAND_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  borderband_test ( )
  timestamp ( )
