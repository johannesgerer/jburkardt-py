#!/usr/bin/env python
#
def mertens ( n ):

#*****************************************************************************80
#
## MERTENS evaluates the Mertens function.
#
#  Discussion:
#
#    The Mertens function M(N) is the sum from 1 to N of the Moebius
#    function MU.  That is,
#
#    M(N) = sum ( 1 <= I <= N ) MU(I)
#
#        N   M(N)
#        --  ----
#         1     1
#         2     0
#         3    -1
#         4    -1
#         5    -2
#         6    -1
#         7    -2
#         8    -2
#         9    -2
#        10    -1
#        11    -2
#        12    -2
#       100     1
#      1000     2
#     10000   -23
#    100000   -48
#
#    The determinant of the Redheffer matrix of order N is equal
#    to the Mertens function M(N).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    M Deleglise, J Rivat,
#    Computing the Summation of the Moebius Function,
#    Experimental Mathematics,
#    Volume 5, 1996, pages 291-295.
#
#    Eric Weisstein,
#    CRC Concise Encyclopedia of Mathematics,
#    CRC Press, 2002,
#    Second edition,
#    ISBN: 1584883472,
#    LC: QA5.W45
#
#  Parameters:
#
#    Input, integer N, the argument.
#
#    Output, integer VALUE, the value.
#
  from moebius import moebius

  value = 0

  for i in range ( 1, n + 1 ):
    value = value + moebius ( i )

  return value

def mertens_test ( ):

#*****************************************************************************80
#
## MERTENS_TEST tests MERTENS.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 February 2015
#
#  Author:
#
#    John Burkardt
#
  from mertens_values import mertens_values

  print ''
  print 'MERTENS_TEST'
  print '  MERTENS computes the Mertens function.'
  print ''
  print '    N   Exact   MERTENS(N)'
  print ''

  n_data = 0

  while ( True ):

    n_data, n, c = mertens_values ( n_data )

    if ( n_data == 0 ):
      break

    c2 = mertens ( n )

    print '  %4d  %8d  %8d' % ( n, c, c2 )
 
  print ''
  print 'MERTENS_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  mertens_test ( )
  timestamp ( )
