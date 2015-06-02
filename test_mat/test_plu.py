#! /usr/bin/env python
#
def test_plu ( ):

#*****************************************************************************80
#
## TEST_PLU tests the PLU factors.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 April 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from bodewig          import bodewig
  from bodewig          import bodewig_plu
  from borderband       import borderband
  from borderband       import borderband_plu
  from dif2             import dif2
  from dif2             import dif2_plu
  from gfpp             import gfpp
  from gfpp             import gfpp_plu
  from givens           import givens
  from givens           import givens_plu
  from i4_uniform_ab    import i4_uniform_ab
  from kms              import kms
  from kms              import kms_plu
  from lehmer           import lehmer
  from lehmer           import lehmer_plu
  from maxij            import maxij
  from maxij            import maxij_plu
  from minij            import minij
  from minij            import minij_plu
  from moler1           import moler1
  from moler1           import moler1_plu
  from moler3           import moler3
  from moler3           import moler3_plu
  from oto              import oto
  from oto              import oto_plu
  from pascal2          import pascal2
  from pascal2          import pascal2_plu
  from plu              import plu
  from plu              import plu_plu
  from r8_uniform_ab    import r8_uniform_ab
  from r8mat_is_plu     import r8mat_is_plu
  from r8mat_norm_fro   import r8mat_norm_fro
  from r8vec_uniform_ab import r8vec_uniform_ab
  from vand2            import vand2
  from vand2            import vand2_plu
  from wilson           import wilson
  from wilson           import wilson_plu

  print ''
  print 'TEST_PLU'
  print '  A = a test matrix of order M by N'
  print '  P, L, U are the PLU factors.'
  print ''
  print '  ||A|| = Frobenius norm of A.'
  print '  ||A-PLU|| = Frobenius norm of A-P*L*U.'
  print ''
  print '  Title                    M     N         ',
  print '||A||        ||A-PLU||'
  print ''
#
#  BODEWIG
#
  title = 'BODEWIG'
  m = 4
  n = 4
  a = bodewig ( )
  p, l, u = bodewig_plu ( )
  error_frobenius = r8mat_is_plu ( m, n, a, p, l, u )
  norm_a_frobenius = r8mat_norm_fro ( m, n, a )
  print '  %-20s  %4d  %4d  %14g  %14g' \
    % ( title, m, n, norm_a_frobenius, error_frobenius )
#
#  BORDERBAND
#
  title = 'BORDERBAND'
  m = 5
  n = 5
  a = borderband ( n )
  p, l, u = borderband_plu ( n )
  error_frobenius = r8mat_is_plu ( m, n, a, p, l, u )
  norm_a_frobenius = r8mat_norm_fro ( m, n, a )
  print '  %-20s  %4d  %4d  %14g  %14g' \
    % ( title, m, n, norm_a_frobenius, error_frobenius )
#
#  DIF2
#
  title = 'DIF2'
  m = 5
  n = 5
  a = dif2 ( m, n )
  p, l, u = dif2_plu ( n )
  error_frobenius = r8mat_is_plu ( m, n, a, p, l, u )
  norm_a_frobenius = r8mat_norm_fro ( m, n, a )
  print '  %-20s  %4d  %4d  %14g  %14g' \
    % ( title, m, n, norm_a_frobenius, error_frobenius )
#
#  GFPP
#
  title = 'GFPP'
  m = 5
  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  a = gfpp ( n, alpha )
  p, l, u = gfpp_plu ( n, alpha )
  error_frobenius = r8mat_is_plu ( m, n, a, p, l, u )
  norm_a_frobenius = r8mat_norm_fro ( m, n, a )
  print '  %-20s  %4d  %4d  %14g  %14g' \
    % ( title, m, n, norm_a_frobenius, error_frobenius )
#
#  GIVENS
#
  title = 'GIVENS'
  m = 5
  n = 5
  a = givens ( m, n )
  p, l, u = givens_plu ( n )
  error_frobenius = r8mat_is_plu ( m, n, a, p, l, u )
  norm_a_frobenius = r8mat_norm_fro ( m, n, a )
  print '  %-20s  %4d  %4d  %14g  %14g' \
    % ( title, m, n, norm_a_frobenius, error_frobenius )
#
#  KMS
#
  title = 'KMS'
  m = 5
  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  a = kms ( alpha, m, n )
  p, l, u = kms_plu ( alpha, n )
  error_frobenius = r8mat_is_plu ( m, n, a, p, l, u )
  norm_a_frobenius = r8mat_norm_fro ( m, n, a )
  print '  %-20s  %4d  %4d  %14g  %14g' \
    % ( title, m, n, norm_a_frobenius, error_frobenius )
