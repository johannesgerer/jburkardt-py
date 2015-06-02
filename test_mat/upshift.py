#! /usr/bin/env python
#
def upshift ( n ):

#*****************************************************************************80
#
## UPSHIFT returns the UPSHIFT matrix.
#
#  Formula:
#
#    if ( J-I == 1 mod ( n ) )
#      A(I,J) = 1
#    else
#      A(I,J) = 0
#
#  Example:
#
#    N = 4
#
#    0 1 0 0
#    0 0 1 0
#    0 0 0 1
#    1 0 0 0
#
#  Rectangular properties:
#
#    A is integral: int ( A ) = A.
#
#    A is a zero/one matrix.
#
#  Square Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is nonsingular.
#
#    A is a permutation matrix.
#
#    If N is even, det ( A ) = -1.
#    If N is odd,  det ( A ) = +1.
#
#    A is unimodular.
#
#    A is persymmetric: A(I,J) = A(N+1-J,N+1-I).
#
#    A is a Hankel matrix: constant along anti-diagonals.
#
#    A is an N-th root of the identity matrix.
#
#    The inverse of A is the downshift matrix.
#
#    A circulant matrix C, whose first row is (c1, c2, ..., cn), can be
#    written as a polynomial in A:
#
#      C = c1 * I + c2 * A + c3 * A**2 + ... + cn * A**n-1.
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
#  Parameters:
#
#    Input, integer N, the number of rows and columns 
#    of the matrix.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np
  from i4_modp import i4_modp

  a = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      if ( i4_modp ( j - i, n ) == 1 ):
        a[i,j] = 1.0

  return a

def upshift_condition ( n ):

#*****************************************************************************80
#
## UPSHIFT_CONDITION computes the L1 condition of the UPSHIFT matrix.
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
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Output, real VALUE, the L1 condition.
#
  a_norm = 1.0;
  b_norm = 1.0;
  value = a_norm * b_norm;

  return value

def upshift_condition_test ( ):

#*****************************************************************************80
#
## UPSHIFT_CONDITION_TEST tests UPSHIFT_CONDITION.
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
  from upshift import upshift
  from r8mat_print import r8mat_print

  print ''
  print 'UPSHIFT_CONDITION_TEST'
  print '  UPSHIFT_CONDITION computes the UPSHIFT condition.'

  m = 5
  n = m
 
  a = upshift ( n )

  r8mat_print ( m, n, a, '  UPSHIFT matrix:' )

  value = upshift_condition ( n )

  print '  Value =  %g' % ( d )

  print ''
  print 'UPSHIFT_CONDITION_TEST'
  print '  Normal end of execution.'

  return

def upshift_determinant ( n ):

#*****************************************************************************80
#
## UPSHIFT_DETERMINANT computes the determinant of the UPSHIFT matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 February 2015
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
  if ( ( n % 2 ) == 0 ):
    value = - 1.0
  else:
    value = 1.0

  return value

def upshift_determinant_test ( ):

#*****************************************************************************80
#
## UPSHIFT_DETERMINANT_TEST tests UPSHIFT_DETERMINANT.
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
  from upshift import upshift
  from r8mat_print import r8mat_print

  print ''
  print 'UPSHIFT_DETERMINANT_TEST'
  print '  UPSHIFT_DETERMINANT computes the UPSHIFT determinant.'

  m = 5
  n = m
 
  a = upshift ( n )

  r8mat_print ( m, n, a, '  UPSHIFT matrix:' )

  value = upshift_determinant ( n )

  print '  Value =  %g' % ( value )

  print ''
  print 'UPSHIFT_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def upshift_inverse ( n ):

#*****************************************************************************80
#
## UPSHIFT_INVERSE returns the inverse of the UPSHIFT matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 March 2015
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
  from downshift import downshift

  a = downshift ( n )

  return a

def upshift_test ( ):

#*****************************************************************************80
#
## UPSHIFT_TEST tests UPSHIFT.
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

  print ''
  print 'UPSHIFT_TEST'
  print '  UPSHIFT computes the UPSHIFT matrix.'

  m = 5
  n = m

  a = upshift ( n )
 
  r8mat_print ( m, n, a, '  UPSHIFT matrix:' )

  print ''
  print 'UPSHIFT_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  upshift_test ( )
  timestamp ( )
