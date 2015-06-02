#!/usr/bin/env python
#
def r8vec_header_read ( filename ):

#*****************************************************************************80
#
## R8VEC_HEADER_READ reads the header from an R8VEC.
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
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
#    Input, string FILENAME, the name of the input file.
#
#    Output, integer M, the number of rows in the file.
#
  from file_row_count import file_row_count

  m = file_row_count ( filename )

  return m

def r8vec_header_read_test ( ):

#*****************************************************************************80
#
## R8VEC_HEADER_READ_TEST tests R8VEC_HEADER_READ.
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
  print 'R8VEC_HEADER_READ_TEST:'
  print '  Test R8VEC_HEADER_READ, which counts rows in a file'
  print '  containing an R8VEC.'

  filename = 'r8vec_write_test.txt'
  m = r8vec_header_read ( filename )
  print ''
  print '  File "%s" contains %d rows.' % ( filename, m )

  print ''
  print 'R8VEC_HEADER_READ_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8vec_header_read_test ( )
  timestamp ( )
