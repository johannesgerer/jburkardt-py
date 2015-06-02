#! /usr/bin/env python
#
def h1s_error_linear ( n, x, u, exact_ux ):

#*****************************************************************************80
#
## H1S_ERROR_LINEAR: seminorm error of a finite element solution.
#
#  Location:
#
#    http://people.sc.fsu.edu/~jburkardt/py_src/fem1d_bvp_linear/h1s_error_linear.py
#
#  Discussion:
#
#    We assume the finite element method has been used, over an interval [A,B]
#    involving N nodes, with piecewise linear elements used for the basis.
#    The finite element solution U(x) has been computed, and a formula for the
#    exact derivative V'(x) is known.
#
#    This function estimates the H1 seminorm of the error:
#
#      H1S = sqrt ( integral ( A <= x <= B ) ( U'(x) - V'(x) )^2 dx
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
#    Input, function EQ = EXACT_UX ( X ), returns the value of the exact
#    derivative at the point X.
#
#    Output, real H1S, the estimated seminorm of the error.
#
  from math import sqrt
  import numpy as np

  h1s = 0.0
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
#  The piecewise linear derivative is a constant in the interval.
#
      uxq = ( ur - ul ) / ( xr - xl )

      exq = exact_ux ( xq )

      h1s = h1s + wq * ( uxq - exq ) ** 2

  h1s = sqrt ( h1s )

  return h1s

def h1s_error_linear_test ( ):

#*****************************************************************************80
#
## H1S_ERROR_LINEAR_TEST tests H1S_ERROR_LINEAR.
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
  from math import cos

  print ''
  print 'H1S_ERROR_LINEAR_TEST:'
  print '  Python version:'
  print '  H1S_ERROR_LINEAR computes the H1 seminorm approximation error between'
  print '  between the exact derivative of a function and the derivative'
  print '  of a piecewise linear approximation to the function,'
  print '  associated with n mesh points x().' 
  print ''
  print '   N    H1S_Error'
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
#
#  Compare the derivative of the piecewise interpolant of U
#  to the actual derivative, cos(x).
#
    e1 = h1s_error_linear ( x_n, x, u, cos )

    print '  %2d  %g' % ( x_n, e1 )

    x_n = 2 * ( x_n - 1 ) + 1
#
#  Terminate.
#
  print ''
  print 'H1S_ERROR_LINEAR_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  h1s_error_linear_test ( )
  timestamp ( )

