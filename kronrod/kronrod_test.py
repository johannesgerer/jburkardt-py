#!/usr/bin/env python

#*****************************************************************************80
#
## KRONROD_TEST tests the KRONROD functions.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 April 2013
#
#  Author:
#
#    John Burkardt
#
from kronrod_test01 import kronrod_test01
from kronrod_test02 import kronrod_test02
from kronrod_test03 import kronrod_test03
from timestamp import timestamp

timestamp ( )

print ''
print 'KRONROD_TEST'
print '  Python version.'
print '  Test the KRONROD library.'

kronrod_test01 ( )
kronrod_test02 ( )
kronrod_test03 ( )
#
#  Terminate.
#
print ''
print 'KRONROD_TEST'
print '  Normal end of execution.'
print ''
timestamp ( )

