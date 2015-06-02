#!/usr/bin/env python
#
def comb_next ( n, k, a, done ):

#*****************************************************************************80
#
## COMB_NEXT computes combinations of K things out of N.
#
#  Discussion:
#
#    The combinations are computed one at a time, in lexicographical order.
#
#    10 April 1009: Thanks to "edA-qa mort-ora-y" for supplying a
#    correction to this code.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Charles Mifsud,
#    Combination in Lexicographic Order,
#    ACM algorithm 154,
#    Communications of the ACM,
#    March 1963.
#
#  Parameters:
#
#    Input, integer N, the total number of things.
#
#    Input, integer K, the number of things in each combination.
#
#    Input, integer A(K), the output value of A on the previous call.
#    This value is not needed on a startup call.
#
#    Input, logical DONE, should be set to TRUE (1) on the first call,
#    and thereafter set to the output value of DONE on the previous call.
#
#    Output, integer(K), the next combination.
#
#    Output, logical DONE, is FALSE (0) if the routine can be called
#    again for more combinations, and TRUE (1) if there are no more.
#
  from i4vec_indicator1 import i4vec_indicator1

  if ( done ):

    if ( 0 < k ):
      a = i4vec_indicator1 ( k )
      done = False

  else:

    done = True
    km1 = k - 1

    if ( a[km1] < n ):

      a[km1] = a[km1] + 1
      done = False

    else:

      for i in range ( k, 1, -1 ):

        if ( a[i-2] < n-k+i-1 ):

          a[i-2] = a[i-2] + 1

          for j in range (  i, k + 1 ):
            a[j-1] = a[i-2] + j - ( i - 1 )
          done = False

          break

  return a, done

def comb_next_test ( ):

#*****************************************************************************80
#
## COMB_NEXT_TEST tests COMB_NEXT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from i4vec_transpose_print import i4vec_transpose_print

  n = 5

  print ''
  print 'COMB_NEXT_TEST'
  print '  COMB_NEXT produces combinations.'
  print '  We are selecting from a set of size %d' % ( n )

  for k in range ( 1, n + 1 ):

    print ''
    print '  Combinations of size %d:' % ( k )
    print ''

    a = np.zeros ( k )
    done = True

    while ( True ):

      a, done = comb_next ( n, k, a, done )
 
      if ( done ):
        break

      i4vec_transpose_print ( k, a, '' )
#
#  Terminate.
#
  print ''
  print 'COMB_NEXT_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  comb_next_test ( )
  timestamp ( )

