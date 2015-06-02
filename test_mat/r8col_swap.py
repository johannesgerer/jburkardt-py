#!/usr/bin/env python

def r8col_swap ( m, n, a, j1, j2 ):

#*****************************************************************************80
#
## R8COL_SWAP swaps two columns of an R8COL.
#
#  Example:
#
#    Input:
#
#      M = 3, N = 4, I = 2, J = 4
#
#      A = (
#        1  2  3  4
#        5  6  7  8
#        9 10 11 12 )
#
#    Output:
#
#      A = (
#        1  4  3  2
#        5  8  7  6
#        9 12 11 10 )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 February 2005
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns in the array.
#
#    Input, real A(M,N), an array of N columns of length M.
#
#    Input, integer J1, J2, the columns to be swapped.
#
#    Output, real A(M,N), the array, with columns swapped.
#
  from sys import exit

  if ( j1 < 0 or n <= j1 or j2 < 0 or n <= j2 ):
    print ''
    print 'R8COL_SWAP - Fatal error!'
    print '  J1 or J2 is out of bounds.'
    print '  J1 =   %d' % ( j1 )
    print '  J2 =   %d' % ( j2 )
    print '  N =    %d' % ( n )
    exit ( 'R8COL_SWAP - Fatal error!' )

  if ( j1 == j2 ):
    return

  for i in range ( 0, m ):
    t       = a[i,j1]
    a[i,j1] = a[i,j2]
    a[i,j2] = t

  return a

def r8col_swap_test ( ):

#*****************************************************************************80
#
## R8COL_SWAP_TEST tests R8COL_SWAP;
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 April 2009
#
#  Author:
#
#    John Burkardt
#
  from r8mat_indicator import r8mat_indicator
  from r8mat_print import r8mat_print

  m = 3;
  n = 4;

  print ''
  print 'R8COL_SWAP_TEST'
  print '  For an R8COL, an array of column vectors;'
  print '  R8COL_SWAP swaps two columns;'

  a = r8mat_indicator ( m, n )

  r8mat_print ( m, n, a, '  The array:' )

  icol1 = 0
  icol2 = 2

  print '';
  print '  Swap columns %d and %d' % ( icol1, icol2 )

  a = r8col_swap ( m, n, a, icol1, icol2 )

  r8mat_print ( m, n, a, '  The updated matrix:' )

  print ''
  print 'R8COL_SWAP_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8col_swap_test ( )
  timestamp ( )
