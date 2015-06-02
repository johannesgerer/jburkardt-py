#!/usr/bin/env python

def r8mat_indicator ( m, n ):

#*****************************************************************************80
#
## R8MAT_INDICATOR sets up an indicator R8MAT.
#
#  Discussion:
#
#    The value of each entry suggests its location, as in:
#
#      11  12  13  14
#      21  22  23  24
#      31  32  33  34
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the number of rows of the matrix.
#    M must be positive.
#
#    Input, integer N, the number of columns of the matrix.
#    N must be positive.
#
#    Output, real TABLE(M,N), the indicator table.
#
  import numpy as np
  from i4_log_10 import i4_log_10

  table = np.zeros ( ( m, n ), dtype = np.float64 )

  fac = 10 ** ( i4_log_10 ( n ) + 1 )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      table[i,j] = fac * ( i + 1 ) + ( j + 1 )

  return table

def r8mat_indicator_test ( ):

#*****************************************************************************80
#
## R8MAT_INDICATOR_TEST tests R8MAT_INDICATOR.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    03 December 2014
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'R8MAT_INDICATOR_TEST'
  print '  R8MAT_INDICATOR creates an "indicator" R8MAT.'

  m = 5
  n = 4
  a = r8mat_indicator ( m, n )
  r8mat_print ( m, n, a, '  The indicator matrix:' )

  print ''
  print 'R8MAT_INDICATOR_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8mat_indicator_test ( )
  timestamp ( )
