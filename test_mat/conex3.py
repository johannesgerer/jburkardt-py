#! /usr/bin/env python
#
def conex3 ( n ):

#*****************************************************************************80
#
## CONEX3 returns the CONEX3 matrix.
#
#  Formula:
#
#    if ( I = J and I < N )
#      A(I,J) =  1.0 for 1<=I<N
#    else if ( I = J = N )
#      A(I,J) = -1.0
#    else if ( J < I )
#      A(I,J) = -1.0
#    else
#      A(I,J) =  0.0
#
#  Example:
#
#    N = 5
#
#     1  0  0  0  0
#    -1  1  0  0  0
#    -1 -1  1  0  0
#    -1 -1 -1  1  0
#    -1 -1 -1 -1 -1
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is integral: int ( A ) = A.
#
#    A is lower triangular.
#
#    det ( A ) = -1.
#
#    A is unimodular.
#
#    LAMBDA = ( 1, 1, 1, 1, -1 )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 October 2007
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Alan Cline, RK Rew,
#    A set of counterexamples to three condition number estimators,
#    SIAM Journal on Scientific and Statistical Computing,
#    Volume 4, 1983, pages 602-611.
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

      if ( j < i ):
        a[i,j] = -1.0
      elif ( j == i and i != n - 1 ):
        a[i,j] = 1.0
      elif ( j == i and i == n - 1 ):
        a[i,j] = - 1.0
      else:
        a[i,j] = 0.0

  return a

def conex3_condition ( n ):

#*****************************************************************************80
#
## CONEX3_CONDITION returns the L1 condition of the CONEX3 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 April 2012
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Output, real COND, the L1 condition number.
#
  cond = n * 2.0 ** ( n - 1 )

  return cond

def conex3_condition_test ( ):

#*****************************************************************************80
#
## CONEX3_CONDITION_TEST tests CONEX3_CONDITION.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 December 2014
#
#  Author:
#
#    John Burkardt
#
  from conex3 import conex3
  from r8mat_print import r8mat_print

  print ''
  print 'CONEX3_CONDITION_TEST'
  print '  CONEX3_CONDITION computes the condition of the CONEX3 matrix.'
  print ''


  n = 5
  a = conex3 ( n )
  r8mat_print ( n, n, a, '  CONEX3 matrix:' )

  value = conex3_condition ( n )

  print ''
  print '  Value =  #g' # ( value )

  print ''
  print 'CONEX3_CONDITION_TEST'
  print '  Normal end of execution.'

  return

def conex3_determinant ( n ):

#*****************************************************************************80
#
## CONEX3_DETERMINANT returns the determinant of the CONEX3 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 January 2015
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
  determ = - 1.0

  return determ

def conex3_determinant_test ( ):

#*****************************************************************************80
#
## CONEX3_DETERMINANT_TEST tests CONEX3_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 January 2015
#
#  Author:
#
#    John Burkardt
#
  from conex3 import conex3
  from r8mat_print import r8mat_print

  print ''
  print 'CONEX3_DETERMINANT_TEST'
  print '  CONEX3_DETERMINANT computes the determinant of the CONEX3 matrix.'
  print ''

  n = 5
  a = conex3 ( n )
  r8mat_print ( n, n, a, '  CONEX3 matrix:' )

  value = conex3_determinant ( n )

  print ''
  print '  Value =  #g' # ( value )

  print ''
  print 'CONEX3_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def conex3_inverse ( n ):

#*****************************************************************************80
#
## CONEX3_INVERSE returns the inverse of the CONEX3 matrix.
#
#  Example:
#
#    N = 5
#
#     1  0  0  0  0
#     1  1  0  0  0
#     2  1  1  0  0
#     4  2  1  1  0
#    -8 -4 -2 -1 -1
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Alan Cline, RK Rew,
#    A set of counterexamples to three condition number estimators,
#    SIAM Journal on Scientific and Statistical Computing,
#    Volume 4, 1983, pages 602-611.
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

      if ( i < n - 1 ):
      
        if ( j < i ):
          a[i,j] = 2.0 ** ( i - j - 1 )
        elif ( i == j ):
          a[i,j] = 1.0

      elif ( i == n - 1 ):
      
        if ( j < i ):
          a[i,j] = - 2.0 ** ( i - j - 1 )
        else:
          a[i,j] = -1.0

  return a

def conex3_test ( ):

#*****************************************************************************80
#
## CONEX3_TEST tests CONEX3.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 December 2014
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'CONEX3_TEST'
  print '  CONEX3 computes the CONEX3 matrix.'

  n = 5
  a = conex3 ( n )
  r8mat_print ( n, n, a, '  CONEX3 matrix:' )

  print ''
  print 'CONEX3_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  conex3_test ( )
  timestamp ( )
