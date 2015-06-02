#! /usr/bin/env python
#
def triangle01_integrals_test ( ):

#*****************************************************************************80
#
## TRIANGLE01_INTEGRALS_TEST tests the TRIANGLE01_INTEGRALS library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 April 2015
#
#  Author:
#
#    John Burkardt
#
  from i4vec_print                   import i4vec_print_test
  from i4vec_uniform_ab              import i4vec_uniform_ab_test
  from monomial_value                import monomial_value_test
  from r8mat_print                   import r8mat_print_test
  from r8mat_print_some              import r8mat_print_some_test
  from r8mat_transpose_print         import r8mat_transpose_print_test
  from r8mat_transpose_print_some    import r8mat_transpose_print_some_test
  from r8mat_uniform_01              import r8mat_uniform_01_test
  from r8vec_print                   import r8vec_print_test
  from r8vec_uniform_01              import r8vec_uniform_01_test
  from timestamp                     import timestamp_test
  from triangle01_monomial_integral  import triangle01_monomial_integral_test01
  from triangle01_monomial_integral  import triangle01_monomial_integral_test02
  from triangle01_sample             import triangle01_sample_test

  print ''
  print 'TRIANGLE01_INTEGRALS_TEST'
  print '  Python version:'
  print '  Test the TRIANGLE01_INTEGRALS library.'
#
#  Utilities:
#
  i4vec_print_test ( )
  i4vec_uniform_ab_test ( )
  r8mat_print_test ( )
  r8mat_print_some_test ( )
  r8mat_transpose_print_test ( )
  r8mat_transpose_print_some_test ( )
  r8mat_uniform_01_test ( )
  r8vec_print_test ( )
  r8vec_uniform_01_test ( )
  timestamp_test ( )
#
#  Library functions:
#
  monomial_value_test ( )
  triangle01_sample_test ( )
  triangle01_monomial_integral_test01 ( )
  triangle01_monomial_integral_test02 ( )
#
#  Terminate.
#
  print ''
  print 'TRIANGLE01_INTEGRALS_TEST:'
  print '  Normal end of execution.'

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  triangle01_integrals_test ( )
  timestamp ( )
