#! /usr/bin/env python

def test_condition ( ):

#*****************************************************************************80
#
## TEST_CONDITION tests the L1 condition number computations.
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
  from aegerter             import aegerter
  from aegerter             import aegerter_condition
  from aegerter             import aegerter_inverse
  from bab                  import bab
  from bab                  import bab_condition
  from bab                  import bab_inverse
  from bauer                import bauer
  from bauer                import bauer_condition
  from bauer                import bauer_inverse
  from bis                  import bis
  from bis                  import bis_condition
  from bis                  import bis_inverse
  from biw                  import biw
  from biw                  import biw_condition
  from biw                  import biw_inverse
  from bodewig              import bodewig
  from bodewig              import bodewig_condition
  from bodewig              import bodewig_inverse
  from boothroyd            import boothroyd
  from boothroyd            import boothroyd_condition
  from boothroyd            import boothroyd_inverse
  from combin               import combin
  from combin               import combin_condition
  from combin               import combin_inverse
  from companion            import companion
  from companion            import companion_condition
  from companion            import companion_inverse
  from conex1               import conex1
  from conex1               import conex1_condition
  from conex1               import conex1_inverse
  from conex2               import conex2
  from conex2               import conex2_condition
  from conex2               import conex2_inverse
  from conex3               import conex3
  from conex3               import conex3_condition
  from conex3               import conex3_inverse
  from conex4               import conex4
  from conex4               import conex4_condition
  from conex4               import conex4_inverse
  from daub2                import daub2
  from daub2                import daub2_condition
  from daub2                import daub2_inverse
  from daub4                import daub4
  from daub4                import daub4_condition
  from daub4                import daub4_inverse
  from daub6                import daub6
  from daub6                import daub6_condition
  from daub6                import daub6_inverse
  from daub8                import daub8
  from daub8                import daub8_condition
  from daub8                import daub8_inverse
  from daub10               import daub10
  from daub10               import daub10_condition
  from daub10               import daub10_inverse
  from daub12               import daub12
  from daub12               import daub12_condition
  from daub12               import daub12_inverse
  from diagonal             import diagonal
  from diagonal             import diagonal_condition
  from diagonal             import diagonal_inverse
  from dif2                 import dif2
  from dif2                 import dif2_condition
  from dif2                 import dif2_inverse
  from downshift            import downshift
  from downshift            import downshift_condition
  from downshift            import downshift_inverse
  from exchange             import exchange
  from exchange             import exchange_condition
  from exchange             import exchange_inverse
  from fibonacci2           import fibonacci2
  from fibonacci2           import fibonacci2_condition
  from fibonacci2           import fibonacci2_inverse
  from gfpp                 import gfpp
  from gfpp                 import gfpp_condition
  from gfpp                 import gfpp_inverse
  from givens               import givens
  from givens               import givens_condition
  from givens               import givens_inverse
  from hankel_n             import hankel_n
  from hankel_n             import hankel_n_condition
  from hankel_n             import hankel_n_inverse
  from harman               import harman
  from harman               import harman_condition
  from harman               import harman_inverse
  from hartley              import hartley
  from hartley              import hartley_condition
  from hartley              import hartley_inverse
  from identity             import identity
  from identity             import identity_condition
  from identity             import identity_inverse
  from ill3                 import ill3
  from ill3                 import ill3_condition
  from ill3                 import ill3_inverse
  from jordan               import jordan
  from jordan               import jordan_condition
  from jordan               import jordan_inverse
  from kershaw              import kershaw
  from kershaw              import kershaw_condition
  from kershaw              import kershaw_inverse
  from lietzke              import lietzke
  from lietzke              import lietzke_condition
  from lietzke              import lietzke_inverse
  from maxij                import maxij
  from maxij                import maxij_condition
  from maxij                import maxij_inverse
  from minij                import minij
  from minij                import minij_condition
  from minij                import minij_inverse
  from orth_symm            import orth_symm
  from orth_symm            import orth_symm_condition
  from orth_symm            import orth_symm_inverse
  from oto                  import oto
  from oto                  import oto_condition
  from oto                  import oto_inverse
  from pascal1              import pascal1
  from pascal1              import pascal1_condition
  from pascal1              import pascal1_inverse
  from pascal3              import pascal3
  from pascal3              import pascal3_condition
  from pascal3              import pascal3_inverse
  from pei                  import pei
  from pei                  import pei_condition
  from pei                  import pei_inverse
  from r8_uniform_ab        import r8_uniform_ab
  from r8mat_norm_l1        import r8mat_norm_l1
  from r8vec_uniform_ab     import r8vec_uniform_ab
  from rodman               import rodman
  from rodman               import rodman_condition
  from rodman               import rodman_inverse
  from rutis1               import rutis1
  from rutis1               import rutis1_condition
  from rutis1               import rutis1_inverse
  from rutis2               import rutis2
  from rutis2               import rutis2_condition
  from rutis2               import rutis2_inverse
  from rutis3               import rutis3
  from rutis3               import rutis3_condition
  from rutis3               import rutis3_inverse
  from rutis5               import rutis5
  from rutis5               import rutis5_condition
  from rutis5               import rutis5_inverse
  from summation            import summation
  from summation            import summation_condition
  from summation            import summation_inverse
  from sweet1               import sweet1
  from sweet1               import sweet1_condition
  from sweet1               import sweet1_inverse
  from sweet2               import sweet2
  from sweet2               import sweet2_condition
  from sweet2               import sweet2_inverse
  from sweet3               import sweet3
  from sweet3               import sweet3_condition
  from sweet3               import sweet3_inverse
  from sweet4               import sweet4
  from sweet4               import sweet4_condition
  from sweet4               import sweet4_inverse
  from tri_upper            import tri_upper
  from tri_upper            import tri_upper_condition
  from tri_upper            import tri_upper_inverse
  from upshift              import upshift
  from upshift              import upshift_condition
  from upshift              import upshift_inverse
  from wilk03               import wilk03
  from wilk03               import wilk03_condition
  from wilk03               import wilk03_inverse
  from wilk04               import wilk04
  from wilk04               import wilk04_condition
  from wilk04               import wilk04_inverse
  from wilk05               import wilk05
  from wilk05               import wilk05_condition
  from wilk05               import wilk05_inverse
  from wilson               import wilson
  from wilson               import wilson_condition
  from wilson               import wilson_inverse

  print ''
  print 'TEST_CONDITION'
  print '  Compute the L1 condition number of an example of each'
  print '  test matrix'
  print ''
  print '  Title                    N            COND            COND'
  print ''
