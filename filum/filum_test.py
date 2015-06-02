#!/usr/bin/env python

#*****************************************************************************80
#
## FILUM_TEST tests the FILUM library.
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
from file_column_count import file_column_count_test
from file_row_count import file_row_count_test
from timestamp import timestamp

timestamp ( )
print ''
print 'FILUM_TEST'
print '  Python version:'
print '  Test the FILUM library.'

file_column_count_test ( )
file_row_count_test ( )
#
#  Terminate.
#
print ''
print 'FILUM_TEST:'
print '  Normal end of execution.'
print ''
timestamp ( )
