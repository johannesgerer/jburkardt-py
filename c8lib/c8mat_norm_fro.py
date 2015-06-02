#!/usr/bin/env python

def c8mat_norm_fro ( m, n, a ):

#*****************************************************************************80
#
## C8MAT_NORM_FRO returns the Frobenius norm of a C8MAT.
#
#  Discussion:
#
#    The Frobenius norm is defined as
#
#      C8MAT_NORM_FRO = sqrt (
#        sum ( 1 <= I <= M ) sum ( 1 <= j <= N ) A(I,J) * A(I,J) )
#
#    The matrix Frobenius norm is not derived from a vector norm, but
#    is compatible with the vector L2 norm, so that:
#
#      c8vec_norm_l2 ( A * x ) <= c8mat_norm_fro ( A ) * c8vec_norm_l2 ( x ).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the number of rows in A.
#
#    Input, integer N, the number of columns in A.
#
#    Input, complex A(M,N), the matrix whose norm is desired.
#
#    Output, real VALUE, the norm of A.
#
  import numpy as np

  value = \
    np.sqrt \
    ( \
      np.sum \
      ( \
        np.sum \
        ( \
          ( \
            np.abs \
            ( \
              a \
            ) \
          ) ** 2 \
        ) \
      ) \
   )

  return value

def c8mat_norm_fro_test ( ):

#*****************************************************************************80
#
## C8MAT_NORM_FRO_TEST tests C8MAT_NORM_FRO.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from c8mat_indicator import c8mat_indicator
  from c8mat_print import c8mat_print

  print ''
  print 'C8MAT_NORM_FRO_TEST'
  print '  C8MAT_NORM_FRO computes the Frobenius norm of a C8MAT.'

  m = 5
  n = 4
  c = c8mat_indicator ( m, n )

  c8mat_print ( m, n, c, '  The Indicator matrix:' )

  value = c8mat_norm_fro ( m, n, c )

  print ''
  print '  Frobenius norm = %g' % ( value )

  print ''
  print 'C8MAT_NORM_FRO_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  c8mat_norm_fro_test ( )
  timestamp ( )

