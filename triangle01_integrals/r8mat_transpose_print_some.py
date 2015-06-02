#!/usr/bin/env python

def r8mat_transpose_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## R8MAT_TRANSPOSE_PRINT_SOME prints a portion of an R8MAT, transposed.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 November 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns of the matrix.
#
#    Input, real A(M,N), an M by N matrix to be printed.
#
#    Input, integer ILO, JLO, the first row and column to print.
#
#    Input, integer IHI, JHI, the last row and column to print.
#
#    Input, string TITLE, a title.
#
  incx = 5

  print ''
  print title

  if ( m <= 0 or n <= 0 ):
    print ''
    print '  (None)'
    return

  for i2lo in range ( max ( ilo, 0 ), min ( ihi, m - 1 ), incx ):

    i2hi = i2lo + incx - 1
    i2hi = min ( i2hi, m - 1 )
    i2hi = min ( i2hi, ihi )
    
    print ''
    print '  Row: ',

    for i in range ( i2lo, i2hi + 1 ):
      print '%7d       ' % ( i ),

    print ''
    print '  Col'

    j2lo = max ( jlo, 0 )
    j2hi = min ( jhi, n - 1 )

    for j in range ( j2lo, j2hi + 1 ):

      print '%7d :' % ( j ),
      
      for i in range ( i2lo, i2hi + 1 ):
        print '%12g  ' % ( a[i,j] ),

      print ''

  return

def r8mat_transpose_print_some_test ( ):

#*****************************************************************************80
#
## R8MAT_TRANSPOSE_PRINT_SOME_TEST tests R8MAT_TRANSPOSE_PRINT_SOME.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ''
  print 'R8MAT_TRANSPOSE_PRINT_SOME_TEST'
  print '  R8MAT_TRANSPOSE_PRINT_SOME prints some of an R8MAT, transposed.'

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = np.float64 )
  r8mat_transpose_print_some ( m, n, v, 0, 3, 2, 5, '  R8MAT, rows 0:2, cols 3:5:' )

  print ''
  print 'R8MAT_TRANSPOSE_PRINT_SOME_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8mat_transpose_print_some_test ( )
  timestamp ( )


