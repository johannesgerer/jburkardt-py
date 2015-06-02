#! /usr/bin/env python
#
def perm0_sign ( n, p ):

#*****************************************************************************80
#
## PERM0_SIGN returns the sign of a permutation of (0,...,N-1).
#
#  Discussion:
#
#    A permutation can always be replaced by a sequence of pairwise
#    transpositions.  A given permutation can be represented by
#    many different such transposition sequences, but the number of
#    such transpositions will always be odd or always be even.
#    If the number of transpositions is even or odd, the permutation is
#    said to be even or odd.
#
#  Example:
#
#    Input:
#
#      N = 9
#      P = 1, 2, 8, 5, 6, 7, 4, 3, 0
#
#    Output:
#
#      P_SIGN = +1
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    30 May 2015
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
#    Input, integer N, the number of objects permuted.
#
#    Input, integer P(N), a permutation, in standard index form.
#
#    Output, integer P_SIGN, the "sign" of the permutation.
#    +1, the permutation is even,
#    -1, the permutation is odd.
#
  import numpy as np
  from sys import exit
  from i4vec_index import i4vec_index
  from perm0_check import perm0_check

  check = perm0_check ( n, p )

  if ( not check ):
    print ''
    print 'PERM0_SIGN - Fatal error!'
    print '  The input array does not represent'
    print '  a proper permutation.  In particular, the'
    print '  array is missing the value %d' % ( ierror )
    exit ( 'PERM0_SIGN - Fatal error!' )
#
#  Make a temporary copy of P.
#  Apparently, the input P is a pointer, and so changes to P
#  that in MATLAB would be local are, in Python, global!
#
  q = np.zeros ( n )
  for i in range ( 0, n ):
    q[i] = p[i]
#
#  Start with P_SIGN indicating an even permutation.
#  Restore each element of the permutation to its correct position,
#  updating P_SIGN as you go.
#
  p_sign = 1

  for i in range ( 0, n - 1 ):

    j = i4vec_index ( n, q, i )

    if ( j != i ):
      t    = q[i]
      q[i] = q[j]
      q[j] = t
      p_sign = - p_sign

  return p_sign

def perm0_sign_test ( ):

#*****************************************************************************80
#
## PERM0_SIGN_TEST tests PERM0_SIGN.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 February 2003
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from perm0_lex_next import perm0_lex_next

  print ''
  print 'PERM0_SIGN_TEST'
  print '  PERM0_SIGN computes the sign of a permutation of (0,...,N-1).'
  print ''
  print '  RANK  SIGN  Permutation'
  print ''

  n = 4
  p = np.zeros ( n )
  more = False

  rank = 0

  while ( True ):

    p, more = perm0_lex_next ( n, p, more )

    p_sign = perm0_sign ( n, p )

    if ( not more ):
      break

    print '  %2d  %4d  ' % ( rank, p_sign ),
    for i in range ( 0, n ):
      print '  %2d' % ( p[i] ),
    print ''

    rank = rank + 1
#
#  Terminate.
#
  print ''
  print 'PERM0_SIGN_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  perm0_sign_test ( )
  timestamp ( )

