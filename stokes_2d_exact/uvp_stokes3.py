#! /usr/bin/env python
#
def uvp_stokes3 ( n, x, y ):

#*****************************************************************************80
#
## UVP_STOKES3 evaluates the exact Stokes solution #3.
#
#  Location:
#
#    http://people.sc.fsu.edu/~jburkardt/py_src/stokes_2d_exact/uvp_stokes3.py
#
#  Discussion:
#
#    The solution is defined over the unit square [-1,+1]x[-1,+1].
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
#    Output, real U(N), V(N), P(N), the velocity components and
#    pressure at each of the points.
#
  import numpy as np

  u = np.zeros ( n )
  v = np.zeros ( n )
  p = np.zeros ( n )

  u =   20.0 * x * y ** 3
  v =    5.0 * ( x ** 4  - y ** 4 )
  p =   60.0 * x ** 2 * y - 2.0 * y ** 3 + 10.0


  return u, v, p

def uvp_stokes3_test ( ):

#*****************************************************************************80
#
## UVP_STOKES3_TEST samples the solution.
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
  print 'UVP_STOKES3_TEST'
  print '  Exact Stokes solution #3.'
  print '  Estimate the range of velocity and pressure'
  print '  using a region that is [-1,+1]x[-1,+1].'

  n = 1000
  x_lo = -1.0
  x_hi = +1.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( n, x_lo, x_hi, seed )
  y, seed = r8vec_uniform_ab ( n, x_lo, x_hi, seed )

  u, v, p = uvp_stokes3 ( n, x, y )

  print ''
  print '           Minimum       Maximum'
  print ''
  print '  U:  %14.6g  %14.6g' % ( np.min ( u ), np.max ( u ) )
  print '  V:  %14.6g  %14.6g' % ( np.min ( v ), np.max ( v ) )
  print '  P:  %14.6g  %14.6g' % ( np.min ( p ), np.max ( p ) )

  print ''
  print 'UVP_STOKES1_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  uvp_stokes3_test ( )
  timestamp ( )

