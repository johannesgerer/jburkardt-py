#!/usr/bin/env python

def i4mat_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## I4MAT_PRINT_SOME prints out a portion of an I4MAT.
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

  for j2lo in range ( max ( jlo, 0 ), min ( jhi, n - 1 ), incx ):

    j2hi = j2lo + incx - 1
    j2hi = min ( j2hi, n - 1 )
    j2hi = min ( j2hi, jhi )
    
    print ''
    print '  Col: ',

    for j in range ( j2lo, j2hi + 1 ):
      print '%7d  ' % ( j ),

    print ''
    print '  Row'

    i2lo = max ( ilo, 0 )
    i2hi = min ( ihi, m - 1 )

    for i in range ( i2lo, i2hi + 1 ):

      print ' %4d: ' % ( i ),
      
      for j in range ( j2lo, j2hi + 1 ):
        print '%7d  ' % ( a[i,j] ),

      print ''

  return

def i4mat_print_some_test ( ):

#*****************************************************************************80
#
## I4MAT_PRINT_SOME_TEST tests I4MAT_PRINT_SOME.
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
  print 'I4MAT_PRINT_SOME_TEST'
  print '  I4MAT_PRINT_SOME prints some of an I4MAT.'

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11, 12, 13, 14, 15, 16 ], 
    [ 21, 22, 23, 24, 25, 26 ], 
    [ 31, 32, 33, 34, 35, 36 ], 
    [ 41, 42, 43, 44, 45, 46 ] ], dtype = np.int32 )
  i4mat_print_some ( m, n, v, 0, 3, 2, 5, '  Here is I4MAT, rows 0:2, cols 3:5:' )

  print ''
  print 'I4MAT_PRINT_SOME_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp

  timestamp ( )
  i4mat_print_some_test ( )
  timestamp ( )


