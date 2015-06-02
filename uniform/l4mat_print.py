#!/usr/bin/env python

def l4mat_print ( m, n, a, title ):

#*****************************************************************************80
#
## L4MAT_PRINT prints an L4MAT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 October 2014
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
  from l4mat_print_some import l4mat_print_some

  l4mat_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

def l4mat_print_test ( ):

#*****************************************************************************80
#
## L4MAT_PRINT_TEST tests L4MAT_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 December 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from l4mat_uniform import l4mat_uniform

  print ''
  print 'L4MAT_PRINT_TEST:'
  print '  Test L4MAT_PRINT, which prints an L4MAT.'

  m = 5
  n = 12
  seed = 123456789
  a, seed = l4mat_uniform ( m, n, seed )
  title = '  A 5 x 3 integer matrix:'
  l4mat_print ( m, n, a, title )

  print ''
  print 'L4MAT_PRINT_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  l4mat_print_test ( )
  timestamp ( )