#
#  LEHMER
#
  title = 'LEHMER'
  m = 5
  n = 5
  a = lehmer ( m, n )
  p, l, u = lehmer_plu ( n )
  error_frobenius = r8mat_is_plu ( m, n, a, p, l, u )
  norm_a_frobenius = r8mat_norm_fro ( m, n, a )
  print '  %-20s  %4d  %4d  %14g  %14g' \
    % ( title, m, n, norm_a_frobenius, error_frobenius )
#
#  MAXIJ
#
  title = 'MAXIJ'
  m = 5
  n = 5
  a = maxij ( m, n )
  p, l, u = maxij_plu ( n )
  error_frobenius = r8mat_is_plu ( m, n, a, p, l, u )
  norm_a_frobenius = r8mat_norm_fro ( m, n, a )
  print '  %-20s  %4d  %4d  %14g  %14g' \
    % ( title, m, n, norm_a_frobenius, error_frobenius )
#
#  MINIJ
#
  title = 'MINIJ'
  m = 5
  n = 5
  a = minij ( n, n )
  p, l, u = minij_plu ( n )
  error_frobenius = r8mat_is_plu ( m, n, a, p, l, u )
  norm_a_frobenius = r8mat_norm_fro ( m, n, a )
  print '  %-20s  %4d  %4d  %14g  %14g' \
    % ( title, m, n, norm_a_frobenius, error_frobenius )
#
#  MOLER1
#
  title = 'MOLER1'
  m = 5
  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  a = moler1 ( alpha, n, n )
  p, l, u = moler1_plu ( alpha, n )
  error_frobenius = r8mat_is_plu ( m, n, a, p, l, u )
  norm_a_frobenius = r8mat_norm_fro ( m, n, a )
  print '  %-20s  %4d  %4d  %14g  %14g' \
    % ( title, m, n, norm_a_frobenius, error_frobenius )
#
#  MOLER3
#
  title = 'MOLER3'
  m = 5
  n = 5
  a = moler3 ( m, n )
  p, l, u = moler3_plu ( n )
  error_frobenius = r8mat_is_plu ( m, n, a, p, l, u )
  norm_a_frobenius = r8mat_norm_fro ( m, n, a )
  print '  %-20s  %4d  %4d  %14g  %14g' \
    % ( title, m, n, norm_a_frobenius, error_frobenius )
#
#  OTO
#
  title = 'OTO'
  m = 5
  n = 5
  a = oto ( m, n )
  p, l, u = oto_plu ( n )
  error_frobenius = r8mat_is_plu ( m, n, a, p, l, u )
  norm_a_frobenius = r8mat_norm_fro ( m, n, a )
  print '  %-20s  %4d  %4d  %14g  %14g' \
    % ( title, m, n, norm_a_frobenius, error_frobenius )
#
#  PASCAL2
#
  title = 'PASCAL2'
  m = 5
  n = 5
  a = pascal2 ( n )
  p, l, u = pascal2_plu ( n )
  error_frobenius = r8mat_is_plu ( m, n, a, p, l, u )
  norm_a_frobenius = r8mat_norm_fro ( m, n, a )
  print '  %-20s  %4d  %4d  %14g  %14g' \
    % ( title, m, n, norm_a_frobenius, error_frobenius )
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
  p, l, u = plu_plu ( n, pivot )
  error_frobenius = r8mat_is_plu ( m, n, a, p, l, u )
  norm_a_frobenius = r8mat_norm_fro ( m, n, a )
  print '  %-20s  %4d  %4d  %14g  %14g' \
    % ( title, m, n, norm_a_frobenius, error_frobenius )
#
#  VAND2
#
  title = 'VAND2'
  m = 4
  n = 4
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( m, r8_lo, r8_hi, seed )
  a = vand2 ( m, x )
  p, l, u = vand2_plu ( m, x )
  error_frobenius = r8mat_is_plu ( m, n, a, p, l, u )
  norm_a_frobenius = r8mat_norm_fro ( m, n, a )
  print '  %-20s  %4d  %4d  %14g  %14g' \
    % ( title, m, n, norm_a_frobenius, error_frobenius )
#
#  WILSON
#
  title = 'WILSON'
  m = 4
  n = 4
  a = wilson ( )
  p, l, u = wilson_plu ( )
  error_frobenius = r8mat_is_plu ( m, n, a, p, l, u )
  norm_a_frobenius = r8mat_norm_fro ( m, n, a )
  print '  %-20s  %4d  %4d  %14g  %14g' \
    % ( title, m, n, norm_a_frobenius, error_frobenius )
#
#  Terminate.
#
  print ''
  print 'TEST_PLU:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  test_plu ( )
  timestamp ( )
