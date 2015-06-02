#!/usr/bin/env python

def i4_ceiling ( x ) :

#*****************************************************************************80
#
## I4_CEILING rounds an R8 up to the next I4.
#
#  Example:
#
#    X         Value
#
#   -1.1      -1
#   -1.0      -1
#   -0.9       0
#   -0.1       0
#    0.0       0
#    0.1       1
#    0.9       1
#    1.0       1
#    1.1       2
#    2.9       3
#    3.0       3
#    3.14159   4
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
#    Input, real X, the number to be rounded up.
#
#    Output, integer VALUE, the rounded value of X.
#
  from math import ceil

  value = int ( ceil ( x ) )

  return value

def i4_ceiling_test ( ):

#*****************************************************************************80
#
## I4_CEILING_TEST tests I4_CEILING.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 September 2014
#
#  Author:
#
#    John Burkardt
#
  from r8_uniform_ab import r8_uniform_ab

  r8_lo = -100.0
  r8_hi =  100.0
  seed = 123456789

  print ' '
  print 'I4_CEILING_TEST'
  print '  I4_CEILING evaluates the "ceiling" of a real number.'
  print ' '
  print '      R8    I4_CEILING(R8)'
  print ' '

  for i in range ( 0, 10 ):
    r8, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
    i4 = i4_ceiling ( r8 )
    print '  %8.4f            %4d' % ( r8, i4 )
#
#  Terminate.
#
  print ' '
  print 'I4_CEILING_TEST'
  print '  Normal end of execution.'

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_ceiling_test ( )
  timestamp ( )
