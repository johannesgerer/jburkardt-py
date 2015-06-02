#!/usr/bin/env python

def i4_to_bvec ( i, n ) :

#*****************************************************************************80
#
## I4_TO_BVEC makes a signed binary vector from an integer.
#
#  Discussion:
#
#    A BVEC is an integer vector of binary digits, intended to
#    represent an integer.  BVEC(1) is the units digit, BVEC(N-1)
#    is the coefficient of 2^(N-2), and BVEC(N) contains sign
#    information.  It is 0 if the number is positive, and 1 if
#    the number is negative.
#
#    To guarantee that there will be enough space for any
#    value of I, it would be necessary to set N = 32.
#
#  Example:
#
#     I       BVEC         binary
#    --  ----------------  ------
#     1  1, 0, 0, 0, 0, 0      1
#     2  0, 1, 0, 0, 0, 0     10
#     3  1, 1, 0, 0, 0, 0     11
#     4  0, 0, 1, 0, 0, 0    100
#     9  1, 0, 0, 1, 0, 0   1001
#    -9  1, 1, 1, 0, 1, 1  -1001 = 110111 (2's complement)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 December 2014
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
#    Output, integer BVEC(N), the signed binary representation.
#
  import numpy as np
  from bvec_complement2 import bvec_complement2
  from bvec_print import bvec_print

  base = 2
  i2 = abs ( i )

  bvec = np.zeros ( n, dtype = np.int32 )

  for j in range ( 0, n - 1 ):
    bvec[j] = ( i2 % base )
    i2 = ( i2 // base )

  bvec[n-1] = 0

  if ( i < 0 ):
    bvec2 = bvec_complement2 ( n, bvec )
    for j in range ( 0, n - 1 ):
      bvec[j] = bvec2[j]
    bvec[n-1] = 1

  return bvec

def i4_to_bvec_test ( ):

#*****************************************************************************80
#
## I4_TO_BVEC_TEST tests I4_TO_BVEC;
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    24 December 2014
#
#  Author:
#
#    John Burkardt
#
  from bvec_print import bvec_print
  from bvec_to_i4 import bvec_to_i4

  n = 10

  print ''
  print 'I4_TO_BVEC_TEST'
  print '  I4_TO_BVEC converts an integer to a '
  print '  signed binary vector.'
  print ''
  print '  I --> BVEC  -->  I'
  print ''

  for i in range ( -3, 11 ):
    bvec = i4_to_bvec ( i, n )
    i2 = bvec_to_i4 ( n, bvec )
    print '  %2d  ' % ( i ),
    for j in range ( n - 1, -1, -1 ):
      print '%1d' % ( bvec[j] ),
    print '  %2d' % ( i2 ) 
 
  print ''
  print 'I4_TO_BVEC_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_to_bvec_test ( )
  timestamp ( )
