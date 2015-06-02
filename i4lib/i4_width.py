#!/usr/bin/env python
#
def i4_width ( i ):

#*****************************************************************************80
#
## I4_WIDTH returns the "width" of an I4.
#
#  Example:
#
#        I  VALUE
#    -----  -------
#    -1234    5
#     -123    4
#      -12    3
#       -1    2
#        0    1
#        1    1
#       12    2
#      123    3
#     1234    4
#    12345    5
#
#  Discussion:
#
#    The width of an integer is the number of characters necessary to print it.
#
#    The width of an integer can be useful when setting the appropriate output
#    format for a vector or array of values.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer I, the number whose width is desired.
#
#    Output, integer VALUE, the number of characters necessary to represent
#    the integer in base 10, including a negative sign if necessary.
#
  from i4_log_10 import i4_log_10

  if ( 0 <= i ):
    value = i4_log_10 ( i ) + 1
  else:
    value = i4_log_10 ( i ) + 2
 
  return value

def i4_width_test ( ):

#*****************************************************************************80
#
## I4_WIDTH_TEST tests I4_WIDTH.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  test_num = 13
  x_test = np.array ( [ 0, 1, 2, 3, 9, 10, 11, 99, 101, -1, -2, -3, -9 ] )

  print ''
  print 'I4_WIDTH_TEST'
  print '  I4_WIDTH determines the printing "width" of an I4.'
  print ' '
  print '            I4      I4_WIDTH'
  print ''

  for test in range ( 0, test_num ):
    x = x_test[test];
    print '  %12d  %12d' % ( x, i4_width ( x ) )
#
#  Terminate.
#
  print ''
  print 'I4_WIDTH_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_width_test ( )
  timestamp ( )
