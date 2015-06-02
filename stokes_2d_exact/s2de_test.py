#! /usr/bin/env python

def s2de_test ( ):

#*****************************************************************************80
#
## S2DE_TEST tests the NS2DE library.
#
#  Location:
#
#    http://people.sc.fsu.edu/~jburkardt/py_src/stokes_2d_exact/s2de_test.py
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
  from grid_2d            import grid_2d_test
  from r8vec_amax         import r8vec_amax_test
  from r8vec_amin         import r8vec_amin_test
  from r8vec_max          import r8vec_max_test
  from r8vec_min          import r8vec_min_test
  from r8vec_norm_l2      import r8vec_norm_l2_test
  from r8vec_print        import r8vec_print_test
  from r8vec_uniform_ab   import r8vec_uniform_ab_test
  from resid_stokes1      import resid_stokes1_test
  from resid_stokes2      import resid_stokes2_test
  from resid_stokes3      import resid_stokes3_test
  from rhs_stokes1        import rhs_stokes1_test
  from rhs_stokes2        import rhs_stokes2_test
  from rhs_stokes3        import rhs_stokes3_test
  from stokes_gnuplot     import stokes1_gnuplot_test
  from stokes_gnuplot     import stokes2_gnuplot_test
  from stokes_gnuplot     import stokes3_gnuplot_test
  from stokes_matplotlib  import stokes1_matplotlib_test
  from stokes_matplotlib  import stokes2_matplotlib_test
  from stokes_matplotlib  import stokes3_matplotlib_test
  from uvp_stokes1        import uvp_stokes1_test
  from uvp_stokes2        import uvp_stokes2_test
  from uvp_stokes3        import uvp_stokes3_test

  print ''
  print 'S2DE_TEST'
  print '  Python version'
  print '  Test the S2DE library.'

  r8vec_amax_test ( )
  r8vec_amin_test ( )
  r8vec_max_test ( )
  r8vec_min_test ( )
  r8vec_norm_l2_test ( )
  r8vec_print_test ( )
  r8vec_uniform_ab_test ( )

  grid_2d_test ( )

  uvp_stokes1_test ( )
  rhs_stokes1_test ( )
  resid_stokes1_test ( )
  stokes1_gnuplot_test ( )
  stokes1_matplotlib_test ( )

  uvp_stokes2_test ( )
  rhs_stokes2_test ( )
  resid_stokes2_test ( )
  stokes2_gnuplot_test ( )
  stokes2_matplotlib_test ( )

  uvp_stokes3_test ( )
  rhs_stokes3_test ( )
  resid_stokes3_test ( )
  stokes3_gnuplot_test ( )
  stokes3_matplotlib_test ( )
#
#  Terminate.
#
  print ''
  print 'S2DE_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  s2de_test ( )
  timestamp ( )
