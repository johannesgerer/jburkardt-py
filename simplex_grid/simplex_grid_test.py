#!/usr/bin/env python

def simplex_grid_test ( ):

#*****************************************************************************80
#
## SIMPLEX_GRID_TEST tests the SIMPLEX_GRID library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    23 April 2015
#
#  Author:
#
#    John Burkardt
#
  from comp_next_grlex              import comp_next_grlex_test
  from comp_random                  import comp_random_test
  from comp_random_grlex            import comp_random_grlex_test
  from comp_rank_grlex              import comp_rank_grlex_test
  from comp_unrank_grlex            import comp_unrank_grlex_test
  from i4_choose                    import i4_choose_test
  from i4_uniform_ab                import i4_uniform_ab_test
  from i4mat_print                  import i4mat_print_test
  from i4mat_print_some             import i4mat_print_some_test
  from i4vec_print                  import i4vec_print_test
  from i4vec_sum                    import i4vec_sum_test
  from i4vec_uniform_ab             import i4vec_uniform_ab_test
  from ksub_random2                 import ksub_random2_test
  from r8_uniform_01                import r8_uniform_01_test
  from r8mat_print                  import r8mat_print_test
  from r8mat_print_some             import r8mat_print_some_test
  from r8mat_write                  import r8mat_write_test
  from simplex_grid_count           import simplex_grid_count_test
  from simplex_grid_index_all       import simplex_grid_index_all_test
  from simplex_grid_index_next      import simplex_grid_index_next_test
  from simplex_grid_index_sample    import simplex_grid_index_sample_test
  from simplex_grid_index_to_point  import simplex_grid_index_to_point_test01
  from simplex_grid_index_to_point  import simplex_grid_index_to_point_test02
  from timestamp                    import timestamp_test

  print ''
  print 'SIMPLEX_GRID_TEST'
  print '  Python version:'
  print '  Test the SIMPLEX_GRID library.'
#
#  Utilities:
#
  comp_next_grlex_test ( )
  comp_random_test ( )
  comp_random_grlex_test ( )
  comp_rank_grlex_test ( )
  comp_unrank_grlex_test ( )

  i4_choose_test ( )
  i4_uniform_ab_test ( )

  i4mat_print_test ( )
  i4mat_print_some_test ( )

  i4vec_print_test ( )
  i4vec_sum_test ( )
  i4vec_uniform_ab_test ( )

  ksub_random2_test ( )

  r8_uniform_01_test ( )

  r8mat_print_test ( )
  r8mat_print_some_test ( )
  r8mat_write_test ( )

  timestamp_test ( )
#
#  Library.
#
  simplex_grid_count_test ( )
  simplex_grid_index_next_test ( )
  simplex_grid_index_sample_test ( )
  simplex_grid_index_all_test ( )
  simplex_grid_index_to_point_test01 ( )
  simplex_grid_index_to_point_test02 ( )
#
#  Terminate.
#
  print ''
  print 'SIMPLEX_GRID_TEST:'
  print '  Normal end of execution.'

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  simplex_grid_test ( )
  timestamp ( )
