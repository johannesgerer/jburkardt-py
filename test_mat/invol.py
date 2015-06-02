#! /usr/bin/env python
#
def invol ( n ):

#*****************************************************************************80
#
## INVOL returns the INVOL matrix.
#
#  Formula:
#
#    A(I,J) = 1 / ( I + J - 1 )
#
#    Set D = -N
#
#    Multiply column 1 of A by D.
#
#    For I = 1 to N-1
#      D = -(N+I)*(N-I)*D/(I*I)
#      Multiply row I + 1 by D.
#    End
#
#  Example:
#
#    N = 5
#
#       -5     0.5     0.33     0.25    0.2
#     -300    40.0    30.00    24.00   20.0
#     1050  -157.5  -126.00  -105.00  -90.0
#    -1400   224.0   186.66   160.00  140.0
#      630  -105.0   -90.00   -78.75  -70.0
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is involutional: A * A = I.
#
#    det ( A ) = +1 or -1.
#
#    A is unimodular.
#
#    The matrices:
#      B = 1/2 ( I - A )
#    and
#      C = 1/2 ( I + A )
#    are idempotent, that is, B * B = B, and C * C = C.
#
#    A is ill-conditioned.
#
#    A is a diagonally scaled version of the Hilbert matrix.
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
#  Reference:
#
#    Alston Householder, John Carpenter,
#    The singular values of involutory and of idempotent matrices,
#    Numerische Mathematik,
#    Volume 5, 1963, pages 234-237.
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
      a[i,j] = 1.0 / float ( i + j + 1 )
 
  for i in range ( 0, n ):
    a[i,0] = - n * a[i,0]

  d = - float ( n )
  for i in range ( 1, n ):
    d = - float ( n + i ) * float ( n - i ) * d  / float ( i * i )
    for j in range ( 0, n ):
      a[i,j] = d * a[i,j]

  return a

def invol_determinant ( n ):

#*****************************************************************************80
#
## INVOL_DETERMINANT computes the determinant of the INVOL matrix.
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
#    Input, integer N, the order of the matrix.
#
#    Output, real DETERM, the determinant.
#
  if ( ( n % 4 ) == 0 or ( n % 4 ) == 3):
    value = 1.0
  else:
    value = - 1.0

  return value

def invol_determinant_test ( ):

#*****************************************************************************80
#
## INVOL_DETERMINANT_TEST tests INVOL_DETERMINANT.
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
  from invol import invol
  from r8mat_print import r8mat_print

  print ''
  print 'INVOL_DETERMINANT_TEST'
  print '  INVOL_DETERMINANT computes the INVOL determinant.'

  m = 5
  n = m
 
  a = invol ( n )

  r8mat_print ( m, n, a, '  INVOL matrix:' )

  value = invol_determinant ( n )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'INVOL_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def invol_inverse ( n ):

#*****************************************************************************80
#
## INVOL_INVERSE returns the inverse of the INVOL matrix.
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
#    Input, integer N, the order of A.
#
#    Output, real A(N,N), the matrix.
#
  a = invol ( n )

  return a

def invol_test ( ):

#*****************************************************************************80
#
## INVOL_TEST tests INVOL.
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

  print ''
  print 'INVOL_TEST'
  print '  INVOL computes the INVOL matrix.'

  m = 5
  n = m

  a = invol ( n )
 
  r8mat_print ( m, n, a, '  INVOL matrix:' )

  print ''
  print 'INVOL_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  invol_test ( )
  timestamp ( )
