#! /usr/bin/env python
#
def fem2d_bvp_linear ( ):
#
## FEM2D_BVP_LINEAR solves a 2D boundary value problem in the unit square.
#
#  Location:
#
#    http://people.sc.fsu.edu/~jburkardt/py_src/fem2d_bvp_linear/fem2d_bvp_linear.py
#
#  Discussion:
#
#    The PDE is defined for 0 < x < 1, 0 < y < 1:
#      - uxx - uyy = f(x)
#    with boundary conditions
#      u(0,y) = 0,
#      u(1,y) = 0,
#      u(x,0) = 0,
#      u(x,1) = 0.
#
#    The exact solution is:
#      exact(x) = x * ( 1 - x ) * y * ( 1 - y ).
#    The right hand side f(x) is:
#      f(x) = 2 * x * ( 1 - x ) + 2 * y * ( 1 - y )
#
#    The unit square is divided into N by N squares.  Bilinear finite 
#    element basis functions are defined, and the solution is sought as a
#    piecewise linear combination of these basis functions.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    13 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Local parameters:
#
#    Local, integer ELEMENT_NUM, the number of elements.
#
#    Local, integer LINEAR_ELEMENT_NUM, the number of elements 
#    in a row in the X or Y dimension.
#
#    Local, integer NODE_LINEAR_NUM, the number of nodes in the X or Y dimension.
#
#    Local, integer NODE_NUM, the number of nodes.
#
  import numpy as np
  import scipy.linalg as la
  from timestamp import timestamp

  timestamp ( )
  print ""
  print "FEM2D_BVP_LINEAR"
  print "  Python version"
  print "  Given the boundary value problem on the unit square:"
  print "    - uxx - uyy = x, 0 < x < 1, 0 < y < 1"
  print "  with boundary conditions"
  print "    u(0,y) = u(1,y) = u(x,0) = u(x,1) = 0,"
  print "  demonstrate how the finite element method can be used to"
  print "  define and compute a discrete approximation to the solution."
  print ""
  print "  This program uses quadrilateral elements"
  print "  and piecewise continuous bilinear basis functions."

  element_linear_num = 4
  node_linear_num = element_linear_num + 1
  element_num = element_linear_num * element_linear_num
  node_num = node_linear_num * node_linear_num
#
#  Set the coordinates of the nodes.
#  The same grid is used for X and Y.
#
  a = 0.0
  b = 1.0
  grid = np.linspace ( a, b, node_linear_num )

  print ""
  print "  Nodes along X axis:"
  print ""
  for i in range ( 0, node_linear_num ):
    print "  %d  %f" %( i, grid[i] )
#
#  Set up a quadrature rule.
#  This rule is defined on the reference interval [0,1].
#
  quad_num = 3

  quad_point = np.array ( ( \
    0.112701665379258311482073460022, \
    0.5, \
    0.887298334620741688517926539978 ) )

  quad_weight = np.array ( ( \
    5.0 / 18.0, \
    8.0 / 18.0, \
    5.0 / 18.0 ) )
#
#  Compute the system matrix A and right hand side RHS.
#  There is an unknown at every node.
#
  A = np.zeros ( ( node_num, node_num ) )
  rhs = np.zeros ( node_num )
#
#  Look at the square in row EX and column EY:
#
#    N  *-----*
#       |     |
#       |     |
#    Y  |     |
#       |     |
#       |     |
#    S  *-----*
#
#       W  X  E
#
  for ex in range ( 0, element_linear_num ):

    w = ex
    e = ex + 1

    xw = grid[w]
    xe = grid[e]

    for ey in range ( 0, element_linear_num ):

      s = ey
      n = ey + 1

      ys = grid[s]
      yn = grid[n]
#
#  Determine the node indices.
#
      sw =   ey       * node_linear_num + ex
      se =   ey       * node_linear_num + ex + 1
      nw = ( ey + 1 ) * node_linear_num + ex
      ne = ( ey + 1 ) * node_linear_num + ex + 1
#
#  The 2D quadrature rule is the "product" of X and Y copies of the 1D rule.
#
      for qx in range ( 0, quad_num ):
        xq = xw + quad_point[qx] * ( xe - xw )
        for qy in range ( 0, quad_num ):
          yq = ys + quad_point[qy] * ( yn - ys )
          wq = quad_weight[qx] * quad_weight[qy] * ( xe - xw ) * ( yn - ys )
#
#  Evaluate all four basis functions, and their X and Y derivatives.
#
          vsw  = ( xe - xq ) / ( xe - xw ) * ( yn - yq ) / ( yn - ys )
          vswx = (    -1.0 ) / ( xe - xw ) * ( yn - yq ) / ( yn - ys )
          vswy = ( xe - xq ) / ( xe - xw ) * (    -1.0 ) / ( yn - ys )

          vse  = ( xq - xw ) / ( xe - xw ) * ( yn - yq ) / ( yn - ys )
          vsex = ( 1.0     ) / ( xe - xw ) * ( yn - yq ) / ( yn - ys )
          vsey = ( xq - xw ) / ( xe - xw ) * (    -1.0 ) / ( yn - ys )

          vnw  = ( xe - xq ) / ( xe - xw ) * ( yq - ys ) / ( yn - ys ) 
          vnwx = (    -1.0 ) / ( xe - xw ) * ( yq - ys ) / ( yn - ys ) 
          vnwy = ( xe - xq ) / ( xe - xw ) * ( 1.0     ) / ( yn - ys ) 

          vne  = ( xq - xw ) / ( xe - xw ) * ( yq - ys ) / ( yn - ys )
          vnex = ( 1.0     ) / ( xe - xw ) * ( yq - ys ) / ( yn - ys )
          vney = ( xq - xw ) / ( xe - xw ) * ( 1.0     ) / ( yn - ys )
