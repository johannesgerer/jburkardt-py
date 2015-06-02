#!/usr/bin/env python

def r8mat_is_solution ( m, n, k, a, x, b ):

#*****************************************************************************80
#
## R8MAT_IS_SOLUTION measures the error in a linear system solution.
#
#  Discussion:
#
#    An R8MAT is a matrix of real values.
#
#    The system matrix A is an M x N matrix.
#    It is not required that A be invertible.
#
#    The solution vector X is actually allowed to be an N x K matrix.
#
#    The right hand side "vector" B is actually allowed to be an M x K matrix.
#
#    This routine simply returns the Frobenius norm of the M x K matrix:
#    A * X - B.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, K, the order of the matrices.
#
#    Input, real A(M,N), X(N,K), B(M,K), the matrices.
#
#    Output, real VALUE, the Frobenius norm
#    of the difference matrix A * X - B, which would be exactly zero
#    if X was the "solution" of the linear system.
#
  from r8mat_norm_fro import r8mat_norm_fro
  from r8mat_mm import r8mat_mm
  from r8mat_sub import r8mat_sub
#
#  AX = A*X
#
  ax = r8mat_mm ( m, n, k, a, x )
#
#  AXMB = AX-B.
#
  axmb = r8mat_sub ( m, k, ax, b )
#
#  Value = ||AX-B|\
#
  value = r8mat_norm_fro ( m, k, axmb )

  return value

def r8mat_is_solution_test ( ):

#*****************************************************************************80
#
## R8MAT_IS_SOLUTION_TEST tests R8MAT_IS_SOLUTION.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 March 2015
#
#  Author:
#
#    John Burkardt
#
  from i4_uniform_ab import i4_uniform_ab
  from r8mat_mm import r8mat_mm
  from r8mat_uniform_ab import r8mat_uniform_ab

  print ''
  print 'R8MAT_IS_SOLUTION_TEST:'
  print '  R8MAT_IS_SOLUTION tests whether X is the solution of'
  print '  A*X=B by computing the Frobenius norm of the residual.'
#
#  Get random shapes.
#
  i4_lo = 1
  i4_hi = 10
  seed = 123456789
  m, seed = i4_uniform_ab ( i4_lo, i4_hi, seed )
  n, seed = i4_uniform_ab ( i4_lo, i4_hi, seed )
  k, seed = i4_uniform_ab ( i4_lo, i4_hi, seed )
#
#  Get a random A.
#
  r8_lo = -5.0
  r8_hi = +5.0
  a, seed = r8mat_uniform_ab ( m, n, r8_lo, r8_hi, seed )
#
#  Get a random X.
#
  r8_lo = -5.0
  r8_hi = +5.0
  x, seed = r8mat_uniform_ab ( n, k, r8_lo, r8_hi, seed )
#
#  Compute B = A * X.
#
  b = r8mat_mm ( m, n, k, a, x )
#
#  Compute || A*X-B||
#
  enorm = r8mat_is_solution ( m, n, k, a, x, b )
  
  print ''
  print '  A is %d by %d' % ( m, n )
  print '  X is %d by %d' % ( n, k )
  print '  B is %d by %d' % ( m, k )
  print '  Frobenius error in A*X-B is %g' % ( enorm )

  print ''
  print 'R8MAT_IS_SOLUTION_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8mat_is_solution_test ( )
  timestamp ( )
