#!/usr/bin/env python

def i4mat_transpose_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## I4MAT_TRANSPOSE_PRINT_SOME prints a portion of an I4MAT, transposed.
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
#    Input, integer M, N, the number of rows and columns of the matrix.
#
#    Input, integer A(M,N), an M by N matrix to be printed.
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
      print '%7d  ' % ( i ),

    print ''
    print '  Col'

    j2lo = max ( jlo, 0 )
    j2hi = min ( jhi, n - 1 )

    for j in range ( j2lo, j2hi + 1 ):

      print ' %4d: ' % ( j ),
      
      for i in range ( i2lo, i2hi + 1 ):
        print '%7d  ' % ( a[i,j] ),

      print ''

  return

def i4mat_transpose_print_some_test ( ):

#*****************************************************************************80
#
## I4MAT_TRANSPOSE_PRINT_SOME_TEST tests I4MAT_TRANSPOSE_PRINT_SOME.
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
  print 'I4MAT_TRANSPOSE_PRINT_SOME_TEST'
  print '  I4MAT_TRANSPOSE_PRINT_SOME prints some of an I4MAT, transposed.'

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11, 12, 13, 14, 15, 16 ], 
    [ 21, 22, 23, 24, 25, 26 ], 
    [ 31, 32, 33, 34, 35, 36 ], 
    [ 41, 42, 43, 44, 45, 46 ] ], dtype = np.int32 )
  i4mat_transpose_print_some ( m, n, v, 0, 3, 2, 5, \
    '  Here is I4MAT, rows 0:2, cols 3:5:' )
#
#  Terminate.
#
  print ''
  print 'I4MAT_TRANSPOSE_PRINT_SOME_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4mat_transpose_print_some_test ( )
  timestamp ( )

