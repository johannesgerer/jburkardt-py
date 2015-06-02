#!/usr/bin/env python

def r8lib_test ( ):

#*****************************************************************************80
#
## R8LIB_TEST tests the R8LIB library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    24 May 2015
#
#  Author:
#
#    John Burkardt
#
  from agm_values                 import agm_values_test

  from gamma_values               import gamma_values_test
  from gamma_log_values           import gamma_log_values_test

  from i4_log_10                  import i4_log_10_test
  from i4_sign                    import i4_sign_test
  from i4_uniform_ab              import i4_uniform_ab_test

  from i4vec_indicator0           import i4vec_indicator0_test
  from i4vec_indicator1           import i4vec_indicator1_test
  from i4vec_print                import i4vec_print_test
  from i4vec_transpose_print      import i4vec_transpose_print_test

  from perm0_check                import perm0_check_test
  from perm0_uniform              import perm0_uniform_test

  from perm1_check                import perm1_check_test
  from perm1_uniform              import perm1_uniform_test

  from r8_abs                     import r8_abs_test
  from r8_acos                    import r8_acos_test
  from r8_acosh                   import r8_acosh_test
  from r8_add                     import r8_add_test
  from r8_agm                     import r8_agm_test
  from r8_asinh                   import r8_asinh_test
  from r8_atan                    import r8_atan_test
  from r8_atanh                   import r8_atanh_test
  from r8_big                     import r8_big_test
  from r8_cas                     import r8_cas_test
  from r8_ceiling                 import r8_ceiling_test
  from r8_choose                  import r8_choose_test
  from r8_cosd                    import r8_cosd_test
  from r8_cotd                    import r8_cotd_test
  from r8_cscd                    import r8_cscd_test
  from r8_cube_root               import r8_cube_root_test
  from r8_diff                    import r8_diff_test
  from r8_digit                   import r8_digit_test
  from r8_e                       import r8_e_test
  from r8_epsilon                 import r8_epsilon_test
  from r8_epsilon_compute         import r8_epsilon_compute_test
  from r8_factorial               import r8_factorial_test
  from r8_factorial_values        import r8_factorial_values_test
  from r8_factorial2              import r8_factorial2_test
  from r8_factorial2_values       import r8_factorial2_values_test
  from r8_fall                    import r8_fall_test
  from r8_fall_values             import r8_fall_values_test
  from r8_fractional              import r8_fractional_test
  from r8_gamma                   import r8_gamma_test
  from r8_gamma_log               import r8_gamma_log_test
  from r8_huge                    import r8_huge_test
  from r8_log_2                   import r8_log_2_test
  from r8_log_b                   import r8_log_b_test
  from r8_mant                    import r8_mant_test
  from r8_max                     import r8_max_test
  from r8_min                     import r8_min_test
  from r8_mod                     import r8_mod_test
  from r8_modp                    import r8_modp_test
  from r8_mop                     import r8_mop_test
  from r8_nint                    import r8_nint_test
  from r8_normal_01               import r8_normal_01_test
  from r8_normal_ab               import r8_normal_ab_test
  from r8_pi                      import r8_pi_test
  from r8_power                   import r8_power_test
  from r8_power_fast              import r8_power_fast_test
  from r8_rise                    import r8_rise_test
  from r8_rise_values             import r8_rise_values_test
  from r8_round2                  import r8_round2_test
  from r8_roundb                  import r8_roundb_test
  from r8_roundx                  import r8_roundx_test
  from r8_secd                    import r8_secd_test
  from r8_sign                    import r8_sign_test
  from r8_sind                    import r8_sind_test
  from r8_swap                    import r8_swap_test
  from r8_swap3                   import r8_swap3_test
  from r8_tand                    import r8_tand_test
  from r8_to_i4                   import r8_to_i4_test
  from r8_to_r8_discrete          import r8_to_r8_discrete_test
  from r8_uniform_01              import r8_uniform_01_test
  from r8_uniform_ab              import r8_uniform_ab_test
  from r8_walsh_1d                import r8_walsh_1d_test
  from r8_wrap                    import r8_wrap_test

  from r82col_print_part          import r82col_print_part_test

  from r82row_print_part          import r82row_print_part_test

  from r83col_print_part          import r83col_print_part_test

  from r83row_print_part          import r83row_print_part_test

  from r8col_swap                 import r8col_swap_test

  from r8mat_house_axh            import r8mat_house_axh_test
  from r8mat_house_form           import r8mat_house_form_test
  from r8mat_indicator            import r8mat_indicator_test
  from r8mat_mm                   import r8mat_mm_test
  from r8mat_mtm                  import r8mat_mtm_test
  from r8mat_mtv                  import r8mat_mtv_test
  from r8mat_mv                   import r8mat_mv_test
  from r8mat_nint                 import r8mat_nint_test
  from r8mat_nonzeros             import r8mat_nonzeros_test
  from r8mat_norm_fro             import r8mat_norm_fro_test
  from r8mat_norm_l1              import r8mat_norm_l1_test
  from r8mat_norm_li              import r8mat_norm_li_test
  from r8mat_print                import r8mat_print_test
  from r8mat_print_some           import r8mat_print_some_test
  from r8mat_sub                  import r8mat_sub_test
  from r8mat_transpose            import r8mat_transpose_test
  from r8mat_transpose_print      import r8mat_transpose_print_test
  from r8mat_transpose_print_some import r8mat_transpose_print_some_test
  from r8mat_uniform_01           import r8mat_uniform_01_test
  from r8mat_uniform_ab           import r8mat_uniform_ab_test

  from r8poly_degree              import r8poly_degree_test
  from r8poly_print               import r8poly_print_test
  from r8poly_value_horner        import r8poly_value_horner_test

  from r8vec_amax                 import r8vec_amax_test
  from r8vec_amin                 import r8vec_amin_test
  from r8vec_asum                 import r8vec_asum_test
  from r8vec_concatenate          import r8vec_concatenate_test
  from r8vec_copy                 import r8vec_copy_test
  from r8vec_direct_product       import r8vec_direct_product_test
  from r8vec_house_column         import r8vec_house_column_test
  from r8vec_indicator0           import r8vec_indicator0_test
  from r8vec_indicator1           import r8vec_indicator1_test
  from r8vec_linspace             import r8vec_linspace_test
  from r8vec_max                  import r8vec_max_test
  from r8vec_mean                 import r8vec_mean_test
  from r8vec_min                  import r8vec_min_test
  from r8vec_nint                 import r8vec_nint_test
  from r8vec_norm_l0              import r8vec_norm_l0_test
  from r8vec_norm_l2              import r8vec_norm_l2_test
  from r8vec_norm_li              import r8vec_norm_li_test
  from r8vec_permute              import r8vec_permute_test
  from r8vec_permute_uniform      import r8vec_permute_uniform_test
  from r8vec_print                import r8vec_print_test
  from r8vec_product              import r8vec_product_test
  from r8vec_sum                  import r8vec_sum_test
  from r8vec_uniform_01           import r8vec_uniform_01_test
  from r8vec_uniform_ab           import r8vec_uniform_ab_test
  from r8vec_variance             import r8vec_variance_test

  from roots_to_r8poly            import roots_to_r8poly_test

  from timestamp                  import timestamp_test

  print ''
  print 'R8LIB_TEST'
  print '  Python version:'
  print '  Test the R8LIB library.'

  agm_values_test ( )

  gamma_values_test ( )
  gamma_log_values_test ( )

  i4_log_10_test ( )
  i4_sign_test ( )
  i4_uniform_ab_test ( )

  i4vec_indicator0_test ( )
  i4vec_indicator1_test ( )
  i4vec_print_test ( )
  i4vec_transpose_print_test ( )

  perm0_check_test ( )
  perm0_uniform_test ( )

  perm1_check_test ( )
  perm1_uniform_test ( )

  r8_abs_test ( )
  r8_acos_test ( )
  r8_acosh_test ( )
  r8_add_test ( )
  r8_agm_test ( )
  r8_asinh_test ( )
  r8_atan_test ( )
  r8_atanh_test ( )
  r8_big_test ( )
  r8_cas_test ( )
  r8_ceiling_test ( )
  r8_choose_test ( )
  r8_cosd_test ( )
  r8_cotd_test ( )
  r8_cscd_test ( )
  r8_cube_root_test ( )
  r8_diff_test ( )
  r8_digit_test ( )
  r8_e_test ( )
  r8_epsilon_test ( )
  r8_epsilon_compute_test ( )
  r8_factorial_test ( )
  r8_factorial_values_test ( )
  r8_factorial2_test ( )
  r8_factorial2_values_test ( )
  r8_fall_test ( )
  r8_fall_values_test ( )
  r8_fractional_test ( )
  r8_gamma_test ( )
  r8_gamma_log_test ( )
  r8_huge_test ( )
  r8_log_2_test ( )
  r8_log_b_test ( )
  r8_mant_test ( )
  r8_max_test ( )
  r8_min_test ( )
  r8_mod_test ( )
  r8_modp_test ( )
  r8_mop_test ( )
  r8_nint_test ( )
  r8_normal_01_test ( )
  r8_normal_ab_test ( )
  r8_pi_test ( )
  r8_power_test ( )
  r8_power_fast_test ( )
  r8_rise_test ( )
  r8_rise_values_test ( )
  r8_round2_test ( )
  r8_roundb_test ( )
  r8_roundx_test ( )
  r8_secd_test ( )
  r8_sign_test ( )
  r8_sind_test ( )
  r8_swap_test ( )
  r8_swap3_test ( )
  r8_tand_test ( )
  r8_to_i4_test ( )
  r8_to_r8_discrete_test ( )
  r8_uniform_01_test ( )
  r8_uniform_ab_test ( )
  r8_walsh_1d_test ( )
  r8_wrap_test ( )

  r82col_print_part_test ( )

  r82row_print_part_test ( )

  r83col_print_part_test ( )

  r83row_print_part_test ( )

  r8col_swap_test ( )

  r8mat_house_axh_test ( )
  r8mat_house_form_test ( )
  r8mat_indicator_test ( )
  r8mat_mm_test ( )
  r8mat_mtm_test ( )
  r8mat_mtv_test ( )
  r8mat_mv_test ( )
  r8mat_nint_test ( )
  r8mat_nonzeros_test ( )
  r8mat_norm_fro_test ( )
  r8mat_norm_l1_test ( )
  r8mat_print_test ( )
  r8mat_print_some_test ( )
  r8mat_sub_test ( )
  r8mat_transpose_test ( )
  r8mat_transpose_print_test ( )
  r8mat_transpose_print_some_test ( )
  r8mat_uniform_01_test ( )
  r8mat_uniform_ab_test ( )

  r8poly_degree_test ( )
  r8poly_print_test ( )
  r8poly_value_horner_test ( )

  r8vec_amax_test ( )
  r8vec_amin_test ( )
  r8vec_asum_test ( )
  r8vec_concatenate_test ( )
  r8vec_copy_test ( )
  r8vec_direct_product_test ( )
  r8vec_house_column_test ( )
  r8vec_indicator0_test ( )
  r8vec_linspace_test ( )
  r8vec_max_test ( )
  r8vec_mean_test ( )
  r8vec_min_test ( )
  r8vec_nint_test ( )
  r8vec_norm_l0_test ( )
  r8vec_norm_l2_test ( )
  r8vec_norm_li_test ( )
  r8vec_permute_test ( )
  r8vec_permute_uniform_test ( )
  r8vec_print_test ( )
  r8vec_product_test ( )
  r8vec_sum_test ( )
  r8vec_uniform_01_test ( )
  r8vec_uniform_ab_test ( )
  r8vec_variance_test ( )

  roots_to_r8poly_test ( )

  timestamp_test ( )
#
#  Terminate.
#
  print ''
  print 'R8LIB_TEST:'
  print '  Normal end of execution.'

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8lib_test ( )
  timestamp ( )
