#!/usr/bin/env python
#
def i4mat_data_read ( filename, m, n ):

#*****************************************************************************80
#
## I4MAT_DATA_READ reads the data from an I4MAT.
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
#    Input, integer M, the number of rows in the file.
#
#    Input, integer N, the number of columns in the file.
#
#    Output, integer TABLE(M,N), the data.
#
  import numpy as np

  j = -1

  input = open ( filename, 'r' )

  table = np.zeros ( ( m, n ), dtype=np.int )

  i = 0
  for line in input:

    if ( line[0] == '#' ):
      continue
    else:
      j = 0
      for word in line.strip().split():
        table[i,j] = int ( word )
        j = j + 1
      i = i + 1

  input.close ( )

  return table

def i4mat_data_read_test ( ):

#*****************************************************************************80
#
## I4MAT_DATA_READ_TEST tests I4MAT_DATA_READ.
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
  from i4mat_print import i4mat_print

  print ''
  print 'I4MAT_DATA_READ_TEST:'
  print '  Test I4MAT_DATA_READ, which reads data from an I4MAT.'

  m = 5
  n = 3
  filename = 'i4mat_write_test.txt'
  a = i4mat_data_read ( filename, m, n )
  i4mat_print ( m, n, a, '  Data read from file:' )

  return

if ( __name__ == '__main__' ):
  i4mat_data_read_test ( )
  print ''
  print 'I4MAT_DATA_READ_TEST:'
  print '  Normal end of execution.'

