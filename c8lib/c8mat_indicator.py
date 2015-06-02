#!/usr/bin/env python

def c8mat_indicator ( m, n ):

#*****************************************************************************80
#
## C8MAT_INDICATOR returns the indicator matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    15 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the order of the matrix.
#
#    Output, complex C(M,N), the indicator matrix.
#
  import numpy

  c = numpy.zeros ( ( m, n ), 'complex' )

  for j in range ( 0, n ): 
    for i in range ( 0, m ):
      c[i][j] = complex ( i + 1, - j - 1 )

  return c

def c8mat_indicator_test ( ):

#*****************************************************************************80
#
## C8MAT_INDICATOR_TEST tests C8MAT_INDICATOR.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    14 February 2015
#
#  Author:
#
#    John Burkardt
#
  from c8mat_print import c8mat_print

  import numpy as np

  m = 5
  n = 3

  print ''
  print 'C8MAT_INDICATOR_TEST'
  print '  C8MAT_INDICATOR returns the complex indicator matrix.'

  c = c8mat_indicator ( m, n )

  c8mat_print ( m, n, c, '  Indicator matrix:' )

  print ''
  print 'C8MAT_INDICATOR_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  c8mat_indicator_test ( )
  timestamp ( )
