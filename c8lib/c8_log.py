#!/usr/bin/env python

def c8_log ( c ):

#*****************************************************************************80
#
## C8_LOG evaluates the logarithm of a C8.
#
#  Discussion:
#
#    Here we use the relationship:
#
#      C8_LOG ( Z ) = LOG ( MAG ( Z ) ) + i * ARG ( Z )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, complex C, the argument.
#
#    Output, complex VALUE, the function value.
#
  import numpy as np
  from c8_arg import c8_arg
  from c8_mag import c8_mag

  arg = c8_arg ( c );
  mag = c8_mag ( c );

  value = np.log ( mag ) + arg * 1j;

  return value

def c8_log_test ( ):

#*****************************************************************************80
#
## C8_LOG_TEST tests C8_LOG.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    11 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from c8_exp import c8_exp
  from c8_uniform_01 import c8_uniform_01

  print ''
  print 'C8_LOG_TEST'
  print '  C8_LOG computes the logarithm of a C8.'
  print ''
  print '       C1=C8_UNIFORM_01          C2=C8_LOG(C1)             C3=C8_EXP(C2)'
  print '     ---------------------     ---------------------     ---------------------'
  print ''

  seed = 123456789

  for i in range ( 0, 10 ):
    c1, seed = c8_uniform_01 ( seed )
    c2 = c8_log ( c1 )
    c3 = c8_exp ( c2 );
    print '  (%12f,%12f)  (%12f,%12f)  (%12f,%12f)' \
      % ( c1.real, c1.imag, c2.real, c2.imag, c3.real, c3.imag )

  print ''
  print 'C8_LOG_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  c8_log_test ( )
  timestamp ( )

