#!/usr/bin/env python

def ytb_enum ( n ):

#*****************************************************************************80
#
## YTB_ENUM enumerates the Young tableaus of size N.
#
#  Discussion:
#
#    If A(N) is the number of Young tableau of size N, then A(1) = 1,
#    A(2) = 2, and
#
#    A(N) = A(N-1) + (N-1) * A(N-2).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the integer which is to be partitioned.
#
#    Output, integer VALUE, the number of Young tableaus of N.
#
  if ( n <= 0 ):
    value = 0
  elif ( n == 1 ):
    value = 1
  elif ( n == 2 ):
    value = 2
  else:
    a2 = 1
    a3 = 2
    for i in range ( 2, n ):
      a1 = a2
      a2 = a3
      a3 = a2 + i * a1
    value = a3

  return value

def ytb_enum_test ( ):

#*****************************************************************************80
#
## YTB_ENUM_TEST tests YTB_ENUM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    22 December 2014
#
#  Author:
#
#    John Burkardt
#
  n = 10

  print ''
  print 'YTB_ENUM_TEST:'
  print '  YTB_ENUM counts Young tableaus.'
  print ''
  print '   N       YTB(N)'
  print ''

  for i in range ( 0, n + 1 ):
    value = ytb_enum ( i )
    print '  %2d  %8d' % ( i, value )
#
#  Terminate.
#
  print ''
  print 'YTB_ENUM_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  ytb_enum_test ( )
  timestamp ( )

