#!/usr/bin/env python

#*****************************************************************************80

def fem1d_heat_explicit_test01 ( ):

#*****************************************************************************80
#
## FEM1D_HEAT_EXPLICIT_TEST01 runs a simple test.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    06 November 2014
#
#  Author:
#
#    John Burkardt
#
  from assemble_mass import assemble_mass
  from fem1d_heat_explicit import fem1d_heat_explicit
  from r8mat_write import r8mat_write
  from r8vec_write import r8vec_write
  import numpy as np
  from mpl_toolkits.mplot3d import Axes3D
  from matplotlib import cm
  from matplotlib.ticker import LinearLocator, FormatStrFormatter
  import matplotlib.pyplot as plt

  print ''
  print 'FEM1D_HEAT_EXPLICIT_TEST01:'
  print '  The time dependent 1D heat equation is'
  print ''
  print '    Ut - k * Uxx = f(x,t)'
  print ''
  print '  for space interval A <= X <= B with boundary conditions'
  print ''
  print '    U(A,t) = UA(t)'
  print '    U(B,t) = UB(t)'
  print ''
  print '  and time interval T0 <= T <= T1 with initial condition'
  print ''
  print '    U(X,T0) = U0(X).'
  print ''
  print '  To compute an approximate solution:'
  print '    the interval [A,B] is replace by a discretized mesh Xi'
  print '    a set of finite element functions PSI(X) are determined,'
  print '    the solution U is written as a weighted sum of the basis functions,'
  print '    the weak form of the differential equation is written,'
  print '    a time grid Tj is imposed, and time derivatives replaced by'
  print '    an explicit forward Euler first difference,'
  print ''
  print '    The continuous PDE has now been transformed into a set of algebraic'
  print '    equations for the coefficients C(Xi,Tj).'
#
#  Set the nodes.
#
  x_num = 21
  x_min = 0.0
  x_max = 1.0
  dx = ( x_max - x_min ) / ( x_num - 1 )
  x = np.linspace ( x_min, x_max, x_num )
#
#  Set the times.
#
  t_num = 401
  t_min = 0.0
  t_max = 80.0
  dt = ( t_max - t_min ) / ( t_num - 1 )
  t = np.linspace ( t_min, t_max, t_num )
#
#  Set finite element information.
#
  element_num = x_num - 1
  element_node = np.zeros ( ( 2, element_num ) )
  for j in range ( 0, element_num ):
    element_node[0,j] = j
    element_node[1,j] = j + 1
  quad_num = 3
  mass = assemble_mass ( x_num, x, element_num, element_node, quad_num )

  print ''
  print '  Number of X nodes = %d' % ( x_num )
  print '  X interval = [ %f, %f ]' % ( x_min, x_max )
  print '  X step size = %f' % ( dx )
  print '  Number of T steps = %d' % ( t_num )
  print '  T interval = [ %f, %f ]' % ( t_min, t_max )
  print '  T step size = %f' % ( dt )
  print '  Number of elements = %d' % ( element_num )
  print '  Number of quadrature points = %d' % ( quad_num )

  u_mat = np.zeros ( ( x_num, t_num ) )

  for j in range ( 0, t_num ):

    if ( j == 0 ):

      u = ic_test01 ( x_num, x, t[j] )
      u = bc_test01 ( x_num, x, t[j], u )

    else:

      u = fem1d_heat_explicit ( x_num, x, t[j-1], dt, k_test01, \
        rhs_test01, bc_test01, element_num, element_node, quad_num, mass, u )

    for i in range ( 0, x_num ):
      u_mat[i,j] = u[i]
#
#  Make a product grid of T and X for plotting.
#
  t_mat, x_mat = np.meshgrid ( t, x )
#
#  Make a mesh plot of the solution.
#
  fig = plt.figure ( )
  ax = fig.add_subplot ( 111, projection = '3d' )
  surf = ax.plot_surface ( x_mat, t_mat, u_mat )
  plt.xlabel ( '<---X--->' )
  plt.ylabel ( '<---T--->' )
  plt.title ( 'U(X,T)' )
  plt.savefig ( 'plot_test01.png' )
  plt.show ( )
#
#  Write the data to files.
#
  r8mat_write ( 'h_test01.txt', x_num, t_num, u_mat )
  r8vec_write ( 't_test01.txt', t_num, t )
  r8vec_write ( 'x_test01.txt', x_num, x )

  print ''
  print '  H(X,T) written to "h_test01.txt"'
  print '  T values written to "t_test01.txt"'
  print '  X values written to "x_test01.txt"'

  print ''
  print 'FEM1D_HEAT_EXPLICIT_TEST01:'
  print '  Normal end of execution.'

  return

def bc_test01 ( x_num, x, t, u ):

#*****************************************************************************80
#
## BC_TEST01 sets the boundary conditions for problem 1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 February 2012
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer X_NUM, the number of nodes.
#
#    Input, real  X(X_NUM,1), the coordinates of the points.
#
#    Input, real T, the current time.
#
#    Input, real U(X_NUM), the solution at time T.
#
#    Output, real U(X_NUM), the solution at time T, with
#    boundary conditions enforced.
#
  u[0]       = 90.0
  u[x_num-1] = 70.0

  return u

def ic_test01 ( x_num, x, t ):

#*****************************************************************************80
#
## IC_TEST01 sets the initial condition for problem 1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 January 2012
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer X_NUM, the number of nodes.
#
#    Input, real X(X_NUM), the node coordinates.
#
#    Input, real T, the time.
#
#    Output, real U(X_NUM), the initial value of U.
#
  import numpy as np

  u = np.zeros ( x_num )

  for i in range ( 0, x_num ):
    u[i] = 50.0

  return u

def k_test01 ( x_num, x, t ):

#*****************************************************************************80
#
## K_TEST01 evaluates the K coefficient for problem 1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 January 2012
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer X_NUM, the number of evaluation points.
#
#    Input, real X(X_NUM,1), the evaluation points.
#
#    Input, real T, the evaluation time.
#
#    Output, real K_VALUE(X_NUM,1), the value of K(X,T).
#
  import numpy as np

  k_value = np.zeros ( x_num )

  for i in range ( 0, x_num ):
    k_value[i] = 0.002

  return k_value

def rhs_test01 ( x_num, x, t ):

#*****************************************************************************80
#
## RHS_TEST01 evaluates the right hand side function for problem 1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 January 2012
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer X_NUM, the number of evaluation points.
#
#    Input, real X(X_NUM), the evaluation points.
#
#    Input, real T, the time.
#
#    Output, real RHS_VALUE(X_NUM), the right hand side function at
#    the given positions and time T.
#
  import numpy as np

  rhs_value = np.zeros ( x_num )

  return rhs_value

if ( __name__ == '__main__' ):
  from timestamp import timestamp

  timestamp ( )
  fem1d_heat_explicit_test01 ( )
  timestamp ( )

