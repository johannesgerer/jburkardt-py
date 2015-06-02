#! /usr/bin/env python
#
def fem1d_bvp_quadratic ( ):
#
## FEM1D_BVP_QUADRATIC solves a two point boundary value problem.
#
#  Location:
#
#    http://people.sc.fsu.edu/~jburkardt/py_src/fem1d_bvp_quadratic/fem1d_bvp_quadratic.html
#
#  Discussion:
#
#    The finite element method is used, with piecewise quadratic elements.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 September 2014
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np
  import scipy.linalg as la
  from timestamp import timestamp

  timestamp ( )
  print ""
  print "FEM1D_BVP_QUADRATIC"
  print "  Python version"
  print "  Given the two point boundary value problem:"
  print "    -u'' = x * ( x + 3 ) * exp ( x ), 0 < x < 1"
  print "  with boundary conditions"
  print "    u(0) = 0, u(1) = 0,"
  print "  demonstrate how the finite element method can be used to"
  print "  define and compute a discrete approximation to the solution."
  print "  This program uses piecewise quadratic elements."
#
#  Define the interval.
#
  a = 0.0
  b = 1.0
#
#  Define the mesh, N_NUM evenly spaced points between A and B.
#  Because we are using quadratic elements, we need N_NUM to be odd!
#
  n_num = 11
  x = np.linspace ( a, b, n_num )

  print ""
  print "  Nodes:"
  print ""
  for i in range ( 0, n_num ):
    print "  %d  %f" %( i, x[i] )
#
#  Set the number of elements.
#
#  Using quadratic elements, the relationship between number of nodes
#  and number of elements is more complicated.
#
#  0  1  2  3  4  5  6  7  8  8 10  0-based node indices
#  1  2  3  4  5  6  7  8  9 10 11  1-based node indices
#  N--n--N--n--N--n--N--n--N--n--N  11 nodes
#  *-----*-----*-----*-----*-----*   5 elements
#     1     2     3     4     5      1-based node indices
#     0     1     2     3     4      0-based node indices
#
  e_num = ( n_num - 1 ) / 2
#
#  Set a 3 point quadrature rule on the reference interval [-1,1].
#
  q_num = 3

  xg = np.array ( ( \
    -0.774596669241483377035853079956, \
     0.0, \
     0.774596669241483377035853079956 ) )

  wg = np.array ( ( \
    5.0 / 9.0, \
    8.0 / 9.0, \
    5.0 / 9.0 ) )
#
#  Compute the system matrix A and right hand side RHS.
#
  A = np.zeros ( ( n_num, n_num ) )
  rhs = np.zeros ( n_num )
#
#  Look at element E: (0, 1, 2, ..., E_NUM-1).
#
  for e in range ( 0, e_num ):

    l = 2 * e
    m = 2 * e + 1
    r = 2 * e + 2

    xl = x[l]
    xm = x[m]
    xr = x[r]
#
#  Consider quadrature point Q: (0, 1, 2 ) in element E.
#
    for q in range ( 0, q_num ):
#
#  Map XG and WG from [-1,1] to
#      XQ and WQ in [XL,XM,XR].
#
      xq = xl + ( xg[q] + 1.0 ) * ( xr - xl ) / 2.0
      wq = wg[q] * ( xr - xl ) / 2.0
#
#  Evaluate PHI(L), PHI(M) and PHI(R), and their derivatives at XQ.
#
#  It must be true that PHI(L) is 1 at XL and 0 at XM and XR,
#  with similar requirements for PHI(M) and PHI(R).
#
      phil =    ( xq - xm ) * ( xq - xr )   / \
              ( ( xl - xm ) * ( xl - xr ) )
      philp = ( ( xq - xr ) + ( xq - xm ) ) / \
              ( ( xl - xm ) * ( xl - xr ) )

      phim =    ( xq - xl ) * ( xq - xr )   / \
              ( ( xm - xl ) * ( xm - xr ) )
      phimp = ( ( xq - xr ) + ( xq - xl ) ) / \
              ( ( xm - xl ) * ( xm - xr ) )

      phir =    ( xq - xl ) * ( xq - xm )   / \
              ( ( xr - xl ) * ( xr - xm ) )
      phirp = ( ( xq - xm ) + ( xq - xl ) ) / \
              ( ( xr - xl ) * ( xr - xm ) )

      fxq = rhs_fn ( xq )
#
#  Add the terms from this element to the matrix.
#
      A[l][l] = A[l][l] + wq * philp * philp
      A[l][m] = A[l][m] + wq * philp * phimp
      A[l][r] = A[l][r] + wq * philp * phirp
      rhs[l]  = rhs[l]  + wq * phil  * fxq

      A[m][l] = A[m][l] + wq * phimp * philp
      A[m][m] = A[m][m] + wq * phimp * phimp
      A[m][r] = A[m][r] + wq * phimp * phirp
      rhs[m]  = rhs[m]  + wq * phim  * fxq

      A[r][l] = A[r][l] + wq * phirp * philp
      A[r][m] = A[r][m] + wq * phirp * phimp
      A[r][r] = A[r][r] + wq * phirp * phirp
      rhs[r]  = rhs[r]  + wq * phir  * fxq
#
#  Modify the linear system to enforce the left boundary condition.
#
  A[0,0] = 1.0
  A[0,1:n_num-1] = 0.0
  rhs[0] = exact_fn ( x[0] )
#
#  Modify the linear system to enforce the right boundary condition.
#
  A[n_num-1,n_num-1] = 1.0
  A[n_num-1,0:n_num-1] = 0.0
  rhs[n_num-1] = exact_fn ( x[n_num-1] )

  r8vec_print ( n_num, rhs, '  RHS' )
#
#  Solve the linear system.
#
  u = la.solve ( A, rhs )
#
#  Evaluate the exact solution at the nodes.
#
  uex = np.zeros ( n_num )
  for i in range ( 0, n_num ):
    uex[i] = exact_fn ( x[i] )
#
#  Compare the solution and the error at the nodes.
#
  print ""
  print "  Node          Ucomp           Uexact          Error"
  print ""
  for i in range ( 0, n_num ):
    err = abs ( uex[i] - u[i] )
    print "  %4d  %14.6g  %14.6g  %14.6g" % ( i, u[i], uex[i], err )
#
#  Plot the computed solution and the exact solution.
#  Evaluate the exact solution at enough points that the curve will look smooth.
#
  npp = 51
  xp = np.linspace ( a, b, npp )
  up = np.zeros ( npp )
  for i in range ( 0, npp ):
    up[i] = exact_fn ( xp[i] )

  plt.plot ( x, u, 'bo-', xp, up, 'r.' )
  plt.show ( )
#
#  Terminate.
#
  print ""
  print "FEM1D_BVP_QUADRATIC:"
  print "  Normal end of execution."
  print ""
  timestamp ( )
#
#  That is the end of the main program.
#  Now we list some helper functions.
#
def exact_fn ( x ):
#
## EXACT_FN evaluates the exact solution.
#
  from math import exp
  value = x * ( 1 - x ) * exp ( x )
  return value

def rhs_fn ( x ):
#
## RHS_FN evaluates the right hand side.
#
  from math import exp
  value = x * ( x + 3 ) * exp ( x )
  return value
#
#  If this script is called directly, then run it as a program.
#
if ( __name__ == '__main__' ):
  fem1d_bvp_quadratic ( )
