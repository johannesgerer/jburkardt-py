#!/usr/bin/env python

def tuple_next ( m1, m2, n, rank, x ):

#*****************************************************************************80
#
## TUPLE_NEXT computes the next element of a tuple space.
#
#  Discussion:
#
#    The elements are N vectors.  Each entry is constrained to lie
#    between M1 and M2.  The elements are produced one at a time.
#    The first element is
#      (M1,M1,...,M1),
#    the second element is
#      (M1,M1,...,M1+1),
#    and the last element is
#      (M2,M2,...,M2)
#    Intermediate elements are produced in lexicographic order.
#
#  Example:
#
#    N = 2, M1 = 1, M2 = 3
#
#    INPUT        OUTPUT
#    -------      -------
#    Rank  X      Rank   X
#    ----  ---    -----  ---
#    0     * *    1      1 1
#    1     1 1    2      1 2
#    2     1 2    3      1 3
#    3     1 3    4      2 1
#    4     2 1    5      2 2
#    5     2 2    6      2 3
#    6     2 3    7      3 1
#    7     3 1    8      3 2
#    8     3 2    9      3 3
#    9     3 3    0      0 0
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 March 2007
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M1, M2, the minimum and maximum entries.
#
#    Input, integer N, the number of components.
#
#    Input, integer RANK, counts the elements.
#    On first call, set RANK to 0.  On subsequent calls, the input value of
#    RANK should be the output value of RANK from the previous call.
#
#    Input, integer X(N), the previous tuple.
#
#    Output, integer RANK, the order of the next tuple.  When there are no
#    more elements, RANK will be returned as 0.
#
#    Output, integer X(N), the next tuple.
#
  if ( m2 < m1 ):

    rank = 0

  elif ( rank <= 0 ):

    for i in range ( 0, n ):
      x[i] = m1
      rank = 1

  else:

    rank = rank + 1
    i = n - 1

    while ( True ):

      if ( x[i] < m2 ):
        x[i] = x[i] + 1
        break

      x[i] = m1

      if ( i == 0 ):
        rank = 0
        for i in range ( 0, n ):
          x[i] = m1
          break

      i = i - 1

  return rank, x

def tuple_next_test ( ):

#*****************************************************************************80
#
## TUPLE_NEXT_TEST tests TUPLE_NEXT.
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
  import numpy as np

  n = 2
  m1 = 2
  m2 = 4

  print ''
  print 'TUPLE_NEXT_TEST'
  print '  TUPLE_NEXT returns the next "tuple", that is,'
  print '  a vector of N integers, each between M1 and M2.'
  print ''
  print '  M1 = %d' % ( m1 )
  print '  M2 = %d' % ( m2 )
  print '  N =  %d' % ( n )
  print ''
  print '   #    X[0]   X[1]'
  print ''
  rank = 0
  x = np.zeros ( n )

  while ( True ):

    rank, x = tuple_next ( m1, m2, n, rank, x )

    if ( rank == 0 ):
      break

    print '%4d  ' % ( rank ),
    for i in range ( 0, n ):
      print '%4d  ' % ( x[i] ),
    print ''
#
#  Terminate.
#
  print ''
  print 'TUPLE_NEXT_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  tuple_next_test ( )
  timestamp ( )

