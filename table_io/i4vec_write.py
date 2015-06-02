#!/usr/bin/env python

def i4vec_write ( filename, n, a ):

#*****************************************************************************80
#
## I4VEC_WRITE writes an I4VEC to a file.
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
#    Input, string FILENAME, the name of the output file.
#
#    Input, integer N, the number of entris in A.
#
#    Input, integer A(N), the matrix.
#
  output = open ( filename, 'w' )

  for i in range ( 0, n ):
    s = '  %d\n' % ( a[i] )
    output.write ( s )

  output.close ( )

  return

def i4vec_write_test ( ):

#*****************************************************************************80
#
## I4VEC_WRITE_TEST tests I4VEC_WRITE.
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
  import numpy as np

  print ''
  print 'I4VEC_WRITE_TEST:'
  print '  Test I4VEC_WRITE, which writes an I4VEC to a file.'
  filename = 'i4vec_write_test.txt'
  n = 5
  a = np.array ( ( 11, 22, 33, 44, 55 ) )
  i4vec_write ( filename, n, a )

  print ''
  print '  Created file "%s".' % ( filename )

  print ''
  print 'I4VEC_WRITE_TEST:'
  print '  Normal end of execution.'

  return
  
if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4vec_write_test ( )
  timestamp ( )
