#!/usr/bin/env python

def truncated_normal_test ( ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_TEST tests the TRUNCATED_NORMAL library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    09 March 2015
#
#  Author:
#
#    John Burkardt
# 
  from i4_uniform_ab                  import i4_uniform_ab_test

  from normal_01_cdf                  import normal_01_cdf_test
  from normal_01_cdf_inv              import normal_01_cdf_inv_test
  from normal_01_cdf_values           import normal_01_cdf_values_test
  from normal_01_mean                 import normal_01_mean_test
  from normal_01_moment               import normal_01_moment_test
  from normal_01_pdf                  import normal_01_pdf_test
  from normal_01_sample               import normal_01_sample_test
  from normal_01_variance             import normal_01_variance_test

  from normal_ms_cdf                  import normal_ms_cdf_test
  from normal_ms_cdf_inv              import normal_ms_cdf_inv_test
  from normal_ms_mean                 import normal_ms_mean_test
  from normal_ms_moment               import normal_ms_moment_test
  from normal_ms_moment_central       import normal_ms_moment_central_test
  from normal_ms_pdf                  import normal_ms_pdf_test
  from normal_ms_sample               import normal_ms_sample_test
  from normal_ms_variance             import normal_ms_variance_test

  from r8_choose                      import r8_choose_test
  from r8_factorial2                  import r8_factorial2_test
  from r8_factorial2_values           import r8_factorial2_values_test
  from r8_mop                         import r8_mop_test
  from r8_uniform_01                  import r8_uniform_01_test

  from r8poly_print                   import r8poly_print_test
  from r8poly_value_horner            import r8poly_value_horner_test

  from r8vec_linspace                 import r8vec_linspace_test
  from r8vec_max                      import r8vec_max_test
  from r8vec_mean                     import r8vec_mean_test
  from r8vec_min                      import r8vec_min_test
  from r8vec_print                    import r8vec_print_test
  from r8vec_uniform_ab               import r8vec_uniform_ab_test
  from r8vec_variance                 import r8vec_variance_test

  from timestamp                      import timestamp_test

  from truncated_normal_a_cdf         import truncated_normal_a_cdf_test
  from truncated_normal_a_cdf_inv     import truncated_normal_a_cdf_inv_test
  from truncated_normal_a_cdf_values  import truncated_normal_a_cdf_values_test
  from truncated_normal_a_mean        import truncated_normal_a_mean_test
  from truncated_normal_a_moment      import truncated_normal_a_moment_test
  from truncated_normal_a_pdf         import truncated_normal_a_pdf_test
  from truncated_normal_a_pdf_values  import truncated_normal_a_pdf_values_test
  from truncated_normal_a_sample      import truncated_normal_a_sample_test
  from truncated_normal_a_variance    import truncated_normal_a_variance_test

  from truncated_normal_ab_cdf        import truncated_normal_ab_cdf_test
  from truncated_normal_ab_cdf_inv    import truncated_normal_ab_cdf_inv_test
  from truncated_normal_ab_cdf_values import truncated_normal_ab_cdf_values_test
  from truncated_normal_ab_mean       import truncated_normal_ab_mean_test
  from truncated_normal_ab_moment     import truncated_normal_ab_moment_test
  from truncated_normal_ab_pdf        import truncated_normal_ab_pdf_test
  from truncated_normal_ab_pdf_values import truncated_normal_ab_pdf_values_test
  from truncated_normal_ab_sample     import truncated_normal_ab_sample_test
  from truncated_normal_ab_variance   import truncated_normal_ab_variance_test

  from truncated_normal_b_cdf         import truncated_normal_b_cdf_test
  from truncated_normal_b_cdf_inv     import truncated_normal_b_cdf_inv_test
  from truncated_normal_b_cdf_values  import truncated_normal_b_cdf_values_test
  from truncated_normal_b_mean        import truncated_normal_b_mean_test
  from truncated_normal_b_moment      import truncated_normal_b_moment_test
  from truncated_normal_b_pdf         import truncated_normal_b_pdf_test
  from truncated_normal_b_pdf_values  import truncated_normal_b_pdf_values_test
  from truncated_normal_b_sample      import truncated_normal_b_sample_test
  from truncated_normal_b_variance    import truncated_normal_b_variance_test

  print ''
  print 'TRUNCATED_NORMAL_TEST'
  print '  Python version:'
  print '  Test the TRUNCATED_NORMAL library.'
#
#  Utilities:
#
  i4_uniform_ab_test ( )

  normal_01_cdf_values_test ( )

  r8_choose_test ( )
  r8_factorial2_test ( )
  r8_factorial2_values_test ( )
  r8_mop_test ( )
  r8_uniform_01_test ( )

  r8poly_print_test ( )
  r8poly_value_horner_test ( )

  r8vec_linspace_test ( )
  r8vec_max_test ( )
  r8vec_mean_test ( )
  r8vec_min_test ( )
  r8vec_print_test ( )
  r8vec_uniform_ab_test ( )
  r8vec_variance_test ( )

  truncated_normal_a_cdf_values_test ( )
  truncated_normal_a_pdf_values_test ( )

  truncated_normal_ab_cdf_values_test ( )
  truncated_normal_ab_pdf_values_test ( )

  truncated_normal_b_cdf_values_test ( )
  truncated_normal_b_pdf_values_test ( )

  timestamp_test ( )
#
#  Library:
#
  normal_01_cdf_test ( )
  normal_01_cdf_inv_test ( )
  normal_01_mean_test ( )
  normal_01_moment_test ( )
  normal_01_pdf_test ( )
  normal_01_sample_test ( )
  normal_01_variance_test ( )

  normal_ms_cdf_test ( )
  normal_ms_cdf_inv_test ( )
  normal_ms_mean_test ( )
  normal_ms_moment_test ( )
  normal_ms_moment_central_test ( )
  normal_ms_pdf_test ( )
  normal_ms_sample_test ( )
  normal_ms_variance_test ( )

  truncated_normal_a_cdf_test ( )
  truncated_normal_a_cdf_inv_test ( )
  truncated_normal_a_mean_test ( )
  truncated_normal_a_moment_test ( )
  truncated_normal_a_pdf_test ( )
  truncated_normal_a_sample_test ( )
  truncated_normal_a_variance_test ( )

  truncated_normal_ab_cdf_test ( )
  truncated_normal_ab_cdf_inv_test ( )
  truncated_normal_ab_mean_test ( )
  truncated_normal_ab_moment_test ( )
  truncated_normal_ab_pdf_test ( )
  truncated_normal_ab_sample_test ( )
  truncated_normal_ab_variance_test ( )

  truncated_normal_b_cdf_test ( )
  truncated_normal_b_cdf_inv_test ( )
  truncated_normal_b_mean_test ( )
  truncated_normal_b_moment_test ( )
  truncated_normal_b_pdf_test ( )
  truncated_normal_b_sample_test ( )
  truncated_normal_b_variance_test ( )
#
#  Terminate.
#
  print ''
  print 'TRUNCATED_NORMAL_TEST:'
  print '  Normal end of execution.'

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  truncated_normal_test ( )
  timestamp ( )
