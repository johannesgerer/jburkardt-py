#!/usr/bin/env python

def r8mat_is_plu ( m, n, a, p, l, u ):

#*****************************************************************************80
#
## R8MAT_IS_PLU measures the error in a PLU factorization.
#
#  Discussion:
#
#    An R8MAT is a matrix of real values.
#
#    This routine computes the Frobenius norm of
#
#      A - P * L * U
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the order of the matrix.
#
#    Input, real A(M,N), the matrix.
#
#    Input, real P(M,M), L(M,M), U(M,N), the PLU factors.
#
#    Output, real VALUE, the Frobenius norm
#    of the difference matrix A - P * L * U.
#
  from r8mat_mm import r8mat_mm
  from r8mat_sub import r8mat_sub
  from r8mat_norm_fro import r8mat_norm_fro

  lu = r8mat_mm ( m, m, n, l, u )
  plu = r8mat_mm ( m, m, n, p, lu )

  d = r8mat_sub ( m, n, a, plu )
 
  value = r8mat_norm_fro ( m, n, d )

  return value

def r8mat_is_plu_test ( ):

#*****************************************************************************80
#
## R8MAT_IS_PLU_TEST tests R8MAT_IS_PLU.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 March 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from r8mat_print import r8mat_print
  from r8vec_print import r8vec_print
#
#  This is the CARRY ( 4.0, 4 ) matrix.
#
  m = 4
  n = m

  a = np.array ( [ \
    [ 5.0,  7.0,  6.0,  5.0 ], \
    [ 7.0, 10.0,  8.0,  7.0 ], \
    [ 6.0,  8.0, 10.0,  9.0 ], \
    [ 5.0,  7.0,  9.0, 10.0 ] ] )

  p = np.array ( [ \
    [ 0.0,  0.0,  0.0,  1.0 ], \
    [ 1.0,  0.0,  0.0,  0.0 ], \
    [ 0.0,  1.0,  0.0,  0.0 ], \
    [ 0.0,  0.0,  1.0,  0.0 ] ] )

  l = np.array ( [ \
   [ 1.0,                0.00,  0.00,  0.00 ], \
   [ 0.857142857142857,  1.00,  0.00,  0.00 ], \
   [ 0.714285714285714,  0.25,  1.00,  0.00 ], \
   [ 0.714285714285714,  0.25, -0.20,  1.00 ] ] )

  u = np.array ( [ \
    [ 7.00, 10.0,               8.0,               7.00 ], \
    [ 0.00, -0.571428571428571, 3.142857142857143, 3.00 ], \
    [ 0.00,  0.0,               2.50,              4.25 ], \
    [ 0.00,  0.0,               0.0,               0.10 ] ] )

  print ''
  print 'R8MAT_IS_PLU_TEST:'
  print '  R8MAT_IS_PLU tests the error in the P*L*U factorization:'
  print '    A - P * L * U = 0'

  r8mat_print ( m, n, a, '  Matrix A:' )
  r8mat_print ( m, m, p, '  Permutation P:' )
  r8mat_print ( m, m, l, '  Lower triangular L:' )
  r8mat_print ( m, n, u, '  Upper triangular U:' )

  value = r8mat_is_plu ( m, n, a, p, l, u  )

  print ''
  print '  Frobenius norm of A-P*L*U is %g' % ( value )

  print ''
  print 'R8MAT_IS_PLU_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8mat_is_plu_test ( )
  timestamp ( )
