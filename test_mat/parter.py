#! /usr/bin/env python
#
def parter ( m, n ):

#*****************************************************************************80
#
## PARTER returns the PARTER matrix.
#
#  Formula:
#
#    A(I,J) = 1 / ( i - j + 0.5 )
#
#  Example:
#
#    N = 5
#
#     2   -2  -2/3 -2/5 -2/7
#    2/3   2   -2  -2/3 -2/5
#    2/5  2/3   2   -2  -2/3
#    2/7  2/5  2/3   2   -2
#    2/9  2/7  2/5  2/3   2
#
#  Properties:
#
#    The diagonal entries are all 2, the first superdiagonals all -2.
#
#    A is Toeplitz: constant along diagonals.
#
#    A is generally not symmetric: A' ~= A.
#
#    A is persymmetric: A(I,J) = A(N+1-J,N+1-I).
#
#    A is a special case of the Cauchy matrix.
#
#    Most of the singular values are very close to Pi.
#
#    The family of matrices is nested as a function of N.
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
#    Seymour Parter,
#    On the distribution of the singular values of Toeplitz matrices,
#    Linear Algebra and Applications,
#    Volume 80, August 1986, pages 115-130.
#
#    Evgeny Tyrtyshnikov,
#    Cauchy-Toeplitz matrices and some applications,
#    Linear Algebra and Applications,
#    Volume 149, 15 April 1991, pages 1-18.
#
#  Parameters:
#
#    Input, integer M, N, the order of A.
#
#    Output, real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( m, n ) )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      a[i,j] = 1.0 / ( float ( i - j ) + 0.5 )

  return a

def parter_determinant ( n ):

#*****************************************************************************80
#
## PARTER_DETERMINANT returns the determinant of the PARTER matrix.
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
#    Output, real VALUE, the determinant.
#
  top = 1.0
  for i in range ( 0, n ):
    for j in range ( i + 1, n ):
      top = top * float ( j - i ) * float ( i - j )

  bottom = 1.0
  for i in range ( 0, n ):
    for j in range ( 0, n ):
      bottom = bottom * ( float ( i - j ) + 0.5 )

  value = top / bottom;

  return value

def parter_determinant_test ( ):

#*****************************************************************************80
#
## PARTER_DETERMINANT_TEST tests PARTER_DETERMINANT.
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
  from parter import parter
  from r8mat_print import r8mat_print
 
  print ''
  print 'PARTER_DETERMINANT_TEST'
  print '  PARTER_DETERMINANT computes the determinant of the PARTER matrix.'
  print ''

  m = 4
  n = m

  a = parter ( m, n )
  r8mat_print ( m, n, a, '  PARTER matrix:' )

  value = parter_determinant ( n )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'PARTER_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def parter_inverse ( n ):

#*****************************************************************************80
#
## PARTER_INVERSE returns the inverse of the PARTER matrix.
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
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n):
    for j in range ( 0, n ):

      top = 1.0;
      bot1 = 1.0;
      bot2 = 1.0;

      for k in range ( 0, n ):

        top = top * ( 0.5 + float ( j - k ) ) * ( 0.5 + float ( k - i ) )

        if ( k != j ):
          bot1 = bot1 * float ( j - k )

        if ( k != i ):
          bot2 = bot2 * float ( k - i )

      a[i,j] = top / ( ( 0.5 + float ( j - i ) ) * bot1 * bot2 )

  return a

def parter_test ( ):

#*****************************************************************************80
#
## PARTER_TEST tests PARTER.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 January 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'PARTER_TEST'
  print '  PARTER computes the PARTER matrix.'

  m = 4
  n = m

  a = parter ( m, n )
  r8mat_print ( m, n, a, '  PARTER matrix:' )

  print ''
  print 'PARTER_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  parter_test ( )
  timestamp ( )
