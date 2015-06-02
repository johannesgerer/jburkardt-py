#!/usr/bin/env python

def l4mat_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## L4MAT_PRINT_SOME prints out a portion of an L4MAT.
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
  incx = 35

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
      print '%2d' % ( j ),

    print ''
    print '  Row'

    i2lo = max ( ilo, 0 )
    i2hi = min ( ihi, m - 1 )

    for i in range ( i2lo, i2hi + 1 ):

      print ' %4d: ' % ( i ),
      
      for j in range ( j2lo, j2hi + 1 ):
        if ( a[i,j] == 0 ):
          print ' F',
        else:
          print ' T',
      print ''

  return

def l4mat_print_some_test ( ):

#*****************************************************************************80
#
## L4MAT_PRINT_SOME_TEST tests L4MAT_PRINT_SOME.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 December 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from l4mat_uniform import l4mat_uniform

  print ''
  print 'L4MAT_PRINT_SOME_TEST'
  print '  L4MAT_PRINT_SOME prints some of an L4MAT.'

  m = 4
  n = 6
  seed = 123456789
  v, seed = l4mat_uniform ( m, n, seed )
  l4mat_print_some ( m, n, v, 0, 3, 2, 5, '  Here is L4MAT, rows 0:2, cols 3:5:' )

  print ''
  print 'L4MAT_PRINT_SOME_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  l4mat_print_some_test ( )
  timestamp ( )


