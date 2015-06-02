#! /usr/bin/env python
#
def tuple_next2 ( n, xmin, xmax, rank, x ):

#*****************************************************************************80
#
## TUPLE_NEXT2 computes the next element of an integer tuple space.
#
#  Discussion:
#
#    The elements X are N vectors.
#
#    Each entry X(I) is constrained to lie between XMIN(I) and XMAX(I).
#
#    The elements are produced one at a time.
#
#    The first element is
#      (XMIN(1), XMIN(2), ..., XMIN(N)),
#    the second is (probably)
#      (XMIN(1), XMIN(2), ..., XMIN(N)+1),
#    and the last element is
#      (XMAX(1), XMAX(2), ..., XMAX(N))
#
#    Intermediate elements are produced in a lexicographic order, with
#    the first index more important than the last, and the ordering of
#    values at a fixed index implicitly defined by the sign of
#    XMAX(I) - XMIN(I).
#
#  Example:
#
#    N = 2,
#    XMIN = (/ 1, 10 /)
#    XMAX = (/ 3,  8 /)
#
#    RANK    X
#    ----  -----
#      1   1 10
#      2   1  9
#      3   1  8
#      4   2 10
#      5   2  9
#      6   2  8
#      7   3 10
#      8   3  9
#      9   3  8
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of components.
#
#    Input, integer XMIN(N), XMAX(N), the "minimum" and "maximum" entry values.
#    These values are minimum and maximum only in the sense of the lexicographic
#    ordering.  In fact, XMIN(I) may be less than, equal to, or greater
#    than XMAX(I).
#
#    Input, integer RANK, is set to 0 on the first call.  Thereafter, RANK
#    should be the value output by RANK on the previous call.
#
#    Input, integer X(N), except on the first call, X should contain
#    the value output in X on the previous call.
#
#    Output, integer RANK, the rank of the output item.  
#    If RANK is zero, there are no more items in the sequence.
#
#    Output, integer X(N), the next tuple.
#
  from sys import exit
  from i4_sign import i4_sign

  if ( rank < 0 ):
    print ''
    print 'TUPLE_NEXT2 - Fatal error!'
    print '  Illegal value of RANK = %d' % ( rank )
    exit ( 'TUPLE_NEXT2 - Fatal error!' )

  t = 1
  for i in range ( 0, n ):
    t = t * ( 1 + abs ( xmax[i] - xmin[i] ) )

  if ( t < rank ):
    print ''
    print 'TUPLE_NEXT2 - Fatal error!'
    print '  Illegal value of RANK = %d' % ( rank )
    exit ( 'TUPLE_NEXT2 - Fatal error!' )

  if ( rank == 0 ):

    for i in range ( 0, n ):
      x[i] = xmin[i]
    rank = 1

  else:
  
    rank = rank + 1
    i = n - 1

    while ( True ):

      if ( x[i] != xmax[i] ):
        x[i] = x[i] + i4_sign ( xmax[i] - xmin[i] )
        break

      x[i] = xmin[i]

      if ( i == 0 ):
        rank = 0
        break

      i = i - 1

  return rank, x

def tuple_next2_test ( ):

#*****************************************************************************80
#
## TUPLE_NEXT2_TEST tests TUPLE_NEXT2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 3

  xmin = np.array ( [ 2, 3, 8 ] )
  xmax = np.array ( [ 4, 3, 5 ] )

  print ''
  print 'TUPLE_NEXT2_TEST'
  print '  TUPLE_NEXT2 returns the next "tuple", that is,'
  print '  a vector of N integers.'
  print ''
  print '  N = %d' % ( n )
  print ''

  print '  Min ',
  for i in range ( 0, n ):
    print '  %2d' % ( xmin[i] ),
  print ''
  print ''

  rank = 0
  x = np.zeros ( n )
  
  while ( True ):

    rank, x = tuple_next2 ( n, xmin, xmax, rank, x )

    if ( rank == 0 ):
      break

    print '  %2d  ' % ( rank ),
    for i in range ( 0, n ):
      print '  %2d' % ( x[i] ),
    print ''

  print ''
  print '  Max ',
  for i in range ( 0, n ):
    print '  %2d' % ( xmax[i] ),
  print ''
#
#  Terminate.
#
  print ''
  print 'TUPLE_NEXT2_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  tuple_next2_test ( )
  timestamp ( )
