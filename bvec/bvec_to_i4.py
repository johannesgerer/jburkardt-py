#!/usr/bin/env python

def bvec_to_i4 ( n, bvec ) :

#*****************************************************************************80
#
## BVEC_TO_I4 makes an integer from a (signed) binary vector.
#
#  Discussion:
#
#    A BVEC is an integer vector of binary digits, intended to
#    represent an integer.  BVEC(1) is the units digit, BVEC(N-1)
#    is the coefficient of 2**(N-2), and BVEC(N) contains sign
#    information.  It is 0 if the number is positive, and 1 if
#    the number is negative.
#
#  Example:
#
#         BVEC   binary  I
#    ----------  -----  --
#    1  2  3  4
#    ----------
#    1, 0, 0, 0       1  1
#    0, 1, 0, 0      10  2
#    0, 0, 1, 1    -100 -4
#    0, 0, 1, 0     100  4
#    1, 0, 0, 1    -111 -9
#    1, 1, 1, 1      -0  0
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
#    Input, integer N, the dimension of the vector.
#
#    Input, integer BVEC(N), the binary representation.
#
#    Output, integer VALUE, the integer.
#
  from bvec_complement2 import bvec_complement2
  import numpy as np

  base = 2

  bvec2 = np.zeros ( n, dtype = np.int32 )
  for i in range ( 0, n ):
    bvec2[i] = bvec[i]

  i_sign = 1

  if ( bvec2[n-1] == base - 1 ):
    i_sign = -1
    bvec3 = bvec_complement2 ( n - 1, bvec2 )
    for i in range ( 0, n - 1 ):
      bvec2[i] = bvec3[i]

  value = 0
  for j in range ( n - 2, -1, -1 ):
    value = base * value + bvec2[j]

  value = i_sign * value

  return value

def bvec_to_i4_test ( ):

#*****************************************************************************80
#
## BVEC_TO_I4_TEST tests BVEC_TO_I4;
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
  from i4_to_bvec import i4_to_bvec

  n = 10

  print ''
  print 'BVEC_TO_I4_TEST'
  print '  BVEC_TO_I4 converts a signed binary vector'
  print '  to an integer;'
  print ''
  print '  I --> BVEC  -->  I'
  print 1, ''

  for i in range ( -3, 11 ):
    bvec = i4_to_bvec ( i, n )
    i2 = bvec_to_i4 ( n, bvec )
    print '  %2d  ' % ( i ),
    for j in range ( n - 1, -1, -1 ):
      print '%1d' % ( bvec[j] ),
    print '  %2d' % ( i2 ) 
 
  print ''
  print 'BVEC_TO_I4_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  bvec_to_i4_test ( )
  timestamp ( )