#
#  Compute contributions to the stiffness matrix.
#
          A[sw,sw] = A[sw,sw] + wq * ( vswx * vswx + vswy * vswy )
          A[sw,se] = A[sw,se] + wq * ( vswx * vsex + vswy * vsey )
          A[sw,nw] = A[sw,nw] + wq * ( vswx * vnwx + vswy * vnwy )
          A[sw,ne] = A[sw,ne] + wq * ( vswx * vnex + vswy * vney )
          rhs[sw]   = rhs[sw] + wq *   vsw  * rhs_fn ( xq, yq )

          A[se,sw] = A[se,sw] + wq * ( vsex * vswx + vsey * vswy )
          A[se,se] = A[se,se] + wq * ( vsex * vsex + vsey * vsey )
          A[se,nw] = A[se,nw] + wq * ( vsex * vnwx + vsey * vnwy )
          A[se,ne] = A[se,ne] + wq * ( vsex * vnex + vsey * vney )
          rhs[se]   = rhs[se] + wq *   vse  * rhs_fn ( xq, yq )

          A[nw,sw] = A[nw,sw] + wq * ( vnwx * vswx + vnwy * vswy )
          A[nw,se] = A[nw,se] + wq * ( vnwx * vsex + vnwy * vsey )
          A[nw,nw] = A[nw,nw] + wq * ( vnwx * vnwx + vnwy * vnwy )
          A[nw,ne] = A[nw,ne] + wq * ( vnwx * vnex + vnwy * vney )
          rhs[nw]   = rhs[nw] + wq *   vnw  * rhs_fn ( xq, yq )

          A[ne,sw] = A[ne,sw] + wq * ( vnex * vswx + vney * vswy )
          A[ne,se] = A[ne,se] + wq * ( vnex * vsex + vney * vsey )
          A[ne,nw] = A[ne,nw] + wq * ( vnex * vnwx + vney * vnwy )
          A[ne,ne] = A[ne,ne] + wq * ( vnex * vnex + vney * vney )
          rhs[ne]   = rhs[ne] + wq *   vne  * rhs_fn ( xq, yq )
#
#  Modify the linear system to enforce the boundary conditions where
#  X = 0 or 1 or Y = 0 or 1.
#
  v = 0
  for j in range ( 0, node_linear_num ):
    for i in range ( 0, node_linear_num ):

      if ( i == 0 or i == node_linear_num - 1 or j == 0 or j == node_linear_num - 1 ):
        A[v,0:node_num] = 0.0
        A[v,v] = 1.0
        rhs[v] = 0.0

      v = v + 1
#
#  Solve the linear system.
#
  u = la.solve ( A, rhs )
#
#  Evaluate the exact solution at the nodes.
#
  uex = np.zeros ( node_linear_num * node_linear_num )

  v = 0
  for j in range ( 0, node_linear_num ):
    y = grid[j]
    for i in range ( 0, node_linear_num ):
      x = grid[i]
      uex[v] = exact_fn ( x, y )
      v = v + 1
#
#  Compare the solution and the error at the nodes.
#
  print ""
  print "   I     J     V    X         Y              U               Uexact"
  print ""
  v = 0
  for j in range ( 0, node_linear_num ):
    y = grid[j]
    for i in range ( 0, node_linear_num ):
      x = grid[i]
      print "%4d  %4d  %4d  %8f  %8f  %14g  %14g" % ( i, j, v, x, y, u[v], uex[v] )
      v = v + 1
#
#  Optionally, print the node coordinates.
#
  if ( false ):
    v = 0
    for j in range ( 0, node_linear_num ):
      y = grid[j]
      for i in range ( 0, node_linear_num ):
        x = grid[i]
        print "%8f  %8f" % ( x, y )
        v = v + 1
#
#  Optionally, print the elements, listing the nodes in counterclockwise order.
#
  if ( false ):
    e = 0
    for j in range ( 0, element_linear_num ):
      y = grid[j]
      for i in range ( 0, element_linear_num ):
        sw =   j       * node_linear_num + i
        se =   j       * node_linear_num + i + 1
        nw = ( j + 1 ) * node_linear_num + i
        ne = ( j + 1 ) * node_linear_num + i + 1
        print "%4d  %4d  %4d  %4d" % ( sw, se, ne, nw )
        e = e + 1
#
#  Terminate.
#
  print ""
  print "FEM2D_BVP_LINEAR:"
  print "  Normal end of execution."
  print ''
  timestamp ( )
#
#  That is the end of the main program.
#  Now we list some helper functions.
#
def exact_fn ( x, y ):
#
## EXACT_FN evaluates the exact solution.
#
  value = x * ( 1 - x ) * y * ( 1 - y )
  return value

def rhs_fn ( x, y ):
#
## RHS_FN evaluates the right hand side.
#
  value = 2 * x * ( 1 - x ) + 2 * y * ( 1 - y )
  return value
#
#  If this script is called directly, then run it as a program.
#
if ( __name__ == '__main__' ):
  fem2d_bvp_linear ( )
