#!/usr/bin/env python

def c8_nint ( c ):

#*****************************************************************************80
#
## C8_NINT returns the nearest complex integer of a C8.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    15 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, complex C1, the value to be NINT'ed.
#
#    Output, complex VALUE, the NINT'ed value.
#
  from math import floor
  from c8_real import c8_real
  from c8_imag import c8_imag
  from c8_mag import c8_mag

  xc = c8_real ( c )
  yc = c8_imag ( c )
#
#  Lower left.
#
  x = floor ( xc )
  y = floor ( yc )
  r = ( x - xc ) ** 2 + ( y - yc ) ** 2
  r_min = r
  x_min = x
  y_min = y
#
#  Lower right.
#
  x = floor ( xc ) + 1.0
  y = floor ( yc )
  r = ( x - xc ) ** 2 + ( y - yc ) ** 2
  if ( r < r_min ):
    r_min = r
    x_min = x
    y_min = y
#
#  Upper right.
#
  x = floor ( xc ) + 1.0
  y = floor ( yc ) + 1.0
  r = ( x - xc ) ** 2 + ( y - yc ) ** 2
  if ( r < r_min ):
    r_min = r
    x_min = x
    y_min = y
#
#  Upper left.
#
  x = floor ( xc )
  y = floor ( yc ) + 1.0
  r = ( x - xc ) ** 2 + ( y - yc ) ** 2
  if ( r < r_min ):
    r_min = r
    x_min = x
    y_min = y
 
  value = x_min + 1j * y_min

  return value

def c8_nint_test ( ):

#*****************************************************************************80
#
## C8_NINT_TEST tests C8_NINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    15 February 2015
#
#  Author:
#
#    John Burkardt
#
  from c8_uniform_01 import c8_uniform_01

  print ''
  print 'C8_NINT_TEST'
  print '  C8_NINT computes the nearest integer to a C8.'
  print ''
  print '       C1=10*C8_UNIFORM_01     C2=C8_NINT(C1)'
  print '     ---------------------     ---------------------'
  print ''

  seed = 123456789

  for i in range ( 0, 10 ):
    c1, seed = c8_uniform_01 ( seed )
    c1 = 10.0 * c1
    c2 = c8_nint ( c1 )
    print '  (%12f,%12f)  (%12f,%12f)' % ( c1.real, c1.imag, c2.real, c2.imag )

  print ''
  print 'C8_NINT_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  c8_nint_test ( )
  timestamp ( )

