#!/usr/bin/env python

def c8_arg ( c ):

#*****************************************************************************80
#
## C8_ARG returns the argument of a C8.
#
#  Discussion:
#
#    The value returned by this function will always lie between 0 and 2*PI.
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
#    Input, complex C, the value whose argument is desired.
#
#    Output, real VALUE, the argument.
#
  from r8_atan import r8_atan

  if ( c.imag == 0.0 and c.real  == 0.0  ):

    value = 0.0

  else:

    r1 = c.imag
    r2 = c.real
    value = r8_atan ( r1, r2 )

  return value

def c8_arg_test ( ):

#*****************************************************************************80
#
## C8_ARG_TEST tests C8_ARG.
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
  print 'C8_ARG_TEST'
  print '  C8_ARG computes the argument of a C8.'
  print ''
  print '       C1=C8_UNIFORM_01          R2=C8_ARG(C1)             R3=NP.ANGLE(C1)'
  print '     ---------------------     ---------------------     ---------------------'
  print ''

  seed = 123456789

  for i in range ( 0, 10 ):
    c1, seed = c8_uniform_01 ( seed )
    r2 = c8_arg ( c1 )
    r3 = np.angle ( c1 )
    print '  (%12f,%12f)  %12f            %12f' % ( c1.real, c1.imag, r2, r3 )

  print ''
  print 'C8_ARG_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  c8_arg_test ( )
  timestamp ( )

