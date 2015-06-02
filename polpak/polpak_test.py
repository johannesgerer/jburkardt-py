#!/usr/bin/env python

def polpak_test ( ):

#*****************************************************************************80
#
## POLPAK_TEST tests the POLPAK library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    11 April 2015
#
#  Author:
#
#    John Burkardt
#
  from agm_values                       import agm_values_test
  from agud                             import agud_test
  from align_enum                       import align_enum_test
  from bell                             import bell_test
  from bell_values                      import bell_values_test
  from benford                          import benford_test
  from bernoulli_number                 import bernoulli_number_test
  from bernoulli_number2                import bernoulli_number2_test
  from bernoulli_number3                import bernoulli_number3_test
  from bernoulli_number_values          import bernoulli_number_values_test
  from bernoulli_poly                   import bernoulli_poly_test
  from bernoulli_poly2                  import bernoulli_poly2_test
  from bernstein_poly                   import bernstein_poly_test
  from bernstein_poly_01_values         import bernstein_poly_01_values_test
  from beta_values                      import beta_values_test
  from bpab                             import bpab_test
  from cardan_poly                      import cardan_poly_test
  from cardan_poly_coef                 import cardan_poly_coef_test
  from cardinal_cos                     import cardinal_cos_test
  from cardinal_sin                     import cardinal_sin_test
  from catalan                          import catalan_test
  from catalan_row_next                 import catalan_row_next_test
  from catalan_values                   import catalan_values_test
  from charlier                         import charlier_test
  from cheby_t_poly                     import cheby_t_poly_test
  from cheby_t_poly_coef                import cheby_t_poly_coef_test
  from cheby_t_poly_values              import cheby_t_poly_values_test
  from cheby_t_poly_zero                import cheby_t_poly_zero_test
  from cheby_u_poly                     import cheby_u_poly_test
  from cheby_u_poly_coef                import cheby_u_poly_coef_test
  from cheby_u_poly_values              import cheby_u_poly_values_test
  from cheby_u_poly_zero                import cheby_u_poly_zero_test
  from chebyshev_discrete               import chebyshev_discrete_test
  from collatz_count                    import collatz_count_test
  from collatz_count_max                import collatz_count_max_test
  from collatz_count_values             import collatz_count_values_test
  from comb_row_next                    import comb_row_next_test
  from commul                           import commul_test
  from complete_symmetric_poly          import complete_symmetric_poly_test
  from cos_power_int                    import cos_power_int_test
  from cos_power_int_values             import cos_power_int_values_test
  from delannoy                         import delannoy_test
  from erf_values                       import erf_values_test
  from euler_number                     import euler_number_test
  from euler_number2                    import euler_number2_test
  from euler_number_values              import euler_number_values_test
  from euler_poly                       import euler_poly_test
  from eulerian                         import eulerian_test
  from f_hofstadter                     import f_hofstadter_test
  from fibonacci_direct                 import fibonacci_direct_test
  from fibonacci_floor                  import fibonacci_floor_test
  from fibonacci_recursive              import fibonacci_recursive_test
  from g_hofstadter                     import g_hofstadter_test
  from gamma_values                     import gamma_values_test
  from gamma_log_values                 import gamma_log_values_test
  from gegenbauer_poly                  import gegenbauer_poly_test
  from gegenbauer_poly_values           import gegenbauer_poly_values_test
  from gen_hermite_poly                 import gen_hermite_poly_test
  from gen_laguerre_poly                import gen_laguerre_poly_test
  from gud                              import gud_test
  from gud_values                       import gud_values_test
  from h_hofstadter                     import h_hofstadter_test
  from hail                             import hail_test
  from hermite_poly_phys                import hermite_poly_phys_test
  from hermite_poly_phys_coef           import hermite_poly_phys_coef_test
  from hermite_poly_phys_values         import hermite_poly_phys_values_test
  from hyper_2f1_values                 import hyper_2f1_values_test
  from i4_choose                        import i4_choose_test
  from i4_factor                        import i4_factor_test
  from i4_factorial                     import i4_factorial_test
  from i4_factorial_values              import i4_factorial_values_test
  from i4_factorial2                    import i4_factorial2_test
  from i4_factorial2_values             import i4_factorial2_values_test
  from i4_is_prime                      import i4_is_prime_test
  from i4_is_triangular                 import i4_is_triangular_test
  from i4_partition_distinct_count      import i4_partition_distinct_count_test
  from i4_to_triangle                   import i4_to_triangle_test
  from i4_uniform_ab                    import i4_uniform_ab_test
  from i4mat_print                      import i4mat_print_test
  from i4mat_print_some                 import i4mat_print_some_test
  from i4vec_print                      import i4vec_print_test
  from jacobi_poly                      import jacobi_poly_test
  from jacobi_poly_values               import jacobi_poly_values_test
  from jacobi_symbol                    import jacobi_symbol_test
  from krawtchouk                       import krawtchouk_test
  from laguerre_associated              import laguerre_associated_test
  from laguerre_poly                    import laguerre_poly_test
  from laguerre_poly_coef               import laguerre_poly_coef_test
  from laguerre_polynomial_values       import laguerre_polynomial_values_test
  from legendre_associated              import legendre_associated_test
  from legendre_associated_values       import legendre_associated_values_test
  from legendre_associated_normalized   import legendre_associated_normalized_test
  from legendre_associated_normalized_sphere_values  import legendre_associated_normalized_sphere_values_test
  from legendre_function_q              import legendre_function_q_test
  from legendre_function_q_values       import legendre_function_q_values_test
  from legendre_poly                    import legendre_poly_test
  from legendre_poly_coef               import legendre_poly_coef_test
  from legendre_poly_values             import legendre_poly_values_test
  from legendre_symbol                  import legendre_symbol_test
  from lerch                            import lerch_test
  from lerch_values                     import lerch_values_test
  from lock                             import lock_test
  from meixner                          import meixner_test
  from mertens                          import mertens_test
  from mertens_values                   import mertens_values_test
  from moebius                          import moebius_test
  from moebius_values                   import moebius_values_test
  from motzkin                          import motzkin_test
  from normal_01_cdf_inverse            import normal_01_cdf_inverse_test
  from normal_01_cdf_values             import normal_01_cdf_values_test
  from omega                            import omega_test
  from omega_values                     import omega_values_test
  from partition_distinct_count_values  import partition_distinct_count_values_test
  from pentagon_num                     import pentagon_num_test
  from phi                              import phi_test
  from phi_values                       import phi_values_test
  from plane_partition_num              import plane_partition_num_test
  from poly_bernoulli                   import poly_bernoulli_test
  from poly_coef_count                  import poly_coef_count_test
  from prime                            import prime_test
  from psi_values                       import psi_values_test
  from pyramid_num                      import pyramid_num_test
  from pyramid_square_num               import pyramid_square_num_test
  from r8_agm                           import r8_agm_test
  from r8_beta                          import r8_beta_test
  from r8_choose                        import r8_choose_test
  from r8_erf                           import r8_erf_test
  from r8_erf_inverse                   import r8_erf_inverse_test
  from r8_euler_constant                import r8_euler_constant_test
  from r8_factorial                     import r8_factorial_test
  from r8_factorial_values              import r8_factorial_values_test
  from r8_factorial_log                 import r8_factorial_log_test
  from r8_factorial_log_values          import r8_factorial_log_values_test
  from r8_gamma                         import r8_gamma_test
  from r8_gamma_log                     import r8_gamma_log_test
  from r8_huge                          import r8_huge_test
  from r8_hyper_2f1                     import r8_hyper_2f1_test
  from r8_mop                           import r8_mop_test
  from r8_nint                          import r8_nint_test
  from r8_pi                            import r8_pi_test
  from r8_psi                           import r8_psi_test
  from r8_uniform_01                    import r8_uniform_01_test
  from r8_uniform_ab                    import r8_uniform_ab_test
  from r8poly_print                     import r8poly_print_test
  from r8poly_degree                    import r8poly_degree_test
  from r8poly_value_horner              import r8poly_value_horner_test
  from r8vec_print                      import r8vec_print_test
  from sigma                            import sigma_test
  from sigma_values                     import sigma_values_test
  from simplex_num                      import simplex_num_test
  from sin_power_int                    import sin_power_int_test
  from sin_power_int_values             import sin_power_int_values_test
  from slice                            import slice_test
  from spherical_harmonic               import spherical_harmonic_test
  from spherical_harmonic_values        import spherical_harmonic_values_test
  from stirling1                        import stirling1_test
  from stirling2                        import stirling2_test
  from tau                              import tau_test
  from tetrahedron_num                  import tetrahedron_num_test
  from timestamp                        import timestamp_test
  from triangle_num                     import triangle_num_test
  from triangle_to_i4                   import triangle_to_i4_test
  from trinomial                        import trinomial_test
  from v_hofstadter                     import v_hofstadter_test
  from vibonacci                        import vibonacci_test
  from zeckendorf                       import zeckendorf_test
  from zernike_poly                     import zernike_poly_test
  from zernike_poly_coef                import zernike_poly_coef_test
  from zeta                             import zeta_test

  print ''
  print 'POLPAK_TEST'
  print '  Python version:'
  print '  Test the POLPAK library.'
