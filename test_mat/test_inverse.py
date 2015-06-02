#!/usr/bin/env python
#
def test_inverse ( ):

#*****************************************************************************80
#
## TEST_INVERSE tests the inverse computations.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 April 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  from aegerter            import aegerter
  from aegerter            import aegerter_inverse
  from bab                 import bab
  from bab                 import bab_inverse
  from bauer               import bauer
  from bauer               import bauer_inverse
  from bernstein           import bernstein
  from bernstein           import bernstein_inverse
  from bis                 import bis
  from bis                 import bis_inverse
  from biw                 import biw
  from biw                 import biw_inverse
  from bodewig             import bodewig
  from bodewig             import bodewig_inverse
  from boothroyd           import boothroyd
  from boothroyd           import boothroyd_inverse
  from borderband          import borderband
  from borderband          import borderband_inverse
  from carry               import carry
  from carry               import carry_inverse
  from cauchy              import cauchy
  from cauchy              import cauchy_inverse
  from cheby_t             import cheby_t
  from cheby_t             import cheby_t_inverse
  from cheby_u             import cheby_u
  from cheby_u             import cheby_u_inverse
  from cheby_van2          import cheby_van2
  from cheby_van2          import cheby_van2_inverse
  from cheby_van3          import cheby_van3
  from cheby_van3          import cheby_van3_inverse
  from chow                import chow
  from chow                import chow_inverse
  from clement1            import clement1
  from clement1            import clement1_inverse
  from clement2            import clement2
  from clement2            import clement2_inverse
  from combin              import combin
  from combin              import combin_inverse
  from companion           import companion
  from companion           import companion_inverse
  from complex_i           import complex_i
  from complex_i           import complex_i_inverse
  from conex1              import conex1
  from conex1              import conex1_inverse
  from conex2              import conex2
  from conex2              import conex2_inverse
  from conex3              import conex3
  from conex3              import conex3_inverse
  from conex4              import conex4
  from conex4              import conex4_inverse
  from conference          import conference
  from conference          import conference_inverse
  from daub2               import daub2
  from daub2               import daub2_inverse
  from daub4               import daub4
  from daub4               import daub4_inverse
  from daub6               import daub6
  from daub6               import daub6_inverse
  from daub8               import daub8
  from daub8               import daub8_inverse
  from daub10              import daub10
  from daub10              import daub10_inverse
  from daub12              import daub12
  from daub12              import daub12_inverse
  from diagonal            import diagonal
  from diagonal            import diagonal_inverse
  from dif1                import dif1
  from dif1                import dif1_inverse
  from dif2                import dif2
  from dif2                import dif2_inverse
  from dorr                import dorr
  from dorr                import dorr_inverse
  from downshift           import downshift
  from downshift           import downshift_inverse
  from eulerian            import eulerian
  from eulerian            import eulerian_inverse
  from exchange            import exchange
  from exchange            import exchange_inverse
  from fibonacci2          import fibonacci2
  from fibonacci2          import fibonacci2_inverse
  from fibonacci3          import fibonacci3
  from fibonacci3          import fibonacci3_inverse
  from fiedler             import fiedler
  from fiedler             import fiedler_inverse
  from forsythe            import forsythe
  from forsythe            import forsythe_inverse
  from fourier_cosine      import fourier_cosine
  from fourier_cosine      import fourier_cosine_inverse
  from fourier_sine        import fourier_sine
  from fourier_sine        import fourier_sine_inverse
  from frank               import frank
  from frank               import frank_inverse
  from gfpp                import gfpp
  from gfpp                import gfpp_inverse
  from givens              import givens
  from givens              import givens_inverse
  from gk316               import gk316
  from gk316               import gk316_inverse
  from gk323               import gk323
  from gk323               import gk323_inverse
  from gk324               import gk324
  from gk324               import gk324_inverse
  from hankel_n            import hankel_n
  from hankel_n            import hankel_n_inverse
  from hanowa              import hanowa
  from hanowa              import hanowa_inverse
  from harman              import harman
  from harman              import harman_inverse
  from hartley             import hartley
  from hartley             import hartley_inverse
  from helmert             import helmert
  from helmert             import helmert_inverse
  from helmert2            import helmert2
  from helmert2            import helmert2_inverse
  from hermite             import hermite
  from hermite             import hermite_inverse
  from herndon             import herndon
  from herndon             import herndon_inverse
  from hilbert             import hilbert
  from hilbert             import hilbert_inverse
  from householder         import householder
  from householder         import householder_inverse
  from identity            import identity
  from identity            import identity_inverse
  from i4_uniform_ab       import i4_uniform_ab
  from ill3                import ill3
  from ill3                import ill3_inverse
  from integration         import integration
  from integration         import integration_inverse
  from invol               import invol
  from invol               import invol_inverse
  from jacobi              import jacobi
  from jacobi              import jacobi_inverse
  from jordan              import jordan
  from jordan              import jordan_inverse
  from kahan               import kahan
  from kahan               import kahan_inverse
  from kershaw             import kershaw
  from kershaw             import kershaw_inverse
  from kershawtri          import kershawtri
  from kershawtri          import kershawtri_inverse
  from kms                 import kms
  from kms                 import kms_inverse
  from laguerre            import laguerre
  from laguerre            import laguerre_inverse
  from legendre            import legendre
  from legendre            import legendre_inverse
  from lehmer              import lehmer
  from lehmer              import lehmer_inverse
  from lesp                import lesp
  from lesp                import lesp_inverse
  from lietzke             import lietzke
  from lietzke             import lietzke_inverse
  from line_adj            import line_adj
  from line_adj            import line_adj_inverse
  from lotkin              import lotkin
  from lotkin              import lotkin_inverse
  from maxij               import maxij
  from maxij               import maxij_inverse
  from milnes              import milnes
  from milnes              import milnes_inverse
  from minij               import minij
  from minij               import minij_inverse
  from moler1              import moler1
  from moler1              import moler1_inverse
  from moler3              import moler3
  from moler3              import moler3_inverse
  from ortega              import ortega
  from ortega              import ortega_inverse
  from orth_symm           import orth_symm
  from orth_symm           import orth_symm_inverse
  from oto                 import oto
  from oto                 import oto_inverse
  from parter              import parter
  from parter              import parter_inverse
  from pascal1             import pascal1
  from pascal1             import pascal1_inverse
  from pascal2             import pascal2
  from pascal2             import pascal2_inverse
  from pascal3             import pascal3
  from pascal3             import pascal3_inverse
  from pds_random          import pds_random
  from pds_random          import pds_random_inverse
  from pei                 import pei
  from pei                 import pei_inverse
  from permutation_random  import permutation_random
  from permutation_random  import permutation_random_inverse
  from plu                 import plu
  from plu                 import plu_inverse
  from r8_uniform_ab       import r8_uniform_ab
  from r8mat_is_inverse    import r8mat_is_inverse
  from r8mat_norm_fro      import r8mat_norm_fro
  from r8vec_uniform_ab    import r8vec_uniform_ab
  from ris                 import ris
  from ris                 import ris_inverse
  from rodman              import rodman
  from rodman              import rodman_inverse
  from rutis1              import rutis1
  from rutis1              import rutis1_inverse
  from rutis2              import rutis2
  from rutis2              import rutis2_inverse
  from rutis3              import rutis3
  from rutis3              import rutis3_inverse
  from rutis4              import rutis4
  from rutis4              import rutis4_inverse
  from rutis5              import rutis5
  from rutis5              import rutis5_inverse
  from schur_block         import schur_block
  from schur_block         import schur_block_inverse
  from spline              import spline
  from spline              import spline_inverse
  from stirling            import stirling
  from stirling            import stirling_inverse
  from summation           import summation
  from summation           import summation_inverse
  from sweet1              import sweet1
  from sweet1              import sweet1_inverse
  from sweet2              import sweet2
  from sweet2              import sweet2_inverse
  from sweet3              import sweet3
  from sweet3              import sweet3_inverse
  from sweet4              import sweet4
  from sweet4              import sweet4_inverse
  from sylvester_kac       import sylvester_kac
  from sylvester_kac       import sylvester_kac_inverse
  from symm_random         import symm_random
  from symm_random         import symm_random_inverse
  from tri_upper           import tri_upper
  from tri_upper           import tri_upper_inverse
  from tris                import tris
  from tris                import tris_inverse
  from triv                import triv
  from triv                import triv_inverse
  from triw                import triw
  from triw                import triw_inverse
  from upshift             import upshift
  from upshift             import upshift_inverse
  from vand1               import vand1
  from vand1               import vand1_inverse
  from vand2               import vand2
  from vand2               import vand2_inverse
  from wilk03              import wilk03
  from wilk03              import wilk03_inverse
  from wilk04              import wilk04
  from wilk04              import wilk04_inverse
  from wilk05              import wilk05
  from wilk05              import wilk05_inverse
  from wilk21              import wilk21
  from wilk21              import wilk21_inverse
  from wilson              import wilson
  from wilson              import wilson_inverse

  print ''
  print 'TEST_INVERSE'
  print '  A = a test matrix of order N'
  print '  B = inverse as computed by a routine.'
  print '  C = inverse as computed by the numpy.linalg.inv() function.'
  print ''
  print '  ||A||    = Frobenius norm of A.'
  print '  ||C||    = Frobenius norm of C.'
  print '  ||I-AC|| = Frobenius norm of I-A*C.'
  print '  ||I-AB|| = Frobenius norm of I-A*B.'
  print ''
  print '  Title                    N      ',
  print '||A||      ||C||      ||I-AC||    ||I-AB||'
  print ''
