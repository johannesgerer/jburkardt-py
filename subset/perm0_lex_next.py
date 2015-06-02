#! /usr/bin/env python
#
def perm0_lex_next ( n, p, more ):

#*****************************************************************************80
#
## PERM0_LEX_NEXT generates permutations of (0,...,N-1) in lexical order.
#
#  Example:
#
#    N = 3
#
#    1   0 1 2
#    2   0 2 1
#    3   1 0 2
#    4   1 2 0
#    5   2 0 1
#    6   2 1 0
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
#    John Burkardt
#
#  Reference:
#
#    Mok-Kong Shen,
#    Algorithm 202: Generation of Permutations in Lexicographical Order,
#    Communications of the ACM,
#    Volume 6, September 1963, page 517.
#
#  Parameters:
#
#    Input, integer N, the number of elements being permuted.
#
#    Input, integer P(N), the permutation, in standard index form.
#
#    Input, logical MORE.
#    On the first call, the user should set MORE = FALSE, which signals
#    the routine to do initialization.
#    On return, if MORE is TRUE, then another permutation has been
#    computed and returned, while if MORE is FALSE, there are no more
#    permutations.
#
#    Output, integer P(N), the next permutation.
#
#    Output, logical MORE.
#    On the first call, the user should set MORE = FALSE, which signals
#    the routine to do initialization.
#    On return, if MORE is TRUE, then another permutation has been
#    computed and returned, while if MORE is FALSE, there are no more
#    permutations.
#
  from i4vec_indicator0 import i4vec_indicator0
#
#  Initialization.
#
  if ( not more ):

    p = i4vec_indicator0 ( n )
    more = True

  else:

    if ( n <= 1 ):
      more = False
      return p, more

    w = n

    while ( p[w-1] < p[w-2] ):

      if ( w == 2 ):
        more = False
        return p, more

      w = w - 1

    u = p[w-2]

    for j in range ( n, w - 1, -1 ):

      if ( u < p[j-1] ):

        p[w-2] = p[j-1]
        p[j-1] = u

        khi = ( n - w - 1 ) // 2

        for k in range ( 0, khi + 1 ):
          t        = p[n-k-1]
          p[n-k-1] = p[w+k-1]
          p[w+k-1] = t

        return p, more

  return p, more

def perm0_lex_next_test ( ):

#*****************************************************************************80
#
## PERM0_LEX_NEXT_TEST tests PERM0_LEX_NEXT.
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
#    John Burkardt
#
  import numpy as np
  from perm_print import perm_print

  n = 4

  print ''
  print 'PERM0_LEX_NEXT_TEST'
  print '  PERM0_LEX_NEXT generates permutations in order.'
  print ''
  
  p = np.zeros ( n )
  more = False
 
  while ( True ):

    p, more = perm0_lex_next ( n, p, more )

    if ( not more ):
      break

    perm_print ( n, p, '' )
#
#  Terminate.
#
  print ''
  print 'PERM0_LEX_NEXT_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  perm0_lex_next_test ( )
  timestamp ( )


