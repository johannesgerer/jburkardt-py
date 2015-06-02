#!/usr/bin/env python

def c8_add ( c1, c2 ):

#*****************************************************************************80
#
## C8_ADD adds two C8's.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, complex C1, C2, the values to add.
#
#    Output, complex VALUE, the function value.
#
  value = c1 + c2

  return value

def c8_add_test ( ):

#*****************************************************************************80
#
## C8_ADD_TEST tests C8_ADD.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    12 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from c8_uniform_01 import c8_uniform_01

  print ''
  print 'C8_ADD_TEST'
  print '  C8_ADD adds two C8s.'
  print ''
  print '       C1=C8_UNIFORM_01          C2=C8_UNIFORM_01          C3=C8_ADD(C1,C2)'
  print '     ---------------------     ---------------------     ---------------------'
  print ''

  seed = 123456789

  for i in range ( 0, 10 ):
    c1, seed = c8_uniform_01 ( seed )
    c2, seed = c8_uniform_01 ( seed )
    c3 = c8_add ( c1, c2 )
    print '  (%12f,%12f)  (%12f,%12f)  (%12f,%12f)' \
      % ( c1.real, c1.imag, c2.real, c2.imag, c3.real, c3.imag )

  print ''
  print 'C8_ADD_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  c8_add_test ( )
  timestamp ( )

