#!/usr/bin/env python
#
def c8_print ( a, title ):

#*****************************************************************************80
#
## C8_PRINT prints a C8.
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
#    Input, complex A, the value to be printed.
#
#    Input, string TITLE, a title.
#
  print '%s  ( %g, %g )' % ( title, a.real, a.imag )

def c8_print_test ( ):

#*****************************************************************************80
#
## C8_PRINT_TEST tests C8_PRINT.
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

  print ''
  print 'C8_PRINT_TEST'
  print '  C8_PRINT prints a C8.'
  print ''

  c1 = 0.0 + 0.0j
  c2 = 1.0 + 0.0j
  c3 = 3.141592653589793 + 0.0j
  c4 =  0.0 + 1.0j
  c5 = 1.0 + 2.0j
  c6 = -12.34 + 56.78j
  c7 = 0.001 + 0.000002j
  c8 = 3.0E+08 - 4.5E+09j

  c8_print ( c1, '  Zero:' )
  c8_print ( c2, '  One:' )
  c8_print ( c3, '  Pi:' )
  c8_print ( c4, '  i:' )
  c8_print ( c5, '  1+2i:' )
  c8_print ( c6, ' -12.34 + 56.78i:' )
  c8_print ( c7, '  1E-3 + 2E-6i' )
  c8_print ( c8, '  3E8 - 4.5E9i:' )

  print ''
  print 'C8_PRINT_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  c8_print_test ( )
  timestamp ( )


