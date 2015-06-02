#! /usr/bin/env python
#
def test_determinant ( ):

#*****************************************************************************80
#
## TEST_DETERMINANT tests the determinant computations.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 April 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  from a123                        import a123
  from a123                        import a123_determinant
  from aegerter                    import aegerter
  from aegerter                    import aegerter_determinant
  from bab                         import bab
  from bab                         import bab_determinant
  from bauer                       import bauer
  from bauer                       import bauer_determinant
  from bernstein                   import bernstein
  from bernstein                   import bernstein_determinant
  from bis                         import bis
  from bis                         import bis_determinant
  from biw                         import biw
  from biw                         import biw_determinant
  from bodewig                     import bodewig
  from bodewig                     import bodewig_determinant
  from boothroyd                   import boothroyd
  from boothroyd                   import boothroyd_determinant
  from borderband                  import borderband
  from borderband                  import borderband_determinant
  from carry                       import carry
  from carry                       import carry_determinant
  from cauchy                      import cauchy
  from cauchy                      import cauchy_determinant
  from cheby_diff1                 import cheby_diff1
  from cheby_diff1                 import cheby_diff1_determinant
  from cheby_t                     import cheby_t
  from cheby_t                     import cheby_t_determinant
  from cheby_u                     import cheby_u
  from cheby_u                     import cheby_u_determinant
  from cheby_van1                  import cheby_van1
  from cheby_van2                  import cheby_van2
  from cheby_van2                  import cheby_van2_determinant
  from cheby_van3                  import cheby_van3
  from cheby_van3                  import cheby_van3_determinant
  from chow                        import chow
  from chow                        import chow_determinant
  from clement1                    import clement1
  from clement1                    import clement1_determinant
  from clement2                    import clement2
  from clement2                    import clement2_determinant
  from combin                      import combin
  from combin                      import combin_determinant
  from companion                   import companion
  from companion                   import companion_determinant
  from complex_i                   import complex_i
  from complex_i                   import complex_i_determinant
  from conex1                      import conex1
  from conex1                      import conex1_determinant
  from conex2                      import conex2
  from conex2                      import conex2_determinant
  from conex3                      import conex3
  from conex3                      import conex3_determinant
  from conex4                      import conex4
  from conex4                      import conex4_determinant
  from conference                  import conference
  from conference                  import conference_determinant
  from creation                    import creation
  from creation                    import creation_determinant
  from daub2                       import daub2
  from daub2                       import daub2_determinant
  from daub4                       import daub4
  from daub4                       import daub4_determinant
  from daub6                       import daub6
  from daub6                       import daub6_determinant
  from daub8                       import daub8
  from daub8                       import daub8_determinant
  from daub10                      import daub10
  from daub10                      import daub10_determinant
  from daub12                      import daub12
  from daub12                      import daub12_determinant
  from diagonal                    import diagonal
  from diagonal                    import diagonal_determinant
  from dif1                        import dif1
  from dif1                        import dif1_determinant
  from dif1cyclic                  import dif1cyclic
  from dif1cyclic                  import dif1cyclic_determinant
  from dif2                        import dif2
  from dif2                        import dif2_determinant
  from dif2cyclic                  import dif2cyclic
  from dif2cyclic                  import dif2cyclic_determinant
  from dorr                        import dorr
  from dorr                        import dorr_determinant
  from downshift                   import downshift
  from downshift                   import downshift_determinant
  from eberlein                    import eberlein
  from eberlein                    import eberlein_determinant
  from eulerian                    import eulerian
  from eulerian                    import eulerian_determinant
  from exchange                    import exchange
  from exchange                    import exchange_determinant
  from fibonacci1                  import fibonacci1
  from fibonacci1                  import fibonacci1_determinant
  from fibonacci2                  import fibonacci2
  from fibonacci2                  import fibonacci2_determinant
  from fibonacci3                  import fibonacci3
  from fibonacci3                  import fibonacci3_determinant
  from fiedler                     import fiedler
  from fiedler                     import fiedler_determinant
  from forsythe                    import forsythe
  from forsythe                    import forsythe_determinant
  from fourier_cosine              import fourier_cosine
  from fourier_cosine              import fourier_cosine_determinant
  from fourier_sine                import fourier_sine
  from fourier_sine                import fourier_sine_determinant
  from frank                       import frank
  from frank                       import frank_determinant
  from gear                        import gear
  from gear                        import gear_determinant
  from gfpp                        import gfpp
  from gfpp                        import gfpp_determinant
  from givens                      import givens
  from givens                      import givens_determinant
  from gk316                       import gk316
  from gk316                       import gk316_determinant
  from gk323                       import gk323
  from gk323                       import gk323_determinant
  from gk324                       import gk324
  from gk324                       import gk324_determinant
  from hankel_n                    import hankel_n
  from hankel_n                    import hankel_n_determinant
  from hanowa                      import hanowa
  from hanowa                      import hanowa_determinant
  from harman                      import harman
  from harman                      import harman_determinant
  from hartley                     import hartley
  from hartley                     import hartley_determinant
  from helmert                     import helmert
  from helmert                     import helmert_determinant
  from hermite                     import hermite
  from hermite                     import hermite_determinant
  from herndon                     import herndon
  from herndon                     import herndon_determinant
  from hilbert                     import hilbert
  from hilbert                     import hilbert_determinant
  from householder                 import householder
  from householder                 import householder_determinant
  from i4_uniform_ab               import i4_uniform_ab
  from i4vec_indicator0            import i4vec_indicator0
  from idem_random                 import idem_random
  from idem_random                 import idem_random_determinant
  from identity                    import identity
  from identity                    import identity_determinant
  from ijfact1                     import ijfact1
  from ijfact1                     import ijfact1_determinant
  from ijfact2                     import ijfact2
  from ijfact2                     import ijfact2_determinant
  from ill3                        import ill3
  from ill3                        import ill3_determinant
  from integration                 import integration
  from integration                 import integration_determinant
  from invol                       import invol
  from invol                       import invol_determinant
  from jacobi                      import jacobi
  from jacobi                      import jacobi_determinant
  from jordan                      import jordan
  from jordan                      import jordan_determinant
  from kahan                       import kahan
  from kahan                       import kahan_determinant
  from kershaw                     import kershaw
  from kershaw                     import kershaw_determinant
  from kershawtri                  import kershawtri
  from kershawtri                  import kershawtri_determinant
  from kms                         import kms
  from kms                         import kms_determinant
  from laguerre                    import laguerre
  from laguerre                    import laguerre_determinant
  from legendre                    import legendre
  from legendre                    import legendre_determinant
  from lehmer                      import lehmer
  from lehmer                      import lehmer_determinant
  from leslie                      import leslie
  from leslie                      import leslie_determinant
  from lesp                        import lesp
  from lesp                        import lesp_determinant
  from lietzke                     import lietzke
  from lietzke                     import lietzke_determinant
  from line_adj                    import line_adj
  from line_adj                    import line_adj_determinant
  from line_loop_adj               import line_loop_adj
  from line_loop_adj               import line_loop_adj_determinant
  from lotkin                      import lotkin
  from lotkin                      import lotkin_determinant
  from maxij                       import maxij
  from maxij                       import maxij_determinant
  from milnes                      import milnes
  from milnes                      import milnes_determinant
  from minij                       import minij
  from minij                       import minij_determinant
  from moler1                      import moler1
  from moler1                      import moler1_determinant
  from moler2                      import moler2
  from moler2                      import moler2_determinant
  from moler3                      import moler3
  from moler3                      import moler3_determinant
  from moler4                      import moler4
  from moler4                      import moler4_determinant
  from neumann                     import neumann
  from neumann                     import neumann_determinant
  from one                         import one
  from one                         import one_determinant
  from ortega                      import ortega
  from ortega                      import ortega_determinant
  from orth_random                 import orth_random
  from orth_random                 import orth_random_determinant
  from orth_symm                   import orth_symm
  from orth_symm                   import orth_symm_determinant
  from oto                         import oto
  from oto                         import oto_determinant
  from parter                      import parter
  from parter                      import parter_determinant
  from pascal1                     import pascal1
  from pascal1                     import pascal1_determinant
  from pascal2                     import pascal2
  from pascal2                     import pascal2_determinant
  from pascal3                     import pascal3
  from pascal3                     import pascal3_determinant
  from pds_random                  import pds_random
  from pds_random                  import pds_random_determinant
  from pei                         import pei
  from pei                         import pei_determinant
  from permutation_random          import permutation_random
  from permutation_random          import permutation_random_determinant
  from plu                         import plu
  from plu                         import plu_determinant
  from poisson                     import poisson
  from poisson                     import poisson_determinant
  from r8_uniform_ab               import r8_uniform_ab
  from r8mat_norm_fro              import r8mat_norm_fro
  from r8vec_uniform_ab            import r8vec_uniform_ab
  from redheffer                   import redheffer
  from redheffer                   import redheffer_determinant
  from ring_adj                    import ring_adj
  from ring_adj                    import ring_adj_determinant
  from ris                         import ris
  from ris                         import ris_determinant
  from rodman                      import rodman
  from rodman                      import rodman_determinant
  from rosser1                     import rosser1
  from rosser1                     import rosser1_determinant
  from routh                       import routh
  from routh                       import routh_determinant
  from rutis1                      import rutis1
  from rutis1                      import rutis1_determinant
  from rutis2                      import rutis2
  from rutis2                      import rutis2_determinant
  from rutis3                      import rutis3
  from rutis3                      import rutis3_determinant
  from rutis4                      import rutis4
  from rutis4                      import rutis4_determinant
  from rutis5                      import rutis5
  from rutis5                      import rutis5_determinant
  from schur_block                 import schur_block
  from schur_block                 import schur_block_determinant
  from spline                      import spline
  from spline                      import spline_determinant
  from stirling                    import stirling
  from stirling                    import stirling_determinant
  from summation                   import summation
  from summation                   import summation_determinant
  from sweet1                      import sweet1
  from sweet1                      import sweet1_determinant
  from sweet2                      import sweet2
  from sweet2                      import sweet2_determinant
  from sweet3                      import sweet3
  from sweet3                      import sweet3_determinant
  from sweet4                      import sweet4
  from sweet4                      import sweet4_determinant
  from sylvester_kac               import sylvester_kac
  from sylvester_kac               import sylvester_kac_determinant
  from symm_random                 import symm_random
  from symm_random                 import symm_random_determinant
  from tri_upper                   import tri_upper
  from tri_upper                   import tri_upper_determinant
  from tris                        import tris
  from tris                        import tris_determinant
  from triv                        import triv
  from triv                        import triv_determinant
  from triw                        import triw
  from triw                        import triw_determinant
  from upshift                     import upshift
  from upshift                     import upshift_determinant
  from vand1                       import vand1
  from vand1                       import vand1_determinant
  from vand2                       import vand2
  from vand2                       import vand2_determinant
  from wilk03                      import wilk03
  from wilk03                      import wilk03_determinant
  from wilk04                      import wilk04
  from wilk04                      import wilk04_determinant
  from wilk05                      import wilk05
  from wilk05                      import wilk05_determinant
  from wilk12                      import wilk12
  from wilk12                      import wilk12_determinant
  from wilk21                      import wilk21
  from wilk21                      import wilk21_determinant
  from wilson                      import wilson
  from wilson                      import wilson_determinant
  from zero                        import zero
  from zero                        import zero_determinant

  print ''
  print 'TEST_DETERMINANT'
  print '  Compute the determinants of an example of each'
  print '  test matrix compare with the determinant routine,'
  print '  if available.  Print the matrix Frobenius norm'
  print '  for an estimate of magnitude.'
  print ''
  print '  Title                    N      ',
  print 'Determ          Determ          ||A||'
  print ''
