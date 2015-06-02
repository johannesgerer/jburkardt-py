#!/usr/bin/env python
#
def fem1d_heat_explicit_test02 ( ):

#*****************************************************************************80
#
## FEM1D_HEAT_EXPLICIT_TEST02 does a problem with known solution.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    09 November 2014
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
  from math import sqrt
  from mpl_toolkits.mplot3d import Axes3D
  from matplotlib import cm
  from matplotlib.ticker import LinearLocator, FormatStrFormatter
  import matplotlib.pyplot as plt

  print ''
  print 'FEM1D_HEAT_EXPLICIT_TEST02:'
  print '  Using the finite element method,'
  print '  compute an approximate solution to the time-dependent'
  print '  one dimensional heat equation for a problem where we'
  print '  know the exact solution.'
  print ''
  print '    dH/dt - K * d2H/dx2 = f(x,t)'
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
  t_num = 51
  t_min = 0.0
  t_max = 10.0
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
  g_mat = np.zeros ( ( x_num, t_num ) )
  h_mat = np.zeros ( ( x_num, t_num ) )

  print ''
  print '  Step            Time       RMS Error'
  print ''

  for j in range ( 0, t_num ):

    if ( j == 0 ):
      h = ic_test02 ( x_num, x, t[j] )
      h = bc_test02 ( x_num, x, t[j], h )
    else:
      h = fem1d_heat_explicit ( x_num, x, t[j-1], dt, k_test02, \
        rhs_test02, bc_test02, element_num, element_node, quad_num, mass, h )

    g = exact_test02 ( x_num, x, t[j] )
    e = 0.0
    for i in range ( 0, x_num ):
      e = e + ( h[i] - g[i] ) ** 2 
    e = sqrt ( e / x_num )
    print '  %4d  %14.6g  %14.6g' % ( j, t[j], e )

    for i in range ( 0, x_num ):
      g_mat[i,j] = g[i]
      h_mat[i,j] = h[i]
#
#  Make a product grid of T and X for plotting.
#
  t_mat, x_mat = np.meshgrid ( t, x )
#
#  Plot the data.
#
  fig = plt.figure ( )
  ax = fig.add_subplot ( 111, projection = '3d' )
  surf = ax.plot_surface ( x_mat, t_mat, h_mat )
  plt.xlabel ( '<---X--->' )
  plt.ylabel ( '<---T--->' )
  plt.title ( 'U(X,T)' )
  plt.savefig ( 'plot_test02.png' )
  plt.show ( )
#
#  Write the data to files.
#
  r8mat_write ( 'g_test02.txt', x_num, t_num, g_mat )
  r8mat_write ( 'h_test02.txt', x_num, t_num, h_mat )
  r8vec_write ( 't_test02.txt', t_num, t )
  r8vec_write ( 'x_test02.txt', x_num, x )

  print ''
  print '  G(X,T) written to "g_test02.txt"'
  print '  H(X,T) written to "h_test02.txt"'
  print '  T values written to "t_test02.txt"'
  print '  X values written to "x_test02.txt"'

  print ''
  print 'FEM1D_HEAT_EXPLICIT_TEST02:'
  print '  Normal end of execution.'

  return

def bc_test02 ( x_num, x, t, h ):

#*****************************************************************************80
#
## BC_TEST02 evaluates the boundary conditions for problem 2.
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
#    Input, real X(X_NUM), the node coordinates.
#
#    Input, real T, the current time.
#
#    Input, real H(X_NUM), the current heat values.
#
#    Output, real H(X_NUM), the current heat values, after boundary
#    conditions have been imposed.
#
  import numpy as np

  x_array = np.zeros ( 1 )

  x_array[0] = x[0]
  h[0] = exact_test02 ( 1, x_array, t )

  x_array[0] = x[x_num-1]
  h[x_num-1] = exact_test02 ( 1, x_array, t )

  return h

def exact_test02 ( x_num, x, t ):

#*****************************************************************************80
#
## EXACT_TEST02 evaluates the exact solution for problem 2.
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
#    Input, real X(X_NUM), the node coordinates.
#
#    Input, real T, the initial time.
#
#    Output, real H(X_NUM), the exact solution at X and T.
#
  from math import exp
  from math import sin
  from math import sqrt
  import numpy as np

  k = k_test02 ( x_num, x, t )

  h = np.zeros ( x_num )

  for i in range ( 0, x_num ):
    h[i] = exp ( - t ) * sin ( sqrt ( k[i] ) * x[i] )

  return h

def ic_test02 ( x_num, x, t ):

#*****************************************************************************80
#
## IC_TEST02 evaluates the initial condition for problem 2.
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
#    Input, real X(X_NUM), the node coordinates.
#
#    Input, real T, the initial time.
#
#    Output, real H(X_NUM), the heat values at the initial time.
#
  h = exact_test02 ( x_num, x, t )

  return h

def k_test02 ( x_num, x, t ):

#*****************************************************************************80
#
## K_TEST02 evaluates the conductivity for problem 2.
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
#    Output, real K, the conducitivity.
#
#  Parameters:
#
#    Input, integer X_NUM, the number of evaluation points.
#
#    Input, real X(X_NUM), the evaluation points.
#
#    Input, real T, the evaluation time.
#
#    Output, real K_VALUE(X_NUM), the value of K(X,T).
#
  import numpy as np

  k_value = np.zeros ( x_num )

  for i in range ( 0, x_num ):
    k_value[i] = 0.002

  return k_value

def rhs_test02 ( x_num, x, t ):

#*****************************************************************************80
#
## RHS_TEST02 evaluates the right hand side for problem 2.
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
#    Input, real X(X_NUM), the node coordinates.
#
#    Input, real T, the time.
#
#    Output, real RHS_VALUE(X_NUM), the source term.
#
  import numpy as np

  rhs_value = np.zeros ( x_num )

  return rhs_value

if ( __name__ == '__main__' ):
  from timestamp import timestamp

  timestamp ( )
  fem1d_heat_explicit_test02 ( )
  timestamp ( )


