#! /usr/bin/env python
#
def dvec_to_i4 ( n, dvec ):

#*****************************************************************************80
#
## DVEC_TO_I4 makes an integer from a (signed) decimal vector.
#
#  Discussion:
#
#    A DVEC is an integer vector of decimal digits, intended to
#    represent an integer.  DVEC(1) is the units digit, DVEC(N-1)
#    is the coefficient of 10**(N-2), and DVEC(N) contains sign
#    information.  It is 0 if the number is positive, and 1 if
#    the number is negative.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the dimension of the vector.
#
#    Input, integer DVEC(N), the decimal representation.
#
#    Output, integer VALUE, the integer.
#
  import numpy as np
  from dvec_complementx import dvec_complementx

  base = 10

  i_sign = 1

  if ( dvec[n-1] == base - 1 ):
    i_sign = -1
    dvec = dvec_complementx ( n, dvec )

  value = 0
  for j in range ( n - 2, -1, -1 ):
    value = base * value + dvec[j]

  value = i_sign * value

  return value

def dvec_to_i4_test ( ):

#*****************************************************************************80
#
## DVEC_TO_I4_TEST tests DVEC_TO_I4
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    28 May 2015
#
#  Author:
#
#    John Burkardt
#
  from i4_to_dvec import i4_to_dvec
  from i4_uniform_ab import i4_uniform_ab

  print ''
  print 'DVEC_TO_I4_TEST'
  print '  DVEC_TO_I4 converts a DVEC to an I4.'
  print ''
  print '        I4 => DVEC => I4'
  print ''

  seed = 123456789
  i1, seed = i4_uniform_ab ( -10000, 10000, seed )

  n = 6
  dvec = i4_to_dvec ( i1, n )

  i2 = dvec_to_i4 ( n, dvec )

  print '  %6d  ' % ( i1 ),
  for i in range ( n - 1, -1, -1 ):
    print '%2d' % ( dvec[i] ),
  print '  %6d' % ( i2 )
#
#  Terminate.
#
  print ''
  print 'DVEC_TO_I4_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  dvec_to_i4_test ( )
  timestamp ( )
