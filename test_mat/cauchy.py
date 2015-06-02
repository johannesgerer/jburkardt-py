#! /usr/bin/env python
#
def cauchy ( n, x, y ):

#*****************************************************************************80
#
## CAUCHY returns the CAUCHY matrix.
#
#  Formula:
#
#    A(I,J) = 1.0 / ( X(I) + Y(J) )
#
#  Example:
#
#    N = 5, X = ( 1, 3, 5, 8, 7 ), Y = ( 2, 4, 6, 10, 9 )
#
#    1/3  1/5  1/7  1/11 1/10
#    1/5  1/7  1/9  1/13 1/12
#    1/7  1/9  1/11 1/15 1/14
#    1/10 1/12 1/14 1/18 1/17
#    1/9  1/11 1/13 1/17 1/16
#
#    or, in decimal form,
#
#    0.333333      0.200000      0.142857      0.0909091     0.100000
#    0.200000      0.142857      0.111111      0.0769231     0.0833333
#    0.142857      0.111111      0.0909091     0.0666667     0.0714286
#    0.100000      0.0833333     0.0714286     0.0555556     0.0588235
#    0.111111      0.0909091     0.0769231     0.0588235     0.0625000
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is totally positive if 0 < X(1) < ... < X(N) and 0 < Y1 < ... < Y(N).
#
#    A will be singular if any X(I) equals X(J), or
#    any Y(I) equals Y(J), or if any X(I)+Y(J) equals zero.
#
#    A is generally not normal: A' * A /= A * A'.
#
#    The Hilbert matrix is a special case of the Cauchy matrix.
#
#    The Parter matrix is a special case of the Cauchy matrix.
#
#    The Ris or "ding-dong" matrix is a special case of the Cauchy matrix.
#
#    det ( A ) = product ( 1 <= I < J <= N ) ( X(J) - X(I) )* ( Y(J) - Y(I) )
#           / product ( 1 <= I <= N, 1 <= J <= N ) ( X(I) + Y(J) )
#
#    The inverse of A is
#
#      INVERSE(A)(I,J) = product ( 1 <= K <= N ) [ (X(J)+Y(K)) * (X(K)+Y(I)) ] /
#            [ (X(J)+Y(I)) * product ( 1 <= K <= N, K /= J ) (X(J)-X(K))
#                          * product ( 1 <= K <= N, K /= I ) (Y(I)-Y(K)) ]
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Gregory, David Karney,
#    Example 3.26,
#    A Collection of Matrices for Testing Computational Algorithms,
#    Wiley, New York, 1969, page 54, 
#    LC: QA263.G68.
#
#    Nicholas Higham,
#    Accuracy and Stability of Numerical Algorithms,
#    SIAM, 1996.
#
#    Donald Knuth,
#    The Art of Computer Programming,
#    Volume 1, Fundamental Algorithms, Second Edition
#    Addison-Wesley, Reading, Massachusetts, 1973, page 36.
#
#    Olga Taussky, Marvin Marcus,
#    Eigenvalues of finite matrices,
#    in Survey of Numerical Analysis, 
#    Edited by John Todd,
#    McGraw-Hill, New York, pages 279-313, 1962.
#
#    Evgeny Tyrtyshnikov,
#    Cauchy-Toeplitz matrices and some applications,
#    Linear Algebra and Applications,
#    Volume 149, 1991, pages 1-18.
#
#  Parameters:
#
#    Input, integer N, the order of A.
#
#    Input, real X(N), Y(N), vectors that determine A.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np
  from sys import exit

  a = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ): 

      if ( x[i] + y[j] == 0.0 ):
        print ''
        print 'CAUCHY - Fatal error!'
        print '  The denominator X(I)+Y(J) was zero'
        print '  for I = %d' % ( i )
        print '  X(I)  = %g' % ( x[i] )
        print '  and J = %d' % ( j )
        print '  Y(J)  = %g' % ( y[j] )
        exit ( 'CAUCHY - Fatal error!' )

      a[i,j] = 1.0 / ( x[i] + y[j] )

  return a

def cauchy_determinant ( n, x, y ):

#*****************************************************************************80
#
## CAUCHY_DETERMINANT computes the determinant of the CAUCHY matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, real X(N), Y(N), vectors that determine A.
#
#    Output, real DETERM, the determinant.
#
  top = 1.0
  for i in range ( 0, n ):
    for j in range ( i + 1, n ):
      top = top * ( x[j] - x[i] ) * ( y[j] - y[i] )

  bottom = 1.0
  for i in range ( 0, n ):
    for j in range ( 0, n ):
      bottom = bottom * ( x[i] + y[j] )

  determ = top / bottom

  return determ