#
#  A123
#
  title = 'A123'
  n = 3
  a = a123 ( )
  determ1 = a123_determinant ( )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  AEGERTER
#
  title = 'AEGERTER'
  n = 5
  a = aegerter ( n )
  determ1 = aegerter_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  ANTICIRCULANT
#
  title = 'ANTICIRCULANT'
  n = 3
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( n, r8_lo, r8_hi, seed )
# a = anticirculant ( n, n, x )
# determ1 = anticirculant_determinant ( n, x )
# determ2 = np.linalg.det ( a )
# norm_frobenius = r8mat_norm_fro ( n, n, a )
# print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
#   title, n, determ1, determ2, norm_frobenius )
#
#  ANTICIRCULANT
#
  title = 'ANTICIRCULANT'
  n = 4
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( n, r8_lo, r8_hi, seed )
# a = anticirculant ( n, n, x )
# determ1 = anticirculant_determinant ( n, x )
# determ2 = np.linalg.det ( a )
# norm_frobenius = r8mat_norm_fro ( n, n, a )
# print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
#   title, n, determ1, determ2, norm_frobenius )
#
#  ANTICIRCULANT
#
  title = 'ANTICIRCULANT'
  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( n, r8_lo, r8_hi, seed )
# a = anticirculant ( n, n, x )
# determ1 = anticirculant_determinant ( n, x )
# determ2 = np.linalg.det ( a )
# norm_frobenius = r8mat_norm_fro ( n, n, a )
# print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
#   title, n, determ1, determ2, norm_frobenius )
#
#  ANTIHADAMARD
#
  title = 'ANTIHADAMARD'
  n = 5
# a = antihadamard ( n )
# determ1 = antihadamard_determinant ( n )
# determ2 = np.linalg.det ( a )
# norm_frobenius = r8mat_norm_fro ( n, n, a )
# print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
#   title, n, determ1, determ2, norm_frobenius )
#
#  ANTISYMM_RANDOM
#
  title = 'ANTISYMM_RANDOM'
  n = 5
  key = 123456789
# a = antisymm_random ( n, key )
# determ2 = np.linalg.det ( a )
# norm_frobenius = r8mat_norm_fro ( n, n, a )
# print '  %-20s  %4d                  %14g  %10.2g' % ( \
#   title, n,          determ2, norm_frobenius )
#
#  ANTISYMM_RANDOM
#
  title = 'ANTISYMM_RANDOM'
  n = 6
  key = 123456789
