#! /usr/bin/env python
#
def test_solution ( ):

#*****************************************************************************80
#
## TEST_SOLUTION tests the linear solution computations.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 March 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  from a123              import a123
  from a123              import a123_rhs
  from a123              import a123_solution
  from bodewig           import bodewig
  from bodewig           import bodewig_rhs
  from bodewig           import bodewig_solution
  from dif2              import dif2
  from dif2              import dif2_rhs
  from dif2              import dif2_solution
  from frank             import frank
  from frank             import frank_rhs
  from frank             import frank_solution
  from poisson           import poisson
  from poisson           import poisson_rhs
  from poisson           import poisson_solution
  from r8mat_is_solution import r8mat_is_solution
  from r8mat_norm_fro    import r8mat_norm_fro
  from wilk03            import wilk03
  from wilk03            import wilk03_rhs
  from wilk03            import wilk03_solution
  from wilk04            import wilk04
  from wilk04            import wilk04_rhs
  from wilk04            import wilk04_solution
  from wilson            import wilson
  from wilson            import wilson_rhs
  from wilson            import wilson_solution

  print ''
  print 'TEST_SOLUTION'
  print '  Compute the Frobenius norm of the solution error:'
  print '    A * X - B'
  print '  given MxN matrix A, NxK solution X, MxK right hand side B.'
  print ''
  print '  Title                    M     N     K       ||A||',
  print '            ||A*X-B||'
  print ''
#
#  A123 matrix.
#
  title = 'A123'
  m = 3
  n = 3
  k = 1
  a = a123 ( )
  b = a123_rhs ( )
  x = a123_solution ( )
  error_frobenius = r8mat_is_solution ( m, n, k, a, x, b )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %4d  %4d  %14g  %14g' \
    % ( title, m, n, k, norm_frobenius, error_frobenius )
#
#  BODEWIG matrix.
#
  title = 'BODEWIG'
  m = 4
  n = 4
  k = 1
  a = bodewig ( )
  b = bodewig_rhs ( )
  x = bodewig_solution ( )
  error_frobenius = r8mat_is_solution ( m, n, k, a, x, b )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %4d  %4d  %14g  %14g' \
    % ( title, m, n, k, norm_frobenius, error_frobenius )
#
#  DIF2 matrix.
#
  title = 'DIF2'
  m = 10
  n = 10
  k = 2
  a = dif2 ( m, n )
  b = dif2_rhs ( m, k )
  x = dif2_solution ( n, k )
  error_frobenius = r8mat_is_solution ( m, n, k, a, x, b )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %4d  %4d  %14g  %14g' \
    % ( title, m, n, k, norm_frobenius, error_frobenius )
#
#  FRANK matrix.
#
  title = 'FRANK'
  m = 10
  n = 10
  k = 2
  a = frank ( n )
  b = frank_rhs ( m, k )
  x = frank_solution ( n, k )
  error_frobenius = r8mat_is_solution ( m, n, k, a, x, b )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %4d  %4d  %14g  %14g' \
    % ( title, m, n, k, norm_frobenius, error_frobenius )
#
#  POISSON matrix.
#
  title = 'POISSON'
  nrow = 4
  ncol = 5
  m = nrow * ncol
  n = nrow * ncol
  k = 1
  a = poisson ( nrow, ncol )
  b = poisson_rhs ( nrow, ncol, k )
  x = poisson_solution ( nrow, ncol, k )
  error_frobenius = r8mat_is_solution ( m, n, k, a, x, b )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %4d  %4d  %14g  %14g' \
    % ( title, m, n, k, norm_frobenius, error_frobenius )
#
#  WILK03 matrix.
#
  title = 'WILK03'
  m = 3
  n = 3
  k = 1
  a = wilk03 ( )
  b = wilk03_rhs ( )
  x = wilk03_solution ( )
  error_frobenius = r8mat_is_solution ( m, n, k, a, x, b )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %4d  %4d  %14g  %14g' \
    % ( title, m, n, k, norm_frobenius, error_frobenius )
#
#  WILK04 matrix.
#
  title = 'WILK04'
  m = 4
  n = 4
  k = 1
  a = wilk04 ( )
  b = wilk04_rhs ( )
  x = wilk04_solution ( )
  error_frobenius = r8mat_is_solution ( m, n, k, a, x, b )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %4d  %4d  %14g  %14g' \
    % ( title, m, n, k, norm_frobenius, error_frobenius )
#
#  WILSON matrix.
#
  title = 'WILSON'
  m = 4
  n = 4
  k = 1
  a = wilson ( )
  b = wilson_rhs ( )
  x = wilson_solution ( )
  error_frobenius = r8mat_is_solution ( m, n, k, a, x, b )
  norm_frobenius = r8mat_norm_fro ( n, n, a )
  print '  %-20s  %4d  %4d  %4d  %14g  %14g' \
    % ( title, m, n, k, norm_frobenius, error_frobenius )
#
#  Terminate.
#
  print ''
  print 'TEST_SOLUTION'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  test_solution ( )
  timestamp ( )
