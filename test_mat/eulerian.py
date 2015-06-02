#! /usr/bin/env python
#
def eulerian ( m, n ):

#*****************************************************************************80
#
## EULERIAN returns the EULERIAN matrix.
#
#  Definition:
#
#    A run in a permutation is a sequence of consecutive ascending values.
#
#    E(I,J) is the number of permutations of I objects which contain
#    exactly J runs.
#
#  Examples:
#
#     N = 7
#
#     1     0     0     0     0     0     0
#     1     1     0     0     0     0     0
#     1     4     1     0     0     0     0
#     1    11    11     1     0     0     0
#     1    26    66    26     1     0     0
#     1    57   302   302    57     1     0
#     1   120  1191  2416  1191   120     1
#
#  Recursion:
#
#    E(I,J) = J * E(I-1,J) + (I-J+1) * E(I-1,J-1).
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is integral: int ( A ) = A.
#
#    A is nonnegative.
#
#    A is unit lower triangular.
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
#    25 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Dennis Stanton, Dennis White,
#    Constructive Combinatorics,
#    Springer Verlag, 1986.
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns of A.
#
#    Output, real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ m, n ] )

  a[0,0] = 1.0

  for i in range ( 1, m ):
    a[i,0] = 1.0
    for j in range ( 1, n ):
      a[i,j] = ( j + 1 ) * a[i-1,j] + ( i - j + 1 ) * a[i-1,j-1]

  return a

def eulerian_determinant ( n ):

#*****************************************************************************80
#
## EULERIAN_DETERMINANT returns the determinant of the EULERIAN matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 January 2015
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
  determ = 1.0

  return determ

def eulerian_determinant_test ( ):

#*****************************************************************************80
#
## EULERIAN_DETERMINANT_TEST tests EULERIAN_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 January 2015
#
#  Author:
#
#    John Burkardt
#
  from eulerian import eulerian
  from r8mat_print import r8mat_print
 
  print ''
  print 'EULERIAN_DETERMINANT_TEST'
  print '  EULERIAN_DETERMINANT computes the determinant of the EULERIAN matrix.'
  print ''

  m = 4
  n = m

  a = eulerian ( m, n )
  r8mat_print ( m, n, a, '  EULERIAN matrix:' )

  value = eulerian_determinant ( n )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'EULERIAN_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def eulerian_inverse ( n ):

#*****************************************************************************80
#
## EULERIAN_INVERSE computes the inverse of the EULERIAN matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Output, real A(N,N), the inverse of the Eulerian matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )
#
#  Set up the Eulerian matrix.
#
  b = eulerian ( n, n )
#
#  Compute the inverse A of a unit lower triangular matrix B.
#
  for j in range ( 0, n ):
    for i in range ( 0, n ):

      if ( i == j ):

        a[i,j] = 1.0

      elif ( j < i ):

        t = 0.0
        for k in range ( j, i ):
          t = t + b[i,k] * a[k,j]
        a[i,j] = - t

  return a

def eulerian_test ( ):

#*****************************************************************************80
#
## EULERIAN_TEST tests EULERIAN.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 January 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'EULERIAN_TEST'
  print '  EULERIAN computes the EULERIAN matrix.'

  m = 4
  n = m

  a = eulerian ( m, n )
  r8mat_print ( m, n, a, '  EULERIAN matrix:' )

  print ''
  print 'EULERIAN_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  eulerian_test ( )
  timestamp ( )
