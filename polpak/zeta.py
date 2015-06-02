#!/usr/bin/env python

def zeta ( p ):

#*****************************************************************************80
#
## ZETA estimates the Riemann Zeta function.
#
#  Definition:
#
#    For 1 < P, the Riemann Zeta function is defined as:
#
#      ZETA ( P ) = Sum ( 1 <= N < Infinity ) 1 / N^P
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Daniel Zwillinger, editor,
#    CRC Standard Mathematical Tables and Formulae,
#    30th Edition,
#    CRC Press, 1996.
#
#  Parameters:
#
#    Input, real P, the power to which the integers are raised.
#    P must be greater than 1.
#
#    Output, real VALUE, an approximation to the Riemann
#    Zeta function.
#
  if ( p <= 1.0 ):
    print ''
    print 'ZETA - Fatal error!'
    print '  Exponent P <= 1.0.'

  value = 0.0
  n = 0

  while ( True ):

    n = n + 1
    value_old = value
    value = value + 1.0 / n ** p

    if ( value <= value_old or 10000 <= n ):
      break

  return value

def zeta_test ( ):

#*****************************************************************************80
#
## ZETA_TEST tests ZETA.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 February 2015
#
#  Author:
#
#    John Burkardt
#
  from zeta_values import zeta_values
  from zeta import zeta

  print ''
  print 'ZETA_TEST:'
  print '  ZETA evaluates the Riemann Zeta function.'
  print ''
  print '      N            ZETA(N)    ZETA(N)'
  print ''

  n_data = 0

  while ( True ):

    n_data, n, z1 = zeta_values ( n_data )

    if ( n_data == 0 ):
      break

    n_real = float ( n )
    z2 = zeta ( n_real )

    print '  %12d  %24.16g  %24.16g' % ( n, z1, z2 )

  print ''
  print 'ZETA_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  zeta_test ( )
  timestamp ( )
