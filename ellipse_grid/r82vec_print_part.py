#!/usr/bin/env python
#
def r82vec_print_part ( n, a, max_print, title ):

#*****************************************************************************80
#
## R82VEC_PRINT_PART prints "part" of an R82VEC.
#
#  Discussion:
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
#    Input, real A(2,N), the vector to be printed.
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
          print '  %4d  %14f  %14f' % ( i, a[0,i], a[1,i] )
 
      elif ( 3 <= max_print ):

        for i in range ( 0, max_print - 2 ):
          print '  %4d  %14f  %14f' % ( i, a[0,i], a[1,i] )
        print '  ....  ..............  ..............'
        i = n - 1
        print '  %4d  %14f  %14f' % ( i, a[0,i], a[1,i] )

      else:

        for i in range ( 0, max_print - 1 ):
          print '  %4d  %14f  %14f' % ( i, a[0,i], a[1,i] )
        i = max_print - 1
        print '  %4d  %14f  %14f  ...more entries...' % ( i, a[0,i], a[1,i] )

  return

def r82vec_print_part_test ( ):

#*****************************************************************************80
#
## R82VEC_PRINT_PART_TEST tests R82VEC_PRINT_PART.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 April 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ''
  print 'R82VEC_PRINT_PART_TEST'
  print '  R82VEC_PRINT_PART prints an R8VEC.'

  n = 10

  v = np.array ( [ \
    [  11,  12, 13, 14, 15, 16, 17, 18, 19, 20 ], \
    [  21,  22, 23, 24, 25, 26, 27, 28, 29, 30 ] ] )

  max_print = 2
  r82vec_print_part ( n, v, max_print, '  Output with MAX_PRINT = 2' )

  max_print = 5
  r82vec_print_part ( n, v, max_print, '  Output with MAX_PRINT = 5' )

  max_print = 25
  r82vec_print_part ( n, v, max_print, '  Output with MAX_PRINT = 25' )

  print ''
  print 'R82VEC_PRINT_PART_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r82vec_print_part_test ( )
  timestamp ( )


