#! /usr/bin/env python
#
def subset_lex_next ( n, jmp, ndim, k, a ):

#*****************************************************************************80
#
## SUBSET_LEX_NEXT generates the subsets of a set of N elements, one at a time.
#
#  Discussion:
#
#    The subsets are generated in lexicographical order.  
#
#    The routine can also be forced to generate only those subsets whose 
#    size is no greater than some user-specified maximum.
#
#  Example:
#
#    N = 5, JMP = ( K == 3 )
#
#    1
#    1 2
#    1 2 3
#    1 2 4
#    1 2 5
#    1 3
#    1 3 4
#    1 3 5
#    1 4
#    1 4 5
#    1 5
#    2
#    2 3
#    2 3 4
#    2 3 5
#    2 4
#    2 4 5
#    2 5
#    3
#    3 4
#    3 4 5
#    3 5
#    4
#    4 5
#    5
#    empty set.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    25 May 2015
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Albert Nijenhuis, Herbert Wilf,
#    Combinatorial Algorithms,
#    Academic Press, 1978, second edition,
#    ISBN 0-12-519260-6.
#
#  Parameters:
#
#    Input, integer N, the order of the main set from which subsets
#    are chosen.
#
#    Input, logical JMP.  In the simplest case, set JMP = FALSE for
#    a normal computation.  But to jump over supersets of the input set,
#    set JMP = TRUE.  Setting JMP = ( K == 3 ) before every new call
#    will, for example, force all the subsets returned
#    to have cardinality 3 or less.
#
#    Input, integer NDIM, the allowed storage for A.  If NDIM < N,
#    JMP must be used to avoid creation of a subset too large to store in A.
#
#    Input, integer K.  On first call, the user must set K = 0 as
#    a startup signal to the program.  Thereafter, set K to the output
#    value of K from the previous call. 
#
#    Input, integer A(NDIM).  On first call, the value of A is not important.  
#    Thereafter, set A to the output value of A from the previous call.
#
#    Output, integer K, the size of the computed subset.  On the last 
#    return, the empty set is returned and K is 0, which is a signal to
#    the user that the computation is complete.
#
#    Output, integer A(NDIM).  A(I) is the I-th element of the
#    subset, listed in increasing order, with 0's in entries
#    beyond entry K.
#  
  if ( k <= 0 ):

    if ( jmp ):
      return k, a

    i = 0
    k = 1
    a[0] = 1

  elif ( a[k-1] != n ):

    i = a[k-1]

    if ( not jmp ):
      k = k + 1

    a[k-1] = i + 1

  else:

    k = k - 1

    if ( k != 0 ):
      a[k-1] = a[k-1] + 1

  return k, a

def subset_lex_next_test ( ):

#*****************************************************************************80
#
## SUBSET_LEX_NEXT_TEST tests SUBSET_LEX_NEXT with size restrictions.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ''
  print 'SUBSET_LEX_NEXT_TEST'
  print '  SUBSET_LEX_NEXT generates all subsets of an N set.'
  print '  The user can impose a restriction on the'
  print '  maximum size of the subsets.'

  n = 5
  ndim = 3
  k = 0
  a = np.zeros ( ndim )
  
  print ''
  print '  Here, we require the subsets to be no larger'
  print '  than %d' % ( ndim )

  while ( True ):
 
    ltest = ( k == ndim )

    k, a = subset_lex_next ( n, ltest, ndim, k, a )
 
    if ( 0 < k ):
      for i in range ( 0, k ):
        print '  %4d' % ( a[i] ),
      print ''
    else:
      print 'The empty set.'
 
    if ( k == 0 ):
      break
#
#  Terminate.
#
  print ''
  print 'SUBSET_LEX_NEXT_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  subset_lex_next_test ( )
  timestamp ( )

