#!/usr/bin/env python

def c8_imag ( c ):

#*****************************************************************************80
#
## C8_IMAG returns the imaginary part of a C8.
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
  value = c.imag

  return value

def c8_imag_test ( ):

#*****************************************************************************80
#
## C8_IMAG_TEST tests C8_IMAG.
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
  print 'C8_IMAG_TEST'
  print '  C8_IMAG computes the imaginary part of a C8.'
  print ''
  print '       C1=C8_UNIFORM_01          R2=C8_IMAG(C1)         R3=C1.IMAG'
  print '     ---------------------     ---------------------  ------------'
  print ''

  seed = 123456789

  for i in range ( 0, 10 ):
    c1, seed = c8_uniform_01 ( seed )
    r2 = c8_imag ( c1 )
    r3 = c1.imag
    print '  (%12f,%12f)  %12f            %12f' % ( c1.real, c1.imag, r2, r3 )

  print ''
  print 'C8_IMAG_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  c8_imag_test ( )
  timestamp ( )

