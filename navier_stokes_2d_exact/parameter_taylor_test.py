#! /usr/bin/env python
#
def parameter_taylor_test ( ):

#*****************************************************************************80
#
## PARAMETER_TAYLOR_TEST monitors solution norms over time for various values of NU, RHO.
#
#  Location:
#
#    http://people.sc.fsu.edu/~jburkardt/py_src/navier_stokes_2d_exact/parameter_taylor_test.py
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 January 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from r8vec_norm_l2 import r8vec_norm_l2
  from r8vec_uniform_ab import r8vec_uniform_ab
  from uvp_taylor import uvp_taylor

  print ''
  print 'PARAMETER_TAYLOR_TEST'
  print '  Taylor Vortex Flow'
  print '  Monitor solution norms over time for various'
  print '  values of NU, RHO.'

  n = 1000
  xy_lo = 0.5
  xy_hi = 2.5
  seed = 123456789
  x, seed = r8vec_uniform_ab ( n, xy_lo, xy_hi, seed )
  y, seed = r8vec_uniform_ab ( n, xy_lo, xy_hi, seed )
#
#  Vary RHO.
#
  print ''
  print '  RHO affects the pressure scaling.'
  print ''
  print '     RHO         NU           T     ||U||       ||V||       ||P||'
  print ''

  nu = 1.0
  rho = 1.0

  for j in range ( 0, 3 ):

    for k in range ( 0, 6 ):

      t = k / 5.0

      u, v, p = uvp_taylor ( nu, rho, n, x, y, t )

      u_norm = r8vec_norm_l2 ( n, u ) / n
      v_norm = r8vec_norm_l2 ( n, v ) / n
      p_norm = r8vec_norm_l2 ( n, p ) / n

      print '  %10.4g  %10.4g  %8.4g  %10.4g  %10.4g  %10.4g' \
        % ( rho, nu, t, u_norm, v_norm, p_norm )

    print ''
    rho = rho / 100.0
#
#  Vary NU.
#
  print ''
  print '  NU affects the time scaling.'
  print ''
  print '     RHO         NU           T     ||U||       ||V||       ||P||'
  print ''

  nu = 1.0;
  rho = 1.0;
  
  for i in range ( 0, 4 ):

    for k in range ( 0, 6 ):

      t = k / 5.0

      u, v, p = uvp_taylor ( nu, rho, n, x, y, t )

      u_norm = r8vec_norm_l2 ( n, u ) / n
      v_norm = r8vec_norm_l2 ( n, v ) / n
      p_norm = r8vec_norm_l2 ( n, p ) / n

      print '  %10.4g  %10.4g  %8.4g  %10.4g  %10.4g  %10.4g' \
        % ( rho, nu, t, u_norm, v_norm, p_norm )

    print ''

    nu = nu / 10.0

  print ''
  print 'PARAMETER_TAYLOR_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  parameter_taylor_test ( )
  timestamp ( )