def cauchy_determinant_test ( ):

#*****************************************************************************80
#
## CAUCHY_DETERMINANT_TEST tests CAUCHY_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 January 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print
  from r8vec_uniform_01 import r8vec_uniform_01

  print ''
  print 'CAUCHY_DETERMINANT_TEST'
  print '  CAUCHY_DETERMINANT computes the CAUCHY determinant.'

  m = 4
  n = 4
  seed = 123456789
  x, seed = r8vec_uniform_01 ( n, seed )
  y, seed = r8vec_uniform_01 ( n, seed )
  a = cauchy ( n, x, y )
  r8mat_print ( m, n, a, '  CAUCHY matrix:' )

  value = cauchy_determinant ( n, x, y )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'CAUCHY_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def cauchy_inverse ( n, x, y ):

#*****************************************************************************80
#
#% CAUCHY_INVERSE returns the inverse of the CAUCHY matrix.
#
#  Formula:
#
#    A(I,J) = product ( 1 <= K <= N ) [(X(J)+Y(K))*(X(K)+Y(I))] /
#      [ (X(J)+Y(I)) * product ( 1 <= K <= N, K /= J ) (X(J)-X(K))
#                    * product ( 1 <= K <= N, K /= I ) (Y(I)-Y(K)) ]
#
#  Example:
#
#    N = 5, X = ( 1, 3, 5, 8, 7 ), Y = ( 2, 4, 6, 10, 9 )
#
#       241.70      -2591.37       9136.23      10327.50     -17092.97
#     -2382.19      30405.38    -116727.19    -141372.00     229729.52
#      6451.76     -89667.70     362119.56     459459.00    -737048.81
#     10683.11    -161528.55     690983.38     929857.44   -1466576.75
#    -14960.00     222767.98    -942480.06   -1253376.00    1983696.00
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    The sum of the entries of A equals the sum of the entries of X and Y.
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
#  Reference:
#
#    Donald Knuth,
#    The Art of Computer Programming,
#    Volume 1, Fundamental Algorithms, Second Edition,
#    Addison-Wesley, Reading, Massachusetts, 1973, page 36.
#
#  Parameters:
#
#    Input, integer N, the order of A.
#
#    Input, real X(N), Y(N), vectors that determine A.
#    The following conditions on X and Y must hold:
#      X(I)+Y(J) must not be zero for any I and J;
#      X(I) must never equal X(J);
#      Y(I) must never equal Y(J).
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np
  from sys import exit

  a = np.zeros ( ( n, n ) )
#
#  Check the data.
#
  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( x[i] + y[j] == 0.0 ):
        print ''
        print 'CAUCHY_INVERSE - Fatal error!'
        print '  The denominator X(I)+Y(J) was zero'
        print '  for I = %d' % ( i )
        print '  and J = %d' % ( j )
        exit ( 'CAUCHY_INVERSE - Fatal error!' )

      if ( i != j and x[i] == x[j] ):
        print ''
        print 'CAUCHY_INVERSE - Fatal error!'
        print '  X(I) equals X(J)'
        print '  for I = %d' % ( i )
        print '  and J = %d' % ( j )
        exit ( 'CAUCHY_INVERSE - Fatal error!' )

      if ( i != j and y[i] == y[j] ):
        print ''
        print 'CAUCHY_INVERSE - Fatal error!'
        print '  Y(I) equals Y(J)'
        print '  for I =%d' % ( i )
        print '  and J = %d' % ( j )
        exit ( 'CAUCHY_INVERSE - Fatal error!' )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      top = 1.0
      bot1 = 1.0
      bot2 = 1.0

      for k in range ( 0, n ):

        top = top * ( x[j] + y[k] ) * ( x[k] + y[i] )

        if ( k != j ):
          bot1 = bot1 * ( x[j] - x[k] )

        if ( k != i ):
          bot2 = bot2 * ( y[i] - y[k] )

      a[i,j] = top / ( ( x[j] + y[i] ) * bot1 * bot2 )

  return a

def cauchy_test ( ):

#*****************************************************************************80
#
## CAUCHY_TEST tests CAUCHY.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 January 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print
  from r8vec_uniform_01 import r8vec_uniform_01

  print ''
  print 'CAUCHY_TEST'
  print '  CAUCHY computes the CAUCHY matrix.'

  m = 4
  n = m
  seed = 123456789
  x, seed = r8vec_uniform_01 ( n, seed )
  y, seed = r8vec_uniform_01 ( n, seed )
  a = cauchy ( n, x, y )
  r8mat_print ( n, n, a, '  CAUCHY matrix:' )

  print ''
  print 'CAUCHY_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  cauchy_test ( )
  timestamp ( )
