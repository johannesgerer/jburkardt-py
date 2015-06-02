#! /usr/bin/env python
#
def colleague ( n, c ):

#*****************************************************************************80
#
## COLLEAGUE returns the COLLEAGUE matrix.
#
#  Discussion:
#
#    The colleague matrix is an analog of the companion matrix, adapted
#    for use with polynomials represented by a sum of Chebyshev polynomials.
#
#    Let the N-th degree polynomial be defined by
#
#      P(X) = C(N)*T_N(X) + C(N-1)*T_(N-1)(X) + ... + C(1)*T1(X) + C(0)*T0(X)
#
#    where T_I(X) is the I-th Chebyshev polynomial.
#
#    Then the roots of P(X) are the eigenvalues of the colleague matrix A(C):
#
#        0   1   0   ...  0                        0    0    0   ...   0
#       1/2  0  1/2  ...  0                        0    0    0   ...   0
#        0  1/2  0   ...  0      - 1/(2*C(N)) *    0    0    0   ...   0
#       ... ... ...  ... ...                      ...  ...  ...  ...  ...
#       ... ... ...   0  1/2                      ...  ...  ...  ...   0
#       ... ... ...  1/2  0                       C(0) C(1) C(2) ... C(N-1)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    I J Good,
#    The Colleague Matrix: A Chebyshev Analogue of the Companion Matrix,
#    The Quarterly Journal of Mathematics,
#    Volume 12, Number 1, 1961, pages 61-68.
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, real C(0:N), the coefficients of the polynomial.
#    C(N) should not be zero#
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  if ( n == 1 ):

    a[0,0] = - c[0] / c[1]

  else:

    a[0,1] = 1.0;

    for i in range ( 1, n ):
      a[i,i-1] = 0.5

    for i in range ( 1, n - 1 ):
      a[i,i+1] = 0.5

    for j in range ( 0, n ):
      a[n-1,j] = a[n-1,j] - 0.5 * c[j] / c[n]

  return a

def colleague_test ( ):

#*****************************************************************************80
#
## COLLEAGUE_TEST tests COLLEAGUE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 March 2015
#
#  Author:
#
#    John Burkardt
#
  from r8vec_uniform_ab import r8vec_uniform_ab
  from r8mat_print import r8mat_print

  print ''
  print 'COLLEAGUE_TEST'
  print '  COLLEAGUE computes the COLLEAGUE matrix.'

  m = 5
  n = m
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  c, seed = r8vec_uniform_ab ( n + 1, r8_lo, r8_hi, seed )

  a = colleague ( n, c )
 
  r8mat_print ( m, n, a, '  COLLEAGUE matrix:' )

  print ''
  print 'COLLEAGUE_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  colleague_test ( )
  timestamp ( )
