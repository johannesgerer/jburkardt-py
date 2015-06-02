#!/usr/bin/env python

#*****************************************************************************80

def fem1d_heat_explicit_cfl ( x_num, k, x, dt ):

#*****************************************************************************80
#
## FEM1D_HEAT_EXPLICIT_CFL: compute the Courant-Friedrichs-Loewy coefficient.
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
#  Reference:
#
#    George Lindfield, John Penny,
#    Numerical Methods Using MATLAB,
#    Second Edition,
#    Prentice Hall, 1999,
#    ISBN: 0-13-012641-1,
#    LC: QA297.P45.
#
#  Parameters:
#
#    Input, integer X_NUM, the number of nodes.
#
#    Input, real K(X_NUM), the heat conductivity coefficient.
#
#    Input, real NODE_X(X_NUM), the coordinates of the nodes.
#
#    Input, real DT, the time step.
#
#    Output, real CFL, the Courant-Friedrichs-Loewy coefficient.
#
  from sys import exit

  cfl = 0.0
  for i in range ( 0, x_num - 2 ):
    cfl = max ( cfl, 2.0 * k[i+1] / ( x[i+2] - x[i] ) ** 2 )
 
  cfl = dt * cfl

  if ( 0.5 <= cfl ):
    print ''
    print 'FEM1D_HEAT_EXPLICIT_CFL - Fatal error!'
    print '  CFL condition failed.'
    print '  0.5 <= K * dT / dX / dX = %g' % ( cfl )
    exit ( 'FEM1D_HEAT_EXPLICIT_CFL - Fatal error!' )

  return cfl

def fem1d_heat_explicit_cfl_test ( ):

#*****************************************************************************80
#
## FEM1D_HEAT_EXPLICIT_CFL_TEST tests FEM1D_HEAT_EXPLICIT_CFL.
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
  import numpy as np

  print ''
  print 'FEM1D_HEAT_EXPLICIT_CFL_TEST:'
  print '  Test FEM1D_HEAT_EXPLICIT_CFL, which evaluates the CFL parameter.'

  x_num = 51
  k = np.zeros ( x_num )
  for i in range ( 0, x_num ):
    k[i] = 1.0
  node_x = np.linspace ( 0.0, 10.0, x_num )
  dt = 0.025

  cfl = fem1d_heat_explicit_cfl ( x_num, k, node_x, dt )

  print ''
  print '  CFL = %g' % ( cfl )

  print ''
  print 'FEM1D_HEAT_EXPLICIT_CFL_TEST:'
  print '  Normal end of execution.'

  return
  
if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  fem1d_heat_explicit_cfl_test ( )
  timestamp ( )

