#!/usr/bin/env python

def r4mat_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## R4MAT_PRINT_SOME prints out a portion of an R4MAT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 December 2014
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

  for j2lo in range ( max ( jlo, 0 ), min ( jhi, n - 1 ), incx ):

    j2hi = j2lo + incx - 1
    j2hi = min ( j2hi, n - 1 )
    j2hi = min ( j2hi, jhi )
    
    print ''
    print '  Col: ',

    for j in range ( j2lo, j2hi + 1 ):
      print '%7d       ' % ( j ),

    print ''
    print '  Row'

    i2lo = max ( ilo, 0 )
    i2hi = min ( ihi, m - 1 )

    for i in range ( i2lo, i2hi + 1 ):

      print '%7d :' % ( i ),
      
      for j in range ( j2lo, j2hi + 1 ):
        print '%12g  ' % ( a[i,j] ),

      print ''

  return

def r4mat_print_some_test ( ):

#*****************************************************************************80
#
## R4MAT_PRINT_SOME_TEST tests R4MAT_PRINT_SOME.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 December 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ''
  print 'R4MAT_PRINT_SOME_TEST'
  print '  R4MAT_PRINT_SOME prints some of an R4MAT.'

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = np.float32 )
  r4mat_print_some ( m, n, v, 0, 3, 2, 5, '  Here is an R4MAT:' )

  print ''
  print 'R4MAT_PRINT_SOME_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r4mat_print_some_test ( )
  timestamp ( )

