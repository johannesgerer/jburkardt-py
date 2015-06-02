#!/usr/bin/env python

def l4vec_print ( n, a, title ):

#*****************************************************************************80
#
## L4VEC_PRINT prints an L4VEC.
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
#  Parameters:
#
#    Input, integer N, the dimension of the vector.
#
#    Input, integer A(N), the vector to be printed.
#
#    Input, string TITLE, a title.
#
  print ''
  print title
  print ''
  for i in range ( 0, n ):
    if ( a[i] == 0 ):
      print '%6d  F' % ( i )
    else:
      print '%6d  T' % ( i )

  return

def l4vec_print_test ( ):

#*****************************************************************************80
#
## L4VEC_PRINT_TEST tests L4VEC_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from l4vec_uniform import l4vec_uniform

  print ''
  print 'L4VEC_PRINT_TEST'
  print '  L4VEC_PRINT prints an L4VEC.'

  n = 10
  seed = 123456789
  v, seed = l4vec_uniform ( n, seed )
  l4vec_print ( n, v, '  Here is an L4VEC:' )

  print ''
  print 'L4VEC_PRINT_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  l4vec_print_test ( )
  timestamp ( )


