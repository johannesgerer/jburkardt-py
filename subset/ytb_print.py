#!/usr/bin/env python
#
def ytb_print ( n, a, title ):

#*****************************************************************************80
#
## YTB_PRINT prints a Young tableau.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the integer that is partitioned.
#
#    Input, integer A(N), describes the Young tableau.
#    A[I-1] is the row of the tableau on which I occurs.
#
#    Input, string TITLE, an optional title.
#
  print ''
  if ( 0 < len ( title ) ):
    print title

  row = 0

  while ( True ):

    row = row + 1

    row_length = 0

    for jm1 in range ( 0, n ):

      j = jm1 + 1

      if ( a[jm1] == row ):
        row_length = row_length + 1
        print '%4d  ' % ( j ),

    if ( row_length <= 0 ):
      break
    else:
      print ''

  return

def ytb_print_test ( ):

#*****************************************************************************80
#
## YTB_PRINT_TEST tests YTB_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ''
  print 'YTB_PRINT_TEST'
  print '  YTB_PRINT prints a Young tableau.'

  n = 6
  a = np.array ( [ 1, 1, 2, 2, 3, 1 ] )
  ytb_print ( n, a, '  A Young tableau:' )
#
#  Terminate.
#
  print ''
  print 'YTB_PRINT_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  ytb_print_test ( )
  timestamp ( )

