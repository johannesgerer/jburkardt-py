#!/usr/bin/env python
#
def i4vec_header_read ( filename ):

#*****************************************************************************80
#
## I4VEC_HEADER_READ reads the header from an I4VEC.
#
#  Discussion:
#
#    An I4VEC is a vector of I4's.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 December 2014
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
  from file_row_count import file_row_count

  m = file_row_count ( filename )

  return m

def i4vec_header_read_test ( ):

#*****************************************************************************80
#
## I4VEC_HEADER_READ_TEST tests I4VEC_HEADER_READ.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 December 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ''
  print 'I4VEC_HEADER_READ_TEST:'
  print '  Test I4VEC_HEADER_READ, which counts rows in a file'
  print '  containing an I4VEC.'

  filename = 'i4vec_write_test.txt'
  m = i4vec_header_read ( filename )
  print ''
  print '  File "%s" contains %d rows.' % ( filename, m )

  print ''
  print 'I4VEC_HEADER_READ_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4vec_header_read_test ( )
  timestamp ( )
