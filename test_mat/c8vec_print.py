#!/usr/bin/env python
#
def c8vec_print ( n, a, title ):

#*****************************************************************************80
#
## C8VEC_PRINT prints a C8VEC.
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

def c8vec_print_test ( ):

#*****************************************************************************80
#
## C8VEC_PRINT_TEST tests C8VEC_PRINT.
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
  print 'C8VEC_PRINT_TEST'
  print '  C8VEC_PRINT prints an C8VEC.'

  n = 4
  v = np.array ( [ complex ( 1.0, 2.0 ), \
                   complex ( 3.0, 4.0 ), \
                   complex ( 5.0, 6.0 ), \
                   complex ( 7.0, 8.0 ) ], dtype = np.complex128 )
  c8vec_print ( n, v, '  Here is a C8VEC:' )

  print ''
  print 'C8VEC_PRINT_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  c8vec_print_test ( )
  timestamp ( )


