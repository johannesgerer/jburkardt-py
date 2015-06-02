#!/usr/bin/env python
#
def file_row_count ( filename ):

#*****************************************************************************80
#
## FILE_ROW_COUNT counts the number of rows (lines) in a file.
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
#    Input, string FILENAME, the name of the file.
#
#    Output, integer ROW_COUNT, the number of rows in the file.
#
  row_count = -1

  input = open ( filename, 'r' )

  row_count = 0

  for line in input:

    if ( line[0] == '#' ):
      continue
    else:

      wc = 0
      for word in line.strip().split():
         wc = wc + 1

      if ( wc == 0 ):
        continue
      else:
        row_count = row_count + 1

  input.close ( )

  return row_count

def file_row_count_test ( ):

#*****************************************************************************80
#
## FILE_ROW_COUNT_TEST tests FILE_ROW_COUNT.
#
  print ''
  print 'FILE_ROW_COUNT_TEST:'
  print '  Python version'
  print '  Count the number of rows in a text file.'
  filename = 'filum_prb_4by5.txt'
  row_count = file_row_count ( filename )
  print ''
  print '  Number of rows in "%s" is %d' % ( filename, row_count )

  return

if ( __name__ == '__main__' ):

#*****************************************************************************80
#
## MAIN calls FILE_ROW_COUNT_TEST.
#
  file_row_count_test ( )
  print ''
  print 'FILE_ROW_COUNT_TEST:'
  print '  Normal end of execution.'
