#!/usr/bin/env python
#
def i4vec_transpose_print ( n, a, title ):

#*****************************************************************************80
#
## I4VEC_TRANSPOSE_PRINT prints an I4VEC "transposed".
#
#  Example:
#
#    A = (/ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 /)
#    TITLE = 'My vector:  '
#
#    My vector:
#
#       1    2    3    4    5
#       6    7    8    9   10
#      11
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of components of the vector.
#
#    Input, integer A(N), the vector to be printed.
#
#    Input, string TITLE, a title.
#
  print ''
  print '%s' % ( title )

  for i in range ( 0, n ):
    if ( i % 5 == 0 ):
      print ''
    print '  %12d' % ( a[i] ),
  print ''

  return

def i4vec_transpose_print_test ( ):

#*****************************************************************************80
#
## I4VEC_TRANSPOSE_PRINT_TEST tests I4VEC_TRANSPOSE_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 April 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ''
  print 'I4VEC_TRANSPOSE_PRINT_TEST'
  print '  I4VEC_TRANSPOSE_PRINT prints an I4VEC'
  print '  with 5 entries to a row, and an optional title.'

  n = 12
  a = np.zeros ( n, dtype = np.int32 )
  
  for i in range ( 0, n ):
    a[i] = i + 1

  i4vec_transpose_print ( n, a, '  My array:  ' )
#
#  Terminate.
#
  print ''
  print 'I4VEC_TRANSPOSE_PRINT_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4vec_transpose_print_test ( )
  timestamp ( )