#
#  AEGERTER
#
  title = 'AEGERTER'
  n = 5
  a = aegerter ( n )
  b = aegerter_inverse ( n )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
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
  b = bab_inverse ( n, alpha, beta )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  BAUER
#
  title = 'BAUER'
  n = 6
  a = bauer ( )
  b = bauer_inverse ( )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  BERNSTEIN
#
  title = 'BERNSTEIN'
  n = 5
  a = bernstein ( n )
  b = bernstein_inverse ( n )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
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
  b = bis_inverse ( alpha, beta, n )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  BIW
#
  title = 'BIW'
  n = 5
  a = biw ( n )
  b = biw_inverse ( n )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  BODEWIG
#
  title = 'BODEWIG'
  n = 4
  a = bodewig ( )
  b = bodewig_inverse ( )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  BOOTHROYD
#
  title = 'BOOTHROYD'
  n = 5
  a = boothroyd ( n )
  b = boothroyd_inverse ( n )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  BORDERBAND
#
  title = 'BORDERBAND'
  n = 5
  a = borderband ( n )
  b = borderband_inverse ( n )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
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
  b = carry_inverse ( n, k )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
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
  b = cauchy_inverse ( n, x, y )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  CHEBY_T
#
  title = 'CHEBY_T'
  n = 5
  a = cheby_t ( n )
  b = cheby_t_inverse ( n )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  CHEBY_U
