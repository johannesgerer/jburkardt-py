#! /usr/bin/env python
#
def l1_error ( n, x, u, exact ):

#*****************************************************************************80
#
## L1_ERROR estimates the l1 error norm of a finite element solution.
#
#  Location:
#
#    http://people.sc.fsu.edu/~jburkardt/py_src/fem1d_bvp_linear/l1_error.py
#
#  Discussion:
#
#    We assume the finite element method has been used, over an interval [A,B]
#    involving N nodes.
#
#    The coefficients U(1:N) have been computed, and a formula for the
#    exact solution is known.
#
#    This function estimates the little l1 norm of the error:
#      L1_NORM = sum ( 1 <= I <= N ) abs ( U(i) - EXACT(X(i)) )
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
#    Output, real E1, the little l1 norm of the error.
#
  e1 = 0.0
  for i in range ( 0, n ):
    e1 = e1 + abs ( u[i] - exact ( x[i] ) )

  e1 = e1 / n

  return e1

def l1_error_test ( ):

#*****************************************************************************80
#
## L1_ERROR_TEST tests L1_ERROR.
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
  print 'L1_ERROR_TEST:'
  print '  Python version:'
  print '  L1_ERROR computes the little l1 approximation error between'
  print '  a function exact(x) and a vector of n values u() at points x().' 
  print ''
  print '   N    L1_Error'
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

    e1 = l1_error ( x_n, x, u, sin )

    print '  %2d  %g' % ( x_n, e1 )

    x_n = 2 * ( x_n - 1 ) + 1
#
#  Terminate.
#
  print ''
  print 'L1_ERROR_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  l1_error_test ( )
  timestamp ( )
