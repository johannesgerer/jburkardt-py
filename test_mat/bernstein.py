#! /usr/bin/env python
#
def bernstein ( n ):

#*****************************************************************************80
#
## BERNSTEIN returns the BERNSTEIN matrix.
#
#  Discussion:
#
#    The Bernstein matrix of order N is an NxN matrix A which can be used to
#    transform a vector of power basis coefficients C representing a polynomial 
#    P(X) to a corresponding Bernstein basis coefficient vector B:
#
#      B = A * C
#
#    The N power basis vectors are ordered as (1,X,X^2,...X^(N-1)) and the N 
#    Bernstein basis vectors as ((1-X)^(N-1), X*(1_X)^(N-2),...,X^(N-1)).
#
#  Example:
#
#    N = 5
#
#    1    -4     6    -4     1
#    0     4   -12    12    -4
#    0     0     6   -12     6
#    0     0     0     4    -4
#    0     0     0     0     1
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Output, real A(N,N), the Bernstein matrix.
#
  import numpy as np
  from r8_choose import r8_choose
  from r8_mop import r8_mop

  a = np.zeros ( ( n, n ) )

  for j in range ( 0, n ):
    for i in range ( 0, j + 1 ):
      a[i,j] = r8_mop ( j - i ) * r8_choose ( n - 1 - i, j - i ) \
        * r8_choose ( n - 1, i )

  return a

def bernstein_determinant ( n ):

#*****************************************************************************80
#
## BERNSTEIN_DETERMINANT returns the determinant of the BERNSTEIN matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 March 2015
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
  from r8_choose import r8_choose

  value = 1.0
  for i in range ( 0, n ):
    value = value * r8_choose ( n - 1, i )

  return value

def bernstein_inverse ( n ):

#*****************************************************************************80
#
## BERNSTEIN_INVERSE returns the inverse of the BERNSTEIN matrix.
#
#  Discussion:
#
#    The inverse Bernstein matrix of order N is an NxN matrix A which can 
#    be used to transform a vector of Bernstein basis coefficients B
#    representing a polynomial P(X) to a corresponding power basis 
#    coefficient vector C:
#
#      C = A * B
#
#    The N power basis vectors are ordered as (1,X,X^2,...X^(N-1)) and the N 
#    Bernstein basis vectors as ((1-X)^(N-1), X*(1_X)^(N-2),...,X^(N-1)).
#
#  Example:
#
#    N = 5
#
#   1.0000    1.0000    1.0000    1.0000    1.0000
#        0    0.2500    0.5000    0.7500    1.0000
#        0         0    0.1667    0.5000    1.0000
#        0         0         0    0.2500    1.0000
#        0         0         0         0    1.0000
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
#    Output, real A(N,N), the inverse Bernstein matrix.
#
  import numpy as np
  from r8_choose import r8_choose

  a = np.zeros ( ( n, n ) )

  for j in range ( 0, n ):
    for i in range ( 0, j + 1 ):
      a[i,j] = r8_choose ( j, i ) / r8_choose ( n - 1, i )

  return a

def bernstein_test ( ):

#*****************************************************************************80
#
## BERNSTEIN_TEST tests BERNSTEIN.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 March 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'BERNSTEIN_TEST'
  print '  BERNSTEIN computes the BERNSTEIN matrix.'

  m = 5
  n = m

  a = bernstein ( n )
 
  r8mat_print ( m, n, a, '  BERNSTEIN matrix:' )

  print ''
  print 'BERNSTEIN_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  bernstein_test ( )
  timestamp ( )
