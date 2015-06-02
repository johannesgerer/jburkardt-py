#! /usr/bin/env python
#
def rhs_taylor ( nu, rho, n, x, y, t ):

#*****************************************************************************80
#
## RHS_TAYLOR returns right hand sides of the Taylor vortex equations.
#
#  Location:
#
#    http://people.sc.fsu.edu/~jburkardt/py_src/navier_stokes_2d_exact/rhs_taylor.py
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
#    Output, real F(N), G(N), H(N), the residuals in the U, V and P equations.
#
  import numpy as np

  f = np.zeros ( n )
  g = np.zeros ( n )
  h = np.zeros ( n )

  return f, g, h

def rhs_taylor_test ( ):

#*****************************************************************************80
#
## RHS_TAYLOR_TEST samples the right hand sides at the initial time.
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
  print 'RHS_TAYLOR_TEST'
  print '  Taylor Vortex Flow:'
  print '  Sample the Navier-Stokes right hand sides'
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

  f, g, h = rhs_taylor ( nu, rho, n, x, y, t )

  print ''
  print '           Minimum       Maximum'
  print ''
  print '  Ur:  %14.6g  %14.6g' % ( np.min ( f ), np.max ( f ) )
  print '  Vr:  %14.6g  %14.6g' % ( np.min ( g ), np.max ( g ) )
  print '  Pr:  %14.6g  %14.6g' % ( np.min ( h ), np.max ( h ) )

  print ''
  print 'RHS_TAYLOR_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  rhs_taylor_test ( )
  timestamp ( )

