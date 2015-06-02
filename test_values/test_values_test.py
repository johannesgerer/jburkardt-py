#!/usr/bin/env python

def test_values_test ( ):

#*****************************************************************************80
#
## TEST_VALUES_TEST tests the TEST_VALUES library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
  from abram0_values                          import abram0_values_test
  from abram1_values                          import abram1_values_test
  from abram2_values                          import abram2_values_test
  from agm_values                             import agm_values_test
  from airy_ai_values                         import airy_ai_values_test
  from airy_ai_int_values                     import airy_ai_int_values_test
  from airy_ai_prime_values                   import airy_ai_prime_values_test
  from airy_bi_values                         import airy_bi_values_test
  from airy_bi_int_values                     import airy_bi_int_values_test
  from airy_bi_prime_values                   import airy_bi_prime_values_test
  from airy_cai_values                        import airy_cai_values_test
  from airy_cbi_values                        import airy_cbi_values_test
  from airy_gi_values                         import airy_gi_values_test
  from arccos_values                          import arccos_values_test
  from arccosh_values                         import arccosh_values_test
  from arcsin_values                          import arcsin_values_test
  from arcsinh_values                         import arcsinh_values_test
  from arctan_values                          import arctan_values_test
  from arctan_int_values                      import arctan_int_values_test
  from arctan2_values                         import arctan2_values_test
  from arctanh_values                         import arctanh_values_test
  from bei0_values                            import bei0_values_test
  from bei1_values                            import bei1_values_test
  from bell_values                            import bell_values_test
  from ber0_values                            import ber0_values_test
  from ber1_values                            import ber1_values_test
  from bernoulli_number_values                import bernoulli_number_values_test
  from bernoulli_poly_values                  import bernoulli_poly_values_test
  from bernstein_poly_01_values               import bernstein_poly_01_values_test
  from bessel_i0_values                       import bessel_i0_values_test
  from bessel_i0_int_values                   import bessel_i0_int_values_test
  from bessel_i0_spherical_values             import bessel_i0_spherical_values_test
  from bessel_i1_values                       import bessel_i1_values_test
  from bessel_i1_spherical_values             import bessel_i1_spherical_values_test
  from bessel_in_values                       import bessel_in_values_test
  from bessel_ix_values                       import bessel_ix_values_test
  from bessel_j0_values                       import bessel_j0_values_test
  from bessel_j0_int_values                   import bessel_j0_int_values_test
  from bessel_j0_spherical_values             import bessel_j0_spherical_values_test
  from bessel_j1_values                       import bessel_j1_values_test
  from bessel_j1_spherical_values             import bessel_j1_spherical_values_test
  from bessel_jn_values                       import bessel_jn_values_test
  from bessel_jx_values                       import bessel_jx_values_test
  from bessel_k0_values                       import bessel_k0_values_test
  from bessel_k0_int_values                   import bessel_k0_int_values_test
  from bessel_k1_values                       import bessel_k1_values_test
  from bessel_kn_values                       import bessel_kn_values_test
  from bessel_kx_values                       import bessel_kx_values_test
  from bessel_y0_values                       import bessel_y0_values_test
  from bessel_y0_int_values                   import bessel_y0_int_values_test
  from bessel_y0_spherical_values             import bessel_y0_spherical_values_test
  from bessel_y1_values                       import bessel_y1_values_test
  from bessel_y1_spherical_values             import bessel_y1_spherical_values_test
  from bessel_yn_values                       import bessel_yn_values_test
  from bessel_yx_values                       import bessel_yx_values_test
  from beta_values                            import beta_values_test
  from beta_cdf_values                        import beta_cdf_values_test
  from beta_inc_values                        import beta_inc_values_test
  from beta_log_values                        import beta_log_values_test
  from beta_noncentral_cdf_values             import beta_noncentral_cdf_values_test
  from binomial_cdf_values                    import binomial_cdf_values_test
  from binomial_values                        import binomial_values_test
  from bivariate_normal_cdf_values            import bivariate_normal_cdf_values_test
  from catalan_values                         import catalan_values_test
  from cauchy_cdf_values                      import cauchy_cdf_values_test
  from cbrt_values                            import cbrt_values_test
  from cheby_t_poly_values                    import cheby_t_poly_values_test
  from cheby_u_poly_values                    import cheby_u_poly_values_test
  from cheby_v_poly_values                    import cheby_v_poly_values_test
  from cheby_w_poly_values                    import cheby_w_poly_values_test
  from chi_values                             import chi_values_test
  from chi_square_cdf_values                  import chi_square_cdf_values_test
  from chi_square_noncentral_cdf_values       import chi_square_noncentral_cdf_values_test
  from ci_values                              import ci_values_test
  from cin_values                             import cin_values_test
  from cinh_values                            import cinh_values_test
  from clausen_values                         import clausen_values_test
  from clebsch_gordan_values                  import clebsch_gordan_values_test
  from collatz_count_values                   import collatz_count_values_test
  from cos_values                             import cos_values_test
  from cos_degree_values                      import cos_degree_values_test
  from cos_power_int_values                   import cos_power_int_values_test
  from cosh_values                            import cosh_values_test
  from cot_values                             import cot_values_test
  from cp_values                              import cp_values_test
  from dawson_values                          import dawson_values_test
  from debye1_values                          import debye1_values_test
  from debye2_values                          import debye2_values_test
  from debye3_values                          import debye3_values_test
  from debye4_values                          import debye4_values_test
  from dedekind_sum_values                    import dedekind_sum_values_test
  from dielectric_values                      import dielectric_values_test
  from dilogarithm_values                     import dilogarithm_values_test
  from e1_values                              import e1_values_test
  from ei_values                              import ei_values_test
  from elliptic_ea_values                     import elliptic_ea_values_test
  from elliptic_em_values                     import elliptic_em_values_test
  from elliptic_ka_values                     import elliptic_ka_values_test
  from elliptic_km_values                     import elliptic_km_values_test
  from erf_values                             import erf_values_test
  from erfc_values                            import erfc_values_test
  from euler_number_values                    import euler_number_values_test
  from euler_poly_values                      import euler_poly_values_test
  from exp_values                             import exp_values_test
  from exp3_int_values                        import exp3_int_values_test
  from exponential_cdf_values                 import exponential_cdf_values_test
  from extreme_values_cdf_values              import extreme_values_cdf_values_test
  from f_cdf_values                           import f_cdf_values_test
  from f_noncentral_cdf_values                import f_noncentral_cdf_values_test
  from fresnel_cos_values                     import fresnel_cos_values_test
  from fresnel_sin_values                     import fresnel_sin_values_test
  from frobenius_number_data_values           import frobenius_number_data_values_test
  from frobenius_number_order_values          import frobenius_number_order_values_test
  from frobenius_number_order2_values         import frobenius_number_order2_values_test
  from gamma_values                           import gamma_values_test
  from gamma_inc_values                       import gamma_inc_values_test
  from gamma_inc_p_values                     import gamma_inc_p_values_test
  from gamma_inc_q_values                     import gamma_inc_q_values_test
  from gamma_inc_tricomi_values               import gamma_inc_tricomi_values_test
  from gamma_log_values                       import gamma_log_values_test
  from gegenbauer_poly_values                 import gegenbauer_poly_values_test
  from geometric_cdf_values                   import geometric_cdf_values_test
  from goodwin_values                         import goodwin_values_test
  from gud_values                             import gud_values_test
  from hermite_function_values                import hermite_function_values_test
  from hermite_poly_phys_values               import hermite_poly_phys_values_test
  from hermite_poly_prob_values               import hermite_poly_prob_values_test
  from hyper_1f1_values                       import hyper_1f1_values_test
  from hyper_2f1_values                       import hyper_2f1_values_test
  from hypergeometric_cdf_values              import hypergeometric_cdf_values_test
  from hypergeometric_pdf_values              import hypergeometric_pdf_values_test
  from hypergeometric_u_values                import hypergeometric_u_values_test
  from i0ml0_values                           import i0ml0_values_test
  from i1ml1_values                           import i1ml1_values_test
  from i4_factorial_values                    import i4_factorial_values_test
  from i4_factorial2_values                   import i4_factorial2_values_test
  from i4_fall_values                         import i4_fall_values_test
  from i4_rise_values                         import i4_rise_values_test
  from int_values                             import int_values_test
  from jacobi_cn_values                       import jacobi_cn_values_test
  from jacobi_dn_values                       import jacobi_dn_values_test
  from jacobi_poly_values                     import jacobi_poly_values_test
  from jacobi_sn_values                       import jacobi_sn_values_test
  from jed_ce_values                          import jed_ce_values_test
  from jed_mjd_values                         import jed_mjd_values_test
  from jed_rd_values                          import jed_rd_values_test
  from jed_weekday_values                     import jed_weekday_values_test
  from kei0_values                            import kei0_values_test
  from kei1_values                            import kei1_values_test
  from ker0_values                            import ker0_values_test
  from ker1_values                            import ker1_values_test
  from laguerre_associated_values             import laguerre_associated_values_test
  from laguerre_general_values                import laguerre_general_values_test
  from laguerre_polynomial_values             import laguerre_polynomial_values_test
  from lambert_w_values                       import lambert_w_values_test
  from laplace_cdf_values                     import laplace_cdf_values_test
  from legendre_associated_values             import legendre_associated_values_test
  from legendre_associated_normalized_values  import legendre_associated_normalized_values_test
  from legendre_associated_normalized_sphere_values  import legendre_associated_normalized_sphere_values_test
  from legendre_function_q_values             import legendre_function_q_values_test
  from legendre_poly_values                   import legendre_poly_values_test
  from lerch_values                           import lerch_values_test
  from lobachevsky_values                     import lobachevsky_values_test
  from lobatto_polynomial_values              import lobatto_polynomial_values_test
  from lobatto_polynomial_derivatives         import lobatto_polynomial_derivatives_test
  from log_values                             import log_values_test
  from log_normal_cdf_values                  import log_normal_cdf_values_test
  from log_series_cdf_values                  import log_series_cdf_values_test
  from log10_values                           import log10_values_test
  from logarithmic_integral_values            import logarithmic_integral_values_test
  from logistic_cdf_values                    import logistic_cdf_values_test
  from mertens_values                         import mertens_values_test
  from moebius_values                         import moebius_values_test
  from negative_binomial_cdf_values           import negative_binomial_cdf_values_test
  from nine_j_values                          import nine_j_values_test
  from normal_01_cdf_values                   import normal_01_cdf_values_test
  from normal_cdf_values                      import normal_cdf_values_test
  from omega_values                           import omega_values_test
  from owen_values                            import owen_values_test
  from partition_count_values                 import partition_count_values_test
  from partition_distinct_count_values        import partition_distinct_count_values_test
  from phi_values                             import phi_values_test
  from pi_values                              import pi_values_test
  from poisson_cdf_values                     import poisson_cdf_values_test
  from polylogarithm_values                   import polylogarithm_values_test
  from prandtl_values                         import prandtl_values_test
  from prime_values                           import prime_values_test
  from psat_values                            import psat_values_test
  from psi_values                             import psi_values_test
  from r8_factorial_values                    import r8_factorial_values_test
  from r8_factorial_log_values                import r8_factorial_log_values_test
  from r8_factorial2_values                   import r8_factorial2_values_test
  from r8_fall_values                         import r8_fall_values_test
  from r8_rise_values                         import r8_rise_values_test
  from rayleigh_cdf_values                    import rayleigh_cdf_values_test
  from secvir_values                          import secvir_values_test
  from shi_values                             import shi_values_test
  from si_values                              import si_values_test
  from sigma_values                           import sigma_values_test
  from sin_values                             import sin_values_test
  from sin_degree_values                      import sin_degree_values_test
  from sin_power_int_values                   import sin_power_int_values_test
  from sinh_values                            import sinh_values_test
  from six_j_values                           import six_j_values_test
  from sound_values                           import sound_values_test
  from sphere_unit_area_values                import sphere_unit_area_values_test
  from sphere_unit_volume_values              import sphere_unit_volume_values_test
  from spherical_harmonic_values              import spherical_harmonic_values_test
  from sqrt_values                            import sqrt_values_test
  from stirling1_values                       import stirling1_values_test
  from stirling2_values                       import stirling2_values_test
  from stromgen_values                        import stromgen_values_test
  from struve_h0_values                       import struve_h0_values_test
  from struve_h1_values                       import struve_h1_values_test
  from struve_l0_values                       import struve_l0_values_test
  from struve_l1_values                       import struve_l1_values_test
  from student_cdf_values                     import student_cdf_values_test
  from student_noncentral_cdf_values          import student_noncentral_cdf_values_test
  from subfactorial_values                    import subfactorial_values_test
  from surten_values                          import surten_values_test
  from synch1_values                          import synch1_values_test
  from synch2_values                          import synch2_values_test
  from tan_values                             import tan_values_test
  from tanh_values                            import tanh_values_test
  from tau_values                             import tau_values_test
  from thercon_values                         import thercon_values_test
  from three_j_values                         import three_j_values_test
  from tran02_values                          import tran02_values_test
  from tran03_values                          import tran03_values_test
  from tran04_values                          import tran04_values_test
  from tran05_values                          import tran05_values_test
  from tran06_values                          import tran06_values_test
  from tran07_values                          import tran07_values_test
  from tran08_values                          import tran08_values_test
  from tran09_values                          import tran09_values_test
  from trigamma_values                        import trigamma_values_test
  from truncated_normal_ab_cdf_values         import truncated_normal_ab_cdf_values_test
  from truncated_normal_ab_pdf_values         import truncated_normal_ab_pdf_values_test
  from truncated_normal_a_cdf_values          import truncated_normal_a_cdf_values_test
  from truncated_normal_a_pdf_values          import truncated_normal_a_pdf_values_test
  from truncated_normal_b_cdf_values          import truncated_normal_b_cdf_values_test
  from truncated_normal_b_pdf_values          import truncated_normal_b_pdf_values_test
  from tsat_values                            import tsat_values_test
  from van_der_corput_values                  import van_der_corput_values_test
  from viscosity_values                       import viscosity_values_test
  from von_mises_cdf_values                   import von_mises_cdf_values_test
  from weekday_values                         import weekday_values_test
  from weibull_cdf_values                     import weibull_cdf_values_test
  from zeta_values                            import zeta_values_test

  print ''
  print 'TEST_VALUES_TEST'
  print '  Python version:'
  print '  Test the TEST_VALUES library.'

  abram0_values_test ( )
  abram1_values_test ( )
  abram2_values_test ( )
  agm_values_test ( )
  airy_ai_values_test ( )
  airy_ai_int_values_test ( )
  airy_ai_prime_values_test ( )
  airy_bi_values_test ( )
  airy_bi_int_values_test ( )
  airy_bi_prime_values_test ( )
  airy_cai_values_test ( )
  airy_cbi_values_test ( )
  airy_gi_values_test ( )
  arccos_values_test ( )
  arccosh_values_test ( )
  arcsin_values_test ( )
  arcsinh_values_test ( )
  arctan_values_test ( )
  arctan_int_values_test ( )
  arctan2_values_test ( )
  arctanh_values_test ( )
  bei0_values_test ( )
  bei1_values_test ( )
  bell_values_test ( )
  ber0_values_test ( )
  ber1_values_test ( )
  bernoulli_number_values_test ( )
  bernoulli_poly_values_test ( )
  bernstein_poly_01_values_test ( )
  bessel_i0_values_test ( )
  bessel_i0_int_values_test ( )
  bessel_i0_spherical_values_test ( )
  bessel_i1_values_test ( )
  bessel_i1_spherical_values_test ( )
  bessel_in_values_test ( )
  bessel_ix_values_test ( )
  bessel_j0_values_test ( )
  bessel_j0_int_values_test ( )
  bessel_j0_spherical_values_test ( )
  bessel_j1_values_test ( )
  bessel_j1_spherical_values_test ( )
  bessel_jn_values_test ( )
  bessel_jx_values_test ( )
  bessel_k0_values_test ( )
  bessel_k0_int_values_test ( )
  bessel_k1_values_test ( )
  bessel_kn_values_test ( )
  bessel_kx_values_test ( )
  bessel_y0_values_test ( )
  bessel_y0_int_values_test ( )
  bessel_y0_spherical_values_test ( )
  bessel_y1_values_test ( )
  bessel_y1_spherical_values_test ( )
  bessel_yn_values_test ( )
  bessel_yx_values_test ( )
  beta_values_test ( )
  beta_cdf_values_test ( )
  beta_inc_values_test ( )
  beta_log_values_test ( )
  beta_noncentral_cdf_values_test ( )
  binomial_values_test ( )
  binomial_cdf_values_test ( )
  bivariate_normal_cdf_values_test ( )
  catalan_values_test ( )
  cauchy_cdf_values_test ( )
  cbrt_values_test ( )
  cheby_t_poly_values_test ( )
  cheby_u_poly_values_test ( )
  cheby_v_poly_values_test ( )
  cheby_w_poly_values_test ( )
  chi_values_test ( )
  chi_square_cdf_values_test ( )
  chi_square_noncentral_cdf_values_test ( )
  ci_values_test ( )
  cin_values_test ( )
  cinh_values_test ( )
  clausen_values_test ( )
  clebsch_gordan_values_test ( )
  collatz_count_values_test ( )
  cos_values_test ( )
  cos_degree_values_test ( )
  cos_power_int_values_test ( )
  cosh_values_test ( )
  cot_values_test ( )
  cp_values_test ( )
  dawson_values_test ( )
  debye1_values_test ( )
  debye2_values_test ( )
  debye3_values_test ( )
  debye4_values_test ( )
  dedekind_sum_values_test ( )
  dielectric_values_test ( )
  dilogarithm_values_test ( )
  e1_values_test ( )
  elliptic_ea_values_test ( )
  elliptic_em_values_test ( )
  elliptic_ka_values_test ( )
  elliptic_km_values_test ( )
  erf_values_test ( )
  erfc_values_test ( )
  euler_number_values_test ( )
  euler_poly_values_test ( )
  exp_values_test ( )
  exp3_int_values_test ( )
  exponential_cdf_values_test ( )
  extreme_values_cdf_values_test ( )
  f_cdf_values_test ( )
  f_noncentral_cdf_values_test ( )
  fresnel_cos_values_test ( )
  fresnel_sin_values_test ( )
  frobenius_number_data_values_test ( )
  frobenius_number_order_values_test ( )
  frobenius_number_order2_values_test ( )
  gamma_values_test ( )
  gamma_inc_values_test ( )
  gamma_inc_p_values_test ( )
  gamma_inc_q_values_test ( )
  gamma_log_values_test ( )
  gegenbauer_poly_values_test ( )
  geometric_cdf_values_test ( )
  goodwin_values_test ( )
  gud_values_test ( )
  hermite_function_values_test ( )
  hermite_poly_phys_values_test ( )
  hermite_poly_prob_values_test ( )
  hyper_1f1_values_test ( )
  hyper_2f1_values_test ( )
  hypergeometric_cdf_values_test ( )
  hypergeometric_pdf_values_test ( )
  hypergeometric_u_values_test ( )
  i0ml0_values_test ( )
  i1ml1_values_test ( )
  i4_factorial_values_test ( )
  i4_factorial2_values_test ( )
  i4_fall_values_test ( )
  i4_rise_values_test ( )
  int_values_test ( )
  jacobi_cn_values_test ( )
  jacobi_dn_values_test ( )
  jacobi_poly_values_test ( )
  jacobi_sn_values_test ( )
  jed_ce_values_test ( )
  jed_mjd_values_test ( )
  jed_rd_values_test ( )
  jed_weekday_values_test ( )
  kei0_values_test ( )
  kei1_values_test ( )
  ker0_values_test ( )
  ker1_values_test ( )
  laguerre_associated_values_test ( )
  laguerre_general_values_test ( )
  laguerre_polynomial_values_test ( )
  lambert_w_values_test ( )
  laplace_cdf_values_test ( )
  legendre_associated_values_test ( )
  legendre_associated_normalized_values_test ( )
  legendre_associated_normalized_sphere_values_test ( )
  legendre_function_q_values_test ( )
  legendre_poly_values_test ( )
  lerch_values_test ( )
  lobachevsky_values_test ( )
  lobatto_polynomial_values_test ( )
  lobatto_polynomial_derivatives_test ( )
  log_values_test ( )
  log_normal_cdf_values_test ( )
  log_series_cdf_values_test ( )
  log10_values_test ( )
  logarithmic_integral_values_test ( )
  logistic_cdf_values_test ( )
  mertens_values_test ( )
  moebius_values_test ( )
  negative_binomial_cdf_values_test ( )
  nine_j_values_test ( )
  normal_01_cdf_values_test ( )
  normal_cdf_values_test ( )
  omega_values_test ( )
  owen_values_test ( )
  partition_count_values_test ( )
  partition_distinct_count_values_test ( )
  phi_values_test ( )
  pi_values_test ( )
  poisson_cdf_values_test ( )
  polylogarithm_values_test ( )
  prandtl_values_test ( )
  prime_values_test ( )
  psat_values_test ( )
  psi_values_test ( )
  r8_factorial_values_test ( )
  r8_factorial_log_values_test ( )
  r8_factorial2_values_test ( )
  r8_fall_values_test ( )
  r8_rise_values_test ( )
  rayleigh_cdf_values_test ( )
  secvir_values_test ( )
  shi_values_test ( )
  si_values_test ( )
  sigma_values_test ( )
  sin_values_test ( )
  sin_degree_values_test ( )
  sin_power_int_values_test ( )
  sinh_values_test ( )
  six_j_values_test ( )
  sound_values_test ( )
  sphere_unit_area_values_test ( )
  sphere_unit_volume_values_test ( )
  spherical_harmonic_values_test ( )
  sqrt_values_test ( )
  stirling1_values_test ( )
  stirling2_values_test ( )
  stromgen_values_test ( )
  struve_h0_values_test ( )
  struve_h1_values_test ( )
  struve_l0_values_test ( )
  struve_l1_values_test ( )
  student_cdf_values_test ( )
  student_noncentral_cdf_values_test ( )
  subfactorial_values_test ( )
  surten_values_test ( )
  synch1_values_test ( )
  synch2_values_test ( )
  tan_values_test ( )
  tanh_values_test ( )
  tau_values_test ( )
  thercon_values_test ( )
  three_j_values_test ( )
  tran02_values_test ( )
  tran03_values_test ( )
  tran04_values_test ( )
  tran05_values_test ( )
  tran06_values_test ( )
  tran07_values_test ( )
  tran08_values_test ( )
  tran09_values_test ( )
  trigamma_values_test ( )
  truncated_normal_ab_cdf_values_test ( )
  truncated_normal_ab_pdf_values_test ( )
  truncated_normal_a_cdf_values_test ( )
  truncated_normal_a_pdf_values_test ( )
  truncated_normal_b_cdf_values_test ( )
  truncated_normal_b_pdf_values_test ( )
  tsat_values_test ( )
  van_der_corput_values_test ( )
  viscosity_values_test
  von_mises_cdf_values_test
  weekday_values_test
  weibull_cdf_values_test
  zeta_values_test
#
#  Terminate.
#
  print ''
  print 'TEST_VALUES_TEST:'
  print '  Normal end of execution.'

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  test_values_test ( )
  timestamp ( )
