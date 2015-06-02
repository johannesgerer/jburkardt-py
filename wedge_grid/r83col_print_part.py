#!/usr/bin/env python
#
def r83col_print_part ( n, a, max_print, title ):

#*****************************************************************************80
#
## R83COL_PRINT_PART prints "part" of an R83COL.
#
#  Discussion:
#
#    An R83COL is a (3,N) array of R8's.
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
#    11 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of entries of the vector.
#
#    Input, real A(N,3), the vector to be printed.
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
          print '  %4d  %14g  %14g  %14g' % ( i, a[i,0], a[i,1], a[i,2] )
 
      elif ( 3 <= max_print ):

        for i in range ( 0, max_print - 2 ):
          print '  %4d  %14g  %14g  %14g' % ( i, a[i,0], a[i,1], a[i,2] )
        print '  ....  ..............  ..............  ..............'
        i = n - 1
        print '  %4d  %14g  %14g  %14g' % ( i, a[i,0], a[i,1], a[i,2] )

      else:

        for i in range ( 0, max_print - 1 ):
          print '  %4d  %14g  %14g  %14g' % ( i, a[i,0], a[i,1], a[i,2] )
        i = max_print - 1
        print '  %4d  %14g  %14g  %14g  ...more entries...' \
          % ( i, a[i,0], a[i,1], a[i,2] )

  return

def r83col_print_part_test ( ):

#*****************************************************************************80
#
## R83COL_PRINT_PART_TEST tests R83COL_PRINT_PART.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 April 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ''
  print 'R83COL_PRINT_PART_TEST'
  print '  R83COL_PRINT_PART prints part of an R83COL.'

  n = 10

  v = np.array ( [ \
    [  11,  12,  13 ], \
    [  21,  22,  23 ], \
    [  31,  32,  33 ], \
    [  41,  42,  43 ], \
    [  51,  52,  53 ], \
    [  61,  62,  63 ], \
    [  71,  72,  73 ], \
    [  81,  82,  83 ], \
    [  91,  92,  93 ], \
    [ 101, 102, 103 ] ] )

  max_print = 2
  r83col_print_part ( n, v, max_print, '  Output with MAX_PRINT = 2' )

  max_print = 5
  r83col_print_part ( n, v, max_print, '  Output with MAX_PRINT = 5' )

  max_print = 25
  r83col_print_part ( n, v, max_print, '  Output with MAX_PRINT = 25' )

  print ''
  print 'R82COL_PRINT_PART_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r83col_print_part_test ( )
  timestamp ( )
