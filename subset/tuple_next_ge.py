#! /usr/bin/env python
#
def tuple_next_ge ( m, n, rank, x ):

#*****************************************************************************80
#
## TUPLE_NEXT_GE computes the next "nondecreasing" element of a tuple space.
#
#  Discussion:
#
#    The elements are N vectors.  Each element is constrained to lie
#    between 1 and M, and to have components that are nondecreasing.
#    That is, for an element X, and any positive K,
#      X(I) <= X(I+K)
#
#    The elements are produced one at a time.
#    The first element is
#      (1,1,...,1)
#    and the last element is
#      (M,M,...,M)
#    Intermediate elements are produced in lexicographic order.
#
#  Example:
#
#    N = 3, M = 3
#
#    RANK   X
#    ----  -----
#       1  1 1 1
#       2  1 1 2
#       3  1 1 3
#       4  1 2 2
#       5  1 2 3
#       6  1 3 3
#       7  2 2 2
#       8  2 2 3
#       9  2 3 3
#      10  3 3 3
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
#  Parameters:
#
#    Input, integer M, the maximum entry.
#
#    Input, integer N, the number of components.
#
#    Input, integer RANK, the rank of the input tuple.
#    On first call, set K to 0.  Thereafter, K will indicate the
#    order of the element returned.  When there are no more elements,
#    K will be returned as 0.
#
#    Input, integer X(N), on input the previous tuple (except
#    on the first call, when the input value of X is not needed.)
#    On output, the next tuple.
#
#    Output, integer RANK, the rank of the output tuple.
#    When there are no more elements, RANK will be returned as 0.
#
#    Output, integer X(N), on input the previous tuple (except
#    on the first call, when the input value of X is not needed.)
#    On output, the next tuple.
#
  if ( rank <= 0 ):
    for i in range ( 0, n ):
      x[i] = 1
    rank = 1
    return rank, x

  for i in range ( n - 1, -1, -1 ):

    if ( x[i] < m ):
      x[i] = x[i] + 1
      for j in range ( i + 1, n ):
        x[j] = x[i]
      rank = rank + 1
      return rank, x

  rank = 0
  for i in range ( 0, n ):
    x[i] = 0

  return rank, x

def tuple_next_ge_test ( ):

#*****************************************************************************80
#
## TUPLE_NEXT_GE_TEST tests TUPLE_NEXT_GE.
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

  m = 3
  n = 3
  rank = 0
  x = np.zeros ( n )

  print ''
  print 'TUPLE_NEXT_GE_TEST'
  print '  TUPLE_NEXT_GE returns the next "tuple", that is,'
  print '  a vector of N integers, each between 1 and M,'
  print '  with the constraint that the entries be'
  print '  nondecreasing.'
  print ''
  print '  M = %d' % ( m )
  print '  N = %d' % ( n )
  print ''

  while ( True ):

    rank, x = tuple_next_ge ( m, n, rank, x )

    if ( rank == 0 ):
      break

    print '  %2d' % ( rank ),
    for i in range ( 0, n ):
      print '  %4d' % ( x[i] ),
    print ''
#
#  Terminate.
#
  print ''
  print 'TUPLE_NEXT_GE_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  tuple_next_ge_test ( )
  timestamp ( )

