#!/usr/bin/env python

def c8_one ( ):

#*****************************************************************************80
#
## C8_ONE returns the value of one as a C8.
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
  value = 1 + 0j

  return value

def c8_one_test ( ):

#*****************************************************************************80
#
## C8_ONE_TEST tests C8_ONE.
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
  print 'C8_ONE_TEST'
  print '  C8_ONE returns the value of one as a C8'

  c1 = c8_one ( )
  print ''
  print '  C1=C8_ONE ( ) = (%g,%g)' % ( c1.real, c1.imag )
  c2 = c1 + c1
  print ''
  print '  C2= C1 + C1 = (%g,%g)' % ( c2.real, c2.imag )

  print ''
  print 'C8_ONE_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  c8_one_test ( )
  timestamp ( )

