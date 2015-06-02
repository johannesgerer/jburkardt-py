#! /usr/bin/env python
#
def ytb_next ( n, lam, a, more ):

#*****************************************************************************80
#
## YTB_NEXT computes the next Young tableau for a given shape.
#
#  Discussion:
#
#    When the routine is called with MORE = FALSE (the first time), and
#    if LAM on this call has M parts, with M < N, then the user
#    must also make sure that LAM(M+1) = 0.
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
#    Input, integer N, the integer which is to be partitioned.
#
#    Input, integer LAM(N), contains a partition of N.
#    The elements of LAM are nonnegative integers that sum to N.
#    On the first call, with MORE = FALSE, the user sets LAM.
#    After the first call, the input value of LAM is not important.
#
#    Input, integer A(N).  On the first call, with MORE = FALSE,
#    no value of A needs to be set.  After the first call, the input
#    value of A should be the output value of A from the previous call.
#
#    Input, logical MORE.  Set MORE to FALSE before the first call.
#    Thereafter, set it to the output value of MORE on the previous call.
#
#    Output, integer LAM(N), contains the partition of N,
#    corresponding to the Young tableau.
#
#    Output, integer A(N), the next Young tableau.  A(I) is the
#    row containing I in the output tableau.
#
#    Output, logical MORE, is TRUE until the last tableau is returned,
#    when the value of MORE is FALSE.
#
  it = n

  if ( more ):

    lam[0] = 1
    for i in range ( 1, n ):
      lam[i] = 0

    isave = 0

    for i in range ( 2, n + 1 ):

      lam[a[i-1]-1] = lam[a[i-1]-1] + 1

      if ( a[i-1] < a[i-2] ):
        isave = i
        break

    if ( isave == 0 ):
      more = False
      return lam, a, more

    it = lam[1+a[isave-1]-1]

    for i in range ( n, 0, -1 ):

      if ( lam[i-1] == it ):
        a[isave-1] = i
        lam[i-1] = lam[i-1] - 1
        it = isave - 1
        break

  k = 1
  ir = 1

  while ( True ):

    if ( n < ir ):
      break

    if ( lam[ir-1] != 0 ):
      a[k-1] = ir
      lam[ir-1] = lam[ir-1] - 1
      k = k + 1
      ir = ir + 1
      continue

    if ( it < k ):
      break

    ir = 1

  if ( n == 1 ):
    more = False
    return lam, a, more

  for j in range ( 2, n + 1 ):
    if ( a[j-1] < a[j-2] ):
      more = True
      return lam, a, more

  more = False

  return lam, a, more

def ytb_next_test ( ):

#*****************************************************************************80
#
## YTB_NEXT_TEST tests YTB_NEXT.
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
  import numpy as np
  from ytb_print import ytb_print

  print ''
  print 'YTB_NEXT_TEST'
  print '  YTB_NEXT generates Young tableaus.'

  n = 6
  lam = np.array ( [ 3, 2, 1, 0, 0, 0 ] )
  a = np.zeros ( n )
  more = False
 
  while ( True ):
 
    lam, a, more = ytb_next ( n, lam, a, more )
 
    ytb_print ( n, a, '' )
 
    if ( not more ):
      break
#
#  Terminate.
#
  print ''
  print 'YTB_NEXT_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  ytb_next_test ( )
  timestamp ( )