#
  title = 'CHEBY_U'
  n = 5
  a = cheby_u ( n )
  b = cheby_u_inverse ( n )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  CHEBY_VAN2
#
  title = 'CHEBY_VAN2'
  n = 5
  a = cheby_van2 ( n )
  b = cheby_van2_inverse ( n )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  CHEBY_VAN3
#
  title = 'CHEBY_VAN3'
  n = 5
  a = cheby_van3 ( n )
  b = cheby_van3_inverse ( n )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
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
  b = chow_inverse ( alpha, beta, n )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  CIRCULANT
#  Requires complex arithmetic.  Not now!
#
  title = 'CIRCULANT'
  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( n, r8_lo, r8_hi, seed )
# a = circulant ( n, n, x )
# b = circulant_inverse ( n, x )
# c = np.linalg.inv ( a )
# error_ab = r8mat_is_inverse ( n, a, b )
# error_ac = r8mat_is_inverse ( n, a, c )
# norma_frobenius = r8mat_norm_fro ( n, n, a )
# normc_frobenius = r8mat_norm_fro ( n, n, c )
# print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
#   % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  CIRCULANT2
#  Requires complex arithmetic.  Not now!
#
  title = 'CIRCULANT2'
  n = 5
# a = circulant2 ( n )
# b = circulant2_inverse ( n )
# c = np.linalg.inv ( a )
# error_ab = r8mat_is_inverse ( n, a, b )
# error_ac = r8mat_is_inverse ( n, a, c )
# norma_frobenius = r8mat_norm_fro ( n, n, a )
# normc_frobenius = r8mat_norm_fro ( n, n, c )
# print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
#   % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  CLEMENT1
#  N must be even.
#
  title = 'CLEMENT1'
  n = 6
  a = clement1 ( n )
  b = clement1_inverse ( n )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  CLEMENT2
