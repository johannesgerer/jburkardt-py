#!/usr/bin/env python

def poly_bernoulli ( n, k ):

#*****************************************************************************80
#
## POLY_BERNOULLI evaluates the poly-Bernolli numbers with negative index.
#
#  Discussion:
#
#    The poly-Bernoulli numbers B_n^k were defined by M Kaneko
#    formally as the coefficients of X^n/n% in a particular power
#    series.  He also showed that, when the super-index is negative,
#    we have
#
#      B_n^(-k) = Sum ( 0 <= j <= min ( n, k ) )
#        (j%)^2 * S(n+1,j+1) * S(k+1,j+1)
#
#    where S(n,k) is the Stirling number of the second kind, the number of
#    ways to partition a set of size n into k nonempty subset.
#
#    B_n^(-k) is also the number of "lonesum matrices", that is, 0-1
#    matrices of n rows and k columns which are uniquely reconstructable
#    from their row and column sums.
#
#    The poly-Bernoulli numbers get large very quickly.
#
#  Table:
#
#    \ K 0  1    2     3      4       5        6
#    N
#    0   1  1    1     1      1       1        1
#    1   1  2    4     8     16      32       64
#    2   1  4   14    46    146     454     1394
#    3   1  8   46   230   1066    4718    20266
#    4   1 16  146  1066   6902   41506   237686
#    5   1 32  454  4718  41506  329462  2441314
#    6   1 64 1394 20266 237686 2441314 22934774
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Chad Brewbaker,
#    Lonesum (0,1) Matrices and Poly-Bernoulli Numbers of Negative Index,
#    MS Thesis,
#    Iowa State University, 2005.
#
#    M Kaneko,
#    Poly-Bernoulli Numbers,
#    Journal Theorie des Nombres Bordeaux,
#    Volume 9, 1997, pages 221-228.
#
#  Parameters:
#
#    Input, integer N, K, the indices.  N and K should be nonnegative.
#
#    Output, integer VALUE, the value of B_N^(-K).
#
  from stirling2 import stirling2

  if ( n < 0 ):
    value = 0
    return value

  if ( n == 0 ):
    value = 1
    return value

  if ( k < 0 ):
    value = 0
    return value

  if ( k == 0 ):
    value = 1
    return value

  jhi = min ( n, k )
  m = max ( n, k ) + 1

  s = stirling2 ( m, m )

  jfact = 1
  value = 0

  for j in range ( 0, jhi + 1 ):

    value = value + jfact * jfact * s[n,j] * s[k,j]

    jfact = jfact * ( j + 1 )

  return value

def poly_bernoulli_test ( ):

#*****************************************************************************80
#
## POLY_BERNOULLI_TEST tests POLY_BERNOULLI.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    25 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'POLY_BERNOULLI_TEST'
  print '  POLY_BERNOULLI computes the poly-Bernoulli numbers'
  print '  of negative index, B_n^(-k)'
  print ''
  print '     N     K    B_N^(-K)'
  print ''

  for k in range ( 0, 7 ):
    print ''
    for n in range ( 0, 7 ):
      b = poly_bernoulli ( n, k )

      print '  %6d  %6d  %6d' % ( n, k, b )

  print ''
  print 'POLY_BERNOULLI_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  poly_bernoulli_test ( )
  timestamp ( )
