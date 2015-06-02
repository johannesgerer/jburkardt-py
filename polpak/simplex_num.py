#!/usr/bin/env python

def simplex_num ( m, n ):

#*****************************************************************************80
#
## SIMPLEX_NUM evaluates the N-th Simplex number in M dimensions.
#
#  Discussion:
#
#     N\M: 1    2    3    4    5
#    --   --   --   --   --   --
#     0    0    0    0    0    0
#     1    1    1    1    1    1
#     2    2    3    4    5    6
#     3    3    6   10   15   21
#     4    4   10   20   35   56
#     5    5   15   35   70  126
#     6    6   21   56  126  252
#     7    7   28   84  210  462
#     8    8   36  120  330  792
#     9    9   45  165  495 1287
#    10   10   55  220  715 2002
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
#  Parameters
#
#    Input, integer M, the spatial dimension.
#
#    Input, integer N, the index of the number.
#
#    Output, integer VALUE, the desired value.
#
  value = 1
  for i in range ( 1, m + 1 ):
    value = ( value * ( n + i - 1 ) ) / i

  return value

def simplex_num_test ( ):

#*****************************************************************************80
#
## SIMPLEX_NUM_TEST tests SIMPLEX_NUM.
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
  print ''
  print 'SIMPLEX_NUM_TEST'
  print '  SIMPLEX_NUM computes the N-th simplex number'
  print '  in M dimensions.'
  print ''
  print '      M:  0      1      2      3      4      5'
  print '   N'
 
  for n in range ( 1, 11 ):
    print '  %2d' % ( n ),
    for m in range ( 0, 6 ):
      value = simplex_num ( m, n )
      print '  %4d' % ( value ),
    print ''

  print ''
  print 'SIMPLEX_NUM_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  simplex_num_test ( )
  timestamp ( )
