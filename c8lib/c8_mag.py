#!/usr/bin/env python

def c8_mag ( c ):

#*****************************************************************************80
#
## C8_MAG returns the magnitude of a C8.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, complex C, the value.
#
#    Output, real VALUE, the magnitude.
#
  import numpy as np

  r1 = c.imag
  r2 = c.real
  value = np.sqrt ( r1 * r1 + r2 * r2 )

  return value

def c8_mag_test ( ):

#*****************************************************************************80
#
## C8_MAG_TEST tests C8_MAG.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    09 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from c8_uniform_01 import c8_uniform_01

  print ''
  print 'C8_MAG_TEST'
  print '  C8_MAG computes the magnitude of a C8.'
  print ''
  print '       C1=C8_UNIFORM_01          R2=C8_MAG(C1)             R3=NP.ABSOLUTE(C1)'
  print '     ---------------------     ---------------------     ---------------------'
  print ''

  seed = 123456789

  for i in range ( 0, 10 ):
    c1, seed = c8_uniform_01 ( seed )
    r2 = c8_mag ( c1 )
    r3 = np.absolute ( c1 )
    print '  (%12f,%12f)  %12f            %12f' % ( c1.real, c1.imag, r2, r3 )

  print ''
  print 'C8_MAG_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  c8_mag_test ( )
  timestamp ( )

