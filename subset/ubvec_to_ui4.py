#! /usr/bin/env python
#
def ubvec_to_ui4 ( n, bvec ):

#*****************************************************************************80
#
## UBVEC_TO_UI4 makes an unsigned integer from an unsigned binary vector.
#
#  Discussion:
#
#    A UBVEC is an integer vector of binary digits, intended to
#    represent a nonnegative integer.  BVEC(1) is the units digit, BVEC(N)
#    is the coefficient of 2^(N-1).
#
#  Example:
#
#    N = 4
#
#         BVEC   binary  I
#    ----------  -----  --
#    1  2  3  4
#    ----------
#    1, 0, 0, 0       1  1
#    0, 1, 0, 0      10  2
#    0, 0, 1, 1      11  3
#    0, 0, 1, 0     100  4
#    1, 0, 0, 1    1001  9
#    1, 1, 1, 1    1111 15
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
#    Input, integer N, the dimension of the vector.
#
#    Input, integer BVEC(N), the binary representation.
#
#    Output, integer VALUE, the integer.
#
  base = 2

  value = 0
  for j in range ( n - 1, -1, -1 ):
    value = base * value + bvec[j]

  return value

def ubvec_to_ui4_test ( ):

#*****************************************************************************80
#
## UBVEC_TO_UI4_TEST tests UBVEC_TO_UI4;
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
  from ui4_to_ubvec import ui4_to_ubvec

  n = 10

  print ''
  print 'UBVEC_TO_UI4_TEST'
  print '  UBVEC_TO_UI4 converts an unsigned binary vector'
  print '  to an unsigned integer;'
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
  print 'UBVEC_TO_UI4_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  ubvec_to_ui4_test ( )
  timestamp ( )

