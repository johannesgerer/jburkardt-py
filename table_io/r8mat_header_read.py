#!/usr/bin/env python
#
def r8mat_header_read ( filename ):

#*****************************************************************************80
#
## R8MAT_HEADER_READ reads the header from an R8MAT.
#
#  Discussion:
#
#    An R8MAT is an array of R8's.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, string FILENAME, the name of the input file.
#
#    Output, integer M, the number of columns in the file.
#
#    Output, integer N, the number of rows in the file.
#
  from file_column_count import file_column_count
  from file_row_count import file_row_count

  m = file_row_count ( filename )
  n = file_column_count ( filename )

  return m, n

def r8mat_header_read_test ( ):

#*****************************************************************************80
#
## R8MAT_HEADER_READ_TEST tests R8MAT_HEADER_READ.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ''
  print 'R8MAT_HEADER_READ_TEST:'
  print '  Test R8MAT_HEADER_READ, which counts rows and columns in a file'
  print '  containing an R8MAT.'

  filename = 'r8mat_write_test.txt'
  m, n = r8mat_header_read ( filename )
  print ''
  print '  File "%s" contains %d rows and %d columns.' % ( filename, m, n )

  print ''
  print 'R8MAT_HEADER_READ_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8mat_header_read_test ( )
  timestamp ( )