#
#  AEGERTER
#
  title = 'AEGERTER'
  n = 5
  cond1 = aegerter_condition ( n )

  a = aegerter ( n )
  b = aegerter_inverse ( n )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 )
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
  cond1 = bab_condition ( n, alpha, beta )

  a = bab ( n, alpha, beta )
  b = bab_inverse ( n, alpha, beta )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 )
#
#  BAUER
#
  title = 'BAUER'
  n = 6
  cond1 = bauer_condition ( )

  a = bauer ( )
  b = bauer_inverse ( )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 )
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
  cond1 = bis_condition ( alpha, beta, n )

  a = bis ( alpha, beta, n, n )
  b = bis_inverse ( alpha, beta, n )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 )
#
#  BIW
#
  title = 'BIW'
  n = 5
  cond1 = biw_condition ( n )

  a = biw ( n )
  b = biw_inverse ( n )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 )
#
#  BODEWIG
#
  title = 'BODEWIG'
  n = 4
  cond1 = bodewig_condition ( )

  a = bodewig ( )
  b = bodewig_inverse ( )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 )
#
#  BOOTHROYD
#
  title = 'BOOTHROYD'
  n = 5
  cond1 = boothroyd_condition ( n )

  a = boothroyd ( n )
  b = boothroyd_inverse ( n )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 )
#
#  COMBIN
#
  title = 'COMBIN'
  n = 3
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  beta, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  cond1 = combin_condition ( alpha, beta, n )

  a = combin ( alpha, beta, n )
  b = combin_inverse ( alpha, beta, n )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 )
#
#  COMPANION
#
  title = 'COMPANION'
  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( n, r8_lo, r8_hi, seed )
  cond1 = companion_condition ( n, x )

  a = companion ( n, x )
  b = companion_inverse ( n, x )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 )
#
#  CONEX1
#
  title = 'CONEX1'
  n = 4
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  cond1 = conex1_condition ( alpha )

  a = conex1 ( alpha )
  b = conex1_inverse ( alpha )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 )
#
#  CONEX2
#
  title = 'CONEX2'
  n = 3
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  cond1 = conex2_condition ( alpha )

  a = conex2 ( alpha )
  b = conex2_inverse ( alpha )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 )
#
#  CONEX3
#
  title = 'CONEX3'
  n = 5
  cond1 = conex3_condition ( n )

  a = conex3 ( n )
  b = conex3_inverse ( n )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 )
#
#  CONEX4
#
  title = 'CONEX4'
  n = 4
  cond1 = conex4_condition ( )

  a = conex4 ( )
  b = conex4_inverse ( )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 )
