#!/usr/bin/env python

def r8vec_write ( filename, n, a ):

#*****************************************************************************80
#
## R8VEC_WRITE writes an R8VEC to a file.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 November 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, string FILENAME, the name of the output file.
#
#    Input, integer N, the number of entries in A.
#
#    Input, real A(N), the matrix.
#
  output = open ( filename, 'w' )

  for i in range ( 0, n ):
    s = '  %g\n' % ( a[i] )
    output.write ( s )

  output.close ( )

  return

def r8vec_write_test ( ):

#*****************************************************************************80
#
## R8VEC_WRITE_TEST tests R8VEC_WRITE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 November 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ''
  print 'R8VEC_WRITE_TEST:'
  print '  Test R8VEC_WRITE, which writes an R8VEC to a file.'
  filename = 'r8vec_write_test.txt'
  n = 5
  a = np.array ( ( 1.1, 2.2, 3.3, 4.4, 5.5 ) )
  r8vec_write ( filename, n, a )

  print ''
  print '  Created file "%s".' % ( filename )

  print ''
  print 'R8VEC_WRITE_TEST:'
  print '  Normal end of execution.'

  return
  
if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8vec_write_test ( )
  timestamp ( )