#  N must be even.
#
  title = 'CLEMENT2'
  n = 6
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( n - 1, r8_lo, r8_hi, seed )
  y, seed = r8vec_uniform_ab ( n - 1, r8_lo, r8_hi, seed )
  a = clement2 ( n, x, y )
  b = clement2_inverse ( n, x, y )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
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
  b = combin_inverse ( alpha, beta, n )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
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
  b = companion_inverse ( n, x )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  COMPLEX_I
#
  title = 'COMPLEX_I'
  n = 2
  a = complex_i ( )
  b = complex_i_inverse ( )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
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
  b = conex1_inverse ( alpha )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
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
  b = conex2_inverse ( alpha )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  CONEX3
#
  title = 'CONEX3'
  n = 5
  a = conex3 ( n )
  b = conex3_inverse ( n )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  CONEX4
#
  title = 'CONEX4'
  n = 4
  a = conex4 ( )
  b = conex4_inverse ( )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  CONFERENCE
#  N-1 must be an odd prime, or a power of an odd prime.
#
  title = 'CONFERENCE'
  n = 6
  a = conference ( n )
  b = conference_inverse ( n )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  DAUB2
#
  title = 'DAUB2'
  n = 4
  a = daub2 ( n )
  b = daub2_inverse ( n )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  DAUB4
#
  title = 'DAUB4'
  n = 8
  a = daub4 ( n )
  b = daub4_inverse ( n )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  DAUB6
#
  title = 'DAUB6'
  n = 12
  a = daub6 ( n )
  b = daub6_inverse ( n )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  DAUB8
#
  title = 'DAUB8'
  n = 16
  a = daub8 ( n )
  b = daub8_inverse ( n )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  DAUB10
#
  title = 'DAUB10'
  n = 20
  a = daub10 ( n )
  b = daub10_inverse ( n )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  DAUB12
#
  title = 'DAUB12'
  n = 24
  a = daub12 ( n )
  b = daub12_inverse ( n )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
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
  b = diagonal_inverse ( n, x )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  DIF1
#  N must be even.
#
  title = 'DIF1'
  n = 6
  a = dif1 ( n, n )
  b = dif1_inverse ( n )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  DIF2
#
  title = 'DIF2'
  n = 5
  a = dif2 ( n, n )
  b = dif2_inverse ( n )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
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
  b = dorr_inverse ( alpha, n )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  DOWNSHIFT
#
  title = 'DOWNSHIFT'
  n = 5
  a = downshift ( n )
  b = downshift_inverse ( n )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  EULERIAN
#
  title = 'EULERIAN'
  n = 5
  a = eulerian ( n, n )
  b = eulerian_inverse ( n )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  EXCHANGE
#
  title = 'EXCHANGE'
  n = 5
  a = exchange ( n, n )
  b = exchange_inverse ( n )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  FIBONACCI2
#
  title = 'FIBONACCI2'
  n = 5
  a = fibonacci2 ( n )
  b = fibonacci2_inverse ( n )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  FIBONACCI3
#
  title = 'FIBONACCI3'
  n = 5
  a = fibonacci3 ( n )
  b = fibonacci3_inverse ( n )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  FIEDLER.
