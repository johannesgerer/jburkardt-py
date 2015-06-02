#! /usr/bin/env python
#
def resid_stokes1 ( n, x, y ):

#*****************************************************************************80
#
## RHS_STOKES1 returns residuals of the exact Stokes solution #1.
#
#  Location:
#
#    http://people.sc.fsu.edu/~jburkardt/py_src/stokes_2d_exact/resid_stokes1.py
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
  from rhs_stokes1 import rhs_stokes1

  ur = np.zeros ( n )
  vr = np.zeros ( n )
  pr = np.zeros ( n )

  f, g, h = rhs_stokes1 ( n, x, y )

  u = - 2.0 * x ** 2 * ( x - 1.0 ) ** 2 * y * ( y - 1.0 ) * ( 2.0 * y - 1.0 )

  ux = - 2.0 * ( 4.0 * x ** 3 - 6.0 * x ** 2  \
       + 2.0 * x ) * y * ( y - 1.0 ) * ( 2.0 * y - 1.0 )

  uxx = - 2.0 * ( 12.0 * x ** 2 - 12.0 * x + 2.0 ) \
        * ( 2.0 * y ** 3 - 3.0 * y ** 2 + y )

  uy = - 2.0 * x ** 2 * ( x - 1.0 ) ** 2 * ( 6.0 * y ** 2 - 3.0 * y + 1.0 )

  uyy = - 2.0 * ( x ** 4 - 2.0 * x ** 3 + x ** 2 ) * ( 12.0 * y - 6.0 )

  v =   2.0 * x * ( x - 1.0 ) * ( 2.0 * x - 1.0 ) * y ** 2 * ( y - 1.0 ) ** 2

  vx =   2.0 * ( 6.0 * x ** 2 - 6.0 * x + 1.0 ) * y ** 2 * ( y - 1.0 ) ** 2

  vxx =   2.0 * ( 12.0 * x - 6.0 ) * y ** 2 * ( y - 1.0 ) ** 2

  vy =   2.0 * x * ( x - 1.0 ) * ( 2.0 * x - 1.0 ) \
         * ( 4.0 * y ** 3 - 6.0 * y ** 2 + 2.0 * y )

  vyy =   2.0 * x * ( x - 1.0 ) * ( 2.0 * x - 1.0 ) \
          * ( 12.0 * y ** 2 - 12.0 * y + 2.0 )

  p = 0.0
  px = 0.0
  py = 0.0

  ur = px - ( uxx + uyy ) - f
  vr = py - ( vxx + vyy ) - g
  pr = ux + vy - h

  return ur, vr, pr

def resid_stokes1_test ( ):

#*****************************************************************************80
#
## RESID_STOKES1_TEST samples the residuals.
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
  print 'RESID_STOKES1_TEST'
  print '  Exact Stokes solution #1.'
  print '  Sample the Stokes residuals.'

  n = 1000
  x_lo = 0.0
  x_hi = +1.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( n, x_lo, x_hi, seed )
  y, seed = r8vec_uniform_ab ( n, x_lo, x_hi, seed )

  ur, vr, pr = resid_stokes1 ( n, x, y )

  print ''
  print '           Minimum       Maximum'
  print ''
  print '  Ur:  %14.6g  %14.6g' % ( np.min ( np.abs ( ur ) ), np.max ( np.abs ( ur ) ) )
  print '  Vr:  %14.6g  %14.6g' % ( np.min ( np.abs ( vr ) ), np.max ( np.abs ( vr ) ) )
  print '  Pr:  %14.6g  %14.6g' % ( np.min ( np.abs ( pr ) ), np.max ( np.abs ( pr ) ) )

  print ''
  print 'RESID_STOKES1_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  resid_stokes1_test ( )
  timestamp ( )

