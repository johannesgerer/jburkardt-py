#!/usr/bin/env python

def lpp_test ( ):

#*****************************************************************************80
#
## LPP_TEST tests the LPP library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    31 October 2014
#
#  Author:
#
#    John Burkardt
#
  from comp_enum               import comp_enum_test
  from comp_next_grlex         import comp_next_grlex_test
  from comp_random_grlex       import comp_random_grlex_test
  from comp_rank_grlex         import comp_rank_grlex_test
  from comp_unrank_grlex       import comp_unrank_grlex_test
  from i4_choose               import i4_choose_test
  from i4_uniform_ab           import i4_uniform_ab_test
  from i4vec_permute           import i4vec_permute_test
  from i4vec_print             import i4vec_print_test
  from i4vec_sort_heap_index_a import i4vec_sort_heap_index_a_test
  from i4vec_sum               import i4vec_sum_test
  from i4vec_uniform_ab        import i4vec_uniform_ab_test
  from lp_coefficients         import lp_coefficients_test
  from lp_value                import lp_value_test
  from lp_values               import lp_values_test
  from lpp_to_polynomial       import lpp_to_polynomial_test
  from lpp_value               import lpp_value_test
  from mono_next_grlex         import mono_next_grlex_test
  from mono_print              import mono_print_test
  from mono_rank_grlex         import mono_rank_grlex_test
  from mono_unrank_grlex       import mono_unrank_grlex_test
  from mono_upto_enum          import mono_upto_enum_test
  from mono_upto_next_grlex    import mono_upto_next_grlex_test
  from mono_upto_random        import mono_upto_random_test
  from mono_value              import mono_value_test
  from perm_uniform            import perm_uniform_test
  from polynomial_compress     import polynomial_compress_test
  from polynomial_print        import polynomial_print_test
  from polynomial_sort         import polynomial_sort_test
  from polynomial_value        import polynomial_value_test
  from r8mat_print             import r8mat_print_test
  from r8mat_print_some        import r8mat_print_some_test
  from r8mat_uniform_ab        import r8mat_uniform_ab_test
  from r8vec_permute           import r8vec_permute_test
  from r8vec_print             import r8vec_print_test
  from r8vec_uniform_ab        import r8vec_uniform_ab_test
  from timestamp               import timestamp

  print ''
  print 'LPP_TEST'
  print '  Python version:'
  print '  Test the LPP library.'

  i4_choose_test ( )
  i4_uniform_ab_test ( )

  i4vec_permute_test ( )
  i4vec_print_test ( )
  i4vec_sort_heap_index_a_test ( )
  i4vec_sum_test ( )
  i4vec_uniform_ab_test ( )

  r8vec_permute_test ( )
  r8vec_print_test ( )
  r8vec_uniform_ab_test ( )

  r8mat_print_test ( )
  r8mat_print_some_test ( )
  r8mat_uniform_ab_test ( )

  perm_uniform_test ( )

  comp_enum_test ( )
  comp_next_grlex_test ( )
  comp_random_grlex_test ( )
  comp_rank_grlex_test ( )
  comp_unrank_grlex_test ( )

  mono_next_grlex_test ( )
  mono_print_test ( )
  mono_rank_grlex_test ( )
  mono_unrank_grlex_test ( )
  mono_upto_enum_test ( )
  mono_upto_next_grlex_test ( )
  mono_upto_random_test ( )
  mono_value_test ( )

  polynomial_compress_test ( )
  polynomial_print_test ( )
  polynomial_sort_test ( )
  polynomial_value_test ( )

  lp_coefficients_test ( )
  lp_value_test ( )
  lp_values_test ( )

  lpp_to_polynomial_test ( )
  lpp_value_test ( )
#
#  Terminate.
#
  print ''
  print 'LPP_TEST:'
  print '  Normal end of execution.'
  print ''

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp

  timestamp ( )
  lpp_test ( )
  timestamp ( )
