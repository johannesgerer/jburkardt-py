#!/usr/bin/env python

def bvec_test ( ):

#*****************************************************************************80
#
## BVEC_TEST tests the BVEC library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    13 March 2015
#
#  Author:
#
#    John Burkardt
#
  from bvec_add                       import bvec_add_test
  from bvec_complement2               import bvec_complement2_test
  from bvec_mul                       import bvec_mul
  from bvec_next                      import bvec_next_test
  from bvec_next_grlex                import bvec_next_grlex_test
  from bvec_print                     import bvec_print_test
  from bvec_sub                       import bvec_sub_test
  from bvec_to_i4                     import bvec_to_i4_test
  from bvec_uniform                   import bvec_uniform_test
  from i4_to_bvec                     import i4_to_bvec_test
  from i4_uniform_ab                  import i4_uniform_ab_test

  print ''
  print 'BVEC_TEST'
  print '  Python version:'
  print '  Test the BVEC library.'

  bvec_add_test ( )
  bvec_complement2_test ( )
  bvec_mul_test ( )
  bvec_next_test ( )
  bvec_next_grlex_test ( )
  bvec_print_test ( )
  bvec_sub_test ( )
  bvec_to_i4_test ( )
  bvec_uniform_test ( )
  i4_to_bvec_test ( )
  i4_uniform_ab_test ( )
#
#  Terminate.
#
  print ''
  print 'BVEC_TEST:'
  print '  Normal end of execution.'
  print ''

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  bvec_test ( )
  timestamp ( )
