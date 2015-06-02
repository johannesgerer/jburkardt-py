#!/usr/bin/env python
#
def r8vec_data_read ( filename, m ):

#*****************************************************************************80
#
## R8VEC_DATA_READ reads the data from an R8VEC.
#
#  Discussion:
#
#    An R8VEC is an array of R8's.
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

  table = np.zeros ( m )

  i = 0
  for line in input:

    if ( line[0] == '#' ):
      continue
    else:
      table[i] = float ( line.strip() )
      i = i + 1

  input.close ( )

  return table

def r8vec_data_read_test ( ):

#*****************************************************************************80
#
## R8VEC_DATA_READ_TEST tests R8VEC_DATA_READ.
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
  from r8vec_print import r8vec_print

  print ''
  print 'R8VEC_DATA_READ_TEST:'
  print '  Test R8VEC_DATA_READ, which reads data from an R8VEC.'

  m = 5
  n = 3
  filename = 'r8vec_write_test.txt'
  a = r8vec_data_read ( filename, m )
  r8vec_print ( m, a, '  Data read from file:' )

  print ''
  print 'R8VEC_DATA_READ_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8vec_data_read_test ( )
  timestamp ( )
