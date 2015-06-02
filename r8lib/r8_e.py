#!/usr/bin/env python

def r8_e ( ):

#*****************************************************************************80
#
## R8_E returns the base of the natural logarithm system.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real VALUE, the base of the natural logarithm system.
#
  value = 2.718281828459045235360287

  return value

def r8_e_test ( ):

#*****************************************************************************80
#
## R8_E_TEST tests R8_E.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'R8_E_TEST'
  print '  R8_E returns the value of E.'
  print '  Compare E to (1+1/n)^n'
  value1 = r8_e ( )
  print '  R8_E = %g' % ( value1 )
  print ' '
  print '        N     Estimate      Error'
  print ''

  n = 1
  for i in range ( 0, 21 ):
    value2 = ( float ( n + 1 ) / float ( n ) ) ** n
    print '  %8d  %14.6g  %14.6g' % ( n, value2, abs ( value1 - value2 ) )
    n = n * 2
#
#  Terminate.
#
  print ''
  print 'R8_E_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_e_test ( )
  timestamp ( )
