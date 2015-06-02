#!/usr/bin/env python

def i4vec_reverse ( n, a ):

#*****************************************************************************80
#
## I4VEC_REVERSE reverses the elements of an I4VEC.
#
#  Example:
#
#    Input:
#
#      N = 5,
#      A = ( 11, 12, 13, 14, 15 ).
#
#    Output:
#
#      A = ( 15, 14, 13, 12, 11 ).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    17 April 2005
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of entries in the array.
#
#    Input, integer A(N), the array to be reversed.
#
#    Output, integer A(N), the reversed array.
#
  for i in range ( 0, n / 2 ):
    j = n - i - 1
    t    = a[i]
    a[i] = a[j]
    a[j] = t

  return a

def i4vec_reverse_test ( ):

#*****************************************************************************80
#
## I4VEC_REVERSE_TEST tests I4VEC_REVERSE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 April 2009
#
#  Author:
#
#    John Burkardt
#
  from i4vec_print import i4vec_print
  from i4vec_uniform_ab import i4vec_uniform_ab

  n = 10
  b = 0
  c = 3 * n

  print ''
  print 'I4VEC_REVERSE_TEST'
  print '  I4VEC_REVERSE reverses a list of integers.'

  seed = 123456789

  a, seed = i4vec_uniform_ab ( n, b, c, seed )

  i4vec_print ( n, a, '  Original vector:' )

  a = i4vec_reverse ( n, a )

  i4vec_print ( n, a, '  Reversed:' )
#
#  Terminate.
#
  print ''
  print 'I4VEC_REVERSE_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4vec_reverse_test ( )
  timestamp ( )
