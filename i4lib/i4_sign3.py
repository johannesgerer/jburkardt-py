#!/usr/bin/env python

def i4_sign3 ( i ):

#*****************************************************************************80
#
## I4_SIGN3 returns the three-way sign of an integer.
#
#  Discussion:
#
#    The value is +1 if the number is positive, 0 if zero, and -1 otherwise.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 September 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer I, the number whose sign is desired.
#
#    Output, integer VALUE, the sign of I.
#
  if ( i < 0 ):
    value = -1
  elif ( i == 0 ):
    value = 0
  else:
    value = +1

  return value

def i4_sign3_test ( ):

#*****************************************************************************80
#
## I4_SIGN3_TEST tests I4_SIGN3.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 September 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  test_num = 5

  i4_vec = np.array ( ( -10, -7, 0, 5, 9 ) )

  print ''
  print 'I4_SIGN3_TEST'
  print '  I4_SIGN3 returns the three-way sign of an I4.'
  print ''
  print '    I4  I4_SIGN3(I4)'
  print ''

  for test in range ( 0, test_num ):
    i4 = i4_vec[test]
    s = i4_sign3 ( i4 )
    print '  %4d  %11d' % ( i4, s )
#
#  Terminate.
#
  print ''
  print 'I4_SIGN3_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_sign3_test ( )
  timestamp ( )
