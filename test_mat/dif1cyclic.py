#! /usr/bin/env python
#
def dif1cyclic ( n ):

#*****************************************************************************80
#
## DIF1CYCLIC returns the cyclic first difference matrix.
#
#  Example:
#
#    N = 5
#
#    0 +1  .  . -1
#   -1  0 +1  .  .
#    . -1  0 +1  .
#    .  . -1  0 +1
#   +1  .  . -1  0
#
#  Square Properties:
#
#    A is integral: int ( A ) = A.
#
#    A is Toeplitz: constant along diagonals.
#
#    A is antisymmetric: A' = -A.
#
#    Because A is antisymmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A has constant row sum = 0.
#
#    A has constant column sum = 0.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of rows and columns of A.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np
  from i4_wrap import i4_wrap

  a = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):

    im1 = i4_wrap ( i - 1, 0, n - 1 )
    a[i,im1] = -1.0

    ip1 = i4_wrap ( i + 1, 0, n - 1 )
    a[i,ip1] = +1.0

  return a

def dif1cyclic_determinant ( n ):

#*****************************************************************************80
#
## DIF1CYCLIC_DETERMINANT computes the determinant of the DIF1CYCLIC matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 January 2015
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

  return determ

def dif1cyclic_determinant_test ( ):

#*****************************************************************************80
#
## DIF1CYCLIC_DETERMINANT_TEST tests DIF1CYCLIC_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 January 2015
#
#  Author:
#
#    John Burkardt
#
  from dif1cyclic import dif1cyclic
  from r8mat_print import r8mat_print

  print ''
  print 'DIF1CYCLIC_DETERMINANT_TEST'
  print '  DIF1CYCLIC_DETERMINANT computes the DIF1CYCLIC determinant.'

  m = 5
  n = m
 
  a = dif1cyclic ( n )

  r8mat_print ( m, n, a, '  DIF1 matrix:' )

  value = dif1cyclic_determinant ( n )

  print '  Value =  %g' % ( value )

  print ''
  print 'DIF1CYCLIC_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def dif1cyclic_null_left ( m, n ):

#*****************************************************************************80
#
## DIF1CYCLIC_NULL_LEFT returns a left null vector of the DIF1CYCLIC matrix.
#
#  Discussion:
#
#    (1,1,1,...,1) is always a null vector.
#
#    If M is even,
#
#    (A,B,A,B,A,B,...,A,B) is also a null vector, for any A and B.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the order of A.
#
#    Output, real X(M), the null vector.
#
  import numpy as np

  if ( ( m % 2 ) != 0 ):

    x = np.ones ( m )

  else:

    a = 1.0
    b = 2.0
    x = np.zeros ( m )
    
    for i in range ( 0, m ):
      x[i] = a
      t = a
      a = b
      b = t

  return x

def dif1cyclic_null_right ( m, n ):

#*****************************************************************************80
#
## DIF1CYCLIC_NULL_RIGHT returns a right null vector of the DIF1CYCLIC matrix.
#
#  Discussion:
#
#    (1,1,1,...,1) is always a null vector.
#
#    If N is even,
#
#    (A,B,A,B,A,B,...,A,B) is also a null vector, for any A and B.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the order of A.
#
#    Output, real X(N), the null vector.
#
  import numpy as np

  if ( ( n % 2 ) != 0 ):

    x = np.ones ( n )

  else:

    a = 1.0
    b = 2.0
    x = np.zeros ( n )
    
    for i in range ( 0, n ):
      x[i] = a
      t = a
      a = b
      b = t

  return x

def dif1cyclic_test ( ):

#*****************************************************************************80
#
## DIF1CYCLIC_TEST tests DIF1CYCLIC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 January 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'DIF1CYCLIC_TEST'
  print '  DIF1CYCLIC computes the DIF1CYCLIC matrix.'

  m = 5
  n = m

  a = dif1cyclic ( n )
 
  r8mat_print ( m, n, a, '  DIF1CYCLIC matrix:' )

  print ''
  print 'DIF1CYCLIC_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  dif1cyclic_test ( )
  dif1cyclic_determinant_test ( )
  timestamp ( )
