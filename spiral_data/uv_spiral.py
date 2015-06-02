#! /usr/bin/env python
#
def uv_spiral ( n, x, y, c ):

#*****************************************************************************80
#
## UV_SPIRAL computes a spiral velocity vector field.
#
#  Discussion:
#
#    Note that the continuous velocity field (U,V)(X,Y) that is discretely
#    sampled here satisfies the homogeneous continuity equation, that is,
#    it has zero divergence.  In other words:
#
#      dU/dX + dV/dY = 0.
#
#    This is by construction, since we have
#
#      U(X,Y) =  10 * d/dY ( PHI(X) * PHI(Y) )
#      V(X,Y) = -10 * d/dX ( PHI(X) * PHI(Y) )
#
#    which guarantees zero divergence.
#
#    The underlying function PHI is defined by
#
#      PHI(Z) = ( 1 - cos ( C * pi * Z ) ) * ( 1 - Z )^2
#
#    where C is a parameter.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of evaluation points.
#
#    Input, real X(N), Y(N), the coordinates of the evaluation points.
#
#    Input, real C, a parameter, typically between 0 and 2 * PI.
#
#    Output, real U(N), V(N), the velocity components.
#
  import numpy as np

  u = np.zeros ( n )
  v = np.zeros ( n )

  u =   10.0 * ( 1.0 - np.cos ( c * np.pi * x ) ) \
           * ( 1.0 - x ) ** 2 \
           * ( \
               c * np.pi * np.sin ( c * np.pi * y ) * ( 1.0 - y ) ** 2 \
             - ( 1.0 - np.cos ( c * np.pi * y ) ) \
             * 2.0 * ( 1.0 - y ) \
             )

  v = - 10.0 * ( 1.0 - np.cos ( c * np.pi * y ) ) \
           * ( 1.0 - y ) ** 2 \
           * ( \
               c * np.pi * np.sin ( c * np.pi * x ) * ( 1.0 - x ) ** 2 \
             - ( 1.0 - np.cos ( c * np.pi * x ) ) \
             * 2.0 * ( 1.0 - x ) \
             )

  return u, v

def uv_spiral_test ( ):

#*****************************************************************************80
#
## UV_SPIRAL_TEST generates a field and estimates its range.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 January 2015
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
  print 'UV_SPIRAL_TEST'
  print '  Sample a spiral velocity field and estimate'
  print '  the range of the solution values.'

  n = 1000
  x_lo = 0.0
  x_hi = +1.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( n, x_lo, x_hi, seed )
  y, seed = r8vec_uniform_ab ( n, x_lo, x_hi, seed )

  c = 1.0
  u, v = uv_spiral ( n, x, y, c )

  print ''
  print '           Minimum       Maximum'
  print ''
  print '  U:  %14.6g  %14.6g' % ( np.min ( u ), np.max ( u ) )
  print '  V:  %14.6g  %14.6g' % ( np.min ( v ), np.max ( v ) )

  print ''
  print 'UV_SPIRAL_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  uv_spiral_test ( )
  timestamp ( )

