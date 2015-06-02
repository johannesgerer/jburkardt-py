#! /usr/bin/env python
#
def vec_gray_unrank ( n, base, rank ):

#*****************************************************************************80
#
## VEC_GRAY_UNRANK computes the product space element of a given rank.
#
#  Discussion:
#
#    The rank applies only to the elements as produced by the routine
#    VEC_GRAY_NEXT.
#
#  Examples:
#
#    N = 2, BASE = ( 2, 3 ), RANK = 4.
#
#    A = ( 1, 2 ).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 May 2015
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
#    Input, integer RANK, the desired rank, or order, of the element in
#    the list of all elements.  The rank count begins at 1 and extends
#    to MAXRANK = Product ( 1 <= I <= N ) BASE(I).
#
#    Output, integer A(N), the product space element of the given rank.
#
  import numpy as np

  a = np.zeros ( n, dtype = np.int32 )

  s = rank - 1

  for i in range ( n - 1, -1, -1 ):

    a[i] = ( s % base[i] )
    s = ( s // base[i] )

    if ( ( s % 2 ) == 1 ):
      a[i] = base[i] - a[i] - 1

  return a

def vec_gray_unrank_test ( ):

#*****************************************************************************80
#
## VEC_GRAY_UNRANK_TEST tests VEC_GRAY_UNRANK.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 4
  base = np.array ( [ 2, 2, 1, 4 ] )
  number = np.prod ( base )

  print ''
  print 'VEC_GRAY_UNRANK_TEST'
  print '  VEC_GRAY_UNRANK unranks product space elements.'
  print ''
  print '  The number of components is %d' % ( n )
  print '  The number of elements is %d' % ( number )
  print '  Each component has its own number of degrees of'
  print '  freedom.'

  rank = 7
  a = vec_gray_unrank ( n, base, rank )

  print ''
  print '  VEC_GRAY_UNRANK reports the element of rank %d:' % ( rank )
  print ''
  for i in range ( 0, n ):
    print '  %d' % ( a[i] ),
  print ''
#
#  Terminate.
#
  print ''
  print 'VEC_GRAY_UNRANK_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  vec_gray_unrank_test ( )
  timestamp ( )
