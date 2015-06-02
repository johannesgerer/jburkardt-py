#! /usr/bin/env python
#
def fem1d_bvp_linear ( n, a, c, f, x ):

#*****************************************************************************80
#
## FEM1D_BVP_LINEAR solves a two point boundary value problem.
#
#  Location:
#
#    http://people.sc.fsu.edu/~jburkardt/py_src/fem1d_bvp_linear/fem1d_bvp_linear.py
#
#  Discussion:
#
#    The program uses the finite element method, with piecewise linear basis
#    functions to solve a boundary value problem in one dimension.
#
#    The problem is defined on the region 0 <= x <= 1.
#
#    The following differential equation is imposed between 0 and 1:
#
#      - d/dx a(x) du/dx + c(x) * u(x) = f(x)
#
#    where a(x), c(x), and f(x) are given functions.
#
#    At the boundaries, the following conditions are applied:
#
#      u(0.0) = 0.0
#      u(1.0) = 0.0
#
#    A set of N equally spaced nodes is defined on this
#    interval, with 0 = X(1) < X(2) < ... < X(N) = 1.0.
#
#    At each node I, we associate a piecewise linear basis function V(I,X),
#    which is 0 at all nodes except node I.  This implies that V(I,X) is
#    everywhere 0 except that
#
#    for X(I-1) <= X <= X(I):
#
#      V(I,X) = ( X - X(I-1) ) / ( X(I) - X(I-1) ) 
#
#    for X(I) <= X <= X(I+1):
#
#      V(I,X) = ( X(I+1) - X ) / ( X(I+1) - X(I) )
#
#    We now assume that the solution U(X) can be written as a linear
#    sum of these basis functions:
#
#      U(X) = sum ( 1 <= J <= N ) U(J) * V(J,X)
#
#    where U(X) on the left is the function of X, but on the right,
#    is meant to indicate the coefficients of the basis functions.
#
#    To determine the coefficient U(J), we multiply the original
#    differential equation by the basis function V(J,X), and use
#    integration by parts, to arrive at the I-th finite element equation:
#
#        Integral A(X) * U'(X) * V'(I,X) + C(X) * U(X) * V(I,X) dx 
#      = Integral F(X) * V(I,X) dx
#
#    We note that the functions U(X) and U'(X) can be replaced by
#    the finite element form involving the linear sum of basis functions,
#    but we also note that the resulting integrand will only be nonzero
#    for terms where J = I - 1, I, or I + 1.
#
#    By writing this equation for basis functions I = 2 through N - 1,
#    and using the boundary conditions, we have N linear equations
#    for the N unknown coefficients U(1) through U(N), which can
#    be easily solved.
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
#    Input, function A ( X ), evaluates a(x);
#
#    Input, function C ( X ), evaluates c(x);
#
#    Input, function F ( X ), evaluates f(x);
#
#    Input, real X(N), the mesh points.
#
#    Output, real U(N), the finite element coefficients, which are also
#    the value of the computed solution at the mesh points.
#
  import numpy as np
  import scipy.linalg as la
#
#  Define a 2 point Gauss-Legendre quadrature rule on [-1,+1].
#
  quad_num = 2
  abscissa = np.array ( [ -0.577350269189625764509148780502, \
                          +0.577350269189625764509148780502 ] )
  weight = np.array ( [ 1.0, 1.0 ] )
#
#  Make room for the matrix A and right hand side b.
#
  A = np.zeros ( [ n, n ] )
  b = np.zeros ( n )
#
#  We assemble the finite element matrix by looking at each element,
#  that is, each interval [ X(L), X(R) ].
#
#  There are only two nonzero piecewise linear basis functions in this
#  element, and we can call them VL and VR.  So the only integrals we
#  need to compute involve products of:
#
#    VL * VL   VR * VL    F * VL
#    VR * VL   VR * VR    F * VR
#
#  and
#
#    VL' * VL'   VR' * VL'
#    VR' * VL'   VR' * VR'
#
  e_num = n - 1

  for e in range ( 0, e_num ):

    l = e
    xl = x[l]

    r = e + 1
    xr = x[r]

    for q in range ( 0, quad_num ):

      xq = ( ( 1.0 - abscissa[q] ) * xl   \
           + ( 1.0 + abscissa[q] ) * xr ) \
           / 2.0

      wq = weight[q] * ( xr - xl ) / 2.0

      vl = ( xr - xq ) / ( xr - xl )
      vlp =     - 1.0  / ( xr - xl )

      vr = ( xq - xl ) / ( xr - xl )
      vrp = +1.0       / ( xr - xl )

      axq = a ( xq )
      cxq = c ( xq )
      fxq = f ( xq )

      A[l,l] = A[l,l] + wq * ( vlp * axq * vlp + vl * cxq * vl )
      A[l,r] = A[l,r] + wq * ( vlp * axq * vrp + vl * cxq * vr )
      b[l]   = b[l]   + wq * ( vl * fxq )

      A[r,l] = A[r,l] + wq * ( vrp * axq * vlp + vr * cxq * vl )
      A[r,r] = A[r,r] + wq * ( vrp * axq * vrp + vr * cxq * vr )
      b[r]   = b[r]   + wq * ( vr * fxq )
