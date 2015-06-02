#!/usr/bin/env python

def c8_abs ( c ):

#*****************************************************************************80
#
## C8_ABS evaluates the absolute value of a C8.
#
#  Discussion:
#
#    A C8 is a complex value.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    08 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, complex C, the argument.
#
#    Output, real VALUE, the absolute value.
#
  from math import sqrt

  value = sqrt ( ( c.real ) ** 2 + ( c.imag ) ** 2 )

  return value

def c8_abs_test ( ):

#*****************************************************************************80
#
## C8_ABS_TEST tests C8_ABS.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    08 February 2015
#
#  Author:
#
#    John Burkardt
#
  from c8_uniform_01 import c8_uniform_01

  print ''
  print 'C8_ABS_TEST'
  print '  C8_ABS computes the absolute value of a C8.'
  print ''
  print '       C1=C8_UNIFORM_01          R2=C8_ABS(C1)             R3=ABS(C1)'
  print '     ---------------------     ---------------------     ---------------------'
  print ''

  seed = 123456789

  for i in range ( 0, 10 ):
    c1, seed = c8_uniform_01 ( seed )
    r2 = c8_abs ( c1 )
    r3 = abs ( c1 )
    print '  (%12f,%12f)  %12f            %12f' % ( c1.real, c1.imag, r2, r3 )

  print ''
  print 'C8_ABS_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  c8_abs_test ( )
  timestamp ( )

