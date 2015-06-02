#! /usr/bin/env python
#
def subset_gray_unrank ( rank, n ):

#*****************************************************************************80
#
## SUBSET_GRAY_UNRANK produces a subset of an N set of the given Gray code rank.
#
#  Example:
#
#    N = 4
#
#     Rank     A    
#    -----  -------
#
#        1  0 0 0 0
#        2  1 0 0 0
#        3  1 1 0 0
#        4  0 1 0 0
#        5  0 1 1 0
#        6  1 1 1 0
#        7  1 0 1 0
#        8  0 0 1 0
#        9  0 0 1 1
#       10  1 0 1 1
#       11  1 1 1 1
#       12  0 1 1 1
#       13  0 1 0 1
#       14  1 1 0 1
#       15  1 0 0 1
#       16  0 0 0 1
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    29 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer RANK, the rank of the subset in the Gray code ordering.
#
#    Input, integer N, the order of the total set from which
#    subsets will be drawn.
#
#    Output, integer A(N) A(I) is 1 if element I is in the set,
#    and 0 otherwise.
#
  from gray_unrank2 import gray_unrank2
  from ui4_to_ubvec import ui4_to_ubvec

  gray = gray_unrank2 ( rank-1 )

  a = ui4_to_ubvec ( gray, n )

  return a

def subset_gray_unrank_test ( ):

#*****************************************************************************80
#
## SUBSET_GRAY_UNRANK_TEST tests SUBSET_GRAY_UNRANK.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 May 2015
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ''
  print 'SUBSET_GRAY_UNRANK_TEST'
  print '  SUBSET_GRAY_UNRANK finds the subset of an N set'
  print '  of a given rank under the Gray code ordering.'
  print ''
  print '  N is %d' % ( n )
  print ''
  print '  Rank   Subset'
  print ''

  for rank in range ( 1, 11 ):
 
    a = subset_gray_unrank ( rank, n )

    print '  %4d' % ( rank ),
    for i in range ( 0, n ):
      print '  %2d' % (a[i] ),
    print ''
#
#  Terminate.
#
  print ''
  print 'SUBSET_GRAY_UNRANK_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  subset_gray_unrank_test ( )
  timestamp ( )

