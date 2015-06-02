#!/usr/bin/env python

def r4mat_print ( m, n, a, title ):

#*****************************************************************************80
#
## R4MAT_PRINT prints an R4MAT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 December 2014
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
#    Input, real A(M,N), the matrix.
#
#    Input, string TITLE, a title.
#
  from r4mat_print_some import r4mat_print_some

  r4mat_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

  return

def r4mat_print_test ( ):

#*****************************************************************************80
#
## R4MAT_PRINT_TEST tests R4MAT_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 December 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ''
  print 'R4MAT_PRINT_TEST'
  print '  R4MAT_PRINT prints an R4MAT.'

  m = 4
  n = 3
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0 ], 
    [ 21.0, 22.0, 23.0 ], 
    [ 31.0, 32.0, 33.0 ], 
    [ 41.0, 42.0, 43.0 ] ], dtype = np.float32 )
  r4mat_print ( m, n, v, '  Here is an R4MAT:' )

  print ''
  print 'R4MAT_PRINT_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r4mat_print_test ( )
  timestamp ( )

