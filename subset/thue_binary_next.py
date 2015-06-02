#! /usr/bin/env python
#
def thue_binary_next ( n, thue ):

#*****************************************************************************80
#
## THUE_BINARY_NEXT returns the next element in a binary Thue sequence.
#
#  Discussion:
#
#    Thue demonstrated that arbitrarily long sequences of 0's and
#    1's could be generated which had the "cubefree" property.  In
#    other words, for a given string S, there was no substring W
#    such that S contained "WWW".  In fact, a stronger result holds:
#    if "a" is the first letter of W, it is never the case that S
#    contains the substring "WWa".
#
#    In this example, the digits allowed are binary, that is, just
#    "0" and "1".  The replacement rules are:
#
#    "0" -> "01"
#    "1" -> "10"
#
#    This routine produces the next binary Thue sequence in a given series.
#    However, the input sequence must be a Thue sequence in order for
#    us to guarantee that the output sequence will also have the
#    cubic nonrepetition property.
#
#    Also, enough space must be set aside in THUE to hold the
#    output sequence.  This will always be twice the input
#    value of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the length of the input sequence.
#
#    Input, integer THUE(N), the initial Thue sequence.
#
#    Output, integer N, the length of the output sequence.
#
#    Output, integer THUE(N), the result of applying the substitution rules once.
#
  import numpy as np
  from sys import exit

  n2 = 2 * n
  thue2 = np.zeros ( n2, dtype = np.int32 )

  i2 = 0
  for i in range ( 0, n ):

    if ( thue[i] == 0 ):
      thue2[i2] = 0
      i2 = i2 + 1
      thue2[i2] = 1
      i2 = i2 + 1
    elif ( thue[i] == 1 ):
      thue2[i2] = 1
      i2 = i2 + 1
      thue2[i2] = 0
      i2 = i2 + 1
    else:
      print ''
      print 'THUE_BINARY_NEXT - Fatal error!'
      print '  The input sequence contains a non-binary digit'
      print '  THUE[%d] = %d' % ( i, thue[i] )
      exit ( 'THUE_BINARY_NEXT - Fatal error!' )
 
  return n2, thue2

def thue_binary_next_test ( ):

#*****************************************************************************80
#
## THUE_BINARY_NEXT_TEST tests THUE_BINARY_NEXT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ''
  print 'THUE_BINARY_NEXT_TEST'
  print '  THUE_BINARY_NEXT returns the next Thue binary sequence.'
  print ''

  n = 1
  thue = np.zeros ( n, dtype = np.int32 )
  thue[0] = 0

  print '  %2d:  ' % ( n ),
  for i in range ( 0, n ):
    print '%d' % ( thue[i] ),
  print ''

  for i in range ( 0, 6 ): 

    n, thue = thue_binary_next ( n, thue )

    print '  %2d:  ' % ( n ),
    for i in range ( 0, n ):
      print '%d' % ( thue[i] ),
    print ''
#
#  Terminate.
#
  print ''
  print 'THUE_BINARY_NEXT_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  thue_binary_next_test ( )
  timestamp ( )
