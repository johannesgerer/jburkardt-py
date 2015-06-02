#! /usr/bin/env python
#
def hanowa ( alpha, n ):

#*****************************************************************************80
#
## HANOWA returns the Hanowa matrix.
#
#  Formula:
#
#    If ( I = J )
#      A(I,J) = ALPHA
#    else if ( I <= N/2 and J = I+N/2 )
#      A(I,J) = -I
#    else if ( N/2 < I and J = I-N/2 )
#      A(I,J) = I-N/2
#    else
#      A(I,J) = 0
#
#  Example:
#
#    ALPHA = 17, N = 6
#
#    17  0  0 -1  0  0
#     0 17  0  0 -2  0
#     0  0 17  0  0 -3
#     1  0  0 17  0  0
#     0  2  0  0 17  0
#     0  0  3  0  0 17
#
#  Properties:
#
#    A is generally not symmetric: A' ~= A.
#
#    A is nonsingular.
#
#    A is antisymmetric: A' = -A.
#
#    Because A is antisymmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A has complex eigenvalues
#
#      LAMBDA(2*I-1) = ALPHA + I * sqrt ( -1 )
#      LAMBDA(2*I)   = ALPHA - I * sqrt ( -1 )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    E Hairer, SP Norsett, G Wanner,
#    Solving Ordinary Differential Equations I: Nonstiff Problems,
#    Springer Verlag, Berlin, 1987, pages 86-87.
#
#  Parameters:
#
#    Input, real ALPHA, the scalar defining the Hanowa matrix.  A
#    typical value is -1.0.
#
#    Input, integer N, the order of A.  N must be even.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np
  from sys import exit

  a = np.zeros ( ( n, n ) )

  if ( ( n % 2 ) != 0 ):
    print''
    print 'HANOWA - Fatal error!'
    print '  Input N = %d' % ( n )
    print '  but N must be a multiple of 2.'
    exit ( 'HANOWA - Fatal error!' )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( i == j ):
        a[i,j] = alpha
      elif ( i + 1 <= ( n // 2 ) and j == i + ( n // 2 ) ):
        a[i,j] = - i - 1
      elif ( ( n // 2 ) < i + 1 and j == i - ( n // 2 ) ):
        a[i,j] = i + 1 - ( n // 2 )

  return a

def hanowa_determinant ( alpha, n ):

#*****************************************************************************80
#
## HANOWA_DETERMINANT returns the determinant of the HANOWA matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 January 2015
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
#    Output, real DETERM, the determinant.
#
  from sys import exit

  if ( ( n % 2 ) != 0 ):
    print ''
    print 'HANOWA_DETERMINANT - Fatal error!'
    print '  Input N = %d' % ( n )
    print '  but N must be a multiple of 2.'
    exit ( 'HANOWA_DETERMINANT - Fatal error!' )

  determ = 1.0

  ihi = ( n // 2 )
  for i in range ( 1, ihi + 1 ):
    determ = determ * ( alpha * alpha + i * i )

  return determ

def hanowa_determinant_test ( ):

#*****************************************************************************80
#
## HANOWA_DETERMINANT_TEST tests HANOWA_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 February 2015
#
#  Author:
#
#    John Burkardt
#
  from hanowa import hanowa
  from r8mat_print import r8mat_print
  from r8_uniform_ab import r8_uniform_ab

  print ''
  print 'HANOWA_DETERMINANT_TEST'
  print '  HANOWA_DETERMINANT computes the determinant of the HANOWA matrix.'
  print ''

  m = 4
  n = m

  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )

  a = hanowa ( alpha, n )
  r8mat_print ( m, n, a, '  HANOWA matrix:' )

  value = hanowa_determinant ( alpha, n )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'HANOWA_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def hanowa_inverse ( alpha, n ):

#*****************************************************************************80
#
## HANOWA_INVERSE returns the inverse of the HANOWA matrix.
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
#  Parameters:
#
#    Input, real ALPHA, the scalar defining the Hanowa matrix.  A
#    typical value is -1.0.
#
#    Input, integer N, the order of A.  N must be even.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np
  from sys import exit

  if ( ( n % 2 ) != 0 ):
    print ''
    print 'HANOWA_INVERSE - Fatal error!'
    print '  The matrix order N must be even.'
    exit ( 'HANOWA_INVERSE - Fatal error!' )

  a = np.zeros ( ( n, n ) )

  n2 = ( n // 2 )

  for i in range ( 0, n2 ):

    ip1 = float ( i + 1 )

    a[i,   i]    =   alpha / ( alpha * alpha + ip1 * ip1 )
    a[i+n2,i]    = -  ip1  / ( alpha * alpha + ip1 * ip1 )

    a[i+n2,i+n2] =   alpha / ( alpha * alpha + ip1 * ip1 )
    a[i,   i+n2] = +  ip1  / ( alpha * alpha + ip1 * ip1 )

  return a

def hanowa_test ( ):

#*****************************************************************************80
#
## HANOWA_TEST tests HANOWA.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 February 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print
  from r8_uniform_ab import r8_uniform_ab

  print ''
  print 'HANOWA_TEST'
  print '  HANOWA computes the HANOWA matrix.'

  m = 6
  n = m

  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )

  a = hanowa ( alpha, n )
  r8mat_print ( m, n, a, '  HANOWA matrix:' )

  print ''
  print 'HANOWA_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  hanowa_test ( )
  timestamp ( )
