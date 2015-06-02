#! /usr/bin/env python
#
def uvp_lucas ( nu, rho, n, x, y, t ):

#*****************************************************************************80
#
## UVP_LUCAS evaluates Lucas Bystricky's exact Navier Stokes solution.
#
#  Location:
#
#    http://people.sc.fsu.edu/~jburkardt/py_src/navier_stokes_2d_exact/uvp_lucas.py
#
#  Discussion:
#
#    There is no time dependence.
#
#    The pressure is 0.
#
#    The preferred domain is the unit square.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real NU, the kinematic viscosity.
#
#    Input, real RHO, the density.
#
#    Input, integer N, the number of points at which the solution is to
#    be evaluated.
#
#    Input, real X(N), Y(N), the coordinates of the points.
#
#    Input, real T or T(N), the time coordinate or coordinates.
#
#    Output, real U(N), V(N), P(N), the velocity components and
#    pressure at each of the points.
#
  import numpy as np

  u = np.zeros ( n )
  v = np.zeros ( n )
  p = np.zeros ( n )

  u = - np.cos ( np.pi * x ) / np.pi

  v = - y * np.sin ( np.pi * x )

  p = 0.0

  return u, v, p

def uvp_lucas_test ( ):

#*****************************************************************************80
#
## UVP_LUCAS_TEST samples the Lucas Bystricky solution at the initial time.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 March 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from r8vec_uniform_ab import r8vec_uniform_ab

  nu = 1.0
  rho = 1.0

  print ''
  print 'UVP_LUCAS_TEST'
  print '  Lucas Bystricky Flow:'
  print '  Estimate the range of velocity and pressure'
  print '  at the initial time T = 0, over the unit square.'
  print '  Kinematic viscosity NU = %g' % ( nu )
  print '  Fluid density RHO = %g' % ( rho )

  n = 1000
  r8_lo = 0.0
  r8_hi = +1.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( n, r8_lo, r8_hi, seed )
  y, seed = r8vec_uniform_ab ( n, r8_lo, r8_hi, seed )
  t = 0.0

  u, v, p = uvp_lucas ( nu, rho, n, x, y, t )

  print ''
  print '           Minimum       Maximum'
  print ''
  print '  U:  %14.6g  %14.6g' % ( np.min ( u ), np.max ( u ) )
  print '  V:  %14.6g  %14.6g' % ( np.min ( v ), np.max ( v ) )
  print '  P:  %14.6g  %14.6g' % ( np.min ( p ), np.max ( p ) )

  print ''
  print 'UVP_LUCAS_TEST:'
  print '  Normal end of execution.'

  return

def uvp_lucas_test2 ( ):

#*****************************************************************************80
#
## UVP_LUCAS_TEST2 samples the Lucas Bystricky flow on the boundary.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 March 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  r8_lo = 0.0
  r8_hi = +1.0

  nu = 1.0
  rho = 1.0
  t = 0.0

  print ''
  print 'UVP_LUCAS_TEST2'
  print '  Lucas Bystricky Flow:'
  print '  Estimate the range of velocity and pressure'
  print '  on the boundary'
  print '  at the initial time T = 0, over the unit square.'
  print '  Kinematic viscosity NU = %g' % ( nu )
  print '  Fluid density RHO = %g' % ( rho )

  n = 400

  x = np.zeros ( n )
  y = np.zeros ( n )

  x[0:100] = np.linspace ( r8_lo, r8_hi, 100 )
  y[0:100] = r8_lo

  x[100:200] = r8_hi
  y[100:200] = np.linspace ( r8_lo, r8_hi, 100 )

  x[200:300] = np.linspace ( r8_hi, r8_lo, 100 )
  y[200:300] = r8_hi

  x[300:400] = r8_lo
  y[300:400] = np.linspace ( r8_lo, r8_hi, 100 )

  u, v, p = uvp_lucas ( nu, rho, n, x, y, t )

  print ''
  print '           Minimum       Maximum'
  print ''
  print '  U:  %14.6g  %14.6g' % ( np.min ( u ), np.max ( u ) )
  print '  V:  %14.6g  %14.6g' % ( np.min ( v ), np.max ( v ) )
  print '  P:  %14.6g  %14.6g' % ( np.min ( p ), np.max ( p ) )

  print ''
  print 'UVP_LUCAS_TEST2:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  uvp_lucas_test ( )
  uvp_lucas_test2 ( )
  timestamp ( )

