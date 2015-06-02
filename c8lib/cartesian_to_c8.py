#!/usr/bin/env python

def cartesian_to_c8 ( x, y ):

#*****************************************************************************80
#
## CARTESIAN_TO_C8 converts cartesian form to a C8.
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
#    Input, real X, Y, the cartesian form.
#
#    Input, complex C, the value.
#
  import numpy as np

  c = x + 1j * y

  return c

def cartesian_to_c8_test ( ):

#*****************************************************************************80
#
## CARTESIAN_TO_C8_TEST tests CARTESIAN_TO_C8.
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
  import numpy as np
  from r8_uniform_01 import r8_uniform_01
  from c8_to_cartesian import c8_to_cartesian

  print ''
  print 'CARTESIAN_TO_C8_TEST'
  print '  CARTESIAN_TO_C8 computes the cartesian form of a C8.'
  print ''
  print '     X1,Y1=R8_UNIFORM_01       C2=CARTESIAN_TO_C8(X1,Y1)    X3,Y3=C8_TO_CARTESIAN(C2)'
  print '     ---------------------     ---------------------     ---------------------'
  print ''

  seed = 123456789

  for i in range ( 0, 10 ):
    x1, seed = r8_uniform_01 ( seed )
    y1, seed = r8_uniform_01 ( seed )
    c2 = cartesian_to_c8 ( x1, y1 )
    x3, y3 = c8_to_cartesian ( c2 )
    print '  (%12f,%12f)  (%12f,%12f)  (%12f,%12f)' % ( x1, y1, c2.real, c2.imag, x3, y3 )

  print ''
  print 'CARTESIAN_TO_C8_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  cartesian_to_c8_test ( )
  timestamp ( )

