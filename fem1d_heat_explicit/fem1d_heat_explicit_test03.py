#! /usr/bin/env python

#*****************************************************************************80

def fem1d_heat_explicit_test03 ( ):

#*****************************************************************************80
#
## FEM1D_HEAT_EXPLICIT_TEST03 does a simple test problem.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    07 November 2014
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
  print 'FEM1D_HEAT_EXPLICIT_TEST03:'
  print '  Using the finite element method,'
  print '  compute an approximate solution to the time-dependent'
  print '  one dimensional heat equation:'
  print ''
  print '    dH/dt - K * d2H/dx2 = f(x,t)'
#
#  Set the nodes.
#
  x_num = 21
  x_min = -5.0
  x_max = +5.0
  dx = ( x_max - x_min ) / ( x_num - 1 )
  x = np.linspace ( x_min, x_max, x_num )
#
#  Set the times.
#
  t_num = 321
  t_min = 0.0
  t_max = 4.0
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
#
#  Running the code produces an array H of temperatures H(t,x),
#  and vectors x and t.
#
  h_mat = np.zeros ( ( x_num, t_num ) )

  for j in range ( 0, t_num ):

    if ( j == 0 ):
      h = ic_test03 ( x_num, x, t[j] )
      h = bc_test03 ( x_num, x, t[j], h )
    else:
      h = fem1d_heat_explicit ( x_num, x, t[j-1], dt, k_test03, \
        rhs_test03, bc_test03, element_num, element_node, quad_num, mass, h )

    for i in range ( 0, x_num ):
      h_mat[i,j] = h[i]

  t_mat, x_mat = np.meshgrid ( t, x )
#
#  Make a mesh plot of the solution.
#
  fig = plt.figure ( )
  ax = fig.add_subplot ( 111, projection = '3d' )
  surf = ax.plot_surface ( x_mat, t_mat, h_mat )
  plt.xlabel ( '<---X--->' )
  plt.ylabel ( '<---T--->' )
  plt.title ( 'U(X,T)' )
  plt.savefig ( 'plot_test03.png' )
  plt.show ( )
#
#  Write the data to files.
#
  r8mat_write ( 'h_test03.txt', x_num, t_num, h_mat )
  r8vec_write ( 't_test03.txt', t_num, t )
  r8vec_write ( 'x_test03.txt', x_num, x )

  print ''
  print '  H(X,T) written to "h_test03.txt"'
  print '  T values written to "t_test03.txt"'
  print '  X values written to "x_test3.txt"'

  print ''
  print 'FEM1D_HEAT_EXPLICIT_TEST03:'
  print '  Normal end of execution.'

  return

def bc_test03 ( x_num, x, t, h ):

#*****************************************************************************80
#
## BC_TEST03 evaluates the boundary conditions for problem 3.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    07 November 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer X_NUM, the number of nodes.
#
#    Input, real X(X_NUM,1), the node coordinates.
#
#    Input, real T, the current time.
#
#    Input, real H(X_NUM), the current heat values.
#
#    Output, real H(X_NUM), the current heat values, after boundary
#    conditions have been imposed.
#
  h[0]       = 15.0
  h[x_num-1] = 25.0

  return h

def ic_test03 ( x_num, x, t ):

#*****************************************************************************80
#
## IC_TEST03 evaluates the initial condition for problem 3.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    07 November 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer X_NUM, the number of nodes.
#
#    Input, real X(X_NUM,1), the node coordinates.
#
#    Input, real T, the initial time.
#
#    Output, real H(X_NUM,1), the heat values at the initial time.
#
  import numpy as np

  h = np.zeros ( x_num )

  for i in range ( 0, x_num ):
    if ( x[i] < 0.0 ):
      h[i] = 15.0
    elif ( x[i] == 0.0 ):
      h[i] = 20.0
    else:
      h[i] = 25.0

  return h

def k_test03 ( x_num, x, t ):

#*****************************************************************************80
#
## K_TEST03 evaluates the conductivity for problem 3.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    07 November 2014
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
    k_value[i] = 2.0

  return k_value

def rhs_test03 ( x_num, x, t ):

#*****************************************************************************80
#
## RHS_TEST03 evaluates the right hand side for problem 3.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    07 November 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer X_NUM, the number of nodes.
#
#    Input, real X(X_NUM,1), the node coordinates.
#
#    Input, real T, the current time.
#
#    Output, real RHS_VALUE(X_NUM,1), the source term.
#
  import numpy as np

  rhs_value = np.zeros ( x_num )

  return rhs_value

if ( __name__ == '__main__' ):
  from timestamp import timestamp

  timestamp ( )
  fem1d_heat_explicit_test03 ( )
  timestamp ( )

