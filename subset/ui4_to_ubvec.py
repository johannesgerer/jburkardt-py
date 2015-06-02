#! /usr/bin/env python
#
def ui4_to_ubvec ( i, n ):

#*****************************************************************************80
#
## UI4_TO_UBVEC makes a unsigned binary vector from an integer.
#
#  Discussion:
#
#    A UBVEC is an integer vector of binary digits, intended to
#    represent a nonnegative integer.  BVEC(1) is the units digit, BVEC(N)
#    is the coefficient of 2**(N-1).
#
#    To guarantee that there will be enough space for any
#    value of I, it would be necessary to set N = 32.
#
#  Example:
#
#     I       BVEC         binary
#    --  ----------------  ------
#     1  1, 0, 0, 0, 0, 0       1
#     2  0, 1, 0, 0, 0, 0      10
#     3  1, 1, 0, 0, 0, 0      11
#     4  0, 0, 1, 0, 0, 0     100
#     9  1, 0, 0, 1, 0, 0    1001
#    -9  1, 1, 1, 0, 1, 1  110111
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 May 2015
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
#    Output, integer BVEC(N), the unsigned binary representation.
#
  import numpy as np

  base = 2
  bvec = np.zeros ( n )

  for j in range ( 0, n ):
    bvec[j] = ( i % base )
    i = ( i // base )

  return bvec

def ui4_to_ubvec_test ( ):

#*****************************************************************************80
#
## UI4_TO_UBVEC_TEST tests UI4_TO_UBVEC;
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 May 2015
#
#  Author:
#
#    John Burkardt
#
  from ubvec_to_ui4 import ubvec_to_ui4

  n = 10

  print ''
  print 'UI4_TO_UBVEC_TEST'
  print '  UI4_TO_UBVEC converts an unsigned integer to an'
  print '  unsigned binary vector;'
  print ''
  print '  UI4 --> UBVEC  -->  UI4'
  print ''

  for i in range ( 0, 11 ):
    bvec = ui4_to_ubvec ( i, n )
    i2 = ubvec_to_ui4 ( n, bvec )
    print '  %2d  ' % ( i ),
    for i in range ( 0, n ):
      print '%1d' % ( bvec[i] ),
    print '  %2d' % ( i2 )
#
#  Terminate.
#
  print ''
  print 'UI4_TO_UBVEC_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  ui4_to_ubvec_test ( )
  timestamp ( )

