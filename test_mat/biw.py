#! /usr/bin/env python
#
def biw ( n ):

#*****************************************************************************80
#
## BIW returns the BIW matrix.
#
#  Discussion:
#
#    BIW is a bidiagonal matrix of Wilkinson.   Originally, this matrix
#    was considered for N = 100.
#
#  Formula:
#
#    if ( I == J )
#      A(I,J) = 0.5 + I / ( 10 * N )
#    else if ( J == I+1 )
#      A(I,J) = -1.0
#    else
#      A(I,J) = 0
#
#  Example:
#
#    N = 5
#
#    0.52 -1.00  0.00  0.00  0.00
#    0.00  0.54 -1.00  0.00  0.00
#    0.00  0.00  0.56 -1.00  0.00
#    0.00  0.00  0.00  0.58 -1.00
#    0.00  0.00  0.00  0.00  0.60
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
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ n, n ] )
  
  for i in range ( 0, n ):
    a[i,i] = 0.5 + float ( i + 1 ) / float ( 10 * n )
  for i in range ( 0, n - 1 ):
    a[i,i+1] = - 1.0

  return a

def biw_condition ( n ):

#*****************************************************************************80
#
## BIW_CONDITION computes the L1 condition of the BIW matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Output, real VALUE, the L1 condition.
#
  if ( n == 1 ):
    a_norm = 0.6
  else:
    a_norm = 1.6

  b_norm = 0.0
  j = n
  for i in range ( n, 0, -1 ):
    aii = 0.5 + ( float ) ( i ) / float ( 10 * n )
    if ( i == j ):
      bij = 1.0 / aii
    elif ( i < j ):
      bij = bij / aii
    b_norm = b_norm + abs ( bij )

  value = a_norm * b_norm

  return value

def biw_determinant ( n ):

#*****************************************************************************80
#
## BIW_DETERMINANT computes the determinant of the BIW matrix.
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
#    Output, real VALUE, the determinant.
#
  value = 1.0
  for i in range ( 0, n ):
    value = value * ( 0.5 + float ( i + 1 ) / float ( 10 * n ) )

  return value

def biw_determinant_test ( ):

#*****************************************************************************80
#
## BIW_DETERMINANT_TEST tests BIW_DETERMINANT.
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
  from r8mat_print import r8mat_print

  print ''
  print 'BIW_DETERMINANT_TEST'
  print '  BIW_DETERMINANT computes the BIW determinant.'

  n = 5
  a = biw ( n )
  r8mat_print ( n, n, a, '  BIW matrix:' )

  value = biw_determinant ( n )
  print '  Value =  %g' % ( value )

  print ''
  print 'BIW_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def biw_inverse ( n ):

#*****************************************************************************80
#
## BIW_INVERSE returns the inverse of the BIW matrix.
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
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  b = np.zeros ( [ n, n ] )
  
  for j in range ( n - 1, -1, -1 ):
    for i in range ( n - 1, -1, -1 ):

      aii = 0.5 + float ( i + 1 ) / float ( 10 * n )
      aiip1 = -1.0

      if ( i == j ):
        b[i,j] = 1.0 / aii
      elif ( i < j ):
        t = aiip1 * b[i+1,j]
        b[i,j] = - t / aii

  return b

def biw_test ( ):

#*****************************************************************************80
#
## BIW_TEST tests BIW.
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
  from r8mat_print import r8mat_print

  print ''
  print 'BIW_TEST'
  print '  BIW computes the BIW matrix.'

  m = 5
  n = 5
  a = biw ( n )
  r8mat_print ( m, n, a, '  BIW matrix:' )

  print ''
  print 'BIW_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  biw_test ( )
  biw_determinant_test ( )
  timestamp ( )