#
#  Equation 0 is the left boundary condition, U(0) = 0.0;
#
  for j in range ( 0, n ):
    A[0,j] = 0.0
  A[0,0] = 1.0
  b[0] = 0.0
#
#  We can keep the matrix symmetric by using the boundary condition
#  to eliminate U(0) from all equations but #0.
#
  for i in range ( 1, n ):
    b[i] = b[i] - A[i,0] * b[0]
    A[i,0] = 0.0
#
#  Equation N-1 is the right boundary condition, U(N-1) = 0.0;
#
  for j in range ( 0, n ):
    A[n-1,j] = 0.0
  A[n-1,n-1] = 1.0
  b[n-1] = 0.0
#
#  We can keep the matrix symmetric by using the boundary condition
#  to eliminate U(N-1) from all equations but #N-1.
#
  for i in range ( 0, n - 1 ):
    b[i] = b[i] - A[i,n-1] * b[n-1]
    A[i,n-1] = 0.0
#
#  Solve the linear system for the finite element coefficients U.
#
  u = la.solve ( A, b )

  return u

def fem1d_bvp_linear_test ( ):

#*****************************************************************************80
#
## FEM1D_BVP_LINEAR_TEST tests FEM1D_BVP_LINEAR.
#
#  Discussion:
#
#    - uxx + u = x  for 0 < x < 1
#    u(0) = u(1) = 0
#
#    exact  = x - sinh(x) / sinh(1)
#    exact' = 1 - cosh(x) / sinh(1)
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
#  Reference:
#
#    Dianne O'Leary,
#    Scientific Computing with Case Studies,
#    SIAM, 2008,
#    ISBN13: 978-0-898716-66-5,
#    LC: QA401.O44.
#
  import matplotlib.pyplot as plt
  import numpy as np
  from h1s_error_linear import h1s_error_linear
  from l1_error import l1_error
  from l2_error_linear import l2_error_linear

  n = 11

  print ''
  print 'FEM1D_BVP_LINEAR_TEST'
  print '  Solve -( A(x) U\'(x) )\' + C(x) U(x) = F(x)'
  print '  for 0 < x < 1, with U(0) = U(1) = 0.'
  print '  A(X)  = 1.0'
  print '  C(X)  = 1.0'
  print '  F(X)  = X'
  print '  U(X)  = X - SINH(X) / SINH(1)'
  print ''
  print '  Number of nodes = %d' % ( n )
#
#  Geometry definitions.
#
  x_lo = 0.0
  x_hi = 1.0
  x = np.linspace ( x_lo, x_hi, n )

  u = fem1d_bvp_linear ( n, a, c, f, x )

  g = np.zeros ( n )
  for i in range ( 0, n ):
    g[i] = exact ( x[i] )
#
#  Print a table.
#
  print ''
  print '     I    X         U         Uexact    Error'
  print ''

  for i in range ( 0, n ):
    print '  %4d  %8f  %8f  %8f  %8e' \
      % ( i, x[i], u[i], g[i], abs ( u[i] - g[i] ) )
#
#  Compute error norms.
#
  e1 = l1_error ( n, x, u, exact )
  e2 = l2_error_linear ( n, x, u, exact )
  h1s = h1s_error_linear ( n, x, u, exactp )

  print ''
  print '  l1 norm of error  = %g' % ( e1 )
  print '  L2 norm of error  = %g' % ( e2 )
  print '  Seminorm of error = %g' % ( h1s  )
#
#  Plot the computed solution.
#
  fig = plt.figure ( )
  plt.plot ( x, u, 'bo-' )
  plt.xlabel ( '<---X--->' )
  plt.ylabel ( '<---U(X)--->' )
  plt.title ( 'FEM1D_BVP_LINEAR_TEST Solution' )
  plt.savefig ( 'fem1d_bvp_linear_test.png' )
  plt.show ( )
#
#  Terminate.
#
  print ''
  print 'FEM1D_BVP_LINEAR_TEST'
  print '  Normal end of execution.'

  return

def a ( x ):
  value = 1.0
  return value

def c ( x ):
  value = 1.0
  return value

def exact ( x ):
  from math import sinh
  value = x - sinh ( x ) / sinh ( 1.0 )
  return value

def exactp ( x ):
  from math import cosh
  from math import sinh
  value = 1.0 - cosh ( x ) / sinh ( 1.0 )
  return value

def f ( x ):
  value = x
  return value

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  fem1d_bvp_linear_test ( )
  timestamp ( )
