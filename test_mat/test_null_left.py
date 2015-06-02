#! /usr/bin/env python
#
def test_null_left ( ):

#*****************************************************************************80
#
## TEST_NULL_LEFT tests left null vectors.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 March 2015
#
#  Author:
#
#    John Burkardt
#
  from a123                import a123
  from a123                import a123_null_left
  from cheby_diff1         import cheby_diff1
  from cheby_diff1         import cheby_diff1_null_left
  from creation            import creation
  from creation            import creation_null_left
  from dif1                import dif1
  from dif1                import dif1_null_left
  from dif1cyclic          import dif1cyclic
  from dif1cyclic          import dif1cyclic_null_left
  from dif2cyclic          import dif2cyclic
  from dif2cyclic          import dif2cyclic_null_left
  from eberlein            import eberlein
  from eberlein            import eberlein_null_left
  from fibonacci1          import fibonacci1
  from fibonacci1          import fibonacci1_null_left
  from lauchli             import lauchli
  from lauchli             import lauchli_null_left
  from line_adj            import line_adj
  from line_adj            import line_adj_null_left
  from moler2              import moler2
  from moler2              import moler2_null_left
  from one                 import one
  from one                 import one_null_left
  from r8_uniform_ab       import r8_uniform_ab
  from r8mat_is_null_left  import r8mat_is_null_left
  from r8mat_norm_fro      import r8mat_norm_fro
  from r8vec_norm_l2       import r8vec_norm_l2
  from ring_adj            import ring_adj
  from ring_adj            import ring_adj_null_left
  from rosser1             import rosser1
  from rosser1             import rosser1_null_left
  from zero                import zero
  from zero                import zero_null_left

  print ''
  print 'TEST_NULL_LEFT'
  print '  A = a test matrix of order M by N'
  print '  x = an M vector, candidate for a left null vector.'
  print ''
  print '  ||A|| = Frobenius norm of A.'
  print '  ||x|| = L2 norm of x.'
  print '  ||A''*x||/||x|| = L2 norm of A\'*x over L2 norm of x.'
  print ''
  print '  Title                    M     N      ',
  print '||A||            ||x||        ||A\'*x||/||x||'
  print ''
#
#  A123
#
  title = 'A123'
  m = 3
  n = 3
  a = a123 ( )
  x = a123_null_left ( )
  error_l2 = r8mat_is_null_left ( m, n, a, x )
  norm_a_frobenius = r8mat_norm_fro ( m, n, a )
  norm_x_l2 = r8vec_norm_l2 ( m, x )
  print '  %-20s  %4d  %4d  %14g  %14g  %10.2g' \
    % ( title, m, n, norm_a_frobenius, norm_x_l2, error_l2 )
#
#  CHEBY_DIFF1
#
  title = 'CHEBY_DIFF1'
  m = 5
  n = m
  a = cheby_diff1 ( n )
  x = cheby_diff1_null_left ( m, n )
  error_l2 = r8mat_is_null_left ( m, n, a, x )
  norm_a_frobenius = r8mat_norm_fro ( m, n, a )
  norm_x_l2 = r8vec_norm_l2 ( m, x )
  print '  %-20s  %4d  %4d  %14g  %14g  %10.2g' \
    % ( title, m, n, norm_a_frobenius, norm_x_l2, error_l2 )
#
#  CREATION
#
  title = 'CREATION'
  m = 5
  n = m
  a = creation ( m, n )
  x = creation_null_left ( m, n )
  error_l2 = r8mat_is_null_left ( m, n, a, x )
  norm_a_frobenius = r8mat_norm_fro ( m, n, a )
  norm_x_l2 = r8vec_norm_l2 ( m, x )
  print '  %-20s  %4d  %4d  %14g  %14g  %10.2g' \
    % ( title, m, n, norm_a_frobenius, norm_x_l2, error_l2 )
#
#  DIF1
#
  title = 'DIF1'
  m = 5
  n = 5
  a = dif1 ( m, n )
  x = dif1_null_left ( m, n )
  error_l2 = r8mat_is_null_left ( m, n, a, x )
  norm_a_frobenius = r8mat_norm_fro ( m, n, a )
  norm_x_l2 = r8vec_norm_l2 ( m, x )
  print '  %-20s  %4d  %4d  %14g  %14g  %10.2g' \
    % ( title, m, n, norm_a_frobenius, norm_x_l2, error_l2 )
#
#  DIF1CYCLIC
#
  title = 'DIF1CYCLIC'
  m = 5
  n = m
  a = dif1cyclic ( n )
  x = dif1cyclic_null_left ( m, n )
  error_l2 = r8mat_is_null_left ( m, n, a, x )
  norm_a_frobenius = r8mat_norm_fro ( m, n, a )
  norm_x_l2 = r8vec_norm_l2 ( m, x )
  print '  %-20s  %4d  %4d  %14g  %14g  %10.2g' \
    % ( title, m, n, norm_a_frobenius, norm_x_l2, error_l2 )
#
#  DIF2CYCLIC
#
  title = 'DIF2CYCLIC'
  m = 5
  n = 5
  a = dif2cyclic ( n )
  x = dif2cyclic_null_left ( m, n )
  error_l2 = r8mat_is_null_left ( m, n, a, x )
  norm_a_frobenius = r8mat_norm_fro ( m, n, a )
  norm_x_l2 = r8vec_norm_l2 ( m, x )
  print '  %-20s  %4d  %4d  %14g  %14g  %10.2g' \
    % ( title, m, n, norm_a_frobenius, norm_x_l2, error_l2 )
