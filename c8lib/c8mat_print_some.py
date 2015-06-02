#!/usr/bin/env python

def c8mat_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## C8MAT_PRINT_SOME prints out a portion of an C8MAT.
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
#    Input, integer M, N, the number of rows and columns of the matrix.
#
#    Input, complex A(M,N), an M by N matrix to be printed.
#
#    Input, integer ILO, JLO, the first row and column to print.
#
#    Input, integer IHI, JHI, the last row and column to print.
#
#    Input, string TITLE, a title.
#
  incx = 4

  print ''
  print title

  if ( m <= 0 or n <= 0 ):
    print ''
    print '  (None)'
    return

  for j2lo in range ( max ( jlo, 0 ), min ( jhi, n - 1 ), incx ):

    j2hi = j2lo + incx - 1
    j2hi = min ( j2hi, n - 1 )
    j2hi = min ( j2hi, jhi )
    
    print ''
    print '  Col: ',

    for j in range ( j2lo, j2hi + 1 ):
      print '       %7d              ' % ( j ),

    print ''
    print '  Row'

    i2lo = max ( ilo, 0 )
    i2hi = min ( ihi, m - 1 )

    for i in range ( i2lo, i2hi + 1 ):

      print '%7d :' % ( i ),
      
      for j in range ( j2lo, j2hi + 1 ):
        print '%12g  %12gi ' % ( a.real[i,j], a.imag[i,j] ),

      print ''

  return

def c8mat_print_some_test ( ):

#*****************************************************************************80
#
## C8MAT_PRINT_SOME_TEST tests C8MAT_PRINT_SOME.
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
  print 'C8MAT_PRINT_SOME_TEST'
  print '  C8MAT_PRINT_SOME prints some of an C8MAT.'

  m = 4
  n = 6
  v = np.array ( [ \
    [ complex(10.0, 1.0), complex(10.0, 2.0), complex(10.0, 3.0), \
      complex(10.0, 4.0), complex(10.0, 5.0), complex(10.0, 6.0) ], \
    [ complex(20.0, 1.0), complex(20.0, 2.0), complex(20.0, 3.0), \
      complex(20.0, 4.0), complex(20.0, 5.0), complex(20.0, 6.0) ], \
    [ complex(30.0, 1.0), complex(30.0, 2.0), complex(30.0, 3.0), \
      complex(30.0, 4.0), complex(30.0, 5.0), complex(30.0, 6.0) ], \
    [ complex(40.0, 1.0), complex(40.0, 2.0), complex(40.0, 3.0), \
      complex(40.0, 4.0), complex(40.0, 5.0), complex(40.0, 6.0) ] ], \
    dtype = np.complex128 )

  c8mat_print_some ( m, n, v, 0, 3, 2, 5, '  Here is a C8MAT:' )

  print ''
  print 'C8MAT_PRINT_SOME_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  c8mat_print_some_test ( )
  timestamp ( )


