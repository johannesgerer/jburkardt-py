#!/usr/bin/env python

def c8_conj ( c ):

#*****************************************************************************80
#
## C8_CONJ evaluates the conjugate of a C8.
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
  from c8_imag import c8_imag
  from c8_real import c8_real

  value = c8_real ( c ) - 1j * c8_imag ( c )

  return value

def c8_conj_test ( ):

#*****************************************************************************80
#
## C8_CONJ_TEST tests C8_CONJ.
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
  from c8_uniform_01 import c8_uniform_01

  print ''
  print 'C8_CONJ_TEST'
  print '  C8_CONJ computes the conjuge of a C8.'
  print ''
  print '       C1=C8_UNIFORM_01          C2=C8_CONJ(C1)             C3=C8_CONJ(C2)'
  print '     ---------------------     ---------------------     ---------------------'
  print ''

  seed = 123456789

  for i in range ( 0, 10 ):
    c1, seed = c8_uniform_01 ( seed )
    c2 = c8_conj ( c1 )
    c3 = c8_conj ( c2 );
    print '  (%12f,%12f)  (%12f,%12f)  (%12f,%12f)' \
      % ( c1.real, c1.imag, c2.real, c2.imag, c3.real, c3.imag )

  print ''
  print 'C8_CONJ_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  c8_conj_test ( )
  timestamp ( )

