#! /usr/bin/env python
#
def resid_spiral ( n, x, y, c ):

#*****************************************************************************80
#
## RESID_SPIRAL computes the residual for a spiral velocity vector field.
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
#    Output, real PR(N), the residual in the continuity equation.
#
  import numpy as np

  pr = np.zeros ( n )
  u = np.zeros ( n )
  ux = np.zeros ( n )
  v = np.zeros ( n )
  vy = np.zeros ( n )

  u =   10.0 * ( 1.0 - np.cos ( c * np.pi * x ) ) \
           * ( 1.0 - x ) ** 2 \
           * ( \
               c * np.pi * np.sin ( c * np.pi * y ) * ( 1.0 - y ) ** 2 \
             - ( 1.0 - np.cos ( c * np.pi * y ) ) \
             * 2.0 * ( 1.0 - y ) \
             )

  ux =   10.0 * \
    ( \
      c * np.pi * np.sin ( c * np.pi * x ) * ( 1.0 - x ) ** 2 \
      - ( 1.0 - np.cos ( c * np.pi * x ) ) \
      * 2.0 * ( 1.0 - x ) \
    ) \
    * \
    ( \
      c * np.pi * np.sin ( c * np.pi * y ) * ( 1.0 - y ) ** 2 \
      - ( 1.0 - np.cos ( c * np.pi * y ) ) \
      * 2.0 * ( 1.0 - y ) \
    );

  v = - 10.0 * ( 1.0 - np.cos ( c * np.pi * y ) ) \
           * ( 1.0 - y ) ** 2 \
           * ( \
               c * np.pi * np.sin ( c * np.pi * x ) * ( 1.0 - x ) ** 2 \
             - ( 1.0 - np.cos ( c * np.pi * x ) ) \
             * 2.0 * ( 1.0 - x ) \
             );

  vy =  - 10.0 * \
    ( \
      c * np.pi * np.sin ( c * np.pi * x ) * ( 1.0 - x ) ** 2 \
      - ( 1.0 - np.cos ( c * np.pi * x ) ) \
      * 2.0 * ( 1.0 - x ) \
    ) \
    * \
    ( \
      c * np.pi * np.sin ( c * np.pi * y ) * ( 1.0 - y ) ** 2 \
      - ( 1.0 - np.cos ( c * np.pi * y ) ) \
      * 2.0 * ( 1.0 - y ) \
    )

  pr = ux + vy;

  return pr

def resid_spiral_test ( ):

#*****************************************************************************80
#
## RESID_SPIRAL_TEST generates a field and samples its residuals.
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

  print ''
  print 'RESID_SPIRAL_TEST'
  print '  Sample a spiral velocity field and estimate the'
  print '  range of residuals in the continuity equation.'

  n = 1000
  x_lo = 0.0
  x_hi = +1.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( n, x_lo, x_hi, seed )
  y, seed = r8vec_uniform_ab ( n, x_lo, x_hi, seed )
  t = 0.0

  c = 1.00

  pr = resid_spiral ( n, x, y, c )

  print ''
  print '           Minimum       Maximum'
  print ''
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

