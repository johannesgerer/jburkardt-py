#! /usr/bin/env python
#
def fem1d_model ( ):
#
## FEM1D_MODEL solves a 1D "model" boundary value problem using finite elements.
#
#  Location:
#
#    http://people.sc.fsu.edu/~jburkardt/py_src/fem1d/fem1d_model.py
#
#  Discussion:
#
#    The PDE is defined for 0 < x < 1:
#      -u'' + u = x
#    with boundary conditions
#      u(0) = 0,
#      u(1) = 0.
#
#    The exact solution is:
#      exact(x) = x - sinh(x) / sinh(1.0)
#
#    This program is different from FEM1D.PY:
#    * the problem to be solved is different, and includes a linear term;
#    * the code to assemble the matrix is different.  We evaluate all the
#      basis functions and derivatives, and then form the combinations
#      that must be added to the system matrix and right hand side.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    23 September 2014
#
#  Author:
#
#    John Burkardt
#
#  Local parameters:
#
#    Local, integer N, the number of elements.
#
  import matplotlib.pyplot as plt
  import numpy as np
  import scipy.linalg as la
  from timestamp import timestamp

  timestamp ( )
  print ""
  print "FEM1D_MODEL"
  print "  Python version"
  print "  Given the model two point boundary value problem:"
  print "    -u'' + u = x, 0 < x < 1"
  print "  with boundary conditions"
  print "    u(0) = 0, u(1) = 0,"
  print "  demonstrate how the finite element method can be used to"
  print "  define and compute a discrete approximation to the solution."
#
#  The mesh will use N+1 points between A and B.
#  These will be indexed X[0] through X[N].
#
  a = 0.0
  b = 1.0
  n = 5
  x = np.linspace ( a, b, n + 1 )

  print ""
  print "  Nodes:"
  print ""
  for i in range ( 0, n + 1 ):
    print "  %d  %f" %( i, x[i] )
#
#  Set a 3 point quadrature rule on the reference interval [0,1].
#
  ng = 3

  xg = np.array ( ( \
    0.112701665379258311482073460022, \
    0.5, \
    0.887298334620741688517926539978 ) )

  wg = np.array ( ( \
    5.0 / 18.0, \
    8.0 / 18.0, \
    5.0 / 18.0 ) )
#
#  Compute the system matrix A and right hand side RHS.
#
  A = np.zeros ( ( n + 1, n + 1 ) )
  rhs = np.zeros ( n + 1 )
#
#  Look at element E: (0, 1, 2, ..., N-1).
#
  for e in range ( 0, n ):

    l = e
    r = e + 1

    xl = x[l]
    xr = x[r]
#
#  Consider quadrature point Q: (0, 1, 2 ) in element E.
#
    for q in range ( 0, ng ):
#
#  Map XG and WG from [0,1] to
#      XQ and QQ in [XL,XR].
#
      xq = xl + xg[q] * ( xr - xl )
      wq = wg[q] * ( xr - xl )
#
#  Evaluate at XQ the basis functions and derivatives for XL and XR.
#
      phil = ( xr - xq  ) / ( xr - xl )
      philp = - 1.0 / ( xr - xl )

      phir = ( xq - xl ) / ( xr - xl )
      phirp = 1.0 / ( xr - xl )
#
#  Compute the following contributions:
#
#    L,L  L,R  L,Fx
#    R,L  R,R  R,Fx
#
      A[l][l] = A[l][l] + wq * ( philp * philp + phil * phil )
      A[l][r] = A[l][r] + wq * ( philp * phirp + phil * phir )
      rhs[l]  = rhs[l]  + wq *                   phil * rhs_fn ( xq )

      A[r][l] = A[r][l] + wq * ( phirp * philp + phir * phil )
      A[r][r] = A[r][r] + wq * ( phirp * phirp + phir * phir )
      rhs[r]  = rhs[r]  + wq *                   phir * rhs_fn ( xq )
#
#  Modify the linear system to enforce the left boundary condition.
#
  A[0,0] = 1.0
  A[0,1:n+1] = 0.0
  rhs[0] = 0.0
#
#  Modify the linear system to enforce the right boundary condition.
#
  A[n,n] = 1.0
  A[n,0:n] = 0.0
  rhs[n] = 0.0
#
#  Solve the linear system.
#
  u = la.solve ( A, rhs )
#
#  Evaluate the exact solution at the nodes.
#
  uex = np.zeros ( n + 1 )
  for i in range ( 0, n + 1 ):
    uex[i] = exact_fn ( x[i] )
#
#  Compare the solution and the error at the nodes.
#
  print ""
  print "  Node          Ucomp           Uexact          Error"
  print ""
  for i in range ( 0, n + 1 ):
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
  print "FEM1D_MODEL:"
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
  from math import sinh
  value = x - sinh ( x ) / sinh ( 1.0 )
  return value

def rhs_fn ( x ):
#
## RHS_FN evaluates the right hand side.
#
  value = x
  return value
#
#  If this script is called directly, then run it as a program.
#
if ( __name__ == '__main__' ):
  fem1d_model ( )
