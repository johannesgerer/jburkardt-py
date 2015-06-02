#! /usr/bin/env python
#
def uvp_taylor ( nu, rho, n, x, y, t ):

#*****************************************************************************80
#
## UVP_TAYLOR evaluates the Taylor exact Navier Stokes solution.
#
#  Location:
#
#    http://people.sc.fsu.edu/~jburkardt/py_src/navier_stokes_2d_exact/uvp_taylor.py
#
#  Discussion:
#
#    This flow is known as a Taylor-Green vortex.
#
#    The given velocity and pressure fields are exact solutions for the 2D 
#    incompressible time-dependent Navier Stokes equations over any region.
#
#    To define a typical problem, one chooses a bounded spatial region 
#    and a starting time, and then imposes boundary and initial conditions
#    by referencing the exact solution appropriately.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Geoffrey Taylor,
#    On the decay of vortices in a viscous fluid,
#    Philosophical Magazine,
#    Volume 46, 1923, pages 671-674.
#
#    Geoffrey Taylor, A E Green,
#    Mechanism for the production of small eddies from large ones,
#    Proceedings of the Royal Society of London, 
#    Series A, Volume 158, 1937, pages 499-521.
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

  cx = np.cos ( np.pi * x )
  cy = np.cos ( np.pi * y )
  c2x = np.cos ( 2.0 * np.pi * x )
  c2y = np.cos ( 2.0 * np.pi * y )
  sx = np.sin ( np.pi * x )
  sy = np.sin ( np.pi * y )
  e2t = np.exp ( - 2.0 * np.pi * np.pi * nu * t )
  e4t = np.exp ( - 4.0 * np.pi * np.pi * nu * t )

  u = np.zeros ( n )
  v = np.zeros ( n )
  p = np.zeros ( n )

  u = - cx * sy * e2t
  v =   sx * cy * e2t
  p = - 0.25 * rho * ( c2x + c2y ) * e4t

  return u, v, p

def uvp_taylor_test ( ):

#*****************************************************************************80
#
## UVP_TAYLOR_TEST samples the solution at the initial time.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 January 2015
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
  print 'UVP_TAYLOR_TEST'
  print '  Estimate the range of velocity and pressure'
  print '  at the initial time T = 0, using a region that is'
  print '  the square centered at (1.5,1.5) with "radius" 1.0,'
  print '  Kinematic viscosity NU = %g' % ( nu )
  print '  Fluid density RHO = %g' % ( rho )

  n = 1000
  x_lo = 0.5
  x_hi = +2.5
  seed = 123456789
  x, seed = r8vec_uniform_ab ( n, x_lo, x_hi, seed )
  y, seed = r8vec_uniform_ab ( n, x_lo, x_hi, seed )
  t = 0.0

  u, v, p = uvp_taylor ( nu, rho, n, x, y, t )

  print ''
  print '           Minimum       Maximum'
  print ''
  print '  U:  %14.6g  %14.6g' % ( np.min ( u ), np.max ( u ) )
  print '  V:  %14.6g  %14.6g' % ( np.min ( v ), np.max ( v ) )
  print '  P:  %14.6g  %14.6g' % ( np.min ( p ), np.max ( p ) )

  print ''
  print 'UVP_TAYLOR_TEST:'
  print '  Normal end of execution.'

  return

def uvp_taylor_test2 ( ):

#*****************************************************************************80
#
## UVP_TAYLOR_TEST2 samples the solution on the boundary at the initial time.
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

  r8_lo = 0.5
  r8_hi = +2.5

  nu = 1.0
  rho = 1.0
  t = 0.0

  print ''
  print 'UVP_TAYLOR_TEST2'
  print '  Estimate the range of velocity and pressure'
  print '  on the boundary'
  print '  at the initial time T = 0, using a region that is'
  print '  the square centered at (1.5,1.5) with "radius" 1.0,'
  print '  Kinematic viscosity NU = %g' % ( nu )
  print '  Fluid density RHO = %g' % ( rho )

  n = 400

  x = np.zeros ( n )
  y = np.zeros ( n )
#
#  Python is consistent in its willful flouting of sensible conventions.
#  X[0:100] means X from 0 to 99...!
#
  x[0:100] = np.linspace ( r8_lo, r8_hi, 100 )
  y[0:100] = r8_lo

  x[100:200] = r8_hi
  y[100:200] = np.linspace ( r8_lo, r8_hi, 100 )

  x[200:300] = np.linspace ( r8_hi, r8_lo, 100 )
  y[200:300] = r8_hi

  x[300:400] = r8_lo
  y[300:400] = np.linspace ( r8_lo, r8_hi, 100 )

  u, v, p = uvp_taylor ( nu, rho, n, x, y, t )

  print ''
  print '           Minimum       Maximum'
  print ''
  print '  U:  %14.6g  %14.6g' % ( np.min ( u ), np.max ( u ) )
  print '  V:  %14.6g  %14.6g' % ( np.min ( v ), np.max ( v ) )
  print '  P:  %14.6g  %14.6g' % ( np.min ( p ), np.max ( p ) )

  print ''
  print 'UVP_TAYLOR_TEST2:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  uvp_taylor_test ( )
  uvp_taylor_test2 ( )
  timestamp ( )

