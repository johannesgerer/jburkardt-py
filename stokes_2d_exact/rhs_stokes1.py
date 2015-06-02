#! /usr/bin/env python
#
def rhs_stokes1 ( n, x, y ):

#*****************************************************************************80
#
## RHS_STOKES1 returns the right hand sides of the exact Stokes solution #1.
#
#  Location:
#
#    http://people.sc.fsu.edu/~jburkardt/py_src/stokes_2d_exact/rhs_stokes1.py
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
#    Output, real F(N), G(N), H(N), the right hand sides in the U,
#    V and P equations.
#
  import numpy as np

  f = np.zeros ( n )
  g = np.zeros ( n )
  h = np.zeros ( n )

  f = + 2.0 \
          * ( 12.0 * x ** 2 - 12.0 * x + 2.0 ) \
          * ( 2.0 * y ** 3 - 3.0 * y ** 2 + y ) \
          + 2.0 \
          * ( x ** 4 - 2.0 * x ** 3 + x ** 2 ) \
          * ( 12.0 * y - 6.0 )

  g = - 2.0 \
          * ( 12.0 * x - 6.0 ) \
          * ( y ** 4 - 2.0 * y ** 3 + y ** 2 ) \
          - 2.0 \
          * ( 2.0 * x ** 3 - 3.0 * x ** 2 + x ) \
          * ( 12.0 * y ** 2 - 12.0 * y + 2.0 )

  return f, g, h

def rhs_stokes1_test ( ):

#*****************************************************************************80
#
## RHS_STOKES1_TEST samples the right hand sides.
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
  print 'RHS_STOKES1_TEST'
  print '  Exact Stokes solution #1.'
  print '  Estimate the range of the right hand side functions'
  print '  using a region that is the unit square.'

  n = 1000
  x_lo = 0.0
  x_hi = +1.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( n, x_lo, x_hi, seed )
  y, seed = r8vec_uniform_ab ( n, x_lo, x_hi, seed )

  f, g, h = rhs_stokes1 ( n, x, y )

  print ''
  print '           Minimum       Maximum'
  print ''
  print '  U:  %14.6g  %14.6g' % ( np.min ( f ), np.max ( f ) )
  print '  V:  %14.6g  %14.6g' % ( np.min ( g ), np.max ( g ) )
  print '  P:  %14.6g  %14.6g' % ( np.min ( h ), np.max ( h ) )

  print ''
  print 'RHS_STOKES1_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  rhs_stokes1_test ( )
  timestamp ( )

