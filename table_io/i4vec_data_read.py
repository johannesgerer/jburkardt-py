#!/usr/bin/env python
#
def i4vec_data_read ( filename, m ):

#*****************************************************************************80
#
## I4VEC_DATA_READ reads the data from an I4VEC.
#
#  Discussion:
#
#    An I4VEC is an array of R8's.
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
#    Input, integer M, the number of rows in the file.
#
#    Output, real TABLE(M), the data.
#
  import numpy as np

  j = -1

  input = open ( filename, 'r' )

  table = np.zeros ( m, dtype = np.int32 )

  i = 0
  for line in input:

    if ( line[0] == '#' ):
      continue
    else:
      table[i] = int ( line.strip() )
      i = i + 1

  input.close ( )

  return table

def i4vec_data_read_test ( ):

#*****************************************************************************80
#
## I4VEC_DATA_READ_TEST tests I4VEC_DATA_READ.
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
  from i4vec_print import i4vec_print

  print ''
  print 'I4VEC_DATA_READ_TEST:'
  print '  Test I4VEC_DATA_READ, which reads data from an I4VEC.'

  m = 5
  n = 3
  filename = 'i4vec_write_test.txt'
  a = i4vec_data_read ( filename, m )
  i4vec_print ( m, a, '  Data read from file:' )

  print ''
  print 'I4VEC_DATA_READ_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4vec_data_read_test ( )
  timestamp ( )
