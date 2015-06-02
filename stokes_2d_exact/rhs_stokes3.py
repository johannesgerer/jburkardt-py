#! /usr/bin/env python
#
def rhs_stokes3 ( n, x, y ):

#*****************************************************************************80
#
## RHS_STOKES3 returns the right hand sides of the exact Stokes solution #3.
#
#  Location:
#
#    http://people.sc.fsu.edu/~jburkardt/py_src/stokes_2d_exact/rhs_stokes3.py
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
#    Output, real F(N), G(N), H(N), the right hand sides in the U,
#    V and P equations.
#
  import numpy as np

  f = np.zeros ( n )
  g = np.zeros ( n )
  h = np.zeros ( n )

  return f, g, h

def rhs_stokes3_test ( ):

#*****************************************************************************80
#
## RHS_STOKES3_TEST samples the right hand sides.
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
  print 'RHS_STOKES3_TEST'
  print '  Exact Stokes solution #3.'
  print '  Estimate the range of the right hand side functions'
  print '  using a region that is [-1,+1]x[-1,+1].'

  n = 1000
  x_lo = -1.0
  x_hi = +1.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( n, x_lo, x_hi, seed )
  y, seed = r8vec_uniform_ab ( n, x_lo, x_hi, seed )

  f, g, h = rhs_stokes3 ( n, x, y )

  print ''
  print '           Minimum       Maximum'
  print ''
  print '  U:  %14.6g  %14.6g' % ( np.min ( f ), np.max ( f ) )
  print '  V:  %14.6g  %14.6g' % ( np.min ( g ), np.max ( g ) )
  print '  P:  %14.6g  %14.6g' % ( np.min ( h ), np.max ( h ) )

  print ''
  print 'RHS_STOKES3_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  rhs_stokes3_test ( )
  timestamp ( )

