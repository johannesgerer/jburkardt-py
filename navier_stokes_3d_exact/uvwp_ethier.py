#! /usr/bin/env python
#
def uvwp_ethier ( a, d, n, x, y, z, t ):

#*****************************************************************************80
#
## UVWP_ETHIER evaluates the Ethier exact Navier Stokes solution.
#
#  Location:
#
#    http://people.sc.fsu.edu/~jburkardt/m_src/navier_stokes_3d_exact/uvwp_ethier.m
#
#  Discussion:
#
#    The reference asserts that the given velocity and pressure fields
#    are exact solutions for the 3D incompressible time-dependent
#    Navier Stokes equations over any region.
#
#    To define a typical problem, one chooses a bounded spatial region 
#    and a starting time, and then imposes boundary and initial conditions
#    by referencing the exact solution appropriately.
#
#    In the reference paper, a calculation is made for the cube centered
#    at (0,0,0) with a "radius" of 1 unit, and over the time interval
#    from t = 0 to t = 0.1, with parameters a = PI/4 and d = PI/2,
#    and with Dirichlet boundary conditions on all faces of the cube.
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
#    C Ross Ethier, David Steinman,
#    Exact fully 3D Navier-Stokes solutions for benchmarking,
#    International Journal for Numerical Methods in Fluids,
#    Volume 19, Number 5, March 1994, pages 369-375.
#
#  Parameters:
#
#    Input, real A, D, the parameters.  Sample values are A = PI/4 and
#    D = PI/2.
#
#    Input, integer N, the number of points at which the solution is to
#    be evaluated.
#
#    Input, real X(N), Y(N), Z(N), the coordinates of the points.
#
#    Input, real T, the time coordinate or coordinates.
#
#    Output, real U(N), V(N), W(N), P(N), the velocity components and
#    pressure at each of the points.
#
  import numpy as np

  ex = np.exp ( a * x )
  ey = np.exp ( a * y )
  ez = np.exp ( a * z )

  e2t = np.exp  ( - d * d * t )

  exy = np.exp ( a * ( x + y ) )
  eyz = np.exp ( a * ( y + z ) )
  ezx = np.exp ( a * ( z + x ) )

  sxy = np.sin ( a * x + d * y )
  syz = np.sin ( a * y + d * z )
  szx = np.sin ( a * z + d * x )

  cxy = np.cos ( a * x + d * y )
  cyz = np.cos ( a * y + d * z )
  czx = np.cos ( a * z + d * x )

  u = - a * ( ex * syz + ez * cxy ) * e2t
  v = - a * ( ey * szx + ex * cyz ) * e2t
  w = - a * ( ez * sxy + ey * czx ) * e2t
  p = 0.5 * a * a * e2t * e2t * ( \
    + ex * ex + 2.0 * sxy * czx * eyz \
    + ey * ey + 2.0 * syz * cxy * ezx \
    + ez * ez + 2.0 * szx * cyz * exy )

  return u, v, w, p

def uvwp_ethier_test ( ):

#*****************************************************************************80
#
## UVWP_ETHIER_TEST samples the solution at the initial time.
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
  import numpy as np
  from r8vec_uniform_ab import r8vec_uniform_ab

  a = np.pi / 4.0
  d = np.pi / 2.0

  print ''
  print 'UVWP_ETHIER_TEST'
  print '  Estimate the range of velocity and pressure'
  print '  at the initial time T = 0, using a region that is'
  print '  the cube centered at (0,0,0) with "radius" 1.0,'
  print '  Parameter A = %g' % ( a )
  print '  Parameter D = %g' % ( d )

  n = 1000
  x_lo = -1.0
  x_hi = +1.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( n, x_lo, x_hi, seed )
  y, seed = r8vec_uniform_ab ( n, x_lo, x_hi, seed )
  z, seed = r8vec_uniform_ab ( n, x_lo, x_hi, seed )
  t = 0.0

  u, v, w, p = uvwp_ethier ( a, d, n, x, y, z, t )

  print ''
  print '           Minimum       Maximum'
  print ''
  print '  U:  %14.6g  %14.6g' % ( np.min ( u ), np.max ( u ) )
  print '  V:  %14.6g  %14.6g' % ( np.min ( v ), np.max ( v ) )
  print '  W:  %14.6g  %14.6g' % ( np.min ( w ), np.max ( w ) )
  print '  P:  %14.6g  %14.6g' % ( np.min ( p ), np.max ( p ) )

  print ''
  print 'UVWP_ETHIER_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  uvwp_ethier_test ( )
  timestamp ( )

