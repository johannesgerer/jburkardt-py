#!/usr/bin/env python

def i4vec_sort_heap_index_a ( n, a ):

#*****************************************************************************80
#
## I4VEC_SORT_HEAP_INDEX_A does an indexed heap ascending sort of an I4VEC.
#
#  Discussion:
#
#    An I4VEC is a vector of I4's.
#
#    The sorting is not actually carried out.  Rather an index array is
#    created which defines the sorting.  This array may be used to sort
#    or index the array, or to sort or index related arrays keyed on the
#    original array.
#
#    Once the index array is computed, the sorting can be carried out
#    "implicitly:
#
#      a(indx(*))
#
#    or explicitly, by the call
#
#      i4vec_permute ( n, indx, a )
#
#    after which a(*) is sorted.
#
#    Note that the index vector is 0-based.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, int N, the number of entries in the array.
#
#    Input, int A[N], an array to be index-sorted.
#
#    Output, int I4VEC_SORT_HEAP_INDEX_A[N], contains the sort index.  The
#    I-th element of the sorted array is A(INDX(I)).
#
  import numpy as np

  indx = np.zeros ( n, dtype = np.int32 )

  for i in range ( 0, n ):
    indx[i] = i

  if ( n == 1 ):
    return indx

  l = n // 2 + 1
  ir = n

  while ( True ):
    if ( 1 < l ):
      l = l - 1
      indxt = indx[l-1]
      aval = a[indxt]
    else:
      indxt = indx[ir-1]
      aval = a[indxt]
      indx[ir-1] = indx[0]
      ir = ir - 1

      if ( ir == 1 ):
        indx[0] = indxt
        break

    i = l
    j = l + l

    while ( j <= ir ):
      if ( j < ir ):
        if ( a[indx[j-1]] < a[indx[j]] ):
          j = j + 1

      if ( aval < a[indx[j-1]] ):
        indx[i-1] = indx[j-1]
        i = j
        j = j + j
      else:
        j = ir + 1
    indx[i-1] = indxt

  return indx

def i4vec_sort_heap_index_a_test ( ):

#*****************************************************************************80
#
## I4VEC_SORT_HEAP_INDEX_A_TEST tests I4VEC_SORT_HEAP_INDEX_A.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 October 2014
#
#  Author:
#
#    John Burkardt
#
  from i4vec_print import i4vec_print
  from i4vec_uniform_ab import i4vec_uniform_ab

  n = 20

  print ''
  print 'I4VEC_SORT_HEAP_INDEX_A_TEST'
  print '  I4VEC_SORT_HEAP_INDEX_A creates an ascending'
  print '  sort index for an I4VEC.'

  b = 0
  c = 3 * n
  seed = 123456789

  a, seed = i4vec_uniform_ab ( n, b, c, seed )

  i4vec_print ( n, a, '  Unsorted array A:' )

  indx = i4vec_sort_heap_index_a ( n, a )

  i4vec_print ( n, indx, '  Sort vector INDX:' )

  print ''
  print '       I   INDX(I)  A(INDX(I))'
  print ''
  for i in range ( 0, n ):
     print '  %8d  %8d  %8d' % ( i, indx[i], a[indx[i]] )

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp

  timestamp ( )
  i4vec_sort_heap_index_a_test ( )
  timestamp ( )
