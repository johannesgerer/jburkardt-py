#!/usr/bin/env python

def test_mat_test ( ):

#*****************************************************************************80
#
## TEST_MAT_TEST tests the TEST_MAT library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    24 March 2015
#
#  Author:
#
#    John Burkardt
#
  from bvec_next_grlex           import bvec_next_grlex_test
  from c8_i                      import c8_i_test
  from c8_normal_01              import c8_normal_01_test
  from c8_uniform_01             import c8_uniform_01_test
  from c8mat_identity            import c8mat_identity_test
  from c8mat_indicator           import c8mat_indicator_test
  from c8mat_uniform_01          import c8mat_uniform_01_test
  from c8vec_print               import c8vec_print_test
  from c8vec_uniform_01          import c8vec_uniform_01_test
  from c8vec_unity               import c8vec_unity_test
  from complete_symmetric_poly   import complete_symmetric_poly_test
  from i4_factor                 import i4_factor_test
  from i4_is_even                import i4_is_even_test
  from i4_is_odd                 import i4_is_odd_test
  from i4_is_prime               import i4_is_prime_test
  from i4_log_10                 import i4_log_10_test
  from i4_modp                   import i4_modp_test
  from i4_rise                   import i4_rise_test
  from i4_rise_values            import i4_rise_values_test
  from i4_sign                   import i4_sign_test
  from i4_uniform_ab             import i4_uniform_ab_test
  from i4_wrap                   import i4_wrap_test
  from i4mat_print               import i4mat_print_test
  from i4mat_print_some          import i4mat_print_some_test
  from i4vec_indicator0          import i4vec_indicator0_test
  from i4vec_print               import i4vec_print_test
  from legendre_symbol           import legendre_symbol_test
  from mertens                   import mertens_test
  from mertens_values            import mertens_values_test
  from moebius                   import moebius_test
  from moebius_values            import moebius_values_test
  from prime                     import prime_test
  from r8_choose                 import r8_choose_test
  from r8_factorial              import r8_factorial_test
  from r8_mop                    import r8_mop_test
  from r8_normal_01              import r8_normal_01_test
  from r8_rise                   import r8_rise_test
  from r8_sign                   import r8_sign_test
  from r8_uniform_01             import r8_uniform_01_test
  from r8_uniform_ab             import r8_uniform_ab_test
  from r8col_swap                import r8col_swap_test
  from r8mat_house_axh           import r8mat_house_axh_test
  from r8mat_house_form          import r8mat_house_form_test
  from r8mat_indicator           import r8mat_indicator_test
  from r8mat_is_eigen_left       import r8mat_is_eigen_left_test
  from r8mat_is_eigen_right      import r8mat_is_eigen_right_test
  from r8mat_is_inverse          import r8mat_is_inverse_test
  from r8mat_is_llt              import r8mat_is_llt_test
  from r8mat_is_null_left        import r8mat_is_null_left_test
  from r8mat_is_null_right       import r8mat_is_null_right_test
  from r8mat_is_plu              import r8mat_is_plu_test
  from r8mat_is_solution         import r8mat_is_solution_test
  from r8mat_mm                  import r8mat_mm_test
  from r8mat_mtm                 import r8mat_mtm_test
  from r8mat_mtv                 import r8mat_mtv_test
  from r8mat_mv                  import r8mat_mv_test
  from r8mat_norm_fro            import r8mat_norm_fro_test
  from r8mat_norm_l1             import r8mat_norm_l1_test
  from r8mat_print               import r8mat_print_test
  from r8mat_print_some          import r8mat_print_some_test
  from r8mat_sub                 import r8mat_sub_test
  from r8mat_transpose           import r8mat_transpose_test
  from r8mat_uniform_01          import r8mat_uniform_01_test
  from r8mat_uniform_ab          import r8mat_uniform_ab_test
  from r8poly_print              import r8poly_print_test
  from r8vec_house_column        import r8vec_house_column_test
  from r8vec_nint                import r8vec_nint_test
  from r8vec_norm_l2             import r8vec_norm_l2_test
  from r8vec_print               import r8vec_print_test
  from r8vec_uniform_01          import r8vec_uniform_01_test
  from r8vec_uniform_ab          import r8vec_uniform_ab_test
  from test_condition            import test_condition
  from test_determinant          import test_determinant
  from test_eigen_left           import test_eigen_left
  from test_eigen_right          import test_eigen_right
  from test_inverse              import test_inverse
  from test_llt                  import test_llt
  from test_null_left            import test_null_left
  from test_null_right           import test_null_right
  from test_plu                  import test_plu
  from test_solution             import test_solution
  from timestamp                 import timestamp_test

  print ''
  print 'TEST_MAT_TEST'
  print '  Python version:'
  print '  Test the TEST_MAT library.'
