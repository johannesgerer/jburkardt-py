#!/usr/bin/env python
#
def r8_ceiling ( x ):

#*****************************************************************************80
#
## R8_CEILING rounds an R8 up to the nearest integral R8.
#
#  Example:
#
#    X         Value
#
#   -1.1      -1.0
#   -1.0      -1.0
#   -0.9       0.0
#   -0.1       0.0
#    0.0       0.0
#    0.1       1.0
#    0.9       1.0
#    1.0       1.0
#    1.1       2.0
#    2.9       3.0
#    3.0       3.0
#    3.14159   4.0
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
#    Input, real X, the number to be rounded up.
#
#    Output, real VALUE, the rounded value of X.
#
  from math import ceil

  value = ceil ( x )

  return value

def r8_ceiling_test ( ):

#*****************************************************************************80
#
## R8_CEILING_TEST tests R8_CEILING.
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
  print ''
  print 'R8_CEILING_TEST'
  print '  R8_CEILING rounds a value up.'
  print ''
  print '       X       R8_CEILING(X)'
  print ''

  for i in range ( -6, 7 ):
    rval = i / 5.0
    ival = r8_ceiling ( rval )
    print '  %14f  %8d' % ( rval, ival )
#
#  Terminate.
#
  print ''
  print 'R8_CEILING_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_ceiling_test ( )
  timestamp ( )
