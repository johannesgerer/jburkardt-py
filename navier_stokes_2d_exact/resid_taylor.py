#! /usr/bin/env python
#
def resid_taylor ( nu, rho, n, x, y, t ):

#*****************************************************************************80
#
## RESID_TAYLOR returns residuals of the Taylor exact Navier Stokes solution.
#
#  Location:
#
#    http://people.sc.fsu.edu/~jburkardt/py_src/navier_stokes_2d_exact/resid_taylor.py
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 January 2015
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
#    Input, real T(N), the time coordinate or coordinates.
#
#    Output, real UR(N), VR(N), PR(N), the residuals in the U, V and P equations.
#
  import numpy as np
  from rhs_taylor import rhs_taylor
#
#  Get the right hand sides.
#
  f, g, h = rhs_taylor ( nu, rho, n, x, y, t );
#
#  Make space.
#
  c2x = np.array ( n )
  c2y = np.array ( n )
  cx = np.array ( n )
  cy = np.array ( n )
  e2t = np.array ( n )
  e4t = np.array ( n )
  p = np.array ( n )
  px = np.array ( n )
  py = np.array ( n )
  s2x = np.array ( n )
  s2y = np.array ( n )
  sx = np.array ( n )
  sy = np.array ( n )
  u = np.array ( n )
  ut = np.array ( n )
  ux = np.array ( n )
  uxx = np.array ( n )
  uy = np.array ( n )
  uyy = np.array ( n )
  v = np.array ( n )
  vt = np.array ( n )
  vx = np.array ( n )
  vxx = np.array ( n )
  vy = np.array ( n )
  vyy = np.array ( n )
#
#  Make some temporaries.
#
  cx = np.cos ( np.pi * x )
  cy = np.cos ( np.pi * y )

  sx = np.sin ( np.pi * x )
  sy = np.sin ( np.pi * y )

  e2t = np.exp ( - 2.0 * np.pi * np.pi * nu * t )

  c2x = np.cos ( 2.0 * np.pi * x )
  c2y = np.cos ( 2.0 * np.pi * y )

  s2x = np.sin ( 2.0 * np.pi * x )
  s2y = np.sin ( 2.0 * np.pi * y )

  e4t = np.exp ( - 4.0 * np.pi * np.pi * nu * t )
#
#  Form the functions and derivatives.
#
  u    =  -                            cx * sy * e2t
  dudx =                       np.pi * sx * sy * e2t
  dudxx =              np.pi * np.pi * cx * sy * e2t
  dudy =  -                    np.pi * cx * cy * e2t
  dudyy =              np.pi * np.pi * cx * sy * e2t
  dudt =  + 2.0 * nu * np.pi * np.pi * cx * sy * e2t

  v    =                               sx * cy * e2t
  dvdx =                       np.pi * cx * cy * e2t
  dvdxx = -            np.pi * np.pi * sx * cy * e2t
  dvdy =  -                    np.pi * sx * sy * e2t
  dvdyy = -            np.pi * np.pi * sx * cy * e2t
  dvdt =  - 2.0 * nu * np.pi * np.pi * sx * cy * e2t

  p =     - 0.25 * rho *       ( c2x + c2y ) * e4t
  dpdx =  + 0.5  * rho * np.pi * s2x         * e4t
  dpdy =  + 0.5  * rho * np.pi       * s2y   * e4t
#
#  Evaluate the residuals.
#
  ur = dudt + u * dudx + v * dudy + ( 1.0 / rho ) * dpdx \
     - nu * ( dudxx + dudyy ) - f

  vr = dvdt + u * dvdx + v * dvdy + ( 1.0 / rho ) * dpdy \
     - nu * ( dvdxx + dvdyy ) - g

  pr = dudx + dvdy - h

  return ur, vr, pr

def resid_taylor_test ( ):

#*****************************************************************************80
#
## RESID_TAYLOR_TEST samples the residual at the initial time.
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
  print 'RESID_TAYLOR_TEST'
  print '  Sample the Navier-Stokes residuals'
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

  ur, vr, pr = resid_taylor ( nu, rho, n, x, y, t )

  print ''
  print '           Minimum       Maximum'
  print ''
  print '  Ur:  %14.6g  %14.6g' % ( np.min ( np.abs ( ur ) ), np.max ( np.abs ( ur ) ) )
  print '  Vr:  %14.6g  %14.6g' % ( np.min ( np.abs ( vr ) ), np.max ( np.abs ( vr ) ) )
  print '  Pr:  %14.6g  %14.6g' % ( np.min ( np.abs ( pr ) ), np.max ( np.abs ( pr ) ) )

  print ''
  print 'RESID_TAYLOR_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  resid_taylor_test ( )
  timestamp ( )

