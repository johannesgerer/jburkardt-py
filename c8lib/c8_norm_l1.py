#!/usr/bin/env python

def c8_norm_l1 ( c ):

#*****************************************************************************80
#
## C8_NORM_L1 evaluates the L1 norm of a C8.
#
#  Discussion:
#
#    Numbers of equal norm lie along diamonds centered at (0,0).
#
#    The L1 norm can be defined here as:
#
#      C8_NORM_L1(X) = abs ( real (X) ) + abs ( imag (X) )
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
#    Output, real VALUE, the L1 norm of C.
#
  value = abs ( c.real ) + abs ( c.imag )

  return value

def c8_norm_l1_test ( ):

#*****************************************************************************80
#
## C8_NORM_L1_TEST tests C8_NORM_L1.
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
  print 'C8_NORM_L1_TEST'
  print '  C8_NORM_L1 computes the L1 norm of a C8.'
  print ''
  print '       C1=C8_UNIFORM_01          R2=C8_NORM_L1(C1)'
  print '     ---------------------     ---------------------'
  print ''

  seed = 123456789

  for i in range ( 0, 10 ):
    c1, seed = c8_uniform_01 ( seed )
    r2 = c8_norm_l1 ( c1 )
    print '  (%12f,%12f)  %12f' % ( c1.real, c1.imag, r2 )

  print ''
  print 'C8_NORM_L1_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  c8_norm_l1_test ( )
  timestamp ( )

