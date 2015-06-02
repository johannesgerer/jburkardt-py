#!/usr/bin/env python

def r8_power ( r, p ):

#*****************************************************************************80
#
## R8_POWER computes the P-th power of R.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    25 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real R, the base.
#
#    Input, integer P, the power, which may be negative.
#
#    Output, real VALUE, the value of R**P.
#
  from math import floor

  mults = 0
#
#  Force P to be an integer.
#
  p = floor ( p )
#
#  Special case.  R^0 = 1.
#
  if ( p == 0 ):
    value = 1.0
#
#  Special case.  Positive powers of 0 are 0.
#  For negative powers, we go ahead and compute it, hoping software will complain.
#
  elif ( r == 0.0 ):
    if ( 0 < p ):
      value = 0.0
    else:
      value = r ** p
  elif ( 1 <= p ):
    value = r ** p
  else:
    value = r ** p

  return value

def r8_power_test ( ):

#*****************************************************************************80
#
## R8_POWER_TEST tests R8_POWER.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 April 2009
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'R8_POWER_TEST'
  print '  R8_POWER computes R^P.'
  print ''
  print '      R          P       R8_POWER'
  print ''

  for i in range ( -5, 6 ):

    r = 2.0
    p = i
    value = r8_power ( r, p )
    print '  %14f  %5d  %14f' % ( r, p, value )
#
#  Terminate.
#
  print ''
  print 'R8_POWER_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_power_test ( )
  timestamp ( )
