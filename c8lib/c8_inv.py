#!/usr/bin/env python

def c8_inv ( c ):

#*****************************************************************************80
#
## C8_INV evaluates the inverse of a C8.
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
  from c8_conj import c8_conj
  from c8_mag import c8_mag

 
  value = c8_conj ( c ) / ( c8_mag ( c )  ) ** 2

  return value

def c8_inv_test ( ):

#*****************************************************************************80
#
## C8_INV_TEST tests C8_INV.
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
  print 'C8_INV_TEST'
  print '  C8_INV computes the inverse of a C8.'
  print ''
  print '       C1=C8_UNIFORM_01          C2=C8_INV(C1)             C3=C8_INV(C2)'
  print '     ---------------------     ---------------------     ---------------------'
  print ''

  seed = 123456789

  for i in range ( 0, 10 ):
    c1, seed = c8_uniform_01 ( seed )
    c2 = c8_inv ( c1 )
    c3 = c8_inv ( c2 );
    print '  (%12f,%12f)  (%12f,%12f)  (%12f,%12f)' \
      % ( c1.real, c1.imag, c2.real, c2.imag, c3.real, c3.imag )

  print ''
  print 'C8_INV_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  c8_inv_test ( )
  timestamp ( )

