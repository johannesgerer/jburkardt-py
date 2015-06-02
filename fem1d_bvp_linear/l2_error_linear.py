#! /usr/bin/env python
#
def l2_error_linear ( n, x, u, exact ):

#*****************************************************************************80
#
## L2_ERROR_LINEAR estimates the L2 error norm of a finite element solution.
#
#  Location:
#
#    http://people.sc.fsu.edu/~jburkardt/py_src/fem1d_bvp_linear/l2_error_linear.py
#
#  Discussion:
#
#    We assume the finite element method has been used, over an interval [A,B]
#    involving N nodes, with piecewise linear elements used for the basis.
#    The coefficients U(1:N) have been computed, and a formula for the
#    exact solution is known.
#
#    This function estimates the L2 norm of the error:
#
#      L2_NORM = Integral ( A <= X <= B ) ( U(X) - EXACT(X) )^2 dX
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
#    Input, integer N, the number of nodes.
#
#    Input, real X(N), the mesh points.
#
#    Input, real U(N), the finite element coefficients.
#
#    Input, function EQ = EXACT ( X ), returns the value of the exact
#    solution at the point X.
#
#    Output, real E2, the estimated L2 norm of the error.
#
  from math import sqrt
  import numpy as np

  e2 = 0.0
#
#  Define a 2 point Gauss-Legendre quadrature rule on [-1,+1].
#
  quad_num = 2
  abscissa = np.array ( [ -0.577350269189625764509148780502, \
                          +0.577350269189625764509148780502 ] )
  weight = np.array ( [ 1.0, 1.0 ] )
#
#  Integrate over each interval.
#
  e_num = n - 1

  for e in range ( 0, e_num ):

    l = e
    xl = x[l]
    ul = u[l]

    r = e + 1
    xr = x[r]
    ur = u[r]

    for q in range ( 0, quad_num ):

      xq = ( ( 1.0 - abscissa[q] ) * xl   \
           + ( 1.0 + abscissa[q] ) * xr ) \
           /   2.0

      wq = weight[q] * ( xr - xl ) / 2.0
#
#  Use the fact that U is a linear combination of piecewise linears.
#
      uq = ( ( xr - xq      ) * ul \
           + (      xq - xl ) * ur ) \
           / ( xr      - xl )

      eq = exact ( xq )

      e2 = e2 + wq * ( uq - eq ) ** 2

  e2 = sqrt ( e2 )

  return e2

def l2_error_linear_test ( ):

#*****************************************************************************80
#
## L2_ERROR_LINEAR_TEST tests L2_ERROR_LINEAR.
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
#    None
#
  import numpy as np
  from math import sin

  print ''
  print 'L2_ERROR_LINEAR_TEST:'
  print '  Python version:'
  print '  L2_ERROR_LINEAR computes the L2 approximation error between'
  print '  a function exact(x) and a piecewise linear function u()'
  print '  associated with n mesh points x().' 
  print ''
  print '   N    L2_Error'
  print ''

  r8_pi = 3.141592653589793
  x_n = 3

  for test in range ( 0, 6 ):
    x_lo = 0.0
    x_hi = r8_pi
    x = np.linspace ( x_lo, x_hi, x_n )
#
#  U is an approximation to sin(x).
#
    u = np.zeros ( x_n )
    for i in range ( 0, x_n ):
      u[i] = x[i] - x[i] ** 3 / 6.0

    e1 = l2_error_linear ( x_n, x, u, sin )

    print '  %2d  %g' % ( x_n, e1 )

    x_n = 2 * ( x_n - 1 ) + 1
#
#  Terminate.
#
  print ''
  print 'L2_ERROR_LINEAR_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  l2_error_linear_test ( )
  timestamp ( )
