#! /usr/bin/env python
#
def thue_ternary_next ( n, thue ):

#*****************************************************************************80
#
## THUE_TERNARY_NEXT returns the next element in a ternary Thue sequence.
#
#  Discussion:
#
#    Thue was interested in showing that there were arbitrarily long
#    sequences of digits which never displayed a pair of contiguous
#    repetitions of any length.  That is, there was no occurrence of
#    "00" or "1010" or "121121", anywhere in the string.  This makes
#    the string "squarefree".
#
#    To do this, he demonstrated a way to start with a single digit,
#    and to repeatedly apply a series of transformation rules to each
#    digit of the sequence, deriving nonrepeating sequences of ever
#    greater length.
#
#    In this example, the digits allowed are ternary, that is, just
#    "0", "1" and "2".  The replacement rules are:
#
#    "0" -> "12"
#    "1" -> "102"
#    "2" -> "0"
#
#    This routine produces the next Thue sequence in a given series.
#    However, the input sequence must be a Thue sequence in order for
#    us to guarantee that the output sequence will also have the
#    nonrepetition property.
#
#    Also, enough space must be set aside in THUE to hold the
#    output sequence.  This will never be more than 3 times the input
#    value of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Brian Hayes,
#    Third Base,
#    American Scientist,
#    Volume 89, Number 6, pages 490-494, November-December 2001.
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
#
#  Determine length.
#
  n2 = 0

  for i in range ( 0, n ):

    if ( thue[i] == 0 ):
      n2 = n2 + 2
    elif ( thue[i] == 1 ):
      n2 = n2 + 3
    elif ( thue[i] == 2 ):
      n2 = n2 + 1
    else:
      print ''
      print 'THUE_TERNARY_NEXT - Fatal error!'
      print '  The input sequence contains a non-ternary digit'
      print '  THUE[%d] = %d' % ( i, thue[i] )
      exit ( 'THUE_TERNARY_NEXT - Fatal error!' )
#
#  Create new string.
#
  thue2 = np.zeros ( n2 )

  i2 = 0

  for i in range ( 0, n ): 

    if ( thue[i] == 0 ):
      thue2[i2] = 1
      i2 = i2 + 1
      thue2[i2] = 2
      i2 = i2 + 1
    elif ( thue[i] == 1 ):
      thue2[i2] = 1
      i2 = i2 + 1
      thue2[i2] = 0
      i2 = i2 + 1
      thue2[i2] = 2
      i2 = i2 + 1
    elif ( thue[i] == 2 ):
      thue2[i2] = 0
      i2 = i2 + 1

  return n2, thue2

def thue_ternary_next_test ( ):

#*****************************************************************************80
#
## THUE_TERNARY_NEXT_TEST tests THUE_TERNARY_NEXT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from i4vec_transpose_print import i4vec_transpose_print

  print ''
  print 'THUE_TERNARY_NEXT_TEST'
  print '  THUE_TERNARY_NEXT returns the next'
  print '  Thue ternary sequence.'
  print ''

  thue = np.zeros ( 1 )
  n = 1
  thue[0] = 1

  i4vec_transpose_print ( n, thue, str ( 0 ) )

  for i in range ( 1, 6 ):
    [ n, thue ] = thue_ternary_next ( n, thue )
    i4vec_transpose_print ( n, thue, str ( i ) )
#
#  Terminate.
#
  print ''
  print 'THUE_TERNARY_NEXT_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  thue_ternary_next_test ( )
  timestamp ( )
