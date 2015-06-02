#! /usr/bin/env python
#
def compnz_next ( n, k, a, more, h, t ):

#*****************************************************************************80
#
## COMPNZ_NEXT computes the compositions of the integer N into K nonzero parts.
#
#  Discussion:
#
#    A composition of the integer N into K nonzero parts is an ordered sequence
#    of K positive integers which sum to N.  The compositions (1,2,1)
#    and (1,1,2) are considered to be distinct.
#
#    The routine computes one composition on each call until there are no more.
#    For instance, one composition of 6 into 3 parts is 3+2+1, another would
#    be 4+1+1 but 5+1+0 is not allowed since it includes a zero part.
#
#    On the first call to this routine, set MORE = FALSE.  The routine
#    will compute the first element in the sequence of compositions, and
#    return it, as well as setting MORE = TRUE.  If more compositions
#    are desired, call again, and again.  Each time, the routine will
#    return with a new composition.
#
#    However, when the LAST composition in the sequence is computed
#    and returned, the routine will reset MORE to FALSE, signaling that
#    the end of the sequence has been reached.
#
#  Example:
#
#    The 10 compositions of 6 into three nonzero parts are:
#
#      4 1 1,  3 2 1,  3 1 2,  2 3 1,  2 2 2,  2 1 3,
#      1 4 1,  1 3 2,  1 2 3,  1 1 4.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Albert Nijenhuis and Herbert Wilf,
#    Combinatorial Algorithms,
#    Academic Press, 1978, second edition,
#    ISBN 0-12-519260-6.
#
#  Parameters:
#
#    Input, integer N, the integer whose compositions are desired.
#
#    Input, integer K, the number of parts in the composition.
#    K must be no greater than N.
#
#    Input, integer A(K), the previous composition.  On the first call,
#    with MORE = FALSE, set A = [].  Thereafter, A should be the 
#    value of A output from the previous call.
#
#    Input, logical MORE.  The input value of MORE on the first
#    call should be FALSE, which tells the program to initialize.
#    On subsequent calls, MORE should be TRUE, or simply the
#    output value of MORE from the previous call.
#
#    Input, integer H, T, internal parameters.  The user should set these
#    to 0 before the first call, and on subsequent calls pass in the previous output
#    values.
#
#    Output, integer A(K), the next composition.
#
#    Output, logical MORE, will be TRUE unless the composition 
#    that is being returned is the final one in the sequence.
#
#    Output, integer H, T, updated internal parameters.
#

#
#  We use the trick of computing ordinary compositions of (N-K)
#  into K parts, and adding 1 to each part.
#
  if ( n < k ):
    more = False
    for i in range ( 0, k ):
      a[i] = -1
    return a, more, h, t

  if ( not more ):

    t = n - k
    h = 0
    a[0] = n - k
    for i in range ( 1, k ):
      a[i] = 0

  else:

    for i in range ( 0, k ):
      a[i] = a[i] - 1

    if ( 1 < t ):
      h = 0

    h = h + 1
    t = a[h-1]
    a[h-1] = 0
    a[0] = t - 1
    a[h] = a[h] + 1

  more = ( a[k-1] != ( n - k ) )

  for i in range ( 0, k ):
    a[i] = a[i] + 1

  return a, more, h, t

def compnz_next_test ( ):

#*****************************************************************************80
#
## COMPNZ_NEXT_TEST tests COMPNZ_NEXT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 April 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ''
  print 'COMPNZ_NEXT_TEST'
  print '  COMPNZ_NEXT generates compositions'
  print '  with nonzero parts.'
  print ''

  n = 6
  k = 3
  a = np.zeros ( k )
  more = False
  h = 0
  t = 0

  print '  Seeking all compositions of N = %d' % ( n )
  print '  using %d nonzero parts.' % ( k )
  print ''

  while ( True ):

    a, more, h, t = compnz_next ( n, k, a, more, h, t )
    
    print '  ',
    for i in range ( 0, k ):
      print '%2d  ' % ( a[i] ),
    print ''

    if ( not more ):
      break
#
#  Terminate.
#
  print ''
  print 'COMPNZ_NEXT_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  compnz_next_test ( )
  timestamp ( )