#
#  Utilities.
#
  bvec_next_grlex_test ( )

  c8_i_test ( )
  c8_normal_01_test ( )
  c8_uniform_01_test ( )

  c8mat_identity_test ( )
  c8mat_indicator_test ( )
  c8mat_uniform_01_test ( )

  c8vec_print_test ( )
  c8vec_uniform_01_test ( )
  c8vec_unity_test ( )

  complete_symmetric_poly_test ( )

  i4_factor_test ( )
  i4_is_even_test ( )
  i4_is_odd_test ( )
  i4_is_prime_test ( )
  i4_log_10_test ( )
  i4_modp_test ( )
  i4_rise_test ( )
  i4_rise_values_test ( )
  i4_sign_test ( )
  i4_uniform_ab_test ( )
  i4_wrap_test ( )

  i4mat_print_test ( )
  i4mat_print_some_test ( )

  i4vec_indicator0_test ( )
  i4vec_print_test ( )

  legendre_symbol_test ( )

  mertens_test ( )
  mertens_values_test ( )

  moebius_test ( )
  moebius_values_test ( )

  prime_test ( )

  r8_choose_test ( )
  r8_factorial_test ( )
  r8_mop_test ( )
  r8_normal_01_test ( )
  r8_rise_test ( )
  r8_sign_test ( )
  r8_uniform_01_test ( )
  r8_uniform_ab_test ( )

  r8col_swap_test ( )

  r8mat_house_axh_test ( )
  r8mat_house_form_test ( )
  r8mat_indicator_test ( )
  r8mat_is_eigen_left_test ( )
  r8mat_is_eigen_right_test ( )
  r8mat_is_inverse_test ( )
  r8mat_is_llt_test ( )
  r8mat_is_null_left_test ( )
  r8mat_is_null_right_test ( )
  r8mat_is_plu_test ( )
  r8mat_is_solution_test ( )
  r8mat_mm_test ( )
  r8mat_mtm_test ( )
  r8mat_mtv_test ( )
  r8mat_mv_test ( )
  r8mat_print_test ( )
  r8mat_print_some_test ( )
  r8mat_sub_test ( )
  r8mat_transpose_test ( )
  r8mat_uniform_01_test ( )
  r8mat_uniform_ab_test ( )

  r8poly_print_test ( )

  r8vec_house_column_test ( )
  r8vec_nint_test ( )
  r8vec_norm_l2_test ( )
  r8vec_print_test ( )
  r8vec_uniform_01_test ( )
  r8vec_uniform_ab_test ( )

  timestamp_test ( )
#
#  Interesting stuff.
#
  test_condition ( )
  test_determinant ( )
  test_eigen_left ( )
  test_eigen_right ( )
  test_inverse ( )
  test_llt ( )
  test_null_left ( )
  test_null_right ( )
  test_plu ( )
  test_solution ( )
#
#  Terminate.
#
  print ''
  print 'TEST_MAT_TEST:'
  print '  Normal end of execution.'
  print ''

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  test_mat_test ( )
  timestamp ( )