#  The FIEDLER_INVERSE routine assumes the X vector is sorted.
#
  title = 'FIEDLER'
  n = 7
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( n, r8_lo, r8_hi, seed )
  x = np.sort ( x )
  a = fiedler ( n, n, x )
  b = fiedler_inverse ( n, x )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
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
  b = forsythe_inverse ( alpha, beta, n )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  FOURIER_COSINE
#
  title = 'FOURIER_COSINE'
  n = 5
  a = fourier_cosine ( n )
  b = fourier_cosine_inverse ( n )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  FOURIER_SINE
#
  title = 'FOURIER_SINE'
  n = 5
  a = fourier_sine ( n )
  b = fourier_sine_inverse ( n )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  FRANK
#
  title = 'FRANK'
  n = 5
  a = frank ( n )
  b = frank_inverse ( n )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
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
  b = gfpp_inverse ( n, alpha )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  GIVENS
#
  title = 'GIVENS'
  n = 5
  a = givens ( n, n )
  b = givens_inverse ( n )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  GK316
#
  title = 'GK316'
  n = 5
  a = gk316 ( n )
  b = gk316_inverse ( n )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  GK323
#
  title = 'GK323'
  n = 5
  a = gk323 ( n, n )
  b = gk323_inverse ( n )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
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
  b = gk324_inverse ( n, x )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  HANKEL_N
#
  title = 'HANKEL_N'
  n = 5
  a = hankel_n ( n )
  b = hankel_n_inverse ( n )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  HANOWA
#  N must be even.
#
  title = 'HANOWA'
  n = 6
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  a = hanowa ( alpha, n )
  b = hanowa_inverse ( alpha, n )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  HARMAN
#
  title = 'HARMAN'
  n = 8
  a = harman ( )
  b = harman_inverse ( )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  HARTLEY
#
  title = 'HARTLEY'
  n = 5 
  a = hartley ( n )
  b = hartley_inverse ( n )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  HELMERT
#
  title = 'HELMERT'
  n = 5 
  a = helmert ( n )
  b = helmert_inverse ( n )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  HELMERT2
#
  title = 'HELMERT2'
  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( n, r8_lo, r8_hi, seed )
  a = helmert2 ( n, x )
  b = helmert2_inverse ( n, x )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  HERMITE
#
  title = 'HERMITE'
  n = 5 
  a = hermite ( n )
  b = hermite_inverse ( n )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  HERNDON
#
  title = 'HERNDON'
  n = 5 
  a = herndon ( n )
  b = herndon_inverse ( n )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  HILBERT
#
  title = 'HILBERT'
  n = 5 
  a = hilbert ( n, n )
  b = hilbert_inverse ( n )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
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
  b = householder_inverse ( n, x )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  IDENTITY
#
  title = 'IDENTITY'
  n = 5
  a = identity ( n, n )
  b = identity_inverse ( n )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  ILL3
#
  title = 'ILL3'
  n = 3
  a = ill3 ( )
  b = ill3_inverse ( )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
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
  b = integration_inverse ( alpha, n )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  INVOL
#
  title = 'INVOL'
  n = 5
  a = invol ( n )
  b = invol_inverse ( n )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  JACOBI
#  N must be even.
#
  title = 'JACOBI'
  n = 6
  a = jacobi ( n, n )
  b = jacobi_inverse ( n )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
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
  b = jordan_inverse ( n, alpha )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
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
  b = kahan_inverse ( alpha, n )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  KERSHAW
#
  title = 'KERSHAW'
  n = 4
  a = kershaw ( )
  b = kershaw_inverse ( )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
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
  b = kershawtri_inverse ( n, x )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
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
  b = kms_inverse ( alpha, n )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  LAGUERRE
#
  title = 'LAGUERRE'
  n = 5
  a = laguerre ( n )
  b = laguerre_inverse ( n )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  LEGENDRE
#
  title = 'LEGENDRE'
  n = 5
  a = legendre ( n )
  b = legendre_inverse ( n )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  LEHMER
#
  title = 'LEHMER'
  n = 5
  a = lehmer ( n, n )
  b = lehmer_inverse ( n )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  LESP
