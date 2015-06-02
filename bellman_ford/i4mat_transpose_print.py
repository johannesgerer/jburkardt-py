#!/usr/bin/env python

def i4mat_transpose_print ( m, n, a, title ):

#*****************************************************************************80
#
## I4MAT_TRANSPOSE_PRINT prints an I4MAT, transposed.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 November 2014
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
#    Input, integer A(M,N), the matrix.
#
#    Input, string TITLE, a title.
#
  from i4mat_transpose_print_some import i4mat_transpose_print_some

  i4mat_transpose_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

def i4mat_transpose_print_test ( ):

#*****************************************************************************80
#
## I4MAT_TRANSPOSE_PRINT_TEST tests I4MAT_TRANSPOSE_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 November 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ''
  print 'I4MAT_TRANSPOSE_PRINT_TEST:'
  print '  Test I4MAT_TRANSPOSE_PRINT, which prints an I4MAT, tranposed.'

  m = 5
  n = 3
  a = np.array ( ( \
    ( 11, 12, 13 ), \
    ( 21, 22, 23 ), \
    ( 31, 32, 33 ), \
    ( 41, 42, 43 ), \
    ( 51, 52, 53 ) ) )
  title = '  A 5 x 3 integer matrix:'
  i4mat_transpose_print ( m, n, a, title )

  print ''
  print 'I4MAT_TRANSPOSE_PRINT_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4mat_transpose_print_test ( )
  timestamp ( )

