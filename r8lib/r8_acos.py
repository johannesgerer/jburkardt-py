#!/usr/bin/env python
#
def r8_acos ( c ):

#*****************************************************************************80
#
## R8_ACOS computes the arc cosine function, with argument truncation.
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
#    Original FORTRAN77 version by Wayne Fullerton.
#    Python version by John Burkardt.
#
#  Parameters:
#
#    Input, real C, the argument.
#
#    Output, real VALUE, the arc-cosine of C.
#
  from math import acos
 
  c2 = max ( c,  - 1.0 )
  c2 = min ( c2, +1.0 )
  
  value = acos ( c2 )

  return value

def r8_acos_test ( ):

#*****************************************************************************80
#
## R8_ACOS_TEST tests R8_ACOS.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 November 2014
#
#  Author:
#
#    John Burkardt
#
  from math import acos
 
  print ''
  print 'R8_ACOS_TEST'
  print '  R8_ACOS computes the arc-cosine of an angle.'
  print ''
  print '       C            R8_ACOS(C)        ACOS(C)'
  print ''

  for test in range ( -1, 14 ):

    c = float ( test - 6 ) / 6.0

    if ( -1.0 <= c and c <= 1.0 ):
      print '  %14.6g  %14.6g  %14.6g' % ( c, r8_acos ( c ), acos ( c ) )
    else:
      print '  %14.6g  %14.6g' % ( c, r8_acos ( c ) )
#
#  Terminate.
#
  print ''
  print 'R8_ACOS_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_acos_test ( )
  timestamp ( )

