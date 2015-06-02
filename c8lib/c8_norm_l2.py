#!/usr/bin/env python

def c8_norm_l2 ( c ):

#*****************************************************************************80
#
## C8_NORM_L2 evaluates the L2 norm of a C8.
#
#  Discussion:
#
#    Numbers of equal norm lie along diamonds centered at (0,0).
#
#    The L2 norm can be defined here as:
#
#      C8_NORM_L2(X) = aqrt ( ( real (X) ) ^ 2 + abs ( imag (X) ) ^ 2 )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, complex C, the value whose norm is desired.
#
#    Output, real VALUE, the L2 norm of C.
#
  import numpy as np

  value = np.sqrt ( ( c.real ) ** 2 + ( c.imag ) ** 2 )

  return value

def c8_norm_l2_test ( ):

#*****************************************************************************80
#
## C8_NORM_L2_TEST tests C8_NORM_L2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    23 February 2015
#
#  Author:
#
#    John Burkardt
#
  from c8_uniform_01 import c8_uniform_01

  print ''
  print 'C8_NORM_L2_TEST'
  print '  C8_NORM_L2 computes the L2 norm of a C8.'
  print ''
  print '       C1=C8_UNIFORM_01          R2=C8_NORM_L21(C1)'
  print '     ---------------------     ---------------------'
  print ''

  seed = 123456789

  for i in range ( 0, 10 ):
    c1, seed = c8_uniform_01 ( seed )
    r2 = c8_norm_l2 ( c1 )
    print '  (%12f,%12f)  %12f' % ( c1.real, c1.imag, r2 )

  print ''
  print 'C8_NORM_L2_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  c8_norm_l2_test ( )
  timestamp ( )