#
  title = 'LESP'
  n = 5
  a = lesp ( n, n )
  b = lesp_inverse ( n )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  LIETZKE
#
  title = 'LIETZKE'
  n = 5
  a = lietzke ( n )
  b = lietzke_inverse ( n )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  LINE_ADJ
#  N must be even.
#
  title = 'LINE_ADJ'
  n = 6
  a = line_adj ( n )
  b = line_adj_inverse ( n )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  LOTKIN
#
  title = 'LOTKIN'
  n = 5
  a = lotkin ( n, n )
  b = lotkin_inverse ( n )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  MAXIJ
#
  title = 'MAXIJ'
  n = 5
  a = maxij ( n, n )
  b = maxij_inverse ( n )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
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
  b = milnes_inverse ( n, x )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  MINIJ
#
  title = 'MINIJ'
  n = 5
  a = minij ( n, n )
  b = minij_inverse ( n )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
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
  b = moler1_inverse ( alpha, n )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  MOLER3
#
  title = 'MOLER3'
  n = 5
  a = moler3 ( n, n )
  b = moler3_inverse ( n )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
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
  b = ortega_inverse ( n, v1, v2, v3 )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  ORTH_SYMM
#
  title = 'ORTH_SYMM'
  n = 5
  a = orth_symm ( n )
  b = orth_symm_inverse ( n )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  OTO
#
  title = 'OTO'
  n = 5
  a = oto ( n, n )
  b = oto_inverse ( n )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  PARTER
#
  title = 'PARTER'
  n = 5
  a = parter ( n, n )
  b = parter_inverse ( n )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  PASCAL1
#
  title = 'PASCAL1'
  n = 5
  a = pascal1 ( n )
  b = pascal1_inverse ( n )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  PASCAL2
#
  title = 'PASCAL2'
  n = 5
  a = pascal2 ( n )
  b = pascal2_inverse ( n )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
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
  b = pascal3_inverse ( n, alpha )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  PDS_RANDOM
#
  title = 'PDS_RANDOM'
  n = 5
  key = 123456789
  a = pds_random ( n, key )
  b = pds_random_inverse ( n, key )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
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
  b = pei_inverse ( alpha, n )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  PERMUTATION_RANDOM
#
  title = 'PERMUTATION_RANDOM'
  n = 5
  key = 123456789
  a = permutation_random ( n, key )
  b = permutation_random_inverse ( n, key )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  PLU
#
  title = 'PLU'
  n = 5
  pivot = np.zeros ( n )
  seed = 123456789
  for i in range ( 0, n ):
    i4_lo = i
    i4_hi = n - 1
    pivot[i], seed = i4_uniform_ab ( i4_lo, i4_hi, seed )
  a = plu ( n, pivot )
  b = plu_inverse ( n, pivot )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  RIS
#
  title = 'RIS'
  n = 5
  a = ris ( n )
  b = ris_inverse ( n )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
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
  b = rodman_inverse ( n, alpha )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  RUTIS1
#
  title = 'RUTIS1'
  n = 4
  a = rutis1 ( )
  b = rutis1_inverse ( )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  RUTIS2
#
  title = 'RUTIS2'
  n = 4
  a = rutis2 ( )
  b = rutis2_inverse ( )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  RUTIS3
#
  title = 'RUTIS3'
  n = 4
  a = rutis3 ( )
  b = rutis3_inverse ( )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  RUTIS4
#
  title = 'RUTIS4'
  n = 4
  a = rutis4 ( n )
  b = rutis4_inverse ( n )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  RUTIS5
#
  title = 'RUTIS5'
  n = 4
  a = rutis5 ( )
  b = rutis5_inverse ( )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  SCHUR_BLOCK
