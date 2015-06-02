#!/usr/bin/env python
#
def i4_power ( i, j ):

#*****************************************************************************80
#
## I4_POWER returns the value of I to the power J.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer I, J, the base and the power.  J should be nonnegative.
#
#    Output, integer VALUE, the value of I^J.
#
  from sys import exit

  if ( j < 0 ):

    if ( i == 1 ):
      value = 1
    elif ( i == 0 ):
      print ''
      print 'I4_POWER - Fatal error!'
      print '  I^J requested, with I = 0 and J negative.'
      exit ( 'I4_POWER - Fatal error!' );
    else:
      value = 0

  elif ( j == 0 ):

    if ( i == 0 ):
      print ''
      print 'I4_POWER - Fatal error!'
      print '  I^J requested, with I = 0 and J = 0.'
      exit ( 'I4_POWER - Fatal error!' );
    else:
      value = 1

  elif ( j == 1 ):

    value = i

  else:

    value = 1
    for k in range ( 1, j + 1 ):
      value = value * i

  return value

def i4_power_test ( ):

#*****************************************************************************80
#
## I4_POWER_TEST tests I4_POWER.
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

  test_num = 7
  i_test = np.array ( [ 0, 1, 2, 3, 10, -1, -2 ] )
  j_test = np.array ( [ 1, 2, 3, 3, 3, 4, 5 ] )

  print ''
  print 'I4_POWER_TEST'
  print '  I4_POWER computes I^J'
  print ''
  print '         I       J  I4_POWER(I,J)'
  print ''

  for test in range ( 0, test_num ):
    i = i_test[test]
    j = j_test[test]
    print '  %8d  %8d  %8d' % ( i, j, i4_power ( i, j ) )

#
#  Terminate.
#
  print ''
  print 'I4_POWER_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_power_test ( )
  timestamp ( )
