#!/usr/bin/env python

def i4mat_write ( filename, m, n, a ):

#*****************************************************************************80
#
## I4MAT_WRITE writes an I4MAT to a file.
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
#    Input, integer A(M,N), the matrix.
#
  output = open ( filename, 'w' )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      s = '  %d' % ( a[i,j] )
      output.write ( s )
    output.write ( '\n' )

  output.close ( )

  return

def i4mat_write_test ( ):

#*****************************************************************************80
#
## I4MAT_WRITE_TEST tests I4MAT_WRITE.
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
  import numpy as np

  print ''
  print 'I4MAT_WRITE_TEST:'
  print '  Test I4MAT_WRITE, which writes an I4MAT to a file.'
  filename = 'i4mat_write_test.txt'
  m = 5
  n = 3
  a = np.array ( (  \
    ( 11, 12, 13 ), \
    ( 21, 22, 23 ), \
    ( 31, 32, 33 ), \
    ( 41, 42, 43 ), \
    ( 51, 52, 53 ) ) )
  i4mat_write ( filename, m, n, a )

  print ''
  print '  Created file "%s".' % ( filename )

  print ''
  print 'I4MAT_WRITE_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4mat_write_test ( )
  timestamp ( )

