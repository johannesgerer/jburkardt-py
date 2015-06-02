#! /usr/bin/env python
#
def resid_stokes3 ( n, x, y ):

#*****************************************************************************80
#
## RHS_STOKES3 returns residuals of the exact Stokes solution #3.
#
#  Location:
#
#    http://people.sc.fsu.edu/~jburkardt/py_src/stokes_2d_exact/resid_stokes3.py
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Howard Elman, Alison Ramage, David Silvester,
#    Finite Elements and Fast Iterative Solvers with
#    Applications in Incompressible Fluid Dynamics,
#    Oxford, 2005,
#    ISBN: 978-0198528678,
#    LC: QA911.E39.
#
#  Parameters:
#
#    Input, integer N, the number of points at which the solution is to
#    be evaluated.
#
#    Input, real X(N), Y(N), the coordinates of the points.
#
#    Output, real UR(N), VR(N), PR(N), the residuals in the U,
#    V and P equations.
#
  import numpy as np
  from rhs_stokes3 import rhs_stokes3

  ur = np.zeros ( n )
  vr = np.zeros ( n )
  pr = np.zeros ( n )

  f, g, h = rhs_stokes3 ( n, x, y )

  u =   20.0 * x * y ** 3
  ux = 20.0 * y ** 3
  uxx = 0.0
  uy = 60.0 * x * y ** 2
  uyy = 120.0 * x * y

  v = 5.0 * ( x ** 4 - y ** 4 )
  vx = 20.0 * x ** 3
  vxx = 60.0 * x ** 2
  vy = - 20.0 * y ** 3
  vyy = - 60.0 * y ** 2

  p =   60.0 * x ** 2 * y - 20.0 * y ** 3 + 10.0
  px = 120.0 * x * y
  py =  60.0 * x ** 2 - 60.0 * y ** 2

  ur = px - ( uxx + uyy ) - f
  vr = py - ( vxx + vyy ) - g
  pr = ux + vy - h

  return ur, vr, pr

def resid_stokes3_test ( ):

#*****************************************************************************80
#
## RESID_STOKES3_TEST samples the residuals.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from r8vec_uniform_ab import r8vec_uniform_ab

  print ''
  print 'RESID_STOKES3_TEST'
  print '  Exact Stokes solution #3.'
  print '  Sample the Stokes residuals.'

  n = 1000
  x_lo = -1.0
  x_hi = +1.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( n, x_lo, x_hi, seed )
  y, seed = r8vec_uniform_ab ( n, x_lo, x_hi, seed )

  ur, vr, pr = resid_stokes3 ( n, x, y )

  print ''
  print '           Minimum       Maximum'
  print ''
  print '  Ur:  %14.6g  %14.6g' % ( np.min ( np.abs ( ur ) ), np.max ( np.abs ( ur ) ) )
  print '  Vr:  %14.6g  %14.6g' % ( np.min ( np.abs ( vr ) ), np.max ( np.abs ( vr ) ) )
  print '  Pr:  %14.6g  %14.6g' % ( np.min ( np.abs ( pr ) ), np.max ( np.abs ( pr ) ) )

  print ''
  print 'RESID_STOKES3_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  resid_stokes3_test ( )
  timestamp ( )

