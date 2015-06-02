#!/usr/bin/env python

def r8mat_is_inverse ( n, a, b ):

#*****************************************************************************80
#
## R8MAT_IS_INVERSE measures the error in a matrix inverse.
#
#  Discussion:
#
#    An R8MAT is a matrix of real values.
#
#    This routine returns the sum of the Frobenius norms of
#      A * B - I and B * A - I.
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
#    Input, integer N, the order of the matrix.
#
#    Input, real A(N,N), the matrix.
#
#    Input, real B(M,N), the inverse matrix.
#
#    Output, real VALUE, the Frobenius norm
#    of the difference matrices A * B - I and B * A - I.
#
  from identity import identity
  from r8mat_mm import r8mat_mm
  from r8mat_sub import r8mat_sub
  from r8mat_norm_fro import r8mat_norm_fro

  ab = r8mat_mm ( n, n, n, a, b )
  ba = r8mat_mm ( n, n, n, b, a )
  id = identity ( n, n )
  d1 = r8mat_sub ( n, n, ab, id )
  d2 = r8mat_sub ( n, n, ba, id )
 
  value = r8mat_norm_fro ( n, n, d1 ) \
        + r8mat_norm_fro ( n, n, d2 )

  return value

def r8mat_is_inverse_test ( ):

#*****************************************************************************80
#
## R8MAT_IS_INVERSE_TEST tests R8MAT_IS_INVERSE.
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
#
#  This is the BODEWIG matrix.
#
  m = 4
  n = m

  a = np.array ( [ \
    [ 2.0,  1.0,  3.0,  4.0 ], \
    [ 1.0, -3.0,  1.0,  5.0 ], \
    [ 3.0,  1.0,  6.0, -2.0 ], \
    [ 4.0,  5.0, -2.0, -1.0 ] ] )

  b  = np.array ( [ \
    [ -139.0 / 568.0,  165.0 / 568.0,  79.0 / 568.0,  111.0 / 568.0 ], \
    [  165.0 / 568.0, -155.0 / 568.0, -57.0 / 568.0,   -1.0 / 568.0 ], \
    [   79.0 / 568.0,  -57.0 / 568.0,  45.0 / 568.0,  -59.0 / 568.0 ], \
    [  111.0 / 568.0,   -1.0 / 568.0, -59.0 / 568.0,  -11.0 / 568.0 ] ] )

  print ''
  print 'R8MAT_IS_INVERSE_TEST:'
  print '  R8MAT_IS_INVERSE tests the error in a matrix inverse:'
  print '    A * B - I = 0'
  print '    B * A - I = 0'

  r8mat_print ( m, n, a, '  Matrix A:' )
  r8mat_print ( m, n, b, '  Inverse matrix B:' )

  value = r8mat_is_inverse ( n, a, b  )

  print ''
  print '  Frobenius norm of error is %g' % ( value )

  print ''
  print 'R8MAT_IS_INVERSE_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8mat_is_inverse_test ( )
  timestamp ( )
