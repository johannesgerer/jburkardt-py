#!/usr/bin/env python
#
def r8mat_data_read ( filename, m, n ):

#*****************************************************************************80
#
## R8MAT_DATA_READ reads the data from an R8MAT.
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
#    Input, integer M, the number of rows in the file.
#
#    Input, integer N, the number of columns in the file.
#
#    Output, real TABLE(M,N), the data.
#
  import numpy as np

  j = -1

  input = open ( filename, 'r' )

  table = np.zeros ( ( m, n ) )

  i = 0
  for line in input:

    if ( line[0] == '#' ):
      continue
    else:
      j = 0
      for word in line.strip().split():
        table[i,j] = float ( word )
        j = j + 1
      i = i + 1

  input.close ( )

  return table

def r8mat_data_read_test ( ):

#*****************************************************************************80
#
## R8MAT_DATA_READ_TEST tests R8MAT_DATA_READ.
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
  from r8mat_print import r8mat_print

  print ''
  print 'R8MAT_DATA_READ_TEST:'
  print '  Test R8MAT_DATA_READ, which reads data from an R8MAT.'

  m = 5
  n = 3
  filename = 'r8mat_write_test.txt'
  a = r8mat_data_read ( filename, m, n )
  r8mat_print ( m, n, a, '  Data read from file:' )

  print ''
  print 'R8MAT_DATA_READ_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8mat_data_read_test ( )
  timestamp ( )
