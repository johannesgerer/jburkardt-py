#!/usr/bin/env python

def c8_sub ( c1, c2 ):

#*****************************************************************************80
#
## C8_SUB subtracts two C8's.
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
#    Input, complex C1, C2, the values to subtract.
#
#    Output, complex VALUE, the function value.
#
  value = c1 - c2

  return value

def c8_sub_test ( ):

#*****************************************************************************80
#
## C8_SUB_TEST tests C8_SUB.
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
  print 'C8_SUB_TEST'
  print '  C8_SUB subs two C8s.'
  print ''
  print '       C1=C8_UNIFORM_01          C2=C8_UNIFORM_01          C3=C8_SUB(C1,C2)'
  print '     ---------------------     ---------------------     ---------------------'
  print ''

  seed = 123456789

  for i in range ( 0, 10 ):
    c1, seed = c8_uniform_01 ( seed )
    c2, seed = c8_uniform_01 ( seed )
    c3 = c8_sub ( c1, c2 )
    print '  (%12f,%12f)  (%12f,%12f)  (%12f,%12f)' \
      % ( c1.real, c1.imag, c2.real, c2.imag, c3.real, c3.imag )

  print ''
  print 'C8_SUB_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  c8_sub_test ( )
  timestamp ( )

