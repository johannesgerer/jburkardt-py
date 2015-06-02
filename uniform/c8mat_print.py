#!/usr/bin/env python

def c8mat_print ( m, n, a, title ):

#*****************************************************************************80
#
## C8MAT_PRINT prints a C8MAT.
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
#    Input, integer M, the number of rows in A.
#
#    Input, integer N, the number of columns in A.
#
#    Input, complex A(M,N), the matrix.
#
#    Input, string TITLE, a title.
#
  from c8mat_print_some import c8mat_print_some

  c8mat_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

  return

def c8mat_print_test ( ):

#*****************************************************************************80
#
## C8MAT_PRINT_TEST tests C8MAT_PRINT.
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
  print 'C8MAT_PRINT_TEST'
  print '  C8MAT_PRINT prints an C8MAT.'

  m = 4
  n = 3
  v = np.array ( [ \
    [ complex(10.0, 1.0), complex(10.0, 2.0), complex(10.0, 3.0) ], \
    [ complex(20.0, 1.0), complex(20.0, 2.0), complex(20.0, 3.0) ], \
    [ complex(30.0, 1.0), complex(30.0, 2.0), complex(30.0, 3.0) ], \
    [ complex(40.0, 1.0), complex(40.0, 2.0), complex(40.0, 3.0) ] ], \
    dtype = np.complex128 )

  c8mat_print ( m, n, v, '  Here is a C8MAT:' )

  print ''
  print 'C8MAT_PRINT_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  c8mat_print_test ( )
  timestamp ( )

