#!/usr/bin/env python

def c8_zero ( ):

#*****************************************************************************80
#
## C8_ZERO returns the value of zero as a C8.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    26 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real VALUE, the value of the imaginary unit.
#
  value = 0 + 0j

  return value

def c8_zero_test ( ):

#*****************************************************************************80
#
## C8_ZERO_TEST tests C8_ZERO.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    26 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'C8_ZERO_TEST'
  print '  C8_ZERO returns the value of zero as a C8'

  c1 = c8_zero ( )
  print ''
  print '  C1=C8_ZERO ( ) = (%g,%g)' % ( c1.real, c1.imag )

  print ''
  print 'C8_ZERO_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  c8_zero_test ( )
  timestamp ( )

