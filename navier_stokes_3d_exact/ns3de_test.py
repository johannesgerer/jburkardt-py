#! /usr/bin/env python

def ns3de_test ( ):

#*****************************************************************************80
#
## NS3DE_TEST tests the NS3DE library.
#
#  Location:
#
#    http://people.sc.fsu.edu/~jburkardt/py_src/navier_stokes_3d_exact/ns3de_test.py
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 January 2015
#
#  Author:
#
#    John Burkardt
#
  from r8vec_amax       import r8vec_amax_test
  from r8vec_amin       import r8vec_amin_test
  from r8vec_max        import r8vec_max_test
  from r8vec_min        import r8vec_min_test
  from r8vec_print      import r8vec_print_test
  from r8vec_uniform_ab import r8vec_uniform_ab_test
  from resid_ethier     import resid_ethier_test
  from uvwp_ethier      import uvwp_ethier_test

  print ''
  print 'NS3DE_TEST'
  print '  Python version'
  print '  Test the NS3DE library.'

  r8vec_amax_test ( )
  r8vec_amin_test ( )
  r8vec_max_test ( )
  r8vec_min_test ( )
  r8vec_print_test ( )
  r8vec_uniform_ab_test ( )
  uvwp_ethier_test ( )
  resid_ethier_test ( )
#
#  Terminate.
#
  print ''
  print 'NS3DE_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  ns3de_test ( )
  timestamp ( )
