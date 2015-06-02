#!/usr/bin/env python

#*****************************************************************************80
#
## TIMER_TEST tests the TIMER library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    13 May 2013
#
#  Author:
#
#    John Burkardt
#
from timer_test01 import timer_test01
from timer_test02 import timer_test02
from timestamp import timestamp

timestamp ( )
print ''
print 'TIMER_TEST'
print '  Python version:'
print '  Test the TIMER library.'

timer_test01 ( )
timer_test02 ( )
#
#  Terminate.
#
print ''
print 'TIMER_TEST:'
print '  Normal end of execution.'

print ''
timestamp ( )
