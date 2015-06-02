#! /usr/bin/env python
#
def test_llt ( ):

#*****************************************************************************80
#
#% TEST_LLT tests LLT factors.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 April 2015
#
#  Author:
#
#    John Burkardt
#
  from dif2           import dif2
  from dif2           import dif2_llt
  from givens         import givens
  from givens         import givens_llt
  from kershaw        import kershaw
  from kershaw        import kershaw_llt
  from lehmer         import lehmer
  from lehmer         import lehmer_llt
  from minij          import minij
  from minij          import minij_llt
  from moler1         import moler1
  from moler1         import moler1_llt
  from moler3         import moler3
  from moler3         import moler3_llt
  from oto            import oto
  from oto            import oto_llt
  from pascal2        import pascal2
  from pascal2        import pascal2_llt
  from wilson         import wilson
  from wilson         import wilson_llt
  from r8_uniform_ab  import r8_uniform_ab
  from r8mat_is_llt   import r8mat_is_llt
  from r8mat_norm_fro import r8mat_norm_fro

  print ''
  print 'TEST_LLT'
  print '  A = a test matrix of order M by M'
  print '  L is an M by N lower triangular Cholesky factor.'
  print ''
  print '  ||A|| = Frobenius norm of A.'
  print '  ||A-LLT|| = Frobenius norm of A-L*L\'.'
  print ''
  print '  Title                    M     N      ',
  print '||A||            ||A-LLT||'
  print ''
#
#  DIF2
#
  title = 'DIF2'
  m = 5
  n = 5
  a = dif2 ( m, n )
  l = dif2_llt ( n )
  error_frobenius = r8mat_is_llt ( m, n, a, l )
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
  l = givens_llt ( n )
  error_frobenius = r8mat_is_llt ( m, n, a, l )
  norm_a_frobenius = r8mat_norm_fro ( m, n, a )
  print '  %-20s  %4d  %4d  %14g  %14g' \
    % ( title, m, n, norm_a_frobenius, error_frobenius )
#
#  KERSHAW
#
  title = 'KERSHAW'
  m = 4
  n = 4
  a = kershaw ( )
  l = kershaw_llt ( )
  error_frobenius = r8mat_is_llt ( m, n, a, l )
  norm_a_frobenius = r8mat_norm_fro ( m, n, a )
  print '  %-20s  %4d  %4d  %14g  %14g' \
    % ( title, m, n, norm_a_frobenius, error_frobenius )
#
#  LEHMER
#
  title = 'LEHMER'
  m = 5
  n = 5
  a = lehmer ( n, n )
  l = lehmer_llt ( n )
  error_frobenius = r8mat_is_llt ( m, n, a, l )
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
  l = minij_llt ( n )
  error_frobenius = r8mat_is_llt ( m, n, a, l )
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
  a = moler1 ( alpha, m, n )
  l = moler1_llt ( alpha, n )
  error_frobenius = r8mat_is_llt ( m, n, a, l )
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
  l = moler3_llt ( n )
  error_frobenius = r8mat_is_llt ( m, n, a, l )
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
  l = oto_llt ( n )
  error_frobenius = r8mat_is_llt ( m, n, a, l )
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
  l = pascal2_llt ( n )
  error_frobenius = r8mat_is_llt ( m, n, a, l )
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
  l = wilson_llt ( )
  error_frobenius = r8mat_is_llt ( m, n, a, l )
  norm_a_frobenius = r8mat_norm_fro ( m, n, a )
  print '  %-20s  %4d  %4d  %14g  %14g' \
    % ( title, m, n, norm_a_frobenius, error_frobenius )
#
#  Terminate.
#
  print ''
  print 'TEST_LLT:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  test_llt ( )
  timestamp ( )