#
#  Utilities.
#
  agm_values_test ( )
  bell_values_test ( )
  bernoulli_number_values_test ( )
  bernstein_poly_01_values_test ( )
  catalan_values_test ( )
  cheby_t_poly_values_test ( )
  cheby_u_poly_values_test ( )
  collatz_count_values_test ( )
  cos_power_int_values_test ( )
  erf_values_test ( )
  euler_number_values_test ( )
  gamma_values_test ( )
  gamma_log_values_test ( )
  gegenbauer_poly_values_test ( )
  gud_values_test ( )
  hermite_poly_phys_values_test ( )
  hyper_2f1_values_test ( )
  i4_factorial_values_test ( )
  i4_factorial2_values_test ( )
  i4_uniform_ab_test ( )
  i4mat_print_test ( )
  i4mat_print_some_test ( )
  i4vec_print_test ( )
  jacobi_poly_values_test ( )
  laguerre_polynomial_values_test ( )
  legendre_associated_values_test ( )
  legendre_associated_normalized_sphere_values_test ( )
  legendre_function_q_values_test ( )
  legendre_poly_values_test ( )
  lerch_values_test ( )
  mertens_values_test ( )
  moebius_values_test ( )
  normal_01_cdf_inverse_test ( )
  normal_01_cdf_values_test ( )
  omega_values_test ( )
  partition_distinct_count_values_test ( )
  phi_values_test ( )
  psi_values_test ( )
  r8_factorial_values_test ( )
  r8_factorial_log_values_test ( )
  r8_huge_test ( )
  r8_mop_test ( )
  r8_nint_test ( )
  r8_pi_test ( )
  r8_uniform_01_test ( )
  r8_uniform_ab_test ( )
  r8poly_degree_test ( )
  r8poly_print_test ( )
  r8poly_value_horner_test ( )
  r8vec_print_test ( )
  sigma_values_test ( )
  sin_power_int_values_test ( )
  spherical_harmonic_values_test ( )
  timestamp_test ( )
