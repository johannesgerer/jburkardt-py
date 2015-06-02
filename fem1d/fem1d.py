#! /usr/bin/env python
#
def fem1d ( ):
#
## FEM1D solves a 1D boundary value problem using finite elements.
#
#  Location:
#
#    http://people.sc.fsu.edu/~jburkardt/py_src/fem1d/fem1d.py
#
#  Discussion:
#
#    The PDE is defined for 0 < x < 1:
#      -u'' = f
#    with right hand side
#      f(x) = -(exact(x)'') 
#    and boundary conditions
#      u(0) = exact(0),
#      u(1) = exact(1).
#
#    The exact solution is:
#      exact(x) = x * ( 1 - x ) * exp ( x )
#    The boundary conditions are
#      u(0) = 0.0 = exact(0.0),
#      u(1) = 0.0 = exact(1.0).
#    The right hand side is:
#      f(x) = x * ( x + 3 ) * exp ( x ) = - ( exact''(x) )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    13 September 2014
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
  print "FEM1D"
  print "  Python version"
  print "  Given the two point boundary value problem:"
  print "    -u'' = x * ( x + 3 ) * exp ( x ), 0 < x < 1"
  print "  with boundary conditions"
  print "    u(0) = 0, u(1) = 0,"
  print "  demonstrate how the finite element method can be used to"
  print "  define and compute a discrete approximation to the solution."
#
#  Define the mesh, N+1 points between A and B.
#  These will be X[0] through X[N].
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

    xl = x[e]
    xr = x[e+1]
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
#  Consider the I-th test function PHI(I,X) and its derivative PHI'(I,X).
#
      for i_local in range ( 0, 2 ):
        i = i_local + e

        if ( i_local == 0 ):
          phii = ( xq - xr ) / ( xl - xr )
          phiip = 1.0 / ( xl - xr )
        else:
          phii = ( xq - xl ) / ( xr - xl )
          phiip = 1.0 / ( xr - xl )

        rhs[i] = rhs[i] + wq * phii * rhs_fn ( xq )
#
#  Consider the J-th basis function PHI(J,X) and its derivative PHI'(J,X).
#  (It turns out we don't need PHI for this particular problem, only PHI')
#
        for j_local in range ( 0, 2 ):
          j = j_local + e

          if ( j_local == 0 ):
            phijp = 1.0 / ( xl - xr )
          else:
            phijp = 1.0 / ( xr - xl )

          A[i][j] = A[i][j] + wq * phiip * phijp
#
#  Modify the linear system to enforce the left boundary condition.
#
  A[0,0] = 1.0
  A[0,1:n+1] = 0.0
  rhs[0] = exact_fn ( x[0] )
#
#  Modify the linear system to enforce the right boundary condition.
#
  A[n,n] = 1.0
  A[n,0:n] = 0.0
  rhs[n] = exact_fn ( x[n] )
#
#  I wanted to check the matrix and right hand side so I printed them.
#  I turned the printing off using "False" as the condition.
#
  if False:
    print ""
    print "  Matrix and RHS:"
    print ""
    for i in range ( 0, n + 1 ):
      for j in range ( 0, n + 1 ):
        print "  %f" % ( A[i,j] ),
      print "  %f" % ( rhs[i] )
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
  print "FEM1D:"
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
  fem1d ( )
