#!/usr/bin/env python

def i4vec_permute ( n, p, a ):

#*****************************************************************************80
#
## I4VEC_PERMUTE permutes an I4VEC in place.
#
#  Discussion:
#
#    An I4VEC is a vector of I4's.
#
#    This routine permutes an array of integer "objects", but the same
#    logic can be used to permute an array of objects of any arithmetic
#    type, or an array of objects of any complexity.  The only temporary
#    storage required is enough to store a single object.  The number
#    of data movements made is N + the number of cycles of order 2 or more,
#    which is never more than N + N/2.
#
#  Example:
#
#    Input:
#
#      N = 5
#      P = (   1,   3,   4,   0,   2 )
#      A = (   1,   2,   3,   4,   5 )
#
#    Output:
#
#      A    = (   2,   4,   5,   1,   3 ).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of objects.
#
#    Input, integer P[N], the permutation.  P(I) = J means
#    that the I-th element of the output array should be the J-th
#    element of the input array.
#
#    Input, integer A[N], the array to be permuted.
#
#    Output, integer A[N], the permuted array.
#
  from perm0_check import perm0_check
  from sys import exit

  check = perm0_check ( n, p );

  if ( not check ):
    print ''
    print 'I4VEC_PERMUTE - Fatal error!'
    print '  PERM0_CHECK rejects the permutation.'
    exit ( 'I4VEC_PERMUTE - Fatal error!' )
#
#  In order for the sign negation trick to work, we need to assume that the
#  entries of P are strictly positive.  Presumably, the lowest number is 0.
#  So temporarily add 1 to each entry to force positivity.
#
  for i in range ( 0, n ):
    p[i] = p[i] + 1
#
#  Search for the next element of the permutation that has not been used.
#
  for istart in range ( 1, n + 1 ):
    if ( p[istart-1] < 0 ):
      continue
    elif ( p[istart-1] == istart ):
      p[istart-1] = - p[istart-1]
    else:
      a_temp = a[istart-1];
      iget = istart;
#
#  Copy the new value into the vacated entry.
#
      while ( True ):
        iput = iget
        iget = p[iget-1]

        p[iput-1] = - p[iput-1]

        if ( iget < 1 or n < iget ):
          print ''
          print 'I4VEC_PERMUTE - Fatal error!'
          print '  Entry IPUT = %d has' % ( iput )
          print '  an illegal value IGET = %d.' % (iget )
          exit ( 'I4VEC_PERMUTE - Fatal error!' )

        if ( iget == istart ):
          a[iput-1] = a_temp
          break

        a[iput-1] = a[iget-1]
#
#  Restore the signs of the entries.
#
  for i in range ( 0, n ):
    p[i] = - p[i]
#
#  Restore the entries.
#
  for i in range ( 0, n ):
    p[i] = p[i] - 1

  return a

def i4vec_permute_test ( ):

#*****************************************************************************80
#
## I4VEC_PERMUTE_TEST tests I4VEC_PERMUTE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 October 2014
#
#  Author:
#
#    John Burkardt
#
  from i4vec_print import i4vec_print
  from i4vec_uniform_ab import i4vec_uniform_ab
  from perm0_uniform import perm0_uniform

  n = 12

  print ''
  print 'I4VEC_PERMUTE_TEST'
  print '  I4VEC_PERMUTE reorders an I4VEC'
  print '  according to a given permutation.'

  b = 0
  c = n
  seed = 123456789
  a, seed = i4vec_uniform_ab ( n, b, c, seed )

  i4vec_print ( n, a, '  A[*], before rearrangement:' )

  p, seed = perm0_uniform ( n, seed )

  i4vec_print ( n, p, '  Permutation vector P[*]:' )

  a = i4vec_permute ( n, p, a )

  i4vec_print ( n, a, '  A[P[*]]:' )
#
#  Terminate.
#
  print ''
  print 'I4VEC_PERMUTE_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4vec_permute_test ( )
  timestamp ( )