# a = antisymm_random ( n, key )
# determ2 = np.linalg.det ( a )
# norm_frobenius = r8mat_norm_fro ( n, n, a )
# print '  %-20s  %4d                  %14g  %10.2g' % ( \
#   title, n,          determ2, norm_frobenius )
#
#  BAB
#
  title = 'BAB'
  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  beta, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  a = bab ( n, alpha, beta )
  determ1 = bab_determinant ( n, alpha, beta )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  BAUER
#
  title = 'BAUER'
  n = 6
  a = bauer ( )
  determ1 = bauer_determinant ( )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  BERNSTEIN
#
  title = 'BERNSTEIN'
  n = 5
  a = bernstein ( n )
  determ1 = bernstein_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  BIMARKOV_RANDOM
#
  title = 'BIMARKOV_RANDOM'
  n = 5
  key = 123456789
# a = bimarkov_random ( n, key )
# determ2 = np.linalg.det ( a )
# norm_frobenius = r8mat_norm_fro ( n, n, a )
# print '  %-20s  %4d                  %14g  %10.2g' % ( \
#   title, n,         determ2, norm_frobenius )
#
#  BIS
#
  title = 'BIS'
  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  beta, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  a = bis ( alpha, beta, n, n )
  determ1 = bis_determinant ( alpha, beta, n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  BIW
#
  title = 'BIW'
  n = 5
  a = biw ( n )
  determ1 = biw_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  BODEWIG
#
  title = 'BODEWIG'
  n = 4
  a = bodewig ( )
  determ1 = bodewig_determinant ( )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  BOOTHROYD
#
  title = 'BOOTHROYD'
  n = 5
  a = boothroyd ( n )
  determ1 = boothroyd_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  BORDERBAND
#
  title = 'BORDERBAND'
  n = 5
  a = borderband ( n )
  determ1 = borderband_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  CARRY
#
  title = 'CARRY'
  n = 5
  i4_lo = 2
  i4_hi = 20
  seed = 123456789
  k, seed = i4_uniform_ab ( i4_lo, i4_hi, seed )
  a = carry ( n, k )
  determ1 = carry_determinant ( n, k )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  CAUCHY
#
  title = 'CAUCHY'
  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( n, r8_lo, r8_hi, seed )
  y, seed = r8vec_uniform_ab ( n, r8_lo, r8_hi, seed )
  a = cauchy ( n, x, y )
  determ1 = cauchy_determinant ( n, x, y )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  CHEBY_DIFF1
#
  title = 'CHEBY_DIFF1'
  n = 5
  a = cheby_diff1 ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d                  %14g  %10.2g' % ( \
    title, n,          determ2, norm_frobenius )
#
#  CHEBY_DIFF1
#
  title = 'CHEBY_DIFF1'
  n = 6
  a = cheby_diff1 ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d                  %14g  %10.2g' % ( \
    title, n,          determ2, norm_frobenius )
#
#  CHEBY_T
#
  title = 'CHEBY_T'
  n = 5
  a = cheby_t ( n )
  determ1 = cheby_t_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  CHEBY_U
#
  title = 'CHEBY_U'
  n = 5
  a = cheby_u ( n )
  determ1 = cheby_u_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  CHEBY_VAN1
#
  title = 'CHEBY_VAN1'
  n = 5
  r8_lo = -1.0
  r8_hi = +1.0
  x = np.linspace ( r8_lo, r8_hi, n )
  a = cheby_van1 ( n, r8_lo, r8_hi, n, x )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d                  %14g  %10.2g' % ( \
    title, n,          determ2, norm_frobenius )
#
#  CHEBY_VAN2
#
  title = 'CHEBY_VAN2'
  n = 2
  a = cheby_van2 ( n )
  determ1 = cheby_van2_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  CHEBY_VAN2
#
  title = 'CHEBY_VAN2'
  n = 3
  a = cheby_van2 ( n )
  determ1 = cheby_van2_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  CHEBY_VAN2
#
  title = 'CHEBY_VAN2'
  n = 4
  a = cheby_van2 ( n )
  determ1 = cheby_van2_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  CHEBY_VAN2
#
  title = 'CHEBY_VAN2'
  n = 5
  a = cheby_van2 ( n )
  determ1 = cheby_van2_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  CHEBY_VAN2
#
  title = 'CHEBY_VAN2'
  n = 6
  a = cheby_van2 ( n )
  determ1 = cheby_van2_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  CHEBY_VAN2
#
  title = 'CHEBY_VAN2'
  n = 7
  a = cheby_van2 ( n )
  determ1 = cheby_van2_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  CHEBY_VAN2
#
  title = 'CHEBY_VAN2'
  n = 8
  a = cheby_van2 ( n )
  determ1 = cheby_van2_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  CHEBY_VAN2
#
  title = 'CHEBY_VAN2'
  n = 9
  a = cheby_van2 ( n )
  determ1 = cheby_van2_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  CHEBY_VAN2
#
  title = 'CHEBY_VAN2'
  n = 10
  a = cheby_van2 ( n )
  determ1 = cheby_van2_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  CHEBY_VAN3
#
  title = 'CHEBY_VAN3'
  n = 5
  a = cheby_van3 ( n )
  determ1 = cheby_van3_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  CHOW
#
  title = 'CHOW'
  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  beta, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  a = chow ( alpha, beta, n, n )
  determ1 = chow_determinant ( alpha, beta, n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  CIRCULANT
#
  title = 'CIRCULANT'
  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( n, r8_lo, r8_hi, seed )
# a = circulant ( n, n, x )
# determ1 = circulant_determinant ( n, x )
# determ2 = np.linalg.det ( a )
# norm_frobenius = r8mat_norm_fro ( n, n, a )
# print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
#   title, n, determ1, determ2, norm_frobenius )
#
#  CIRCULANT2
#
  title = 'CIRCULANT2'
  n = 3
# a = circulant2 ( n )
# determ1 = circulant2_determinant ( n )
# determ2 = np.linalg.det ( a )
# norm_frobenius = r8mat_norm_fro ( n, n, a )
# print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
#   title, n, determ1, determ2, norm_frobenius )
#
#  CIRCULANT2
#
  title = 'CIRCULANT2'
  n = 4
# a = circulant2 ( n )
# determ1 = circulant2_determinant ( n )
# determ2 = np.linalg.det ( a )
# norm_frobenius = r8mat_norm_fro ( n, n, a )
# print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
#   title, n, determ1, determ2, norm_frobenius )
#
#  CIRCULANT2
#
  title = 'CIRCULANT2'
  n = 5
# a = circulant2 ( n )
# determ1 = circulant2_determinant ( n )
# determ2 = np.linalg.det ( a )
# norm_frobenius = r8mat_norm_fro ( n, n, a )
# print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
#   title, n, determ1, determ2, norm_frobenius )
#
#  CLEMENT1
#
  title = 'CLEMENT1'
  n = 5
  a = clement1 ( n )
  determ1 = clement1_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  CLEMENT1
#
  title = 'CLEMENT1'
  n = 6
  a = clement1 ( n )
  determ1 = clement1_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  CLEMENT2
#
  title = 'CLEMENT2'
  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( n - 1, r8_lo, r8_hi, seed )
  y, seed = r8vec_uniform_ab ( n - 1, r8_lo, r8_hi, seed )
  a = clement2 ( n, x, y )
  determ1 = clement2_determinant ( n, x, y )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  CLEMENT2
#
  title = 'CLEMENT2'
  n = 6
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( n - 1, r8_lo, r8_hi, seed )
  y, seed = r8vec_uniform_ab ( n - 1, r8_lo, r8_hi, seed )
  a = clement2 ( n, x, y )
  determ1 = clement2_determinant ( n, x, y )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  COMBIN
#
  title = 'COMBIN'
  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  beta, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  a = combin ( alpha, beta, n )
  determ1 = combin_determinant ( alpha, beta, n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  COMPANION
#
  title = 'COMPANION'
  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( n, r8_lo, r8_hi, seed )
  a = companion ( n, x )
  determ1 = companion_determinant ( n, x )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  COMPLEX_I
#
  title = 'COMPLEX_I'
  n = 2
  a = complex_i ( )
  determ1 = complex_i_determinant ( )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  CONEX1
#
  title = 'CONEX1'
  n = 4
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  a = conex1 ( alpha )
  determ1 = conex1_determinant ( alpha )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  CONEX2
#
  title = 'CONEX2'
  n = 3
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  a = conex2 ( alpha )
  determ1 = conex2_determinant ( alpha )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  CONEX3
#
  title = 'CONEX3'
  n = 5
  a = conex3 ( n )
  determ1 = conex3_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  CONEX4
#
  title = 'CONEX4'
  n = 4
  a = conex4 ( )
  determ1 = conex1_determinant ( alpha )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  CONFERENCE
#  N-1 must be an odd prime, or a power of an odd prime.
#
  title = 'CONFERENCE'
  n = 6
  a = conference ( n )
  determ1 = conference_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  CREATION
#
  title = 'CREATION'
  n = 5
  a = creation ( n, n )
  determ1 = creation_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  DAUB2
#
  title = 'DAUB2'
  n = 4
  a = daub2 ( n )
  determ1 = daub2_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  DAUB4
#
  title = 'DAUB4'
  n = 8
  a = daub4 ( n )
  determ1 = daub4_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  DAUB6
#
  title = 'DAUB6'
  n = 12
  a = daub6 ( n )
  determ1 = daub6_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  DAUB8
#
  title = 'DAUB8'
  n = 16
  a = daub8 ( n )
  determ1 = daub8_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  DAUB10
#
  title = 'DAUB10'
  n = 20
  a = daub10 ( n )
  determ1 = daub10_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  DAUB12
#
  title = 'DAUB12'
  n = 24
  a = daub12 ( n )
  determ1 = daub12_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  DIAGONAL
#
  title = 'DIAGONAL'
  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( n, r8_lo, r8_hi, seed )
  a = diagonal ( n, n, x )
  determ1 = diagonal_determinant ( n, x )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  DIF1
#
  title = 'DIF1'
  n = 5
  a = dif1 ( n, n )
  determ1 = dif1_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  DIF1
#
  title = 'DIF1'
  n = 6
  a = dif1 ( n, n )
  determ1 = dif1_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  DIF1CYCLIC
#
  title = 'DIF1CYCLIC'
  n = 5
  a = dif1cyclic ( n )
  determ1 = dif1cyclic_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  DIF2
#
  title = 'DIF2'
  n = 5
  a = dif2 ( n, n )
  determ1 = dif2_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  DIF2CYCLIC
#
  title = 'DIF2CYCLIC'
  n = 5
  a = dif2cyclic ( n )
  determ1 = dif2cyclic_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  DORR
#
  title = 'DORR'
  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  a = dorr ( alpha, n )
  determ1 = dorr_determinant ( alpha, n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  DOWNSHIFT
#
  title = 'DOWNSHIFT'
  n = 5
  a = downshift ( n )
  determ1 = downshift_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  EBERLEIN
#
  title = 'EBERLEIN'
  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  a = eberlein ( alpha, n )
  determ1 = eberlein_determinant ( alpha, n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  EULERIAN
#
  title = 'EULERIAN'
  n = 5
  a = eulerian ( n, n )
  determ1 = eulerian_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  EXCHANGE
#
  title = 'EXCHANGE'
  n = 5
  a = exchange ( n, n )
  determ1 = exchange_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  FIBONACCI1
#
  title = 'FIBONACCI1'
  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  beta, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  a = fibonacci1 ( n, alpha, beta )
  determ1 = fibonacci1_determinant ( n, alpha, beta )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  FIBONACCI2
#
  title = 'FIBONACCI2'
  n = 5
  a = fibonacci2 ( n )
  determ1 = fibonacci2_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  FIBONACCI3
#
  title = 'FIBONACCI3'
  n = 5
  a = fibonacci3 ( n )
  determ1 = fibonacci3_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  FIEDLER
#
  title = 'FIEDLER'
  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( n, r8_lo, r8_hi, seed )
  a = fiedler ( n, n, x )
  determ1 = fiedler_determinant ( n, x )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  FORSYTHE
#
  title = 'FORSYTHE'
  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  beta, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  a = forsythe ( alpha, beta, n )
  determ1 = forsythe_determinant ( alpha, beta, n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  FORSYTHE
#
  title = 'FORSYTHE'
  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  beta, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  a = forsythe ( alpha, beta, n )
  determ1 = forsythe_determinant ( alpha, beta, n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  FOURIER_COSINE
#
  title = 'FOURIER_COSINE'
  n = 5
  a = fourier_cosine ( n )
  determ1 = fourier_cosine_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  FOURIER_SINE
#
  title = 'FOURIER_SINE'
  n = 5
  a = fourier_sine ( n )
  determ1 = fourier_sine_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  FRANK
#
  title = 'FRANK'
  n = 5
  a = frank ( n )
  determ1 = frank_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  GEAR
#
  for n in range ( 4, 9 ):
    title = 'GEAR'
    i4_lo = -n
    i4_hi = +n
    seed = 123456789
    ii, seed = i4_uniform_ab ( i4_lo, i4_hi, seed )
    jj, seed = i4_uniform_ab ( i4_lo, i4_hi, seed )
    a = gear ( ii, jj, n )
    determ1 = gear_determinant ( ii, jj, n )
    determ2 = np.linalg.det ( a )
    norm_frobenius = r8mat_norm_fro ( n, n, a )
    print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
      title, n, determ1, determ2, norm_frobenius )
#
#  GFPP
#
  title = 'GFPP'
  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  a = gfpp ( n, alpha )
  determ1 = gfpp_determinant ( n, alpha )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  GIVENS
#
  title = 'GIVENS'
  n = 5
  a = givens ( n, n )
  determ1 = givens_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  GK316
#
  title = 'GK316'
  n = 5
  a = gk316 ( n )
  determ1 = gk316_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  GK323
#
  title = 'GK323'
  n = 5
  a = gk323 ( n, n )
  determ1 = gk323_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  GK324
#
  title = 'GK324'
  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( n - 1, r8_lo, r8_hi, seed )
  a = gk324 ( n, n, x )
  determ1 = gk324_determinant ( n, x )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  GRCAR
#
  title = 'GRCAR'
  n = 5
  i4_lo = 1
  i4_hi = n - 1
  seed = 123456789
  k, seed = i4_uniform_ab ( i4_lo, i4_hi, seed )
# a = grcar ( n, n, k )
# determ2 = np.linalg.det ( a )
# norm_frobenius = r8mat_norm_fro ( n, n, a )
# print '  %-20s  %4d                  %14g  %10.2g' % ( \
#   title, n,          determ2, norm_frobenius )
#
#  HADAMARD
#
  title = 'HADAMARD'
  n = 5
# a = hadamard ( n, n )
# determ2 = np.linalg.det ( a )
# norm_frobenius = r8mat_norm_fro ( n, n, a )
# print '  %-20s  %4d                  %14g  %10.2g' % ( \
#   title, n,          determ2, norm_frobenius )
#
#  HANKEL
#
  title = 'HANKEL'
  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( 2 * n - 1, r8_lo, r8_hi, seed )
# a = hankel ( n, x )
# determ2 = np.linalg.det ( a )
# norm_frobenius = r8mat_norm_fro ( n, n, a )
# print '  %-20s  %4d                  %14g  %10.2g' % ( \
#   title, n,           determ2, norm_frobenius )
#
#  HANKEL_N
#
  title = 'HANKEL_N'
  n = 5
  a = hankel_n ( n )
  determ1 = hankel_n_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  HANOWA
#
  title = 'HANOWA'
  n = 6
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  a = hanowa ( alpha, n )
  determ1 = hanowa_determinant ( alpha, n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  HARMAN
#
  title = 'HARMAN'
  n = 8
  a = harman ( )
  determ1 = harman_determinant ( )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  HARTLEY
#
  for n in range ( 5, 9 ):
    title = 'HARTLEY'
    a = hartley ( n )
    determ1 = hartley_determinant ( n )
    determ2 = np.linalg.det ( a )
    norm_frobenius = r8mat_norm_fro ( n, n, a )
    print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
      title, n, determ1, determ2, norm_frobenius )
#
#  HELMERT
#
  title = 'HELMERT'
  n = 5 
  a = helmert ( n )
  determ1 = helmert_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  HELMERT2
#
  title = 'HELMERT2'
  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( n, r8_lo, r8_hi, seed )
# a = helmert2 ( n, x )
# determ2 = np.linalg.det ( a )
# norm_frobenius = r8mat_norm_fro ( n, n, a )
# print '  %-20s  %4d                  %14g  %10.2g' % ( \
#   title, n,           determ2, norm_frobenius )
#
#  HERMITE
#
  title = 'HERMITE'
  n = 5 
  a = hermite ( n )
  determ1 = hermite_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  HERNDON
#
  title = 'HERNDON'
  n = 5 
  a = herndon ( n )
  determ1 = herndon_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  HILBERT
#
  title = 'HILBERT'
  n = 5 
  a = hilbert ( n, n )
  determ1 = hilbert_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  HOUSEHOLDER
#
  title = 'HOUSEHOLDER'
  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( n, r8_lo, r8_hi, seed )
  a = householder ( n, x )
  determ1 = householder_determinant ( n, x )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  IDEM_RANDOM
#
  title = 'IDEM_RANDOM'
  n = 5
  i4_lo = 0
  i4_hi = n
  seed = 123456789
  rank, seed = i4_uniform_ab ( i4_lo, i4_hi, seed )
  key = 123456789
  a = idem_random ( n, rank, key )
  determ1 = idem_random_determinant ( n, rank, key )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  IDENTITY
#
  title = 'IDENTITY'
  n = 5
  a = identity ( n, n )
  determ1 = identity_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  IJFACT1
#
  title = 'IJFACT1'
  n = 5
  a = ijfact1 ( n )
  determ1 = ijfact1_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  IJFACT2
#
  title = 'IJFACT2'
  n = 5
  a = ijfact2 ( n )
  determ1 = ijfact2_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  ILL3
#
  title = 'ILL3'
  n = 3
  a = ill3 ( )
  determ1 = ill3_determinant ( )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  INTEGRATION
#
  title = 'INTEGRATION'
  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  a = integration ( alpha, n )
  determ1 = integration_determinant ( alpha, n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  INVOL
#
  title = 'INVOL'
  n = 5
  a = invol ( n )
  determ1 = invol_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  INVOL_RANDOM
#
  title = 'INVOL_RANDOM'
  n = 5
  i4_lo = 0
  i4_hi = n
  seed = 123456789
  rank, seed = i4_uniform_ab ( i4_lo, i4_hi, seed )
  key = 123456789
# a = invol_random ( n, rank, key )
# determ2 = np.linalg.det ( a )
# norm_frobenius = r8mat_norm_fro ( n, n, a )
# print '  %-20s  %4d                  %14g  %10.2g' % ( \
#   title, n,           determ2, norm_frobenius )
#
#  JACOBI
#
  title = 'JACOBI'
  n = 5
  a = jacobi ( n, n )
  determ1 = jacobi_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  JACOBI
#
  title = 'JACOBI'
  n = 6
  a = jacobi ( n, n )
  determ1 = jacobi_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  JORDAN
#
  title = 'JORDAN'
  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  a = jordan ( n, n, alpha )
  determ1 = jordan_determinant ( n, alpha )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  KAHAN
#
  title = 'KAHAN'
  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  a = kahan ( alpha, n, n )
  determ1 = kahan_determinant ( alpha, n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  KERSHAW
#
  title = 'KERSHAW'
  n = 4
  a = kershaw ( )
  determ1 = kershaw_determinant ( )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  KERSHAWTRI
#
  title = 'KERSHAWTRI'
  n = 5
  x_n = ( ( n + 1 ) // 2 )
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( x_n, r8_lo, r8_hi, seed )
  a = kershawtri ( n, x )
  determ1 = kershawtri_determinant ( n, x )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  KMS
#
  title = 'KMS'
  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  a = kms ( alpha, n, n )
  determ1 = kms_determinant ( alpha, n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  LAGUERRE
#
  title = 'LAGUERRE'
  n = 5
  a = laguerre ( n )
  determ1 = laguerre_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  LEGENDRE
#
  title = 'LEGENDRE'
  n = 5
  a = legendre ( n )
  determ1 = legendre_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  LEHMER
#
  title = 'LEHMER'
  n = 5
  a = lehmer ( n, n )
  determ1 = lehmer_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  LESLIE
#
  title = 'LESLIE'
  n = 4
  b =  0.025
  di = 0.010
  da = 0.100
  a = leslie ( b, di, da )
  determ1 = leslie_determinant ( b, di, da )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  LESP
#
  title = 'LESP'
  n = 5
  a = lesp ( n, n )
  determ1 = lesp_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  LIETZKE
#
  title = 'LIETZKE'
  n = 5
  a = lietzke ( n )
  determ1 = lietzke_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  LIGHTS_OUT
#
  title = 'LIGHTS_OUT'
  row_num = 5
  col_num = 5
# n, a = lights_out ( row_num, col_num )
# determ2 = np.linalg.det ( a )
# norm_frobenius = r8mat_norm_fro ( n, n, a )
# print '  %-20s  %4d                  %14g  %10.2g' % ( \
#   title, n,           determ2, norm_frobenius )
#
#  LINE_ADJ
#
  title = 'LINE_ADJ'
  n = 5
  a = line_adj ( n )
  determ1 = line_adj_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  LINE_ADJ
#
  title = 'LINE_ADJ'
  n = 6
  a = line_adj ( n )
  determ1 = line_adj_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  LINE_LOOP_ADJ
#
  title = 'LINE_LOOP_ADJ'
  n = 5
  a = line_loop_adj ( n )
  determ1 = line_loop_adj_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  LOEWNER
#
  title = 'LOEWNER'
  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  w, seed = r8vec_uniform_ab ( n, r8_lo, r8_hi, seed )
  x, seed = r8vec_uniform_ab ( n, r8_lo, r8_hi, seed )
  y, seed = r8vec_uniform_ab ( n, r8_lo, r8_hi, seed )
  z, seed = r8vec_uniform_ab ( n, r8_lo, r8_hi, seed )
# a = loewner ( w, x, y, z, n )
# determ2 = np.linalg.det ( a )
# norm_frobenius = r8mat_norm_fro ( n, n, a )
# print '  %-20s  %4d                  %14g  %10.2g' % ( \
#   title, n,          determ2, norm_frobenius )
#
#  LOTKIN
#
  title = 'LOTKIN'
  n = 5
  a = lotkin ( n, n )
  determ1 = lotkin_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  MARKOV_RANDOM
#
  title = 'MARKOV_RANDOM'
  n = 5
  key = 123456789
# a = markov_random ( n, key )
# determ2 = np.linalg.det ( a )
# norm_frobenius = r8mat_norm_fro ( n, n, a )
# print '  %-20s  %4d                  %14g  %10.2g' % ( \
#   title, n,          determ2, norm_frobenius )
#
#  MAXIJ
#
  title = 'MAXIJ'
  n = 5
  a = maxij ( n, n )
  determ1 = maxij_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  MILNES
#
  title = 'MILNES'
  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( n, r8_lo, r8_hi, seed )
  a = milnes ( n, n, x )
  determ1 = milnes_determinant ( n, x )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  MINIJ
#
  title = 'MINIJ'
  n = 5
  a = minij ( n, n )
  determ1 = minij_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  MOLER1
#
  title = 'MOLER1'
  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  a = moler1 ( alpha, n, n )
  determ1 = moler1_determinant ( alpha, n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  MOLER2
#
  title = 'MOLER2'
  n = 5
  a = moler2 ( )
  determ1 = moler2_determinant ( )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  MOLER3
#
  title = 'MOLER3'
  n = 5
  a = moler3 ( n, n )
  determ1 = moler3_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  MOLER4
#
  title = 'MOLER4'
  n = 4
  a = moler4 ( )
  determ1 = moler4_determinant ( )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  NEUMANN
#
  title = 'NEUMANN'
  row_num = 5
  col_num = 5
  n = row_num * col_num
  a = neumann ( row_num, col_num )
  determ1 = neumann_determinant ( row_num, col_num )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  ONE
#
  title = 'ONE'
  n = 5
  a = one ( n, n )
  determ1 = one_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  ORTEGA
#
  title = 'ORTEGA'
  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  v1, seed = r8vec_uniform_ab ( n, r8_lo, r8_hi, seed )
  v2, seed = r8vec_uniform_ab ( n, r8_lo, r8_hi, seed )
  v3, seed = r8vec_uniform_ab ( n, r8_lo, r8_hi, seed )
  a = ortega ( n, v1, v2, v3 )
  determ1 = ortega_determinant ( n, v1, v2, v3 )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  ORTH_RANDOM
#
  title = 'ORTH_RANDOM'
  n = 5
  key = 123456789
  a = orth_random ( n, key )
  determ1 = orth_random_determinant ( n, key )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  ORTH_SYMM
#
  title = 'ORTH_SYMM'
  n = 5
  a = orth_symm ( n )
  determ1 = orth_symm_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  OTO
#
  title = 'OTO'
  n = 5
  a = oto ( n, n )
  determ1 = oto_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  PARTER
#
  title = 'PARTER'
  n = 5
  a = parter ( n, n )
  determ1 = parter_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  PASCAL1
#
  title = 'PASCAL1'
  n = 5
  a = pascal1 ( n )
  determ1 = pascal1_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  PASCAL2
#
  title = 'PASCAL2'
  n = 5
  a = pascal2 ( n )
  determ1 = pascal2_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  PASCAL3
#
  title = 'PASCAL3'
  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  a = pascal3 ( n, alpha )
  determ1 = pascal3_determinant ( n, alpha )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  PDS_RANDOM
#
  title = 'PDS_RANDOM'
  n = 5
  key = 123456789
  a = pds_random ( n, key )
  determ1 = pds_random_determinant ( n, key )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  PEI
#
  title = 'PEI'
  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  a = pei ( alpha, n )
  determ1 = pei_determinant ( alpha, n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  PERMUTATION_RANDOM
#
  title = 'PERMUTATION_RANDOM'
  n = 5
  key = 123456789
  a = permutation_random ( n, key )
  determ1 = permutation_random_determinant ( n, key )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  PLU
#
  title = 'PLU'
  m = 5
  n = 5
  pivot = np.zeros ( n )
  seed = 123456789
  for i in range ( 0, n ):
    i4_lo = i
    i4_hi = n - 1
    pivot[i], seed = i4_uniform_ab ( i4_lo, i4_hi, seed )
  a = plu ( n, pivot )
  determ1 = plu_determinant ( n, pivot )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  POISSON
#
  title = 'POISSON'
  row_num = 5
  col_num = 5
  n = row_num * col_num
  a = poisson ( row_num, col_num )
  determ1 = poisson_determinant ( row_num, col_num )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  PROLATE
#
  title = 'PROLATE'
  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
# a = prolate ( alpha, n )
# determ2 = np.linalg.det ( a )
# norm_frobenius = r8mat_norm_fro ( n, n, a )
# print '  %-20s  %4d                  %14g  %10.2g' % ( \
#   title, n,          determ2, norm_frobenius )
#
#  RECTANGLE_ADJ
#
  title = 'RECTANGLE_ADJ'
  row_num = 5
  col_num = 5
  n = row_num * col_num
# a = rectangle_adj ( row_num, col_num, n  )
# determ1 = rectangle_adj_determinant ( row_num, col_num )
# determ2 = np.linalg.det ( a )
# norm_frobenius = r8mat_norm_fro ( n, n, a )
# print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
#   title, n, determ1, determ2, norm_frobenius )
#
#  REDHEFFER
#
  title = 'REDHEFFER'
  n = 5
  a = redheffer ( n )
  determ1 = redheffer_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  REF_RANDOM
#
  title = 'REF_RANDOM'
  n = 5
  prob = 0.85
  key = 123456789
# a = ref_random ( n, n, prob, key )
# determ1, seed = ref_random_determinant ( n, prob, key )
# determ2 = np.linalg.det ( a )
# norm_frobenius = r8mat_norm_fro ( n, n, a )
# print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
#   title, n, determ1, determ2, norm_frobenius )
#
#  RIEMANN
#
  title = 'RIEMANN'
  n = 5
# a = riemann ( n, n )
# determ2 = np.linalg.det ( a )
# norm_frobenius = r8mat_norm_fro ( n, n, a )
# print '  %-20s  %4d                  %14g  %10.2g' % ( \
#   title, n,          determ2, norm_frobenius )
#
#  RING_ADJ
#
  for m in range ( 1, 9 ):
    n = m
    title = 'RING_ADJ'
    a = ring_adj ( m, n )
    determ1 = ring_adj_determinant ( n )
    determ2 = np.linalg.det ( a )
    norm_frobenius = r8mat_norm_fro ( m, n, a )
    print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
      title, n, determ1, determ2, norm_frobenius )
#
#  RIS
#
  title = 'RIS'
  n = 5
  a = ris ( n )
  determ1 = ris_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  RODMAN
#
  title = 'RODMAN'
  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  a = rodman ( n, n, alpha )
  determ1 = rodman_determinant ( n, alpha )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  ROSSER1
#
#  Note that while the correct determinant of this matrix is 0,
#  that value is very difficult to calculate correctly.  MATLAB
#  returns np.linalg.det ( A ) = -10611, for instance.
#
  title = 'ROSSER1'
  n = 8
  a = rosser1 ( )
  determ1 = rosser1_determinant ( )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  ROUTH
#
  title = 'ROUTH'
  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( n, r8_lo, r8_hi, seed )
  a = routh ( n, x )
  determ1 = routh_determinant ( n, x )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  RUTIS1
#
  title = 'RUTIS1'
  n = 4
  a = rutis1 ( )
  determ1 = rutis1_determinant ( )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  RUTIS2
#
  title = 'RUTIS2'
  n = 4
  a = rutis2 ( )
  determ1 = rutis2_determinant ( )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  RUTIS3
#
  title = 'RUTIS3'
  n = 4
  a = rutis3 ( )
  determ1 = rutis3_determinant ( )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  RUTIS4
#
  title = 'RUTIS4'
  n = 5
  a = rutis4 ( n )
  determ1 = rutis4_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  RUTIS5
#
  title = 'RUTIS5'
  n = 4
  a = rutis5 ( )
  determ1 = rutis5_determinant ( )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  SCHUR_BLOCK
#
  title = 'SCHUR_BLOCK'
  n = 5
  seed = 123456789
  x_n = ( ( n + 1 ) // 2 )
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( x_n, r8_lo, r8_hi, seed )
  y_n = ( n // 2 )
  y, seed = r8vec_uniform_ab ( y_n, r8_lo, r8_hi, seed )
  a = schur_block ( n, x, y )
  determ1 = schur_block_determinant ( n, x, y )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  SKEW_CIRCULANT
#
  title = 'SKEW_CIRCULANT'
  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( n, r8_lo, r8_hi, seed )
# a = skew_circulant ( n, n, x )
# determ1 = skew_circulant_determinant ( n, x )
# determ2 = np.linalg.det ( a )
# norm_frobenius = r8mat_norm_fro ( n, n, a )
# print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
#   title, n, determ1, determ2, norm_frobenius )
#
#  SMOKE1
#  (complex matrix)
#
  if ( False ):
    title = 'SMOKE1'
    n = 5
#   a = smoke1 ( n )
#   determ1 = smoke1_determinant ( n )
#   determ2 = np.linalg.det ( a )
#   norm_frobenius = r8mat_norm_fro ( n, n, a )
#   print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
#     title, n, determ1, determ2, norm_frobenius )
#
#  SMOKE2
#  (complex matrix)
#
  if ( False ):
    title = 'SMOKE2'
    n = 5
#   a = smoke2 ( n )
#   determ1 = smoke2_determinant ( n )
#   determ2 = np.linalg.det ( a )
#   norm_frobenius = r8mat_norm_fro ( n, n, a )
#   print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
#     title, n, determ1, determ2, norm_frobenius )
#
#  SPLINE
#
  title = 'SPLINE'
  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( n - 1, r8_lo, r8_hi, seed )
  a = spline ( n, x )
  determ1 = spline_determinant ( n, x )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  STIRLING
#
  title = 'STIRLING'
  n = 5
  a = stirling ( n, n )
  determ1 = stirling_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  STRIPE
#
  title = 'STRIPE'
  n = 5
# a = stripe ( n )
# determ2 = np.linalg.det ( a )
# norm_frobenius = r8mat_norm_fro ( n, n, a )
# print '  %-20s  %4d                  %14g  %10.2g' % ( \
#   title, n,           determ2, norm_frobenius )
#
#  SUMMATION
#
  title = 'SUMMATION'
  n = 5
  a = summation ( n, n )
  determ1 = summation_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  SWEET1
#
  title = 'SWEET1'
  n = 6
  a = sweet1 ( )
  determ1 = sweet1_determinant ( )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  SWEET2
#
  title = 'SWEET2'
  n = 6
  a = sweet2 ( )
  determ1 = sweet2_determinant ( )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  SWEET3
#
  title = 'SWEET3'
  n = 6
  a = sweet3 ( )
  determ1 = sweet3_determinant ( )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  SWEET4
#
  title = 'SWEET4'
  n = 13
  a = sweet4 ( )
  determ1 = sweet4_determinant ( )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  SYLVESTER
#
  title = 'SYLVESTER'
  n = 5
  x_n = 3 + 1
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( x_n, r8_lo, r8_hi, seed )
  y_n = 2 + 1
  y, seed = r8vec_uniform_ab ( y_n, r8_lo, r8_hi, seed )
# a = sylvester ( n, x_n - 1, x, y_n - 1, y )
# determ2 = np.linalg.det ( a )
# norm_frobenius = r8mat_norm_fro ( n, n, a )
# print '  %-20s  %4d                  %14g  %10.2g' % ( \
#   title, n,          determ2, norm_frobenius )
#
#  SYLVESTER_KAC
#
  title = 'SYLVESTER_KAC'
  n = 5
  a = sylvester_kac ( n )
  determ1 = sylvester_kac_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  SYLVESTER_KAC
#
  title = 'SYLVESTER_KAC'
  n = 6
  a = sylvester_kac ( n )
  determ1 = sylvester_kac_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  SYMM_RANDOM
#
  title = 'SYMM_RANDOM'
  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  d, seed = r8vec_uniform_ab ( n, r8_lo, r8_hi, seed )
  key = 123456789
  a = symm_random ( n, d, key )
  determ1 = symm_random_determinant ( n, d, key )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  TOEPLITZ
#
  title = 'TOEPLITZ'
  n = 5
  x_n = 2 * n - 1
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( x_n, r8_lo, r8_hi, seed )
# a = toeplitz ( n, x )
# determ2 = np.linalg.det ( a )
# norm_frobenius = r8mat_norm_fro ( n, n, a )
# print '  %-20s  %4d                  %14g  %10.2g' % ( \
#   title, n,          determ2, norm_frobenius )
#
#  TOEPLITZ_5DIAG
#
  title = 'TOEPLITZ_5DIAG'
  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  d1, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  d2, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  d3, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  d4, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  d5, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
# a = toeplitz_5diag ( n, d1, d2, d3, d4, d5 )
# determ2 = np.linalg.det ( a )
# norm_frobenius = r8mat_norm_fro ( n, n, a )
# print '  %-20s  %4d                  %14g  %10.2g' % ( \
#   title, n,          determ2, norm_frobenius )
#
#  TOEPLITZ_5S
#
  title = 'TOEPLITZ_5S'
  row_num = 5
  col_num = 5
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  beta, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  gamma, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  gamma = round ( 50.0 * gamma - 25.0 ) / 5.0
# n, a = toeplitz_5s ( row_num, col_num, alpha, beta, gamma )
# determ2 = np.linalg.det ( a )
# norm_frobenius = r8mat_norm_fro ( n, n, a )
# print '  %-20s  %4d                  %14g  %10.2g' % ( \
#   title, n,          determ2, norm_frobenius )
#
#  TOEPLITZ_PDS
#
  title = 'TOEPLITZ_PDS'
  m = 3
  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( m, r8_lo, r8_hi, seed )
  y, seed = r8vec_uniform_ab ( m, r8_lo, r8_hi, seed )
# y_sum = r8vec_sum ( m, y )
# for i in range ( 0, m ):
#   y[i] = y[i] / y_sum
# a = toeplitz_pds ( m, n, x, y )
# determ2 = np.linalg.det ( a )
# norm_frobenius = r8mat_norm_fro ( n, n, a )
# print '  %-20s  %4d                  %14g  %10.2g' % ( \
#   title, n,          determ2, norm_frobenius )
#
#  TOURNAMENT_RANDOM
#
  title = 'TOURNAMENT_RANDOM'
  n = 5
  key = 123456789
# a = tournament_random ( n, key )
# seed = seed_save
# determ1, seed = tournament_random_determinant ( n, key )
# determ2 = np.linalg.det ( a )
# norm_frobenius = r8mat_norm_fro ( n, n, a )
# print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
#   title, n, determ1, determ2, norm_frobenius )
#
#  TRANSITION_RANDOM
#
  title = 'TRANSITION_RANDOM'
  n = 5
  key = 123456789
# a = transition_random ( n, key )
# determ2 = np.linalg.det ( a )
# norm_frobenius = r8mat_norm_fro ( n, n, a )
# print '  %-20s  %4d                  %14g  %10.2g' % ( \
#   title, n,          determ2, norm_frobenius )
#
#  TRENCH
#
  title = 'TRENCH'
  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
# a = trench ( alpha, n, n )
# determ2 = np.linalg.det ( a )
# norm_frobenius = r8mat_norm_fro ( n, n, a )
# print '  %-20s  %4d                  %14g  %10.2g' % ( \
#   title, n,          determ2, norm_frobenius )
#
#  TRI_UPPER
#
  title = 'TRI_UPPER'
  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  a = tri_upper ( alpha, n )
  determ1 = tri_upper_determinant ( alpha, n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  TRIS
#
  title = 'TRIS'
  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  d1, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  d2, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  d3, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  a = tris ( n, n, d1, d2, d3 )
  determ1 = tris_determinant ( n, d1, d2, d3 )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  TRIV
#
  title = 'TRIV'
  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( n - 1, r8_lo, r8_hi, seed )
  y, seed = r8vec_uniform_ab ( n, r8_lo, r8_hi, seed )
  z, seed = r8vec_uniform_ab ( n - 1, r8_lo, r8_hi, seed )
  a = triv ( n, x, y, z )
  determ1 = triv_determinant ( n, x, y, z )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  TRIW
#
  title = 'TRIW'
  n = 5
  i4_lo = 0
  i4_hi = n - 1
  seed = 123456789
  k, seed = i4_uniform_ab ( i4_lo, i4_hi, seed )
  r8_lo = -5.0
  r8_hi = +5.0
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  a = triw ( alpha, k, n )
  determ1 = triw_determinant ( alpha, k, n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  UPSHIFT
#
  title = 'UPSHIFT'
  n = 5
  a = upshift ( n )
  determ1 = upshift_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  VAND1
#
  title = 'VAND1'
  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( n, r8_lo, r8_hi, seed )
  a = vand1 ( n, x )
  determ1 = vand1_determinant ( n, x )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  VAND2
#
  title = 'VAND2'
  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( n, r8_lo, r8_hi, seed )
  a = vand2 ( n, x )
  determ1 = vand2_determinant ( n, x )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  WATHEN
#
  title = 'WATHEN'
  row_num = 5
  col_num = 5
# n, a = wathen ( row_num, col_num )
# determ2 = np.linalg.det ( a )
# norm_frobenius = r8mat_norm_fro ( n, n, a )
# print '  %-20s  %4d                  %14g  %10.2g' % ( \
#   title, n,          determ2, norm_frobenius )
#
#  WILK03
#
  title = 'WILK03'
  n = 3
  a = wilk03 ( )
  determ1 = wilk03_determinant ( )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  WILK04
#
  title = 'WILK04'
  n = 4
  a = wilk04 ( )
  determ1 = wilk04_determinant ( )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  WILK05
#
  title = 'WILK05'
  n = 5
  a = wilk05 ( )
  determ1 = wilk05_determinant ( )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  WILK12
#
  title = 'WILK12'
  n = 12
  a = wilk12 ( )
  determ1 = wilk12_determinant ( )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  WILK20
#
  title = 'WILK20'
  n = 20
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
# a = wilk20 ( alpha )
# determ2 = np.linalg.det ( a )
# norm_frobenius = r8mat_norm_fro ( n, n, a )
# print '  %-20s  %4d                  %14g  %10.2g' % ( \
#   title, n,          determ2, norm_frobenius )
#
#  WILK21
#
  title = 'WILK21'
  n = 21
  a = wilk21 ( n )
  determ1 = wilk21_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  WILSON
#
  title = 'WILSON'
  n = 4
  a = wilson ( )
  determ1 = wilson_determinant ( )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  ZERO
#
  title = 'ZERO'
  n = 5
  a = zero ( n, n )
  determ1 = zero_determinant ( n )
  determ2 = np.linalg.det ( a )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %14g  %14g  %10.2g' % ( \
    title, n, determ1, determ2, norm_frobenius )
#
#  ZIELKE
#
  title = 'ZIELKE'
  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  d1, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  d2, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  d3, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
# a = zielke ( n, d1, d2, d3 )
# determ2 = np.linalg.det ( a )
# norm_frobenius = r8mat_norm_fro ( n, n, a )
# print '  %-20s  %4d                  %14g  %10.2g' % ( \
#   title, n,          determ2, norm_frobenius )
#
#  Terminate.
#
  print ''
  print 'TEST_DETERMINANT'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  test_determinant ( )
  timestamp ( )