#
#  EBERLEIN
#
  title = 'EBERLEIN'
  m = 5
  n = 5
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  a = eberlein ( alpha, n )
  x = eberlein_null_left ( m, n )
  error_l2 = r8mat_is_null_left ( m, n, a, x )
  norm_a_frobenius = r8mat_norm_fro ( m, n, a )
  norm_x_l2 = r8vec_norm_l2 ( m, x )
  print '  %-20s  %4d  %4d  %14g  %14g  %10.2g' \
    % ( title, m, n, norm_a_frobenius, norm_x_l2, error_l2 )
#
#  FIBONACCI1
#
  title = 'FIBONACCI1'
  m = 5
  n = m
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  f1, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  f2, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  a = fibonacci1 ( n, f1, f2 )
  x = fibonacci1_null_left ( m, n, f1, f2 )
  error_l2 = r8mat_is_null_left ( m, n, a, x )
  norm_a_frobenius = r8mat_norm_fro ( m, n, a )
  norm_x_l2 = r8vec_norm_l2 ( m, x )
  print '  %-20s  %4d  %4d  %14g  %14g  %10.2g' \
    % ( title, m, n, norm_a_frobenius, norm_x_l2, error_l2 )
#
#  LAUCHLI
#
  title = 'LAUCHLI'
  m = 6
  n = m - 1
  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
  a = lauchli ( alpha, m, n )
  x = lauchli_null_left ( alpha, m, n )
  error_l2 = r8mat_is_null_left ( m, n, a, x )
  norm_a_frobenius = r8mat_norm_fro ( m, n, a )
  norm_x_l2 = r8vec_norm_l2 ( m, x )
  print '  %-20s  %4d  %4d  %14g  %14g  %10.2g' \
    % ( title, m, n, norm_a_frobenius, norm_x_l2, error_l2 )
#
#  LINE_ADJ
#
  title = 'LINE_ADJ'
  m = 7
  n = m
  a = line_adj ( n )
  x = line_adj_null_left ( m, n )
  error_l2 = r8mat_is_null_left ( m, n, a, x )
  norm_a_frobenius = r8mat_norm_fro ( m, n, a )
  norm_x_l2 = r8vec_norm_l2 ( m, x )
  print '  %-20s  %4d  %4d  %14g  %14g  %10.2g' \
    % ( title, m, n, norm_a_frobenius, norm_x_l2, error_l2 )
#
#  MOLER2
#
  title = 'MOLER2'
  m = 5
  n = m
  a = moler2 ( )
  x = moler2_null_left ( )
  error_l2 = r8mat_is_null_left ( m, n, a, x )
  norm_a_frobenius = r8mat_norm_fro ( m, n, a )
  norm_x_l2 = r8vec_norm_l2 ( m, x )
  print '  %-20s  %4d  %4d  %14g  %14g  %10.2g' \
    % ( title, m, n, norm_a_frobenius, norm_x_l2, error_l2 )
#
#  ONE
#
  title = 'ONE'
  m = 5
  n = 5
  a = one ( m, n )
  x = one_null_left ( m, n )
  error_l2 = r8mat_is_null_left ( m, n, a, x )
  norm_a_frobenius = r8mat_norm_fro ( m, n, a )
  norm_x_l2 = r8vec_norm_l2 ( m, x )
  print '  %-20s  %4d  %4d  %14g  %14g  %10.2g' \
    % ( title, m, n, norm_a_frobenius, norm_x_l2, error_l2 )
#
#  RING_ADJ
#  N must be a multiple of 4 for there to be a null vector.
#
  title = 'RING_ADJ'
  m = 12
  n = 12
  a = ring_adj ( m, n )
  x = ring_adj_null_left ( m, n )
  error_l2 = r8mat_is_null_left ( m, n, a, x )
  norm_a_frobenius = r8mat_norm_fro ( m, n, a )
  norm_x_l2 = r8vec_norm_l2 ( m, x )
  print '  %-20s  %4d  %4d  %14g  %14g  %10.2g' \
    % ( title, m, n, norm_a_frobenius, norm_x_l2, error_l2 )
#
#  ROSSER1
#
  title = 'ROSSER1'
  m = 8
  n = 8
  a = rosser1 ( )
  x = rosser1_null_left ( )
  error_l2 = r8mat_is_null_left ( m, n, a, x )
  norm_a_frobenius = r8mat_norm_fro ( m, n, a )
  norm_x_l2 = r8vec_norm_l2 ( m, x )
  print '  %-20s  %4d  %4d  %14g  %14g  %10.2g' \
    % ( title, m, n, norm_a_frobenius, norm_x_l2, error_l2 )
#
#  ZERO
#
  title = 'ZERO'
  m = 5
  n = 5
  a = zero ( m, n )
  x = zero_null_left ( m, n )
  error_l2 = r8mat_is_null_left ( m, n, a, x )
  norm_a_frobenius = r8mat_norm_fro ( m, n, a )
  norm_x_l2 = r8vec_norm_l2 ( m, x )
  print '  %-20s  %4d  %4d  %14g  %14g  %10.2g' \
    % ( title, m, n, norm_a_frobenius, norm_x_l2, error_l2 )
#
#  Terminate.
#
  print ''
  print 'TEST_NULL_LEFT:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  test_null_left ( )
  timestamp ( )
