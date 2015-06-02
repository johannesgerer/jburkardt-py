#!/usr/bin/env python

#*****************************************************************************80

def fd1d_heat_explicit_test02 ( ):

#*****************************************************************************80
#
## FD1D_HEAT_EXPLICIT_TEST02 does a problem with known solution.
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
  print 'FD1D_HEAT_EXPLICIT_TEST02:'
  print '  Compute an approximate solution to the time-dependent'
  print '  one dimensional heat equation for a problem where we'
  print '  know the exact solution.'
  print ''
  print '    dH/dt - K * d2H/dx2 = f(x,t)'
  print ''
  print '  Run a simple test case.'
#
#  Heat coefficient.
#
  k = k_test02 ( )
#
#  X_NUM is the number of equally spaced nodes to use between 0 and 1.
#
  x_num = 21
  x_min = 0.0
  x_max = 1.0
  dx = ( x_max - x_min ) / ( x_num - 1 )
  x = np.linspace ( x_min, x_max, x_num )
#
#  T_NUM is the number of equally spaced time points between 0 and 10.0.
#
  t_num = 26
  t_min = 0.0
  t_max = 10.0
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
  gmat = np.zeros ( ( x_num, t_num ) )
  hmat = np.zeros ( ( x_num, t_num ) )

  print ''
  print '  Step            Time       RMS Error'
  print ''

  for j in range ( 0, t_num ):

    if ( j == 0 ):
      h = ic_test02 ( x_num, x, t[j] )
      h = bc_test02 ( x_num, x, t[j], h )
    else:
      h = fd1d_heat_explicit ( x_num, x, t[j-1], dt, cfl, rhs_test02, bc_test02, h )

    g = exact_test02 ( x_num, x, t[j] )

    e = 0.0
    for i in range ( 0, x_num ):
      e = e + ( h[i] - g[i] ) ** 2
    e = sqrt ( e ) / sqrt ( x_num )

    print '  %4d  %14.6g  %14.6g' % ( j, t[j], e )
    for i in range ( 0, x_num ):
      gmat[i,j] = g[i]
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
  plt.savefig ( 'plot_test02.png' )
  plt.show ( )
#
#  Write the data to files.
#
  r8mat_write ( 'g_test02.txt', x_num, t_num, gmat )
  r8mat_write ( 'h_test02.txt', x_num, t_num, hmat )
  r8vec_write ( 't_test02.txt', t_num, t )
  r8vec_write ( 'x_test02.txt', x_num, x )

  print ''
  print '  G(X,T) written to "g_test02.txt"'
  print '  H(X,T) written to "h_test02.txt"'
  print '  T values written to "t_test02.txt"'
  print '  X values written to "x_test02.txt"'

  return

#*****************************************************************************80

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
  import numpy as np

  h = np.zeros ( x_num )
#
#  Because EXACT_TEST02 expects an array as an input argument,
#  we can't simply pass the scalar x[0], but have to create an
#  array.
#
  x_array = np.zeros ( 1 )

  x_array[0] = x[0]
  h[0]       = exact_test02 ( 1, x_array, t )

  x_array[0] = x[x_num-1]
  h[x_num-1] = exact_test02 ( 1, x_array, t )

  return h

#*****************************************************************************80

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
#    Input, real T, the initial time.
#
#    Output, real H(X_NUM), the exact solution at X and T.
#
  from math import exp
  from math import sin
  from math import sqrt
  import numpy as np

  k = k_test02 ( )

  h = np.zeros ( x_num )

  for i in range ( 0, x_num ):
    h[i] = exp ( - t ) * sin ( sqrt ( k ) * x[i] )

  return h

#*****************************************************************************80

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
  h = exact_test02 ( x_num, x, t )

  return h

#*****************************************************************************80

def k_test02 ( ):

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
  k = 0.002

  return k

#*****************************************************************************80

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
#    Output, real VALUE(X_NUM,1), the source term.
#
  import numpy as np

  value = np.zeros ( x_num )

  return value

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  fd1d_heat_explicit_test02 ( )
  timestamp ( )

