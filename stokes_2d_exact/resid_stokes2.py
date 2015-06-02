#! /usr/bin/env python
#
def resid_stokes2 ( n, x, y ):

#*****************************************************************************80
#
## RHS_STOKES2 returns residuals of the exact Stokes solution #2.
#
#  Location:
#
#    http://people.sc.fsu.edu/~jburkardt/py_src/stokes_2d_exact/resid_stokes2.py
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Junping Wang, Yanqiu Wang, Xiu Ye,
#    A robust numerical method for Stokes equations based on divergence-free
#    H(div) finite element methods,
#    SIAM Journal on Scientific Computing,
#    Volume 31, Number 4, 2009, pages 2784-2802.
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
  from rhs_stokes2 import rhs_stokes2

  ur = np.zeros ( n )
  vr = np.zeros ( n )
  pr = np.zeros ( n )

  f, g, h = rhs_stokes2 ( n, x, y )

  u =     2.0              * np.sin ( 2.0 * np.pi * x ) * np.cos ( 2.0 * np.pi * y )
  ux =    4.0 * np.pi      * np.cos ( 2.0 * np.pi * x ) * np.cos ( 2.0 * np.pi * y )
  uxx = - 8.0 * np.pi ** 2 * np.sin ( 2.0 * np.pi * x ) * np.cos ( 2.0 * np.pi * y )
  uy =  - 4.0 * np.pi      * np.sin ( 2.0 * np.pi * x ) * np.sin ( 2.0 * np.pi * y )
  uyy = - 8.0 * np.pi ** 2 * np.sin ( 2.0 * np.pi * x ) * np.cos ( 2.0 * np.pi * y )

  v =   - 2.0              * np.cos ( 2.0 * np.pi * x ) * np.sin ( 2.0 * np.pi * y )
  vx =    4.0 * np.pi      * np.sin ( 2.0 * np.pi * x ) * np.sin ( 2.0 * np.pi * y )
  vxx =   8.0 * np.pi ** 2 * np.cos ( 2.0 * np.pi * x ) * np.sin ( 2.0 * np.pi * y )
  vy =  - 4.0 * np.pi      * np.cos ( 2.0 * np.pi * x ) * np.cos ( 2.0 * np.pi * y )
  vyy =   8.0 * np.pi ** 2 * np.cos ( 2.0 * np.pi * x ) * np.sin ( 2.0 * np.pi * y )

  p = x ** 2 + y ** 2
  px = 2.0 * x
  py = 2.0 * y

  ur = px - ( uxx + uyy ) - f
  vr = py - ( vxx + vyy ) - g
  pr = ux + vy - h

  return ur, vr, pr

def resid_stokes2_test ( ):

#*****************************************************************************80
#
## RESID_STOKES2_TEST samples the residuals.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 January 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from r8vec_uniform_ab import r8vec_uniform_ab

  print ''
  print 'RESID_STOKES2_TEST'
  print '  Exact Stokes solution #2.'
  print '  Sample the Stokes residuals.'

  n = 1000
  x_lo = 0.0
  x_hi = +1.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( n, x_lo, x_hi, seed )
  y, seed = r8vec_uniform_ab ( n, x_lo, x_hi, seed )

  ur, vr, pr = resid_stokes2 ( n, x, y )

  print ''
  print '           Minimum       Maximum'
  print ''
  print '  Ur:  %14.6g  %14.6g' % ( np.min ( np.abs ( ur ) ), np.max ( np.abs ( ur ) ) )
  print '  Vr:  %14.6g  %14.6g' % ( np.min ( np.abs ( vr ) ), np.max ( np.abs ( vr ) ) )
  print '  Pr:  %14.6g  %14.6g' % ( np.min ( np.abs ( pr ) ), np.max ( np.abs ( pr ) ) )

  print ''
  print 'RESID_STOKES2_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  resid_stokes2_test ( )
  timestamp ( )

