#!/usr/bin/env python

def r8mat_transpose_write ( filename, m, n, a ):

#*****************************************************************************80
#
## R8MAT_TRANSPOSE_WRITE writes the transpose of an R8MAT to a file.
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
#    Input, string FILENAME, the name of the output file.
#
#    Input, integer M, the number of rows in A.
#
#    Input, integer N, the number of columns in A.
#
#    Input, real A(M,N), the matrix.
#
  output = open ( filename, 'w' )

  for j in range ( 0, n ):
    for i in range ( 0, m ):
      s = '  %g' % ( a[i,j] )
      output.write ( s )
    output.write ( '\n' )

  output.close ( )

  return

def r8mat_transpose_write_test ( ):

#*****************************************************************************80
#
## R8MAT_TRANSPOSE_WRITE_TEST tests R8MAT_TRANSPOSE_WRITE.
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
  print 'R8MAT_TRANSPOSE_WRITE_TEST:'
  print '  Test R8MAT_TRANSPOSE_WRITE, which writes the transpose of an R8MAT to a file.'
  filename = 'r8mat_transpose_write_test.txt'
  m = 5
  n = 3
  a = np.array ( (  \
    ( 1.1, 1.2, 1.3 ), \
    ( 2.1, 2.2, 2.3 ), \
    ( 3.1, 3.2, 3.3 ), \
    ( 4.1, 4.2, 4.3 ), \
    ( 5.1, 5.2, 5.3 ) ) )
  r8mat_transpose_write ( filename, m, n, a )

  print ''
  print '  Created file "%s".' % ( filename )

  print ''
  print 'R8MAT_TRANSPOSE_WRITE_TEST:'
  print '  Normal end of execution.'

  return
  
if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8mat_transpose_write_test ( )
  timestamp ( )

