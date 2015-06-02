#!/usr/bin/env python
#
def c4vec_print ( n, a, title ):

#*****************************************************************************80
#
## C4VEC_PRINT prints a C4VEC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the dimension of the vector.
#
#    Input, complex A(N), the vector to be printed.
#
#    Input, string TITLE, a title.
#
  print ''
  print title
  print ''
  for i in range ( 0, n ):
    print '%6d  %12g  %12g' % ( i, a.real[i], a.imag[i] )

def c4vec_print_test ( ):

#*****************************************************************************80
#
## C4VEC_PRINT_TEST tests C4VEC_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 December 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ''
  print 'C4VEC_PRINT_TEST'
  print '  C4VEC_PRINT prints an C4VEC.'

  n = 4
  v = np.array ( [ complex ( 1.0, 2.0 ), \
                   complex ( 3.0, 4.0 ), \
                   complex ( 5.0, 6.0 ), \
                   complex ( 7.0, 8.0 ) ], dtype = np.complex64 )
  c4vec_print ( n, v, '  Here is an C4VEC:' )

  print ''
  print 'C4VEC_PRINT_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  c4vec_print_test ( )
  timestamp ( )


