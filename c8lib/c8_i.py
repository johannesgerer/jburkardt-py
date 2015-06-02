#!/usr/bin/env python

def c8_i ( ):

#*****************************************************************************80
#
## C8_I returns the value of the imaginary unit as a C8.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    13 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real VALUE, the value of the imaginary unit.
#
  value = 1j

  return value

def c8_i_test ( ):

#*****************************************************************************80
#
## C8_I_TEST tests C8_I.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    13 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'C8_I_TEST'
  print '  C8_I returns the value of the imaginary unit.'

  c1 = c8_i ( )
  print ''
  print '  C1=C8_I ( ) = (%g,%g)' % ( c1.real, c1.imag )
  c2 = c1 * c1
  print ''
  print '  C2= C1 * C1 = (%g,%g)' % ( c2.real, c2.imag )

  print ''
  print 'C8_I_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  c8_i_test ( )
  timestamp ( )

