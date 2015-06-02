#!/usr/bin/env python
#
def file_column_count ( filename ):

#*****************************************************************************80
#
## FILE_COLUMN_COUNT counts the number of words in a typical column of a file.
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
#    Output, integer COLUMN_COUNT, the number of words in a typical column.
#
  column_count = -1

  input = open ( filename, 'r' )

  column_count = 0

  for line in input:

    if ( line[0] == '#' ):
      continue
    else:

      wc = 0
      for word in line.strip().split():
         wc = wc + 1

      if ( wc == 0 ):
        continue
      elif ( column_count == 0 ):
        column_count = wc
        break

  input.close ( )

  return column_count

def file_column_count_test ( ):

#*****************************************************************************80
#
## FILE_COLUMN_COUNT_TEST tests FILE_COLUMN_COUNT.
#
  print ''
  print 'FILE_COLUMN_COUNT_TEST:'
  print '  Python version'
  print '  Count the number of columns in a typical text file line.'
  filename = 'filum_prb_4by5.txt'
  column_count = file_column_count ( filename )
  print ''
  print '  Number of columns in "%s" is %d' % ( filename, column_count )

  return

if ( __name__ == '__main__' ):

#*****************************************************************************80
#
## MAIN calls FILE_COLUMN_COUNT_TEST.
#
  file_column_count_test ( )
  print ''
  print 'FILE_COLUMN_COUNT_TEST:'
  print '  Normal end of execution.'
