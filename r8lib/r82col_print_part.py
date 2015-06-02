#!/usr/bin/env python
#
def r82col_print_part ( n, a, max_print, title ):

#*****************************************************************************80
#
## R82COL_PRINT_PART prints "part" of an R82COL.
#
#  Discussion:
#
#    An R82COL is an (N,2) array of R8's.
#
#    The user specifies MAX_PRINT, the maximum number of lines to print.
#
#    If N, the size of the vector, is no more than MAX_PRINT, then
#    the entire vector is printed, one entry per line.
#
#    Otherwise, if possible, the first MAX_PRINT-2 entries are printed,
#    followed by a line of periods suggesting an omission,
#    and the last entry.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 December 2001
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of entries of the vector.
#
#    Input, real A(N,2), the vector to be printed.
#
#    Input, integer MAX_PRINT, the maximum number of lines
#    to print.
#
#    Input, string TITLE, a title.
#
  if ( 0 < max_print ):

    if ( 0 < n ):

      if ( 0 < len ( title ) ):
        print ''
        print title

      print ''

      if ( n <= max_print ):

        for i in range ( 0, n ):
          print '  %4d  %14g  %14g' % ( i, a[i,0], a[i,1] )
 
      elif ( 3 <= max_print ):

        for i in range ( 0, max_print - 2 ):
          print '  %4d  %14g  %14g' % ( i, a[i,0], a[i,1] )
        print '  ....  ..............  ..............'
        i = n - 1
        print '  %4d  %14g  %14g' % ( i, a[i,0], a[i,1] )

      else:

        for i in range ( 0, max_print - 1 ):
          print '  %4d  %14g  %14g' % ( i, a[i,0], a[i,1] )
        i = max_print - 1
        print '  %4d  %14g  %14g  ...more entries...' % ( i, a[i,0], a[i,1] )

  return

def r82col_print_part_test ( ):

#*****************************************************************************80
#
## R82COL_PRINT_PART_TEST tests R82COL_PRINT_PART.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 April 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ''
  print 'R82COL_PRINT_PART_TEST'
  print '  R82COL_PRINT_PART prints an R82COL.'

  n = 10

  v = np.array ( [ \
    [  11,  12 ], \
    [  21,  22 ], \
    [  31,  32 ], \
    [  41,  42 ], \
    [  51,  52 ], \
    [  61,  62 ], \
    [  71,  72 ], \
    [  81,  82 ], \
    [  91,  92 ], \
    [ 101, 102 ] ] )

  max_print = 2
  r82col_print_part ( n, v, max_print, '  Output with MAX_PRINT = 2' )

  max_print = 5
  r82col_print_part ( n, v, max_print, '  Output with MAX_PRINT = 5' )

  max_print = 25
  r82col_print_part ( n, v, max_print, '  Output with MAX_PRINT = 25' )

  print ''
  print 'R82COL_PRINT_PART_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r82col_print_part_test ( )
  timestamp ( )


