#!/usr/bin/env python
#
def v_hofstadter ( n ):

#*****************************************************************************80
#
## V_HOFSTADTER computes the Hofstadter V sequence.
#
#  Discussion:
#
#    V(N) = 0                          if N = 0
#         = 1                          if 1 <= N <= 4
#         = V(N-V(N-1)) + V(N-V(N-4)), otherwise.
#
#    V(N) is defined for all nonnegative integers.
#
#  Table:
#
#     N  V(N)
#    --  ----
#
#     0     0
#     1     1
#     2     1
#     3     1
#     4     1
#     5     2
#     6     3
#     7     4
#     8     5
#     9     5
#    10     6
#    11     6
#    12     7
#    13     8
#    14     8
#    15     9
#    16     9
#    17    10
#    18    11
#    19    11
#    20    11
#    21    12
#    22    12
#    23    13
#    24    14
#    25    14
#    26    15
#    27    15
#    28    16
#    29    17
#    30    17
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 July 2004
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the argument of the function.
#
#    Output, integer VALUE, the value of the function.
#
  if ( n <= 0 ):
    value = 0
  elif ( n <= 4 ):
    value = 1
  else:
    value = v_hofstadter ( n - v_hofstadter(n-1) ) \
          + v_hofstadter ( n - v_hofstadter(n-4) )

  return value

def v_hofstadter_test ( ):

#*****************************************************************************80
#
## V_HOFSTADTER_TEST tests V_HOFSTADTER.
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
  print 'V_HOFSTADTER_TEST'
  print '  V_HOFSTADTER evaluates Hofstadter\'s recursive V function.'
  print ''
  print '     N   V(N)'
  print ''

  for i in range ( 0, 31 ):
    v = v_hofstadter ( i )
    print '  %6d  %6d' % ( i, v )
 
  print ''
  print 'V_HOFSTADTER_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  v_hofstadter_test ( )
  timestamp ( )
