#!/usr/bin/env python

def c8_real ( c ):

#*****************************************************************************80
#
## C8_REAL returns the real part of a C8.
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
#    10 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, complex C, the argument.
#
#    Output, real VALUE, the real part of C.
#
  value = c.real

  return value

def c8_real_test ( ):

#*****************************************************************************80
#
## C8_REAL_TEST tests C8_REAL.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    10 February 2015
#
#  Author:
#
#    John Burkardt
#
  from c8_uniform_01 import c8_uniform_01

  print ''
  print 'C8_REAL_TEST'
  print '  C8_REAL computes the real part of a C8.'
  print ''
  print '       C1=C8_UNIFORM_01          R2=C8_REAL(C1)         R3=C1.REAL'
  print '     ---------------------     ---------------------  ------------'
  print ''

  seed = 123456789

  for i in range ( 0, 10 ):
    c1, seed = c8_uniform_01 ( seed )
    r2 = c8_real ( c1 )
    r3 = c1.real
    print '  (%12f,%12f)  %12f            %12f' % ( c1.real, c1.imag, r2, r3 )

  print ''
  print 'C8_REAL_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  c8_real_test ( )
  timestamp ( )