#
#  Interesting stuff.
#
  agud_test ( )
  align_enum_test ( )
  bell_test ( )
  benford_test ( )
  bernoulli_number_test ( )
  bernoulli_number2_test ( )
  bernoulli_number3_test ( )
  bernoulli_poly_test ( )
  bernoulli_poly2_test ( )
  bernstein_poly_test ( )
  bpab_test ( )
  cardan_poly_test ( )
  cardan_poly_coef_test ( )
  cardinal_cos_test ( )
  cardinal_sin_test ( )
  catalan_test ( )
  catalan_row_next_test ( )
  charlier_test ( )
  cheby_t_poly_test ( )
  cheby_t_poly_coef_test ( )
  cheby_t_poly_zero_test ( )
  cheby_u_poly_test ( )
  cheby_u_poly_coef_test ( )
  chebyshev_discrete_test ( )
  collatz_count_test ( )
  comb_row_next_test ( )
  commul_test ( )
  complete_symmetric_poly_test ( )
  cos_power_int_test ( )
  delannoy_test ( )
  euler_number_test ( )
  euler_number2_test ( )
  euler_poly_test ( )
  eulerian_test ( )
  f_hofstadter_test ( )
  fibonacci_direct_test ( )
  fibonacci_floor_test ( )
  fibonacci_recursive_test ( )
  g_hofstadter_test ( )
  gegenbauer_poly_test ( )
  gen_hermite_poly_test ( )
  gen_laguerre_poly_test ( )
  gud_test ( )
  h_hofstadter_test ( )
  hail_test ( )
  hermite_poly_phys_test ( )
  hermite_poly_phys_coef_test ( )
  i4_choose_test ( )
  i4_factor_test ( )
  i4_factorial_test ( )
  i4_factorial2_test ( )
  i4_is_prime_test ( )
  i4_is_triangular_test ( )
  i4_partition_distinct_count_test ( )
  i4_to_triangle_test ( )
  jacobi_poly_test ( )
  jacobi_symbol_test ( )
  krawtchouk_test ( )
  laguerre_associated_test ( )
  laguerre_poly_test ( )
  laguerre_poly_coef_test ( )
  legendre_associated_test ( )
  legendre_associated_normalized_test ( )
  legendre_function_q_test ( )
  legendre_poly_test ( )
  legendre_poly_coef_test ( )
  legendre_symbol_test ( )
  lerch_test ( )
  lock_test ( )
  meixner_test ( )
  mertens_test ( )
  moebius_test ( )
  motzkin_test ( )
  omega_test ( )
  pentagon_num_test ( )
  phi_test ( )
  plane_partition_num_test ( )
  poly_bernoulli_test ( )
  poly_coef_count_test ( )
  prime_test ( )
  pyramid_num_test ( )
  pyramid_square_num_test ( )
  r8_agm_test ( )
  r8_beta_test ( )
  r8_choose_test ( )
  r8_erf_test ( )
  r8_erf_inverse_test ( )
  r8_euler_constant_test ( )
  r8_factorial_test ( )
  r8_factorial_log_test ( )
  r8_gamma_test ( )
  r8_gamma_log_test ( )
  r8_hyper_2f1_test ( )
  r8_psi_test ( )
  sigma_test ( )
  simplex_num_test ( )
  sin_power_int_test ( )
  slice_test ( )
  spherical_harmonic_test ( )
  stirling1_test ( )
  stirling2_test ( )
  tau_test ( )
  tetrahedron_num_test ( )
  triangle_num_test ( )
  triangle_to_i4_test ( )
  trinomial_test ( )
  v_hofstadter_test ( )
  vibonacci_test ( )
  zeckendorf_test ( )
  zernike_poly_test ( )
  zernike_poly_coef_test ( )
  zeta_test ( )
#
#  Terminate.
#
  print ''
  print 'POLPAK_TEST:'
  print '  Normal end of execution.'

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  polpak_test ( )
  timestamp ( )
