#!/usr/bin/env python

def i4lib_test ( ):

#*****************************************************************************80
#
## I4LIB_TEST tests the I4LIB library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    27 May 2015
#
#  Author:
#
#    John Burkardt
#
  from i4_abs                     import i4_abs_test
  from i4_bit_hi1                 import i4_bit_hi1_test
  from i4_bit_lo0                 import i4_bit_lo0_test
  from i4_bit_lo1                 import i4_bit_lo1_test
  from i4_bit_reverse             import i4_bit_reverse_test
  from i4_ceiling                 import i4_ceiling_test
  from i4_characteristic          import i4_characteristic_test
  from i4_choose                  import i4_choose_test
  from i4_div_rounded             import i4_div_rounded_test
  from i4_division                import i4_division_test
  from i4_divp                    import i4_divp_test
  from i4_factorial               import i4_factorial_test
  from i4_factorial2              import i4_factorial2_test
  from i4_fall                    import i4_fall_test
  from i4_floor                   import i4_floor_test
  from i4_gcd                     import i4_gcd_test
  from i4_gcdb                    import i4_gcdb_test
  from i4_huge                    import i4_huge_test
  from i4_huge_normalizer         import i4_huge_normalizer_test
  from i4_is_even                 import i4_is_even_test
  from i4_is_odd                  import i4_is_odd_test
  from i4_is_prime                import i4_is_prime_test
  from i4_lcm                     import i4_lcm_test
  from i4_log_10                  import i4_log_10_test
  from i4_log_2                   import i4_log_2_test
  from i4_log_i4                  import i4_log_i4_test
  from i4_log_r8                  import i4_log_r8_test
  from i4_mant                    import i4_mant_test
  from i4_max                     import i4_max_test
  from i4_min                     import i4_min_test
  from i4_mod_inv                 import i4_mod_inv
  from i4_moddiv                  import i4_moddiv_test
  from i4_modp                    import i4_modp_test
  from i4_mop                     import i4_mop_test
  from i4_power                   import i4_power_test
  from i4_rise                    import i4_rise_test
  from i4_sign                    import i4_sign_test
  from i4_sign3                   import i4_sign3_test
  from i4_swap                    import i4_swap_test
  from i4_swap3                   import i4_swap3_test
  from i4_to_angle                import i4_to_angle_test
  from i4_to_halton               import i4_to_halton_test
  from i4_to_isbn                 import i4_to_isbn_test
  from i4_to_l4                   import i4_to_l4_test
  from i4_to_pascal               import i4_to_pascal_test
  from i4_to_pascal_degree        import i4_to_pascal_degree_test
  from i4_to_triangle             import i4_to_triangle_test
  from i4_uniform_ab              import i4_uniform_ab_test
  from i4_unswap3                 import i4_unswap3_test
  from i4_walsh_1d                import i4_walsh_1d_test
  from i4_width                   import i4_width_test
  from i4_wrap                    import i4_wrap_test
  from i4_xor                     import i4_xor_test

  from i4mat_indicator            import i4mat_indicator_test
  from i4mat_max                  import i4mat_max_test
  from i4mat_min                  import i4mat_min_test
  from i4mat_mm                   import i4mat_mm_test
  from i4mat_print                import i4mat_print_test
  from i4mat_print_some           import i4mat_print_some_test
  from i4mat_transpose_print      import i4mat_transpose_print_test
  from i4mat_transpose_print_some import i4mat_transpose_print_some_test
  from i4mat_u1_inverse           import i4mat_u1_inverse_test
  from i4mat_uniform_ab           import i4mat_uniform_ab_test

  from i4vec_add                  import i4vec_add_test
  from i4vec_amax                 import i4vec_amax_test
  from i4vec_amin                 import i4vec_amin_test
  from i4vec_concatenate          import i4vec_concatenate_test
  from i4vec_copy                 import i4vec_copy_test
  from i4vec_cum                  import i4vec_cum_test
  from i4vec_cum0                 import i4vec_cum0_test
  from i4vec_decrement            import i4vec_decrement_test
  from i4vec_frac                 import i4vec_frac_test
  from i4vec_increment            import i4vec_increment_test
  from i4vec_index                import i4vec_index_test
  from i4vec_indicator0           import i4vec_indicator0_test
  from i4vec_indicator1           import i4vec_indicator1_test
  from i4vec_max                  import i4vec_max_test
  from i4vec_max_index_last       import i4vec_max_index_last_test
  from i4vec_min                  import i4vec_min_test
  from i4vec_pairwise_prime       import i4vec_pairwise_prime_test
  from i4vec_permute              import i4vec_permute_test
  from i4vec_permute_uniform      import i4vec_permute_uniform_test
  from i4vec_print                import i4vec_print_test
  from i4vec_product              import i4vec_product_test
  from i4vec_reverse              import i4vec_reverse_test
  from i4vec_sort_heap_index_a    import i4vec_sort_heap_index_a_test
  from i4vec_sort_heap_index_d    import i4vec_sort_heap_index_d_test
  from i4vec_sum                  import i4vec_sum_test
  from i4vec_transpose_print      import i4vec_transpose_print_test
  from i4vec_uniform_ab           import i4vec_uniform_ab_test

  from pascal_to_i4               import pascal_to_i4_test

  from perm0_check                import perm0_check_test
  from perm0_uniform              import perm0_uniform_test

  from perm1_check                import perm1_check_test
  from perm1_uniform              import perm1_uniform_test

  from prime                      import prime_test

  from r8_uniform_ab              import r8_uniform_ab_test

  from timestamp                  import timestamp_test

  from triangle_to_i4             import triangle_to_i4_test

  print ''
  print 'I4LIB_TEST'
  print '  Python version:'
  print '  Test the I4LIB library.'

  i4_abs_test ( )
  i4_bit_hi1_test ( )
  i4_bit_lo0_test ( )
  i4_bit_lo1_test ( )
  i4_bit_reverse_test ( )
  i4_ceiling_test ( )
  i4_characteristic_test ( )
  i4_choose_test ( )
  i4_div_rounded_test ( )
  i4_division_test ( )
  i4_divp_test ( )
  i4_factorial_test ( )
  i4_factorial2_test ( )
  i4_fall_test ( )
  i4_floor_test ( )
  i4_gcd_test ( )
  i4_gcdb_test ( )
  i4_huge_test ( )
  i4_huge_normalizer_test ( )
  i4_is_even_test ( )
  i4_is_odd_test ( )
  i4_is_prime_test ( )
  i4_lcm_test ( )
  i4_log_10_test ( )
  i4_log_2_test ( )
  i4_log_i4_test ( )
  i4_log_r8_test ( )
  i4_mant_test ( )
  i4_max_test ( )
  i4_min_test ( )
  i4_moddiv_test ( )
  i4_modp_test ( )
  i4_mop_test ( )
  i4_power_test ( )
  i4_rise_test ( )
  i4_sign_test ( )
  i4_sign3_test ( )
  i4_swap_test ( )
  i4_swap3_test ( )
  i4_to_angle_test ( )
  i4_to_halton_test ( )
  i4_to_isbn_test ( )
  i4_to_l4_test ( )
  i4_to_pascal_test ( )
  i4_to_pascal_degree_test ( )
  i4_to_triangle_test ( )
  i4_uniform_ab_test ( )
  i4_unswap3_test ( )
  i4_walsh_1d_test ( )
  i4_width_test ( )
  i4_wrap_test ( )
  i4_xor_test ( )

  i4mat_indicator_test ( )
  i4mat_max_test ( )
  i4mat_min_test ( )
  i4mat_mm_test ( )
  i4mat_print_test ( )
  i4mat_print_some_test ( )
  i4mat_transpose_print_test ( )
  i4mat_transpose_print_some_test ( )
  i4mat_u1_inverse_test ( )
  i4mat_uniform_ab_test ( )

  i4vec_add_test ( )
  i4vec_amax_test ( )
  i4vec_amin_test ( )
  i4vec_concatenate_test ( )
  i4vec_copy_test ( )
  i4vec_cum_test ( )
  i4vec_cum0_test ( )
  i4vec_decrement_test ( )
  i4vec_frac_test ( )
  i4vec_increment_test ( )
  i4vec_index_test ( )
  i4vec_indicator0_test ( )
  i4vec_indicator1_test ( )
  i4vec_max_test ( )
  i4vec_max_index_last_test ( )
  i4vec_min_test ( )
  i4vec_pairwise_prime_test ( )
  i4vec_permute_test ( )
  i4vec_permute_uniform_test ( )
  i4vec_print_test ( )
  i4vec_product_test ( )
  i4vec_reverse_test ( )
  i4vec_sort_heap_index_a_test ( )
  i4vec_sort_heap_index_d_test ( )
  i4vec_sum_test ( )
  i4vec_transpose_print_test ( )
  i4vec_uniform_ab_test ( )

  pascal_to_i4_test ( ) 

  perm0_check_test ( )
  perm0_uniform_test ( )

  perm1_check_test ( )
  perm1_uniform_test ( )

  prime_test ( )

  r8_uniform_ab_test ( )

  timestamp_test ( )

  triangle_to_i4_test ( )
#
#  Terminate.
#
  print ''
  print 'I4LIB_TEST:'
  print '  Normal end of execution.'

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4lib_test ( )
  timestamp ( )

