#!/usr/bin/env python

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

if ( __name__ == '__main__' ) :
  print ''
  print 'MAIN_DEMO:'
  print '  Quick demonstration for I4_POWER.'
  print '  which computes K = I ^ J for integers I and J.'
  print
  print '   I   J     K'
  print ' '
  i = 4
  j = 3
  k = i4_power ( i, j )
  print '  %2d  %2d  %4d' % ( i, j, k )
  i = -2
  j = 7
  k = i4_power ( i, j )
  print '  %2d  %2d  %4d' % ( i, j, k )
  
