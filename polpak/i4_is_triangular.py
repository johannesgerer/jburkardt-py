#!/usr/bin/env python

def i4_is_triangular ( i ) :

#*****************************************************************************80
#
## I4_IS_TRIANGULAR determines whether an integer is triangular.
#
#  Discussion:
#
#    The N-th triangular number is equal to the sum of the first
#    N integers.
#
#  First Values:
#
#    Index  Value
#     0      0
#     1      1
#     2      3
#     3      6
#     4     10
#     5     15
#     6     21
#     7     28
#     8     36
#     9     45
#    10     55
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer I, the integer to be checked.
#
#    Output, boolean VALUE, is TRUE if I is triangular.
#
  from i4_to_triangle import i4_to_triangle

  if ( i < 0 ):

    value = False

  elif ( i == 0 ):

    value = True

  else:

    j, k = i4_to_triangle ( i )

    if ( j == k ):
      value = True
    else:
      value = False

  return value

def i4_is_triangular_test ( ) :

#*****************************************************************************80
#
## I4_IS_TRIANGULAR_TEST tests I4_IS_TRIANGULAR.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'I4_IS_TRIANGULAR_TEST'
  print '  I4_IS_TRIANGULAR reports whether an I4 is prime.'
  print ' '
  print '         I  I4_IS_TRIANGULAR(I)'
  print ' '

  for i in range ( 0, 21 ):
    j = i4_is_triangular ( i )
    print '  %8d  %r' % ( i, j )

  print ''
  print 'I4_IS_TRIANGULAR_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_is_triangular_test ( )
  timestamp ( )
