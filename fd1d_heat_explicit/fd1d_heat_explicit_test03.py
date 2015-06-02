#!/usr/bin/env python

#*****************************************************************************80

def fd1d_heat_explicit_test03 ( ):

#*****************************************************************************80
#
## FD1D_HEAT_EXPLICIT_TEST03 does a simple test problem.
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
  from fd1d_heat_explicit import fd1d_heat_explicit
  from fd1d_heat_explicit_cfl import fd1d_heat_explicit_cfl
  from math import sqrt
  from r8mat_write import r8mat_write
  from r8vec_write import r8vec_write
  from mpl_toolkits.mplot3d import Axes3D
  from matplotlib import cm
  from matplotlib.ticker import LinearLocator, FormatStrFormatter
  import matplotlib.pyplot as plt
  import numpy as np

  print ''
  print 'FD1D_HEAT_EXPLICIT_TEST03:'
  print '  Compute an approximate solution to the time-dependent'
  print '  one dimensional heat equation:'
  print ''
  print '    dH/dt - K * d2H/dx2 = f(x,t)'
  print ''
  print '  Run a simple test case.'
#
#  Heat coefficient.
#
  k = k_test03 ( )
#
#  X_NUM is the number of equally spaced nodes to use between 0 and 1.
#
  x_num = 21
  x_min = -5.0
  x_max = +5.0
  dx = ( x_max - x_min ) / ( x_num - 1 )
  x = np.linspace ( x_min, x_max, x_num )
#
#  T_NUM is the number of equally spaced time points between 0 and 10.0.
#
  t_num = 81
  t_min = 0.0
  t_max = 4.0
  dt = ( t_max - t_min ) / ( t_num - 1 )
  t = np.linspace ( t_min, t_max, t_num )
#
#  Get the CFL coefficient.
#
  cfl = fd1d_heat_explicit_cfl ( k, t_num, t_min, t_max, x_num, x_min, x_max )

  print ''
  print '  Number of X nodes = %d' % ( x_num )
  print '  X interval is [%f,%f]' % ( x_min, x_max )
  print '  X spacing is %f' % ( dx )
  print '  Number of T values = %d' % ( t_num )
  print '  T interval is [%f,%f]' % ( t_min, t_max )
  print '  T spacing is %f' % ( dt )
  print '  Constant K = %g' % ( k )
  print '  CFL coefficient = %g' % ( cfl )
#
#  Running the code produces an array H of temperatures H(t,x),
#  and vectors x and t.
#
  hmat = np.zeros ( ( x_num, t_num ) )

  for j in range ( 0, t_num ):
    if ( j == 0 ):
      h = ic_test03 ( x_num, x, t[j] )
      h = bc_test03 ( x_num, x, t[j], h )
    else:
      h = fd1d_heat_explicit ( x_num, x, t[j-1], dt, cfl, rhs_test03, bc_test03, h )
    for i in range ( 0, x_num ):
      hmat[i,j] = h[i]
#
#  Plot the data.
#
  tmat, xmat = np.meshgrid ( t, x )
  fig = plt.figure ( )
  ax = Axes3D ( fig )
  surf = ax.plot_surface ( xmat, tmat, hmat )
  plt.xlabel ( '<---X--->' )
  plt.ylabel ( '<---T--->' )
  plt.title ( 'U(X,T)' )
  plt.savefig ( 'plot_test03.png' )
  plt.show ( )
#
#  Write the data to files.
#
  r8mat_write ( 'h_test03.txt', x_num, t_num, hmat )
  r8vec_write ( 't_test03.txt', t_num, t )
  r8vec_write ( 'x_test03.txt', x_num, x )

  print ''
  print '  H(X,T) written to "h_test03.txt"'
  print '  T values written to "t_test03.txt"'
  print '  X values written to "x_test3.txt"'
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
#    06 November 2014
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
#    Input, real H(X_NUM,1), the current heat values.
#
#    Output, real H(X_NUM,1), the current heat values, after boundary
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
#    06 November 2014
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

def k_test03 ( ):

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
#    06 November 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real K, the conducitivity.
#
  k = 2.0

  return k

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
#    06 November 2014
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
#    Output, real VALUE(X_NUM), the source term.
#
  import numpy as np

  value = np.zeros ( x_num )

  return value

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  fd1d_heat_explicit_test03 ( )
  timestamp ( )

