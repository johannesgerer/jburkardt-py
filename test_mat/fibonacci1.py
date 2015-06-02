#! /usr/bin/env python
#
def fibonacci1 ( n, f1, f2 ):

#*****************************************************************************80
#
## FIBONACCI1 returns the FIBONACCI1 matrix.
#
#  Example:
#
#    N = 5
#    F1 = 1, F2 = 2
#
#    1  2  3  5  8
#    2  3  5  8 13
#    3  5  8 13 21
#    5  8 13 21 34
#    8 13 21 34 55
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#    If F1 and F2 are integral, then so is A.
#
#    If A is integral, then det ( A ) is integral, and
#    det ( A ) * inverse ( A ) is integral.
#
#    A is a Hankel matrix: constant along anti-diagonals.
#
#    If B is the Fibonacci iteration matrix:
#
#      B * A(F1,F2) = A(F2,F2+F1) = A(F2,F3)
#
#    and in general,
#
#      B^N * A(F1,F2) = A(F(N+1),F(N+2))
#
#    For 2 < N, the matrix is singular, because row 3 is the sum
#    of row 1 and row 2.
#
#    For 2 <= N,
#      rank ( A ) = 2
#
#    If N = 1, then
#      det ( A ) = 1
#    else if N = 2 then
#      det ( A ) = -1
#    else if 1 < N then
#      det ( A ) = 0
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, real F1, F2, the first two elements of the sequence
#    that will generate the Fibonacci sequence.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ n, n ] )

  a[0,0] = f1

  if ( 1 < n ):

    a[1,0] = f2
    a[0,1] = f2

    fnm2 = f1
    fnm1 = f2
    fn   = fnm1 + fnm2

    for k in range ( 2, n + n - 1 ):

      i = min ( k,     n - 1 )
      j = max ( 0, k - n + 1 )

      while ( 0 <= i and j < n ):
        a[i,j] = fn
        i = i - 1
        j = j + 1

      fnm2 = fnm1
      fnm1 = fn
      fn   = fnm1 + fnm2

  return a

def fibonacci1_determinant ( n, f1, f2 ):

#*****************************************************************************80
#
## FIBONACCI1_DETERMINANT returns the determinant of the FIBONACCI1 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, real F1, F2, the first two elements of the sequence
#    that will generate the Fibonacci sequence.
#
#    Output, real DETERM, the determinant.
#
  if ( n == 1 ):
    determ = 1.0
  elif ( n == 2 ):
    determ = -1.0
  else:
    determ = 0.0

  return determ

def fibonacci1_determinant_test ( ):

#*****************************************************************************80
#
## FIBONACCI1_DETERMINANT_TEST tests FIBONACCI1_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 January 2015
#
#  Author:
#
#    John Burkardt
#
  from fibonacci1 import fibonacci1
  from r8_uniform_ab import r8_uniform_ab
  from r8mat_print import r8mat_print


  print ''
  print 'FIBONACCI1_DETERMINANT_TEST'
  print '  FIBONACCI1_DETERMINANT computes the determinant of the FIBONACCI1 matrix.'
  print ''

  m = 5
  n = m

  f_lo = 1.0
  f_hi = 10.0
  seed = 123456789
  f1, seed = r8_uniform_ab ( f_lo, f_hi, seed )
  f2, seed = r8_uniform_ab ( f_lo, f_hi, seed )

  a = fibonacci1 ( n, f1, f2 )
  r8mat_print ( m, n, a, '  FIBONACCI1 matrix:' )

  value = fibonacci1_determinant ( n, f1, f2 )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'FIBONACCI1_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def fibonacci1_null_left ( m, n, f1, f2 ):

#*****************************************************************************80
#
## FIBONACCI1_NULL_LEFT returns a left null vector of the FIBONACCI1 matrix.
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
#    Input, integer M, N, the order of the matrix.
#
#    Input, real F1, F2, the first two elements of the sequence
#    that will generate the Fibonacci sequence.
#
#    Output, real X(M), a null vector.
#
  import numpy as np
  from sys import exit

  if ( m < 3 ):
    print ''
    print 'FIBONACCI1_NULL_LEFT - Fatal error!'
    print '  3 <= M is required.'
    exit ( 'FIBONACCI1_NULL_LEFT - Fatal error!' )

  x = np.zeros ( m )

  x[m-3] = -1.0
  x[m-2] = -1.0
  x[m-1] = +1.0 

  return x

def fibonacci1_null_right ( m, n, f1, f2 ):

#*****************************************************************************80
#
## FIBONACCI1_NULL_RIGHT returns a right null vector of the FIBONACCI1 matrix.
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
#    Input, integer M, N, the order of the matrix.
#
#    Input, real F1, F2, the first two elements of the sequence
#    that will generate the Fibonacci sequence.
#
#    Output, real X(N), a null vector.
#
  import numpy as np
  from sys import exit

  if ( n < 3 ):
    print ''
    print 'FIBONACCI1_NULL_RIGHT - Fatal error!'
    print '  3 <= N is required.'
    exit ( 'FIBONACCI1_NULL_RIGHT - Fatal error!' )

  x = np.zeros ( n )

  x[n-3] = -1.0
  x[n-2] = -1.0
  x[n-1] = +1.0 

  return x

def fibonacci1_test ( ):

#*****************************************************************************80
#
## FIBONACCI1_TEST tests FIBONACCI1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 January 2015
#
#  Author:
#
#    John Burkardt
#
  from r8_uniform_ab import r8_uniform_ab
  from r8mat_print import r8mat_print

  print ''
  print 'FIBONACCI1_TEST'
  print '  FIBONACCI1 computes the FIBONACCI1 matrix.'

  m = 5
  n = m

  f_lo = 1.0
  f_hi = 10.0
  seed = 123456789
  f1, seed = r8_uniform_ab ( f_lo, f_hi, seed )
  f2, seed = r8_uniform_ab ( f_lo, f_hi, seed )

  a = fibonacci1 ( n, f1, f2 )
  r8mat_print ( m, n, a, '  FIBONACCI1 matrix:' )

  print ''
  print 'FIBONACCI1_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  fibonacci1_test ( )
  timestamp ( )
