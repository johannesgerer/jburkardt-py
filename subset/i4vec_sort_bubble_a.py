#!/usr/bin/env python

def i4vec_sort_bubble_a ( n, a ):

#*****************************************************************************80
#
## I4VEC_SORT_BUBBLE_A ascending sorts an integer vector using bubble sort.
#
#  Discussion:
#
#    Bubble sort is simple to program, but inefficient.  It should not
#    be used for large arrays.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of entries in the array.
#
#    Input, integer A(N), an unsorted array.
#
#    Output, integer A(N), the array has been sorted.
#
  for i in range ( 0, n - 1 ):
    for j in range ( i + 1, n ):
      if ( a[j] < a[i] ):
        t    = a[i]
        a[i] = a[j]
        a[j] = t

  return a

def i4vec_sort_bubble_a_test ( ):

#*****************************************************************************80
#
## I4VEC_SORT_BUBBLE_A_TEST tests I4VEC_SORT_BUBBLE_A.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 May 2015
#
#  Author:
#
#    John Burkardt
#
  from i4vec_transpose_print import i4vec_transpose_print
  from i4vec_uniform_ab import i4vec_uniform_ab
  
  print ''
  print 'I4VEC_SORT_BUBBLE_A_TEST'
  print '  I4VEC_SORT_BUBBLE_A ascending sorts an I4VEC.'

  n = 20
  i4_lo = 0
  i4_hi = 3 * n
  seed = 123456789

  a, seed = i4vec_uniform_ab ( n, i4_lo, i4_hi, seed )

  i4vec_transpose_print ( n, a, '  Unsorted:' )

  a = i4vec_sort_bubble_a ( n, a )

  i4vec_transpose_print ( n, a, '  Ascending sorted:' )
#
#  Terminate.
#
  print ''
  print 'I4VEC_SORT_BUBBLE_A_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4vec_sort_bubble_a_test ( )
  timestamp ( )
