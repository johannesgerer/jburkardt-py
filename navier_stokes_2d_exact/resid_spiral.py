#! /usr/bin/env python
#
def resid_spiral ( nu, rho, n, x, y, t ):

#*****************************************************************************80
#
## RESID_SPIRAL returns residuals of the Spiral Flow equations.
#
#  Location:
#
#    http://people.sc.fsu.edu/~jburkardt/py_src/navier_stokes_2d_exact/resid_spiral.py
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
  from rhs_spiral import rhs_spiral

  ur = np.zeros ( n )
  vr = np.zeros ( n )
  pr = np.zeros ( n )
#
#  Get the right hand side functions.
#
  f, g, h = rhs_spiral ( nu, rho, n, x, y, t );
#
#  Form the functions and derivatives for the left hand side.
#
  u = ( 1.0 + nu * t ) * 2.0 \
    * ( x ** 4 - 2.0 * x ** 3 + x ** 2 ) \
    * ( 2.0 * y ** 3 - 3.0 * y ** 2 + y )

  dudt = nu * 2.0 \
    * ( x ** 4 - 2.0 * x ** 3 + x ** 2 ) \
    * ( 2.0 * y ** 3  - 3.0 * y ** 2 + y )

  dudx = ( 1.0 + nu * t ) * 2.0 \
    * ( 4.0 * x ** 3 - 6.0 * x ** 2 + 2.0 * x ) \
    * ( 2.0 * y ** 3 - 3.0 * y ** 2 + y )

  dudxx = ( 1.0 + nu * t ) * 2.0 \
    * ( 12.0 * x ** 2 - 12.0 * x + 2.0 ) \
    * ( 2.0 * y ** 3 - 3.0 * y ** 2 + y )

  dudy = ( 1.0 + nu * t ) * 2.0 \
    * ( x ** 4 - 2.0 * x ** 3 + x ** 2 ) \
    * ( 6.0 * y ** 2  - 6.0 * y + 1.0 )

  dudyy = ( 1.0 + nu * t ) * 2.0 \
    * ( x ** 4 - 2.0 * x ** 3 + x ** 2 ) \
    * ( 12.0 * y - 6.0 )

  v = - ( 1.0 + nu * t ) * 2.0 \
    * ( 2.0 * x ** 3 - 3.0 * x ** 2 + x ) \
    * ( y ** 4 - 2.0 * y ** 3 + y ** 2 )

  dvdt = - nu * 2.0 \
    * ( 2.0 * x ** 3 - 3.0 * x ** 2 + x ) \
    * ( y ** 4 - 2.0 * y ** 3 + y ** 2 )

  dvdx = - ( 1.0 + nu * t ) * 2.0 \
    * ( 6.0 * x ** 2 - 6.0 * x + 1.0 ) \
    * ( y ** 4 - 2.0 * y ** 3 + y ** 2 )

  dvdxx = - ( 1.0 + nu * t ) * 2.0 \
    * ( 12.0 * x - 6.0 ) \
    * ( y ** 4 - 2.0 * y ** 3 + y ** 2 )

  dvdy = - ( 1.0 + nu * t ) * 2.0 \
    * ( 2.0 * x ** 3 - 3.0 * x ** 2 + x ) \
    * ( 4.0 * y ** 3 - 6.0 * y ** 2 + 2.0 * y )

  dvdyy = - ( 1.0 + nu * t ) * 2.0 \
    * ( 2.0 * x ** 3 - 3.0 * x ** 2 + x ) \
    * ( 12.0 * y ** 2 - 12.0 * y + 2.0 )

  p = rho * y
  dpdx = 0.0
  dpdy = rho
#
#  Evaluate the residuals.
#
  ur = dudt - nu * ( dudxx + dudyy ) \
    + u * dudx + v * dudy + dpdx / rho - f

  vr = dvdt - nu * ( dvdxx + dvdyy ) \
    + u * dvdx + v * dvdy + dpdy / rho - g

  pr = dudx + dvdy - h

  return ur, vr, pr

def resid_spiral_test ( ):

#*****************************************************************************80
#
## RESID_SPIRAL_TEST samples the residuals at the initial time.
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
  import numpy as np
  from r8vec_uniform_ab import r8vec_uniform_ab

  nu = 1.0
  rho = 1.0

  print ''
  print 'RESID_SPIRAL_TEST'
  print '  Spiral Flow:'
  print '  Sample the Navier-Stokes residuals'
  print '  at the initial time T = 0, over the unit square.'
  print '  Kinematic viscosity NU = %g' % ( nu )
  print '  Fluid density RHO = %g' % ( rho )

  n = 1000
  x_lo = 0.0
  x_hi = 1.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( n, x_lo, x_hi, seed )
  y, seed = r8vec_uniform_ab ( n, x_lo, x_hi, seed )
  t = 0.0

  ur, vr, pr = resid_spiral ( nu, rho, n, x, y, t )

  print ''
  print '           Minimum       Maximum'
  print ''
  print '  Ur:  %14.6g  %14.6g' % ( np.min ( np.abs ( ur ) ), np.max ( np.abs ( ur ) ) )
  print '  Vr:  %14.6g  %14.6g' % ( np.min ( np.abs ( vr ) ), np.max ( np.abs ( vr ) ) )
  print '  Pr:  %14.6g  %14.6g' % ( np.min ( np.abs ( pr ) ), np.max ( np.abs ( pr ) ) )

  print ''
  print 'RESID_SPIRAL_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  resid_spiral_test ( )
  timestamp ( )

