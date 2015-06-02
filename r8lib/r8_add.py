#!/usr/bin/env python
#
def r8_add ( x, y ):

#*****************************************************************************80
#
## R8_ADD adds two R8's.
#
#  Discussion:
#
#    An R8 is a double precision real value.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, Y, the numbers to be added.
#
#    Output, real VALUE, the sum of X and Y.
#
  value = x + y

  return value

def r8_add_test ( ):

#*****************************************************************************80
#
## R8_ADD_TEST tests R8_ADD.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 May 2015
#
#  Author:
#
#    John Burkardt
#
  from r8_uniform_ab import r8_uniform_ab

  print ''
  print 'R8_ADD_TEST'
  print '  R8_ADD adds two R8\'s.' 
  print ''
  print '       R1             R2              R3              R4'
  print '                                      R1+R2     R8_ADD(R1,R2)'
  print ''

  r8_lo = - 500.0
  r8_hi = + 500.0
  seed = 123456789

  for test in range ( 0, 5 ):

    r1, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
    r2, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
    r3 = r1 + r2
    r4 = r8_add ( r1, r2 )

    print '  %14.6g  %14.6g  %14.6g  %14.6g' % ( r1, r2, r3, r4 )
#
#  Terminate.
#
  print ''
  print 'R8_ADD_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_add_test ( )
  timestamp ( )
