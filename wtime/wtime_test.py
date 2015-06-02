#!/usr/bin/env python

#*****************************************************************************80
#
## WTIME_TEST tests the WTIME library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    12 May 2013
#
#  Author:
#
#    John Burkardt
#
from wtime_test01 import wtime_test01
from timestamp import timestamp

timestamp ( )
print ''
print 'WTIME_TEST'
print '  Python version:'
print '  Test the WTIME library.'

wtime_test01 ( )
wtime_test02 ( )
#
#  Terminate.
#
print ''
print 'WTIME_TEST:'
print '  Normal end of execution.'
print ''
timestamp ( )
