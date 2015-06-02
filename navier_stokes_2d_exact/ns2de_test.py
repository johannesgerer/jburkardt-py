#! /usr/bin/env python

def ns2de_test ( ):

#*****************************************************************************80
#
## NS2DE_TEST tests the NS2DE library.
#
#  Location:
#
#    http://people.sc.fsu.edu/~jburkardt/py_src/navier_stokes_2d_exact/ns2de_test.py
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 March 2015
#
#  Author:
#
#    John Burkardt
#
  from grid_2d                import grid_2d_test
  from ns2de_gnuplot          import ns2de_gnuplot_lucas_test
  from ns2de_gnuplot          import ns2de_gnuplot_spiral_test
  from ns2de_gnuplot          import ns2de_gnuplot_taylor_test
  from ns2de_matplotlib       import ns2de_matplotlib_lucas_test
  from ns2de_matplotlib       import ns2de_matplotlib_spiral_test
  from ns2de_matplotlib       import ns2de_matplotlib_taylor_test
  from parameter_spiral_test  import parameter_spiral_test
  from parameter_taylor_test  import parameter_taylor_test
  from r8vec_amax             import r8vec_amax_test
  from r8vec_amin             import r8vec_amin_test
  from r8vec_max              import r8vec_max_test
  from r8vec_min              import r8vec_min_test
  from r8vec_norm_l2          import r8vec_norm_l2_test
  from r8vec_print            import r8vec_print_test
  from r8vec_uniform_ab       import r8vec_uniform_ab_test
  from resid_lucas            import resid_lucas_test
  from resid_spiral           import resid_spiral_test
  from resid_taylor           import resid_taylor_test
  from rhs_lucas              import rhs_lucas_test
  from rhs_spiral             import rhs_spiral_test
  from rhs_taylor             import rhs_taylor_test
  from uvp_lucas              import uvp_lucas_test
  from uvp_lucas              import uvp_lucas_test2
  from uvp_spiral             import uvp_spiral_test
  from uvp_spiral             import uvp_spiral_test2
  from uvp_taylor             import uvp_taylor_test
  from uvp_taylor             import uvp_taylor_test2

  print ''
  print 'NS2DE_TEST'
  print '  Python version'
  print '  Test the NS2DE library.'

  r8vec_amax_test ( )
  r8vec_amin_test ( )
  r8vec_max_test ( )
  r8vec_min_test ( )
  r8vec_norm_l2_test ( )
  r8vec_print_test ( )
  r8vec_uniform_ab_test ( )

  grid_2d_test ( )
#
#  Taylor Vortes Flow
#
  uvp_taylor_test ( )
  uvp_taylor_test2 ( )
  rhs_taylor_test ( )
  resid_taylor_test ( )
  ns2de_gnuplot_taylor_test ( )
  ns2de_matplotlib_taylor_test ( )
  parameter_taylor_test ( )
#
#  Spiral Flow.
#
  uvp_spiral_test ( )
  uvp_spiral_test2 ( )
  rhs_spiral_test ( )
  resid_spiral_test ( )
  ns2de_gnuplot_spiral_test ( )
  ns2de_matplotlib_spiral_test ( )
  parameter_spiral_test ( )
#
#  Lucas Bystricky Flow.
#
  uvp_lucas_test ( )
  uvp_lucas_test2 ( )
  rhs_lucas_test ( )
  resid_lucas_test ( )
  ns2de_gnuplot_lucas_test ( )
  ns2de_matplotlib_lucas_test ( )
#
#  Terminate.
#
  print ''
  print 'NS2DE_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  ns2de_test ( )
  timestamp ( )
