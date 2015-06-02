#!/usr/bin/env python

def r4vec_print ( n, a, title ):

#*****************************************************************************80
#
## R4VEC_PRINT prints an R4VEC.
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
#    Input, integer N, the dimension of the vector.
#
#    Input, real A(N), the vector to be printed.
#
#    Input, string TITLE, a title.
#
  print ''
  print title
  print ''
  for i in range ( 0, n ):
    print '%6d  %12g' % ( i, a[i] )

def r4vec_print_test ( ):

#*****************************************************************************80
#
## R4VEC_PRINT_TEST tests R4VEC_PRINT.
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
  print 'R4VEC_PRINT_TEST'
  print '  R4VEC_PRINT prints an R4VEC.'

  n = 4
  v = np.array ( [ 123.456, 0.000005, -1.0E+06, 3.14159265 ], dtype = np.float32 )
  r4vec_print ( n, v, '  Here is an R4VEC:' )

  print ''
  print 'R4VEC_PRINT_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r4vec_print_test ( )
  timestamp ( )

