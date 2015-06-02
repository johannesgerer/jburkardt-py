#!/usr/bin/env python
#
def normal_01_moment ( order ):

#*****************************************************************************80
#
## NORMAL_01_MOMENT evaluates the moments of the Normal 01 PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer ORDER, the order of the moment.
#
#    Output, real VALUE, the value of the moment.
# 
  from r8_factorial2 import r8_factorial2

  if ( ( order % 2 ) == 0 ):
    value = r8_factorial2 ( order - 1 )
  else:
    value = 0.0

  return value

def normal_01_moment_test ( ):

#*****************************************************************************80
#
## NORMAL_01_MOMENT_TEST tests NORMAL_01_MOMENT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 March 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'NORMAL_01_MOMENT_TEST'
  print '  NORMAL_01_MOMENT evaluates moments of the Normal 01 PDF;'
  print ''
  print '   Order     Moment'
  print ''

  for order in range ( 0, +11 ):

    moment = normal_01_moment ( order )
    print '  %6d  %14.6g' % ( order, moment )
#
#  Terminate.
#
  print ''
  print 'NORMAL_01_MOMENT_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  normal_01_moment_test ( )
  timestamp ( )
