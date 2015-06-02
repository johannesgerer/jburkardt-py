#! /usr/bin/env python
#
def vec_gray_rank ( n, base, a ):

#*****************************************************************************80
#
## VEC_GRAY_RANK computes the rank of a product space element.
#
#  Discussion:
#
#    The rank applies only to the elements as produced by the routine
#    VEC_GRAY_NEXT.
#
#  Example:
#
#    N = 2, BASE = (/ 2, 3 /), A = ( 1, 2 ),
#
#    RANK = 4.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Dennis Stanton, Dennis White,
#    Constructive Combinatorics,
#    Springer, 1986,
#    ISBN: 0387963472,
#    LC: QA164.S79.
#
#  Parameters:
#
#    Input, integer N, the number of components.
#
#    Input, integer BASE(N), contains the number of degrees of
#    freedom of each component.  The output values of A will
#    satisfy 0 <= A(I) < BASE(I).
#
#    Input, integer A(N), the product space element, with the
#    property that 0 <= A(I) < BASE(I) for each entry I.
#
#    Output, integer RANK, the rank, or order, of the element in
#    the list of all elements.  The rank count begins at 1.
#
  rank = 0

  for i in range ( 0, n ):

    if ( ( rank % 2 ) == 1 ):
      c = base[i] - a[i] - 1
    else:
      c = a[i]

    rank = base[i] * rank + c

  rank = rank + 1

  return rank

def vec_gray_rank_test ( ):

#*****************************************************************************80
#
## VEC_GRAY_RANK_TEST tests VEC_GRAY_RANK.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 4
  base = np.array ( [ 2, 2, 1, 4 ] )
  ne = np.prod ( base )

  print ''
  print 'VEC_GRAY_RANK_TEST'
  print '  VEC_GRAY_RANK ranks product space elements.'
  print ''
  print '  The number of components is %d' % ( n )
  print '  The number of elements is %d' % ( ne )
  print '  Each component has its own number of degrees of'
  print '  freedom.'

  a = np.zeros ( n )
  for i in range ( 0, n ):
    a[i] = base[i] // 2

  rank = vec_gray_rank ( n, base, a )

  print ''
  print '  VEC_GRAY_RANK reports the element'
  print ''
  for i in range ( 0, n ):
    print '  %d' % ( a[i] ),
  print ''
  print ''
  print '  has rank %d' % ( rank )
#
#  Terminate.
#
  print ''
  print 'VEC_GRAY_RANK_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  vec_gray_rank_test ( )
  timestamp ( )
