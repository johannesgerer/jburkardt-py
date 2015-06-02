#!/usr/bin/env python

def r8_epsilon_compute ( ):

#*****************************************************************************80
#
## R8_EPSILON_COMPUTE returns the R8 roundoff unit.
#
#  Discussion:
#
#    The roundoff unit is a number R which is a power of 2 with the 
#    property that, to the precision of the computer's arithmetic,
#      1 < 1 + R
#    but 
#      1 = ( 1 + R / 2 )
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
#    Output, real VALUE, the roundoff unit.
#
  one = 1.0
  value = one
  temp = value / 2.0
  test = one + temp

  while ( one < test ):
    value = temp
    temp = value / 2.0
    test = one + temp

  return value

def r8_epsilon_compute_test ( ):

#*****************************************************************************80
#
## R8_EPSILON_COMPUTE_TEST tests R8_EPSILON_COMPUTE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 September 2012
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'R8_EPSILON_COMPUTE_TEST'
  print '  R8_EPSILON_COMPUTE computes the R8 roundoff unit.'
  print ''

  r = r8_epsilon_compute ( )
  print '  R = R8_EPSILON_COMPUTE() = %e' % ( r )

  s = ( 1.0 + r ) - 1.0
  print '  ( 1 + R ) - 1            = %e' % ( s )

  s = ( 1.0 + ( r / 2.0 ) ) - 1.0
  print '  ( 1 + (R/2) ) - 1        = %e' % ( s )
#
#  Terminate.
#
  print ''
  print 'R8_EPSILON_COMPUTE_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  r8_epsilon_compute_test ( )
  timestamp ( )
