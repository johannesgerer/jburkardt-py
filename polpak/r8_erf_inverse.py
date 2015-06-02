#!/usr/bin/env python

def r8_erf_inverse ( y ):

#*****************************************************************************80
#
## R8_ERF_INVERSE inverts the error function.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real Y, the value of the error function.
#
#    Output, real VALUE, the value such that R8_ERF(VALUE) = Y.
#
  import numpy as np
  from normal_01_cdf_inverse import normal_01_cdf_inverse

  z = ( y + 1.0 ) / 2.0

  value = normal_01_cdf_inverse ( z )

  value = value / np.sqrt ( 2.0 )

  return value

def r8_erf_inverse_test ( ):

#*****************************************************************************80
#
## R8_ERF_INVERSE_TEST tests R8_ERF_INVERSE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 February 2015
#
#  Author:
#
#    John Burkardt
#
  from erf_values import erf_values

  print ''
  print 'R8_ERF_INVERSE_TEST:'
  print '  R8_ERF_INVERSE inverts the error function.'
  print ''
  print '     FX              X    R8_ERF_INVERSE(FX)'
  print ''

  n_data = 0

  while ( True ):

    n_data, x1, fx = erf_values ( n_data )

    if ( n_data == 0 ):
      break

    x2 = r8_erf_inverse ( fx )

    print '  %12g  %24.16g  %24.16g' % ( fx, x1, x2 )

  print ''
  print 'R8_ERF_INVERSE_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  r8_erf_inverse_test ( )
  timestamp ( )
