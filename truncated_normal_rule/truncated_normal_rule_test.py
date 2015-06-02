#!/usr/bin/env python

def truncated_normal_rule_test ( ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_RULE_TEST tests the functions in TRUNCATED_NORMAL_RULE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 March 2015
#
#  Author:
#
#    John Burkardt
#
  from i4_uniform_ab              import i4_uniform_ab_test
  from moment_method              import moment_method_test
  from normal_01_cdf              import normal_01_cdf_test
  from normal_01_moment           import normal_01_moment_test
  from normal_01_pdf              import normal_01_pdf_test
  from normal_ms_moment           import normal_ms_moment_test
  from r8_choose                  import r8_choose_test
  from r8_factorial               import r8_factorial_test
  from r8_factorial2              import r8_factorial2_test
  from r8_huge                    import r8_huge_test
  from r8_mop                     import r8_mop_test
  from r8mat_print                import r8mat_print_test
  from r8mat_print_some           import r8mat_print_some_test
  from r8vec_print                import r8vec_print_test
  from r8vec_write                import r8vec_write_test
  from rule_write                 import rule_write_test
  from timestamp                  import timestamp_test
  from truncated_normal_a_moment  import truncated_normal_a_moment_test
  from truncated_normal_ab_moment import truncated_normal_ab_moment_test
  from truncated_normal_b_moment  import truncated_normal_b_moment_test
  from truncated_normal_rule      import option0_test
  from truncated_normal_rule      import option1_test
  from truncated_normal_rule      import option2_test
  from truncated_normal_rule      import option3_test

  print ''
  print 'TRUNCATED_NORMAL_RULE_TEST:'
  print '  Test the functions used by TRUNCATED_NORMAL_RULE.'
#
#  Utilities.
#
  i4_uniform_ab_test ( )
  r8_choose_test ( )
  r8_factorial_test ( )
  r8_factorial2_test ( )
  r8_huge_test ( )
  r8_mop_test ( )
  r8mat_print_test ( )
  r8mat_print_some_test ( )
  r8vec_print_test ( )
  r8vec_write_test ( )
  rule_write_test ( )
  timestamp_test ( )
#
#  Library functions.
#
  normal_01_cdf_test ( )
  normal_01_moment_test ( )
  normal_01_pdf_test ( )
  normal_ms_moment_test ( )
  truncated_normal_a_moment_test ( )
  truncated_normal_ab_moment_test ( )
  truncated_normal_b_moment_test ( )
  moment_method_test ( )
#
#  Direct calls to truncated_normal_rule:
#
  option0_test ( )
  option1_test ( )
  option2_test ( )
  option3_test ( )
#
#  Terminate.
#
  print ''
  print 'TRUNCATED_NORMAL_RULE_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp

  timestamp ( )
  truncated_normal_rule_test ( )
  timestamp ( )


