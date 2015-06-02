#!/usr/bin/env python
#
def i4mat_header_read ( filename ):

#*****************************************************************************80
#
## I4MAT_HEADER_READ reads the header from an I4MAT.
#
#  Discussion:
#
#    An I4MAT is an array of I4's.
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
#    Output, integer M, the number of rows in the file.
#
#    Output, integer N, the number of columns in the file.
#
  from file_column_count import file_column_count
  from file_row_count import file_row_count

  m = file_row_count ( filename )
  n = file_column_count ( filename )

  return m, n

def i4mat_header_read_test ( ):

#*****************************************************************************80
#
## I4MAT_HEADER_READ_TEST tests I4MAT_HEADER_READ.
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
  print 'I4MAT_HEADER_READ_TEST:'
  print '  Test I4MAT_HEADER_READ, which counts rows and columns in a file'
  print '  containing an I4MAT.'

  filename = 'i4mat_write_test.txt'
  m, n = i4mat_header_read ( filename )
  print ''
  print '  File "%s" contains %d rows and %d columns.' % ( filename, m, n )

  return

if ( __name__ == '__main__' ):
  i4mat_header_read_test ( )
  print ''
  print 'I4MAT_HEADER_READ_TEST:'
  print '  Normal end of execution.'

