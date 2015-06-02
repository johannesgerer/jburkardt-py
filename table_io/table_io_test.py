#!/usr/bin/env python

def table_io_test ( ):

#*****************************************************************************80
#
## TABLE_IO_TEST tests the TABLE_IO library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    08 April 2015
#
#  Author:
#
#    John Burkardt
#
  from file_column_count      import file_column_count_test
  from file_row_count         import file_row_count_test
  from i4_log_10              import i4_log_10_test
  from i4mat_data_read        import i4mat_data_read_test
  from i4mat_header_read      import i4mat_header_read_test
  from i4mat_indicator        import i4mat_indicator_test
  from i4mat_print            import i4mat_print_test
  from i4mat_print_some       import i4mat_print_some_test
  from i4mat_write            import i4mat_write_test
  from i4vec_data_read        import i4vec_data_read_test
  from i4vec_header_read      import i4vec_header_read_test
  from i4vec_print            import i4vec_print_test
  from i4vec_write            import i4vec_write_test
  from r8mat_data_read        import r8mat_data_read_test
  from r8mat_header_read      import r8mat_header_read_test
  from r8mat_indicator        import r8mat_indicator_test
  from r8mat_print            import r8mat_print_test
  from r8mat_print_some       import r8mat_print_some_test
  from r8mat_transpose_write  import r8mat_transpose_write_test
  from r8mat_write            import r8mat_write_test
  from r8vec_data_read        import r8vec_data_read_test
  from r8vec_header_read      import r8vec_header_read_test
  from r8vec_print            import r8vec_print_test
  from r8vec_write            import r8vec_write_test
  from timestamp              import timestamp_test

  print ''
  print 'TABLE_IO_TEST'
  print '  Python version:'
  print '  Test the TABLE_IO library.'

  file_column_count_test ( )
  file_row_count_test ( )

  i4_log_10_test ( )

  i4mat_indicator_test ( )
  i4mat_print_test ( )
  i4mat_print_some_test ( )

  i4vec_print_test ( )

  r8mat_indicator_test ( )
  r8mat_print_test ( )
  r8mat_print_some_test ( )

  r8vec_print_test ( )

  timestamp_test ( )
#
#  Write an I4MAT to a file, then read header and data.
#
  i4mat_write_test ( )
  i4mat_header_read_test ( )
  i4mat_data_read_test ( )
#
#  Write an I4VEC to a file, then read header and data.
#
  i4vec_write_test ( )
  i4vec_header_read_test ( )
  i4vec_data_read_test ( )
#
#  Write an R8MAT transposed to a file.
#
  r8mat_transpose_write_test ( )
#
#  Write an R8MAT to a file, then read header and data.
#
  r8mat_write_test ( )
  r8mat_header_read_test ( )
  r8mat_data_read_test ( )
#
#  Write an R8VEC to a file, then read header and data.
#
  r8vec_write_test ( )
  r8vec_header_read_test ( )
  r8vec_data_read_test ( )
#
#  Terminate.
#
  print ''
  print 'TABLE_IO_TEST'
  print '  Normal end of execution.'

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  table_io_test ( )
  timestamp ( )
