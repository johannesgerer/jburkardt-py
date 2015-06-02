#!/usr/bin/env python

def c8_exp ( c ):

#*****************************************************************************80
#
## C8_EXP evaluates the exponential of a C8.
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
  from c8_real import c8_real
  from c8_imag import c8_imag

  cr = c8_real ( c );
  ci = c8_imag ( c );

  value = np.exp ( cr ) * ( np.cos ( ci ) + np.sin ( ci ) * 1j );

  return value

def c8_exp_test ( ):

#*****************************************************************************80
#
## C8_EXP_TEST tests C8_EXP.
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
  from c8_log import c8_log
  from c8_uniform_01 import c8_uniform_01

  print ''
  print 'C8_EXP_TEST'
  print '  C8_EXP computes the exponential of a C8.'
  print ''
  print '       C1=C8_UNIFORM_01          C2=C8_EXP(C1)             C3=C8_LOG(C2)'
  print '     ---------------------     ---------------------     ---------------------'
  print ''

  seed = 123456789

  for i in range ( 0, 10 ):
    c1, seed = c8_uniform_01 ( seed )
    c2 = c8_exp ( c1 )
    c3 = c8_log ( c2 );
    print '  (%12f,%12f)  (%12f,%12f)  (%12f,%12f)' \
      % ( c1.real, c1.imag, c2.real, c2.imag, c3.real, c3.imag )

  print ''
  print 'C8_EXP_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  c8_exp_test ( )
  timestamp ( )