#
  title = 'SCHUR_BLOCK'
  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  x_n = ( ( n + 1 ) // 2 )
  x, seed = r8vec_uniform_ab ( x_n, r8_lo, r8_hi, seed )
  y_n = ( n // 2 )
  y, seed = r8vec_uniform_ab ( y_n, r8_lo, r8_hi, seed )
  a = schur_block ( n, x, y )
  b = schur_block_inverse ( n, x, y )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
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
  b = spline_inverse ( n, x )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  STIRLING
#
  title = 'STIRLING'
  n = 5
  a = stirling ( n, n )
  b = stirling_inverse ( n )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  SUMMATION
#
  title = 'SUMMATION'
  n = 5
  a = summation ( n, n )
  b = summation_inverse ( n )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  SWEET1
#
  title = 'SWEET1'
  n = 6
  a = sweet1 ( )
  b = sweet1_inverse ( )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  SWEET2
#
  title = 'SWEET2'
  n = 6
  a = sweet2 ( )
  b = sweet2_inverse ( )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  SWEET3
#
  title = 'SWEET3'
  n = 6
  a = sweet3 ( )
  b = sweet3_inverse ( )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  SWEET4
#
  title = 'SWEET4'
  n = 13
  a = sweet4 ( )
  b = sweet4_inverse ( )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  SYLVESTER_KAC
#  N must be even.
#
  title = 'SYLVESTER_KAC'
  n = 6
  a = sylvester_kac ( n )
  b = sylvester_kac_inverse ( n )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  SYMM_RANDOM
#
  title = 'SYMM_RANDOM'
  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( n, r8_lo, r8_hi, seed )
  key = 123456789
  a = symm_random ( n, x, key )
  b = symm_random_inverse ( n, x, key )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
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
  b = tri_upper_inverse ( alpha, n )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  TRIS
#
  title = 'TRIS'
  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  beta, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  gamma, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  a = tris ( n, n, alpha, beta, gamma )
  b = tris_inverse ( n, alpha, beta, gamma )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
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
  b = triv_inverse ( n, x, y, z )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  TRIW
#
  title = 'TRIW'
  n = 5
  i4_lo = 0
  i4_hi = n - 1
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  k, seed = i4_uniform_ab ( i4_lo, i4_hi, seed )
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  a = triw ( alpha, k, n )
  b = triw_inverse ( alpha, k, n )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  UNITARY_RANDOM
#
  title = 'UNITARY_RANDOM'
  n = 5
  key = 123456789
# a = unitary_random ( n, key )
# b = unitary_random_inverse ( n, key )
# c = np.linalg.inv ( a )
# error_ab = c8mat_is_inverse ( n, a, b )
# error_ac = c8mat_is_inverse ( n, a, c )
# norma_frobenius = c8mat_norm_fro ( n, n, a )
# normc_frobenius = c8mat_norm_fro ( n, n, c )
# print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
#   % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  UPSHIFT
#
  title = 'UPSHIFT'
  n = 5
  a = upshift ( n )
  b = upshift_inverse ( n )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
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
  b = vand1_inverse ( n, x )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
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
  b = vand2_inverse ( n, x )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  WILK03
#
  title = 'WILK03'
  n = 3
  a = wilk03 ( )
  b = wilk03_inverse ( )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  WILK04
#
  title = 'WILK04'
  n = 4
  a = wilk04 ( )
  b = wilk04_inverse ( )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  WILK05
#
  title = 'WILK05'
  n = 5
  a = wilk05 ( )
  b = wilk05_inverse ( )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  WILK21
#
  title = 'WILK21'
  n = 21
  a = wilk21 ( n )
  b = wilk21_inverse ( n )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  WILSON
#
  title = 'WILSON'
  n = 4
  a = wilson ( )
  b = wilson_inverse ( )
  c = np.linalg.inv ( a )
  error_ab = r8mat_is_inverse ( n, a, b )
  error_ac = r8mat_is_inverse ( n, a, c )
  norma_frobenius = r8mat_norm_fro ( n, n, a )
  normc_frobenius = r8mat_norm_fro ( n, n, c )
  print '  %-20s  %4d  %10.2g  %10.2g  %10.2g  %10.2g' \
    % ( title, n, norma_frobenius, normc_frobenius, error_ac, error_ab )
#
#  Terminate.
#
  print ''
  print 'TEST_INVERSE:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  test_inverse ( )
  timestamp ( )
