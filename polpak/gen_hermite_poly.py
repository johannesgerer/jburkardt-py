#!/usr/bin/env python
#
def gen_hermite_poly ( n, x, mu ):

#*****************************************************************************80
#
## GEN_HERMITE_POLYevaluates the generalized Hermite polynomials at X.
#
#  Discussion:
#
#    The generalized Hermite polynomials are orthogonal under the weight
#    function:
#
#      w(x) = |x|^(2*MU) * exp ( - x^2 )
#
#    over the interval (-oo,+oo).
#
#    When MU = 0, the generalized Hermite polynomial reduces to the standard
#    Hermite polynomial.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Theodore Chihara,
#    An Introduction to Orthogonal Polynomials,
#    Gordon and Breach, 1978,
#    ISBN: 0677041500,
#    LC: QA404.5 C44.
#
#  Parameters:
#
#    Input, integer N, the highest order polynomial to compute.
#
#    Input, real X, the point at which the polynomials are
#    to be evaluated.
#
#    Input, real MU, the parameter.
#    - 1 / 2 < MU.
#
#    Output, real P(1:N+1), the values of the first N+1
#    polynomials at the point X.
#
  import numpy as np

  p = np.zeros ( n + 1 )


  p[0] = 1.0

  if ( 0 < n ):
 
    p[1] = 2.0 * x

    for i in range ( 1, n ):
 
      if ( ( i % 2 ) == 0 ):
        theta = 0.0
      else:
        theta = 2.0 * mu

      p[i+1] = 2.0 * x * p[i] - 2.0 * ( i + theta ) * p[i-1]

  return p

def gen_hermite_poly_test ( ):

#*****************************************************************************80
#
## GEN_HERMITE_POLY_TEST tests GEN_HERMITE_POLY.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 10

  mu_test = np.array ( ( 0.0, 0.0, 0.1, 0.1, 0.5, 1.0 ) );
  x_test = np.array ( ( 0.0, 1.0, 0.0, 0.5, 0.5, 0.5 ) )

  print ''
  print 'GEN_HERMITE_POLY_TEST'
  print '  GEN_HERMITE_POLY evaluates the generalized Hermite polynomial.'

  for i in range ( 0, 6 ):

    x = x_test[i]
    mu = mu_test[i]

    print ''
    print '  Table of H(N,MU)(X) for'
    print ''
    print '    N(max) = %d' % ( n )
    print '    MU =     %f' % ( mu )
    print '    X =      %f' % ( x )
    print ''
  
    c = gen_hermite_poly ( n, x, mu )
 
    for j in range ( 0, n + 1 ):
      print '  %4d  %12f' % ( j, c[j] )
 
  print ''
  print 'GEN_HERMITE_POLY_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  gen_hermite_poly_test ( )
  timestamp ( )
