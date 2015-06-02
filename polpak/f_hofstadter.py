#!/usr/bin/env python
#
def f_hofstadter ( n ):

#*****************************************************************************80
#
## F_HOFSTADTER computes the Hofstadter F sequence.
#
#  Discussion:
#
#    F(N) = 0                if N = 0
#         = N - F ( N - 1 ), otherwise.
#
#    F(N) is defined for all nonnegative integers, and turns out
#    to be equal to int ( ( N + 1 ) / 2 ).
#
#  Table:
#
#     N  F(N)
#    --  ----
#
#     0     0
#     1     1
#     2     1
#     3     2
#     4     2
#     5     3
#     6     3
#     7     4
#     8     4
#     9     5
#    10     5
#    11     6
#    12     6
#    13     7
#    14     7
#    15     8
#    16     8
#    17     9
#    18     9
#    19    10
#    20    10
#    21    11
#    22    11
#    23    12
#    24    12
#    25    13
#    26    13
#    27    14
#    28    14
#    29    15
#    30    15
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Douglas Hofstadter,
#    Goedel, Escher, Bach,
#    Basic Books, 1979.
#
#  Parameters:
#
#    Input, integer N, the argument of the function.
#
#    Output, integer VALUE, the value of the function.
#
  if ( n <= 0 ):
    value = 0
  else:
    value = n - f_hofstadter ( n - 1 )

  return value

def f_hofstadter_test ( ):

#*****************************************************************************80
#
## F_HOFSTADTER_TEST tests F_HOFSTADTER.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'F_HOFSTADTER_TEST'
  print '  F_HOFSTADTER evaluates Hofstadter\'s recursive F function.'
  print ''
  print '     N   F(N)'
  print ''

  for i in range ( 0, 31 ):
    f = f_hofstadter ( i )
    print '  %6d  %6d' % ( i, f )
 
  print ''
  print 'F_HOFSTADTER_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  f_hofstadter_test ( )
  timestamp ( )
