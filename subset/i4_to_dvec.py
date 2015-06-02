#! /usr/bin/env python
#
def i4_to_dvec ( i, n ):

#*****************************************************************************80
#
## I4_TO_DVEC makes a signed decimal vector from an integer.
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
#    Input, integer I, an integer to be represented.
#
#    Input, integer N, the dimension of the vector.
#
#    Output, integer DVEC(N), the signed decimal representation.
#
  import numpy as np
  from dvec_complementx import dvec_complementx

  base = 10
  i2 = abs ( i )

  dvec = np.zeros ( n, dtype = np.int32 )

  for j in range ( 0, n - 1 ):
    dvec[j] = ( i2 % base )
    i2 = ( i2 // base )

  dvec[n-1] = 0

  if ( i < 0 ):
    dvec = dvec_complementx ( n, dvec )

  return dvec

def i4_to_dvec_test ( ):

#*****************************************************************************80
#
## I4_TO_DVEC_TEST tests I4_TO_DVEC
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
  from dvec_to_i4 import dvec_to_i4
  from i4_uniform_ab import i4_uniform_ab

  print ''
  print 'I4_TO_DVEC_TEST'
  print '  I4_TO_DVEC converts an I4 to a DVEC.'
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
  print 'I4_TO_DVEC_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_to_dvec_test ( )
  timestamp ( )
