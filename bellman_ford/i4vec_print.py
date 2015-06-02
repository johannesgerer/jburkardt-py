#!/usr/bin/env python

def i4vec_print ( n, a, title ):

#*****************************************************************************80
#
## I4VEC_PRINT prints an I4VEC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 August 2014
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
    print '%6d  %6d' % ( i, a[i] )

def i4vec_print_test ( ):

#*****************************************************************************80
#
## I4VEC_PRINT_TEST tests I4VEC_PRINT.
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

  print ''
  print 'I4VEC_PRINT_TEST'
  print '  I4VEC_PRINT prints an I4VEC.'

  n = 4
  v = np.array ( [ 91, 92, 93, 94 ], dtype = np.int32 )
  i4vec_print ( n, v, '  Here is an I4VEC:' )

  print ''
  print 'I4VEC_PRINT_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp

  timestamp ( )
  i4vec_print_test ( )
  timestamp ( )