#
#  DAUB2
#
  title = 'DAUB2'
  n = 4
  cond1 = daub2_condition ( n )

  a = daub2 ( n )
  b = daub2_inverse ( n )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 )
#
#  DAUB4
#
  title = 'DAUB4'
  n = 8
  cond1 = daub4_condition ( n )

  a = daub4 ( n )
  b = daub4_inverse ( n )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 )
#
#  DAUB6
#
  title = 'DAUB6'
  n = 12
  cond1 = daub6_condition ( n )

  a = daub6 ( n )
  b = daub6_inverse ( n )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 )
#
#  DAUB8
#
  title = 'DAUB8'
  n = 16
  cond1 = daub8_condition ( n )

  a = daub8 ( n )
  b = daub8_inverse ( n )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 )
#
#  DAUB10
#
  title = 'DAUB10'
  n = 20
  cond1 = daub10_condition ( n )

  a = daub10 ( n )
  b = daub10_inverse ( n )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 )
#
#  DAUB12
#
  title = 'DAUB12'
  n = 24
  cond1 = daub12_condition ( n )

  a = daub12 ( n )
  b = daub12_inverse ( n )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 )
#
#  DIAGONAL
#
  title = 'DIAGONAL'
  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( n, r8_lo, r8_hi, seed )
  cond1 = diagonal_condition ( n, x )

  a = diagonal ( n, n, x )
  b = diagonal_inverse ( n, x )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 )
#
#  DIF2
#
  title = 'DIF2'
  n = 5
  cond1 = dif2_condition ( n )

  a = dif2 ( n, n )
  b = dif2_inverse ( n )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 )
#
#  DOWNSHIFT
#
  title = 'DOWNSHIFT'
  n = 5
  cond1 = downshift_condition ( n )

  a = downshift ( n )
  b = downshift_inverse ( n )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 )
#
#  EXCHANGE
#
  title = 'EXCHANGE'
  n = 5
  cond1 = exchange_condition ( n )

  a = exchange ( n, n )
  b = exchange_inverse ( n )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 )
#
#  FIBONACCI2
#
  title = 'FIBONACCI2'
  n = 5
  cond1 = fibonacci2_condition ( n )

  a = fibonacci2 ( n )
  b = fibonacci2_inverse ( n )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 )
#
#  GFPP
#
  title = 'GFPP'
  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  cond1 = gfpp_condition ( n, alpha )

  a = gfpp ( n, alpha )
  b = gfpp_inverse ( n, alpha )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 )
#
#  GIVENS
#
  title = 'GIVENS'
  n = 5
  cond1 = givens_condition ( n )

  a = givens ( n, n )
  b = givens_inverse ( n )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 )
#
#  HANKEL_N
#
  title = 'HANKEL_N'
  n = 5
  cond1 = hankel_n_condition ( n )

  a = hankel_n ( n )
  b = hankel_n_inverse ( n )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 )
#
#  HARMAN
#
  title = 'HARMAN'
  n = 8
  cond1 = harman_condition ( )

  a = harman ( )
  b = harman_inverse ( )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 )
#
#  HARTLEY
#
  title = 'HARTLEY'
  n = 5
  cond1 = hartley_condition ( n )

  a = hartley ( n )
  b = hartley_inverse ( n )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 )
#
#  IDENTITY
#
  title = 'IDENTITY'
  n = 5
  cond1 = identity_condition ( n )

  a = identity ( n, n )
  b = identity_inverse ( n )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 )
#
#  ILL3
#
  title = 'ILL3'
  n = 3
  cond1 = ill3_condition ( )

  a = ill3 ( )
  b = ill3_inverse ( )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 )
#
#  JORDAN
#
  title = 'JORDAN'
  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  cond1 = jordan_condition ( n, alpha )

  a = jordan ( n, n, alpha )
  b = jordan_inverse ( n, alpha )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 )
#
#  KERSHAW
#
  title = 'KERSHAW'
  n = 4
  cond1 = kershaw_condition ( )

  a = kershaw ( )
  b = kershaw_inverse ( )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 )
#
#  LIETZKE
#
  title = 'LIETZKE'
  n = 5
  cond1 = lietzke_condition ( n )

  a = lietzke ( n )
  b = lietzke_inverse ( n )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 )
#
#  MAXIJ
#
  title = 'MAXIJ'
  n = 5
  cond1 = maxij_condition ( n )

  a = maxij ( n, n )
  b = maxij_inverse ( n )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 )
#
#  MINIJ
#
  title = 'MINIJ'
  n = 5
  cond1 = minij_condition ( n )

  a = minij ( n, n )
  b = minij_inverse ( n )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 )
