#! /usr/bin/env python
#
def triangle_integrals_test ( ):

#*****************************************************************************80
#
## TRIANGLE_INTEGRALS_TEST tests the TRIANGLE_INTEGRALS library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 April 2015
#
#  Author:
#
#    John Burkardt
#
  from i4_to_pascal                  import i4_to_pascal_test
  from i4_to_pascal_degree           import i4_to_pascal_degree_test
  from pascal_to_i4                  import pascal_to_i4_test
  from poly_power                    import poly_power_test
  from poly_power_linear             import poly_power_linear_test
  from poly_print                    import poly_print_test
  from poly_product                  import poly_product_test
  from r8mat_print                   import r8mat_print_test
  from r8mat_print_some              import r8mat_print_some_test
  from rs_to_xy_map                  import rs_to_xy_map_test
  from timestamp                     import timestamp_test
  from triangle_area                 import triangle_area_test
  from triangle_monomial_integral    import triangle_monomial_integral_test
  from triangle_poly_integral        import triangle_poly_integral_test
  from triangle_xy_integral          import triangle_xy_integral_test
  from triangle01_monomial_integral  import triangle01_monomial_integral_test
  from triangle01_poly_integral      import triangle01_poly_integral_test
  from trinomial                     import trinomial_test
  from xy_to_rs_map                  import xy_to_rs_map_test

  print ''
  print 'TRIANGLE_INTEGRALS_TEST'
  print '  Python version:'
  print '  Test the TRIANGLE_INTEGRALS library.'
#
#  Utilities:
#
  i4_to_pascal_test ( )
  i4_to_pascal_degree_test ( )
  pascal_to_i4_test ( )
  r8mat_print_test ( )
  r8mat_print_some_test ( )
  timestamp_test ( )
  trinomial_test ( )

  rs_to_xy_map_test ( )
  xy_to_rs_map_test ( )

  poly_print_test ( )
  poly_power_linear_test ( )
  poly_power_test ( )
  poly_product_test ( )
#
#  Library functions:
#
  triangle01_monomial_integral_test ( )
  triangle01_poly_integral_test ( )

  triangle_area_test ( )
  triangle_xy_integral_test ( )
  triangle_monomial_integral_test ( )
  triangle_poly_integral_test ( )
#
#  Terminate.
#
  print ''
  print 'TRIANGLE_INTEGRALS_TEST:'
  print '  Normal end of execution.'

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  triangle_integrals_test ( )
  timestamp ( )
