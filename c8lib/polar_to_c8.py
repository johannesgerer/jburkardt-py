#!/usr/bin/env python

def polar_to_c8 ( r, t ):

#*****************************************************************************80
#
## POLAR_TO_C8 converts polar form to a C8.
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
#    Input, real R, T, the polar form.
#
#    Input, complex C, the value.
#
  import numpy as np

  c = r * ( np.cos ( t ) + 1j * np.sin ( t ) )

  return c

def polar_to_c8_test ( ):

#*****************************************************************************80
#
## POLAR_TO_C8_TEST tests POLAR_TO_C8.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    27 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from r8_uniform_01 import r8_uniform_01
  from c8_to_polar import c8_to_polar

  print ''
  print 'POLAR_TO_C8_TEST'
  print '  POLAR_TO_C8 computes the polar form of a C8.'
  print ''
  print '     R1,T1=R8_UNIFORM_01       C2=POLAR_TO_C8(R1,T1)    R3,T3=C8_TO_POLAR(C2)'
  print '     ---------------------     ---------------------     ---------------------'
  print ''

  seed = 123456789

  for i in range ( 0, 10 ):
    r1, seed = r8_uniform_01 ( seed )
    t1, seed = r8_uniform_01 ( seed )
    t1 = t1 * 2.0 * np.pi
    c2 = polar_to_c8 ( r1, t1 )
    r3, t3 = c8_to_polar ( c2 )
    print '  (%12f,%12f)  (%12f,%12f)  (%12f,%12f)' % ( r1, t1, c2.real, c2.imag, r3, t3 )

  print ''
  print 'POLAR_TO_C8_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  polar_to_c8_test ( )
  timestamp ( )