#
#  ORTH_SYMM
#
  title = 'ORTH_SYMM'
  n = 5
  cond1 = orth_symm_condition ( n )

  a = orth_symm ( n )
  b = orth_symm_inverse ( n )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 )
#
#  OTO
#
  title = 'OTO'
  n = 5
  cond1 = oto_condition ( n )

  a = oto ( n, n )
  b = oto_inverse ( n )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 )
#
#  PASCAL1
#
  title = 'PASCAL1'
  n = 5
  cond1 = pascal1_condition ( n )

  a = pascal1 ( n )
  b = pascal1_inverse ( n )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 )
#
#  PASCAL3
#
  title = 'PASCAL3'
  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  cond1 = pascal3_condition ( n, alpha )

  a = pascal3 ( n, alpha )
  b = pascal3_inverse ( n, alpha )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 )
#
#  PEI
#
  title = 'PEI'
  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  cond1 = pei_condition ( alpha, n )

  a = pei ( alpha, n )
  b = pei_inverse ( alpha, n )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 )
#
#  RODMAN
#
  title = 'RODMAN'
  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  cond1 = rodman_condition ( n, alpha )

  a = rodman ( n, n, alpha )
  b = rodman_inverse ( n, alpha )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 )
#
#  RUTIS1
#
  title = 'RUTIS1'
  n = 4
  cond1 = rutis1_condition ( )

  a = rutis1 ( )
  b = rutis1_inverse ( )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 )
#
#  RUTIS2
#
  title = 'RUTIS2'
  n = 4
  cond1 = rutis2_condition ( )

  a = rutis2 ( )
  b = rutis2_inverse ( )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 )
#
#  RUTIS3
#
  title = 'RUTIS3'
  n = 4
  cond1 = rutis3_condition ( )

  a = rutis3 ( )
  b = rutis3_inverse ( )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 )
#
#  RUTIS5
#
  title = 'RUTIS5'
  n = 4
  cond1 = rutis5_condition ( )

  a = rutis5 ( )
  b = rutis5_inverse ( )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 )
#
#  SUMMATION
#
  title = 'SUMMATION'
  n = 5
  cond1 = summation_condition ( n )

  a = summation ( n, n )
  b = summation_inverse ( n )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 )
#
#  SWEET1
#
  title = 'SWEET1'
  n = 6
  cond1 = sweet1_condition ( )

  a = sweet1 ( )
  b = sweet1_inverse ( )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 )
#
#  SWEET2
#
  title = 'SWEET2'
  n = 6
  cond1 = sweet2_condition ( )

  a = sweet2 ( )
  b = sweet2_inverse ( )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 )
#
#  SWEET3
#
  title = 'SWEET3'
  n = 6
  cond1 = sweet3_condition ( )

  a = sweet3 ( )
  b = sweet3_inverse ( )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 )
#
#  SWEET4
#
  title = 'SWEET4'
  n = 13
  cond1 = sweet4_condition ( )

  a = sweet4 ( )
  b = sweet4_inverse ( )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 )
#
#  TRI_UPPER
#
  title = 'TRI_UPPER'
  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  cond1 = tri_upper_condition ( alpha, n )

  a = tri_upper ( alpha, n )
  b = tri_upper_inverse ( alpha, n )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 )
#
#  UPSHIFT
#
  title = 'UPSHIFT'
  n = 5
  cond1 = upshift_condition ( n )

  a = upshift ( n )
  b = upshift_inverse ( n )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 )
#
#  WILK03
#
  title = 'WILK03'
  n = 3
  cond1 = wilk03_condition ( )

  a = wilk03 ( )
  b = wilk03_inverse ( )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 )
#
#  WILK04
#
  title = 'WILK04'
  n = 4
  cond1 = wilk04_condition ( )

  a = wilk04 ( )
  b = wilk04_inverse ( )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 )
#
#  WILK05
#
  title = 'WILK05'
  n = 5
  cond1 = wilk05_condition ( )

  a = wilk05 ( )
  b = wilk05_inverse ( )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 )
#
#  WILSON
#
  title = 'WILSON'
  n = 4
  cond1 = wilson_condition ( )

  a = wilson ( )
  b = wilson_inverse ( )
  a_norm = r8mat_norm_l1 ( n, n, a )
  b_norm = r8mat_norm_l1 ( n, n, b )
  cond2 = a_norm * b_norm

  print '  %-20s  %4d  %14.6g  %14.6g' % ( title, n, cond1, cond2 )
#
#  Terminate.
#
  print ''
  print 'TEST_CONDITION'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  test_condition ( )
  timestamp ( )
